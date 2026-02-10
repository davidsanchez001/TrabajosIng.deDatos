import pandas as pd

# EXTRACT
df = pd.read_csv("Base de datos.csv", sep=";")

# TRANSFORM
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

df = df.dropna(how="all")

df = df.drop_duplicates()

df["time_start"] = pd.to_datetime(df["time_start"], errors="coerce")
df["time_end"] = pd.to_datetime(df["time_end"], errors="coerce")

numeric_cols = [
    "launched", "destroyed", "not_reach_goal", "still_attacking",
    "num_hit_location", "num_fall_fragment_location",
    "turbojet", "turbojet_destroyed"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

df["duration_hours"] = (
    (df["time_end"] - df["time_start"]).dt.total_seconds() / 3600
)

df["destruction_rate"] = df["destroyed"] / df["launched"]

# LOAD
df.to_csv("base_limpia.csv", index=False)
