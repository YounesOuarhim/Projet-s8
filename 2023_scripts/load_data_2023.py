import gzip
import os
import numpy as np
import pandas as pd
import polars as pl
import time
import tqdm

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# decompressing data
start = time.time()
for i, month in enumerate(months):
    print("loading A2023{}.csv.gz".format(month))
    input_file = "D:\\projet s8 files\\A2023{}.csv.gz".format(month)
    output_file = "D:\\projet s8 files\\A2023\\A2023{}.csv".format(month)

    file_size = os.path.getsize(input_file)  # Get compressed file size

    with gzip.open(input_file, "rb") as f_in, open(output_file, "wb") as f_out, tqdm.tqdm(
        total=file_size, unit="B", unit_scale=True, desc="Decompressing"
    ) as pbar:
        for chunk in iter(lambda: f_in.read(1024 * 1024), b""):  # Read 1MB at a time
            f_out.write(chunk)
            pbar.update(len(chunk))  # Update progress bar

end = time.time()
print('Time taken to decompress data:', end - start)
        


