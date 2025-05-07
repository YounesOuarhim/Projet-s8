import polars as pl
import time

DATA_2023 = []
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
start_time = time.time()
for month in months: 
    DATA_2023.append(pl.read_csv("D:\\projet s8 files\\A2023\\A2023{}.csv".format(month), separator=';', ignore_errors=True, columns=['AGE_BEN_SNDS', 'ASU_NAT', 'BEN_SEX_COD', 'CPT_ENV_TYP', 'FLT_PAI_MNT', 'FLT_REM_MNT']))
end_time = time.time()
print("The time needed for the loading of the data is : {}s".format(end_time-start_time))

total_depenses = 0
total_remboursés = 0
total_soin_de_ville_seulement = 0
start_time = time.time()
for idx, month in enumerate(months):
    total_depenses += DATA_2023[idx]['FLT_PAI_MNT'].sum()
    total_remboursés += DATA_2023[idx].filter(DATA_2023[idx]['CPT_ENV_TYP'].is_in([1,2]))['FLT_REM_MNT'].sum()
    total_soin_de_ville_seulement += DATA_2023[idx].filter(DATA_2023[idx]['CPT_ENV_TYP'] == 1)['FLT_REM_MNT'].sum()
end_time = time.time()
print("The time needed for the computing of the mean is : {}s".format(end_time-start_time))
print("somme remboursée par la SS pour l'enveloppe 1 et 2: {}€".format(total_remboursés))
print("somme remboursée par la SS pour l'enveloppe 1: {}€".format(total_soin_de_ville_seulement))
print("somme dépensée sur les santé: {}€".format(total_depenses))



