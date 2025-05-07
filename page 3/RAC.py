import os
import pandas as pd


def get_yearly_data(year):
    # Définir le dossier principal contenant les sous-dossiers
    main_path = f"/raid/datasets/allianzsante/A{year}"

    # Liste pour stocker les résultats
    all_data = []
    print("start")
    k=0


    for file in os.listdir(main_path):
        if file.endswith(".csv"):
            file_path = os.path.join(main_path, file)
            use_cols = ['FLX_ANN_MOI',"PRS_REM_TAU", "BEN_SEX_COD", "AGE_BEN_SNDS", "FLT_PAI_MNT", "FLT_REM_MNT",'ASU_NAT',
                    'BEN_CMU_TOP','BEN_QLT_COD', 'BEN_RES_REG','CPT_ENV_TYP']
            data = pd.read_csv(file_path, sep=';', usecols = use_cols)
                    
            data = data[(data['PRS_REM_TAU'] <= 100) & (data['FLT_REM_MNT'] >= 0) & (data['FLT_PAI_MNT'] > 0)]
            data["RAC"] = data['FLT_PAI_MNT'] - data['FLT_REM_MNT']
                    
            # Stocker les données
            all_data.append(data)
        k+=1
        print(k)
        


    # Concaténer tous les fichiers
    df_final = pd.concat(all_data)

    # Agréger les résultats par mois (exemple : somme d'une colonne "valeur")
    result = df_final.groupby(['FLX_ANN_MOI','AGE_BEN_SNDS','BEN_SEX_COD','BEN_RES_REG'])[["RAC",'FLT_PAI_MNT']].sum().reset_index()
    existe = os.path.exists(r"/raid/home/allianzsante/fadli_oth/Desktop/Getting Started/data_cleaning/RAC_par_mois.csv")

    result.to_csv(r"/raid/home/allianzsante/fadli_oth/Desktop/Getting Started/RAC_par_mois.csv", index=False, mode='a', header=not existe)


if __name__ == "__main__":
    for year in range(2019, 2025):
        get_yearly_data(year)
        print(f"Data for {year} processed.")

