"""Download NZ half-hourly generation data from EMI into data/raw/.

EMI (Electricity Market Information, Electricity Authority) publishes monthly generation
CSVs by trading period (48 per day). This script fetches one month and drops it in
data/raw/ (gitignored). See grid/README.md for dataset provenance and the licence caveat.

The exact per-file URL pattern on the EMI portal should be confirmed before relying on the
default below — pass --url explicitly if the portal path differs.

Usage:
    pip install -e ".[part-a]"
    python grid/ingest_emi.py --month 2026-07
    python grid/ingest_emi.py --month 2026-07 --url "https://.../202607_Generation_MD.csv"
"""

from __future__ import annotations

import argparse
from pathlib import Path

import requests

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
# Dataset landing page (verified 2026-08-20). Per-file naming should be confirmed here:
EMI_DATASET_PAGE = "https://www.emi.ea.govt.nz/Wholesale/Datasets/Generation/Generation_MD"


def download(month: str, url: str, out_dir: Path = RAW_DIR) -> Path:
    """Fetch the month's CSV to data/raw/ and return the written path."""
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{month.replace('-', '')}_generation_md.csv"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    dest.write_bytes(resp.content)
    return dest


def build_default_url(month: str) -> str:
    """Best-guess EMI file URL for a YYYY-MM month. Confirm against EMI_DATASET_PAGE."""
    yyyymm = month.replace("-", "")
    return f"https://www.emi.ea.govt.nz/Wholesale/Datasets/Generation/Generation_MD/{yyyymm}_Generation_MD.csv"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download EMI monthly generation data.")
    parser.add_argument("--month", required=True, help="Month to fetch, as YYYY-MM.")
    parser.add_argument(
        "--url",
        default=None,
        help=f"Explicit CSV URL. If omitted, a default is built; confirm at {EMI_DATASET_PAGE}",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    url = args.url or build_default_url(args.month)
    path = download(args.month, url)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
