import sys
from pathlib import Path
import pandas as pd

src, dst = sys.argv[1:3]
df = pd.read_csv(src)
df["date"] = df["timestamp"].str[:10]

Path(dst).parent.mkdir(parents=True, exist_ok=True)
df.to_csv(dst, index=False)
