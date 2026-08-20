"""Simulate renewable-following scheduling of flexible compute.

Given a half-hourly renewable-share series (derived from EMI grid data, see grid/) and a
threshold policy, work out how much cleaner the average scheduled token is versus running
flat out, and what fraction of work is deferred (the SLA cost proxy).

Step 4 skeleton: the policy and the accounting are real; the inputs are passed in so the
notebook (notebooks/04-renewable-scheduling-sim.ipynb) and tests can drive it directly.

Usage:
    python scheduling/simulate.py            # runs the built-in demo series
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ScheduleResult:
    baseline_renewable_share: float
    scheduled_renewable_share: float
    deferred_fraction: float

    @property
    def clean_energy_gain(self) -> float:
        """Absolute improvement in renewable share from scheduling (percentage points)."""
        return self.scheduled_renewable_share - self.baseline_renewable_share


def simulate(renewable_share: list[float], threshold: float) -> ScheduleResult:
    """Run flexible compute only in periods at/above `threshold` renewable share.

    `renewable_share` is a list of per-period fractions in [0, 1]. Returns the baseline
    (run-anytime) average share, the scheduled average share, and the deferred fraction.
    """
    if not renewable_share:
        raise ValueError("renewable_share series is empty")

    baseline = sum(renewable_share) / len(renewable_share)
    eligible = [s for s in renewable_share if s >= threshold]
    scheduled = sum(eligible) / len(eligible) if eligible else baseline
    deferred = 1.0 - (len(eligible) / len(renewable_share))

    return ScheduleResult(
        baseline_renewable_share=baseline,
        scheduled_renewable_share=scheduled,
        deferred_fraction=deferred,
    )


def main() -> None:
    # Demo series: a day where renewable share dips overnight and peaks midday.
    demo = [0.6, 0.55, 0.5, 0.65, 0.8, 0.9, 0.95, 0.85, 0.7, 0.6]
    result = simulate(demo, threshold=0.8)
    print(
        f"baseline={result.baseline_renewable_share:.2%} "
        f"scheduled={result.scheduled_renewable_share:.2%} "
        f"gain={result.clean_energy_gain:.2%} "
        f"deferred={result.deferred_fraction:.2%}"
    )


if __name__ == "__main__":
    main()
