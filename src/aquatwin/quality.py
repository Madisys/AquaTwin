from dataclasses import dataclass
from math import isfinite


PLAUSIBILITY = {
    "water_temp_c": (-2.0, 35.0),
    "oxygen_mg_l": (0.0, 25.0),
    "oxygen_sat_pct": (0.0, 200.0),
    "salinity_psu": (0.0, 50.0),
    "ph": (5.0, 10.0),
    "chlorophyll_a": (0.0, 1000.0),
}


@dataclass(frozen=True)
class QualityResult:
    valid: bool
    quality_flag: str
    score: float
    reasons: tuple[str, ...]


def assess_observation(variable_code: str, value: float, source_id: str) -> QualityResult:
    reasons: list[str] = []
    if not source_id.strip():
        reasons.append("missing_source")
    if not isfinite(value):
        reasons.append("non_finite_value")
    bounds = PLAUSIBILITY.get(variable_code)
    if bounds and isfinite(value) and not (bounds[0] <= value <= bounds[1]):
        reasons.append("outside_engineering_plausibility_range")

    if not reasons:
        return QualityResult(True, "PASS", 1.0, ())
    if "non_finite_value" in reasons or "missing_source" in reasons:
        return QualityResult(False, "REJECT", 0.0, tuple(reasons))
    return QualityResult(True, "REVIEW", 0.5, tuple(reasons))
