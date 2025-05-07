import polars as pl
import time

DATA_2023 = []
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
start_time = time.time()
for month in months: 
    DATA_2023.append(pl.read_csv("D:\\projet s8 files\\A2023\\A2023{}.csv".format(month), separator=';', ignore_errors=True, columns=['AGE_BEN_SNDS', 'ASU_NAT', 'BEN_SEX_COD', 'CPT_ENV_TYP', 'FLT_PAI_MNT', 'FLT_REM_MNT', 'PRS_REM_TYP', 'PRS_REM_MNT', 'PRS_NAT']))
    print("The data for the month {} has been loaded".format(month))
end_time = time.time()
print("The time needed for the loading of the data is : {}s".format(end_time-start_time))

