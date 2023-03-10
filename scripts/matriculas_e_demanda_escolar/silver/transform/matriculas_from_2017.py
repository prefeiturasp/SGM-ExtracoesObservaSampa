from core.extractors.file_system import DfLoaderGenerator
from core.utils.clean import remover_acentos
from pandas import DataFrame
import pandas as pd
import numpy as np
import os
from typing import Generator

from config import DATA_FOLDER

class MatriculasCleanFrom2017:

    folder = 'demanda_e_matriculas'

    def __init__(self):

        self.load = DfLoaderGenerator(tier='bronze', data_dir=DATA_FOLDER, add_file=True)

    def check_col(self, col:str, check_set:set)->bool:

        col = col.lower().strip()

        return col in check_set
    
    def get_col_posit(self, df:DataFrame, check_set:set)->int:

        for i, col in enumerate(df.columns):
            if self.check_col(col, check_set):
                return i
        else:
            raise RuntimeError(f'Colunas {check_set} não encontradas no dataframe')

    def get_col_fim(self, df:DataFrame)->int:

        check_set = {'matrícula em processo', 'matricula em processo'}
        
        return self.get_col_posit(df, check_set)
    
    def get_col_inicio(self, df:DataFrame)->int:

        check_set = {'matrículas', 'matriculas'}
        
        return self.get_col_posit(df, check_set)
    
    def subset_matriculas_data(self, df:DataFrame, inicio:int, fim:int)->DataFrame:

        df = df.iloc[:, inicio:fim].copy()

        return df
    
    def get_col_distrito(self, df:DataFrame)->int:

        check_set = {'distrito'}
        
        return self.get_col_posit(df, check_set)
    
    def get_dist_data(self, df:DataFrame, col_dist_posit:int)->DataFrame:

        dist_data = df.iloc[:, col_dist_posit].copy()
        return dist_data

    def join_distritos_data(self, df:DataFrame, dist_data:pd.Series)->DataFrame:

        return pd.concat([dist_data, df], axis=1)
    
    def pipeline_filter_columns(self, df:DataFrame)->DataFrame:

        col_inicio = self.get_col_inicio(df)
        col_fim = self.get_col_fim(df)

        data = self.subset_matriculas_data(df, col_inicio, col_fim)

        col_dists = self.get_col_distrito(df)
        dist_data = self.get_dist_data(df, col_dists)

        data = self.join_distritos_data(data, dist_data)

        return data
    
    def set_true_columns(self, df:DataFrame)->DataFrame:

        df = df.copy()
        cols_true = df.iloc[0]
        df.columns = cols_true

        df.rename({np.NaN : 'Distrito'}, axis=1, inplace=True)

        return df

    def get_last_row(self, df:DataFrame)->int:

        try:
            return df[df.iloc[:,0]=='TOTAL'].index[0]
        except KeyError:
            raise RuntimeError(f'O DataFrame não possui uma linha de TOTAL')

    def subset_rows(self, df:DataFrame)->DataFrame:

        last_row = self.get_last_row(df)

        df = df.iloc[:last_row, :].copy()
        
        return df

    def get_file(self, df:DataFrame)->str:

        return df['file'].unique()[0]
    
    def extract_year_from_file(self, file:str)->str:

        return os.path.split(file)[-1].split('.xls')[0][-4:]

    def set_year_col_pipeline(self, df:DataFrame, og_df:DataFrame)->None:

        file = self.get_file(og_df)
        year = self.extract_year_from_file(file)
        df['ano'] = year
    
    def pipeline_subset_df(self, df:DataFrame)->DataFrame:

        og_df = df.copy()

        df = self.pipeline_filter_columns(df)
        df = self.subset_rows(df)
        df = self.set_true_columns(df)
        df.drop(0, inplace=True)
        
        self.set_year_col_pipeline(df, og_df)

        return df
    
    def subset_all_dfs(self, df_gen:Generator)->DataFrame:
        
        dfs = []
        for df in df_gen:
            df_subset = self.pipeline_subset_df(df)
            dfs.append(df_subset)

        return pd.concat(dfs)

    def padrao_col_fund(self, col:str)->str:

        if col.startswith('ens_fund'):
            col = col.replace('ens_', '')
        
        return col

    def padrao_ens_medio(self, col:str)->str:

        if col == 'ens_medio':
            col = col.replace('io', '')

        return col
    
    def clean_col(self, col:str)->str:

        col = col.lower()
        col = col.replace('.', ' ')
        col = col.replace(' ', '_')
        col = col.replace('__', '_')
        col = col.strip('_')
        col = remover_acentos(col)
        col = self.padrao_col_fund(col)
        col = self.padrao_ens_medio(col)

        return col
    
    def clean_all_cols(self, df:DataFrame)->None:

        rename = {col : self.clean_col(col) 
                  for col in df.columns}

        df.rename(rename, axis=1, inplace=True)

        return df
    
    def cols_to_int(self, df:DataFrame)->None:

        for col in df.columns:
            if col!='Distrito':
                df[col] = df[col].astype(int)
    
    def __call__(self)->DataFrame:

        df_gen = self.load(self.folder, extension='.xls')

        df = self.subset_all_dfs(df_gen)
        self.cols_to_int(df)
        self.clean_all_cols(df)

        return df





    