"""Temporal feature construction for AT-MORT-001.

Feature definitions are engineering transforms, not biological thresholds.
"""
from __future__ import annotations
import pandas as pd

WINDOWS = (24, 72, 168)

def build_environment_features(df: pd.DataFrame) -> pd.DataFrame:
    required={"cage_id","observed_at","variable_code","value"}
    missing=required-set(df.columns)
    if missing: raise ValueError(f"missing columns: {sorted(missing)}")
    x=df.copy()
    x["observed_at"]=pd.to_datetime(x["observed_at"], utc=True)
    x=x.sort_values(["cage_id","variable_code","observed_at"])
    wide=x.pivot_table(index=["cage_id","observed_at"],columns="variable_code",values="value",aggfunc="mean").sort_index()
    out=[]
    for cage_id,g in wide.groupby(level=0):
        g=g.droplevel(0)
        row={"cage_id":cage_id,"feature_at":g.index.max()}
        for col in g.columns:
            s=g[col].dropna()
            for hours in WINDOWS:
                w=s.loc[s.index >= (g.index.max()-pd.Timedelta(hours=hours))]
                if len(w):
                    row[f"{col}_mean_{hours}h"]=float(w.mean())
                    row[f"{col}_min_{hours}h"]=float(w.min())
                    row[f"{col}_max_{hours}h"]=float(w.max())
                    row[f"{col}_std_{hours}h"]=float(w.std(ddof=0))
        out.append(row)
    return pd.DataFrame(out)
