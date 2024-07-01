#%%
import os
import pandas as pd
from pathlib import Path
# %%
excel_lj = pd.ExcelFile('lj_gab edit.xlsx')
# %% read label jawaban
lj_cek ={}
lj_gab = {}
for sheet_ in excel_lj.sheet_names:
    df_ = pd.read_excel(excel_lj,sheet_name=sheet_)
    df_['Label'] = df_['Label'].astype(str)
    df_.set_index('Label',inplace=True)
    lj_cek[sheet_]=df_
    lj_gab[sheet_] ={}
    for kol in df_:
        lj_gab[sheet_][kol] = df_[kol].dropna().to_dict()
# %% cek duplikat value label jawaban
for key_ in lj_cek.keys():
    print(key_)
    for kol in lj_cek[key_]:
        val = lj_cek[key_][kol].value_counts()
        if val[val>1].shape[0] > 0:
            print(val[val>1])

# %% invers label jawaban
lj_gab_invers = {}
for kues in lj_gab.keys():
    lj_gab_invers[kues] ={}
    for key_ in lj_gab[kues]:
        lj_gab_invers[kues][key_] = {v:k for k,v in lj_gab[kues][key_].items()}

# %% read dan invers data value
path_dataClean = Path.joinpath(Path(__file__).parents[0],'data_clean')
data_clean = {}
# read data 
for kues in lj_gab.keys():
    file_ = [x for x in os.listdir(path_dataClean) if kues in x and 'gab.parquet' in x]
    print(kues)
    print(file_)
    df_= pd.read_parquet(Path.joinpath(path_dataClean,file_[0]))
    for kolom in lj_gab[kues]:
        print(kolom)
        # df_.replace(lj_gab[kues][kolom],inplace=True)
        df_[kolom].replace(lj_gab[kues][kolom],inplace=True)

    data_clean[kues] =df_
# %%  
for kues in data_clean.keys():
    data_clean[kues].to_excel(Path.joinpath(Path(__file__).parents[0],'data_invers',f'{kues}.xlsx'),index=False)
