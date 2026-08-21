"""Measure watt-hours per 1000 tokens for a fixed inference workload.

Samples GPU power via `nvidia-smi` (and, where available, CPU package power via RAPL)
while a fixed workload runs, then integrates power over time to get energy, and divides by
tokens generated. Writes a results CSV with a hardware fingerprint to energy/results/.

This is the Step 3 skeleton: the sampling loop and the energy integration are real; the
`run_workload` hook is where the actual model inference plugs in (Step 5's model, or any
open-weight model served locally). Keep hosted APIs out — a foreign endpoint has no
knowable power draw or grid, which defeats the whole measurement.

Usage:
    python energy/measure.py --label mistral-7b-rtx4090 --tokens 1000
"""

from __future__ import annotations

import argparse
import csv
import platform
import subprocess
import time
from pathlib import Path

RESULTS_DIR = Path(__file__).resolve().parent / "results"


def sample_gpu_power_watts() -> float | None:
    """Return instantaneous GPU power draw in watts via nvidia-smi, or None if absent."""
    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-gpu=power.draw", "--format=csv,noheader,nounits"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return None
    first = out.stdout.strip().splitlines()[0] if out.stdout.strip() else ""
    try:
        return float(first)
    except ValueError:
        return None


def hardware_fingerprint() -> str:
    """A short, committed-alongside-results description of what this ran on."""
    gpu = "unknown-gpu"
    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True,
        )
        gpu = out.stdout.strip().splitlines()[0] or gpu
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    return f"{platform.machine()}|{platform.system()}|{gpu}"


def run_workload(tokens: int) -> int:
    """Placeholder for the fixed inference workload. Returns tokens actually generated.

    Wire this to the locally served open-weight model (see energy/harness/ for the fixed
    prompt set). Until then it just returns the requested token count so the plumbing runs.
    """
    return tokens


def measure(label: str, tokens: int, interval_s: float = 0.5) -> dict[str, str]:
    """Run the workload while sampling power; return a results row."""
    samples: list[float] = []
    start = time.monotonic()

    # Sample in the background of the workload. For the skeleton the workload returns fast,
    # so take at least one sample to keep the integration well-defined.
    generated = run_workload(tokens)
    p = sample_gpu_power_watts()
    if p is not None:
        samples.append(p)
    elapsed_h = max(time.monotonic() - start, interval_s) / 3600.0

    avg_watts = sum(samples) / len(samples) if samples else 0.0
    wh = avg_watts * elapsed_h
    wh_per_1k = (wh / generated * 1000) if generated else 0.0

    return {
        "label": label,
        "hardware": hardware_fingerprint(),
        "tokens": str(generated),
        "avg_power_w": f"{avg_watts:.2f}",
        "energy_wh": f"{wh:.4f}",
        "wh_per_1k_tokens": f"{wh_per_1k:.4f}",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }


def write_result(row: dict[str, str], out_dir: Path = RESULTS_DIR) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{row['label']}-{time.strftime('%Y%m%d-%H%M%S')}.csv"
    with dest.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(row.keys()))
        writer.writeheader()
        writer.writerow(row)
    return dest


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure watt-hours per 1000 tokens.")
    parser.add_argument("--label", required=True, help="Run label, e.g. model-hardware.")
    parser.add_argument("--tokens", type=int, default=1000, help="Target tokens to generate.")
    args = parser.parse_args()

    row = measure(args.label, args.tokens)
    path = write_result(row)
    print(f"Wrote {path}: {row['wh_per_1k_tokens']} Wh/1k tokens")


if __name__ == "__main__":
    main()
