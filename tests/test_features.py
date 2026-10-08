import pandas as pd
from aquatwin.features import build_environment_features

def test_temporal_features_are_cage_specific():
    df=pd.DataFrame([
      {"cage_id":"A","observed_at":"2026-01-01T00:00:00Z","variable_code":"oxygen_mg_l","value":8.0},
      {"cage_id":"A","observed_at":"2026-01-01T01:00:00Z","variable_code":"oxygen_mg_l","value":6.0},
      {"cage_id":"B","observed_at":"2026-01-01T01:00:00Z","variable_code":"oxygen_mg_l","value":9.0},
    ])
    out=build_environment_features(df).set_index("cage_id")
    assert out.loc["A","oxygen_mg_l_mean_24h"] == 7.0
    assert out.loc["B","oxygen_mg_l_mean_24h"] == 9.0
