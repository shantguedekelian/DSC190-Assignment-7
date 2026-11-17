import sys
from pathlib import Path
import pandas as pd

# Adjust to match your dataset's allowed event types
VALID_EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}

src, dst = sys.argv[1:3]
df = pd.read_csv(src, dtype=str, keep_default_na=False)
df = df.apply(lambda c: c.str.strip())

df = df.replace("", pd.NA).dropna()
df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

dur = pd.to_numeric(df["duration_seconds"], errors="coerce")
ts = pd.to_datetime(df["timestamp"], errors="coerce")
mask = dur.notna() & (dur > 0) & ts.notna()
df = df[mask].copy()

df["duration_seconds"] = dur[mask].round().astype(int)
df["timestamp"] = ts[mask].dt.strftime("%Y-%m-%dT%H:%M:%S")

Path(dst).parent.mkdir(parents=True, exist_ok=True)
df.to_csv(dst, index=False)
