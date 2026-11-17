import sys
from pathlib import Path
import pandas as pd

src, dst = sys.argv[1:3]
df = pd.read_csv(src)
df["duration_minutes"] = df["duration_seconds"] / 60
df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

Path(dst).parent.mkdir(parents=True, exist_ok=True)
df.to_csv(dst, index=False)
