import polars as pl
import glob

data_path = "GOLD"
output_file = "GOLD-1m(1).parquet"

files = sorted(glob.glob(f"{data_path}/*.csv"))

(
    pl.scan_csv(
        files,
        has_header=False,
        infer_schema=False,   
        ignore_errors=True    
    )
    .sink_parquet(output_file)
)

print("✅ DONE")
