from aquatwin.quality import assess_observation


def test_plausible_oxygen_passes():
    result = assess_observation("oxygen_mg_l", 8.1, "sensor-test")
    assert result.valid
    assert result.quality_flag == "PASS"
    assert result.score == 1.0


def test_implausible_oxygen_requires_review_not_silent_correction():
    result = assess_observation("oxygen_mg_l", 99.0, "sensor-test")
    assert result.valid
    assert result.quality_flag == "REVIEW"
    assert "outside_engineering_plausibility_range" in result.reasons


def test_missing_source_rejected():
    result = assess_observation("water_temp_c", 12.0, "")
    assert not result.valid
    assert result.quality_flag == "REJECT"
