import sqlite3
import os
from datetime import datetime
import pandas as pd
import plot
import sys_log

class ETLvendas:
    def __init__(self):
        self.con = sqlite3.connect(f'../db/teste_tecnico.db')
        self.cur = self.con.cursor()
        self.dir_s3 = os.path.join(os.getcwd(), '../bucket_s3')

    def _extract(self):
        """
        Realiza a extra o dos dados da tabela 'vendas' do SQLite e retorna um DataFrame com os dados.
        """
        try:
            df = pd.read_sql_query('SELECT * FROM vendas', self.con)
            sys_log.extract()
            
            return df
        except Exception as e:
            sys_log.error_log(sys_log.detail_error(e))
    
    def _transform(self):
        """
        Realiza a transforma o dos dados extra dos da tabela 'vendas' do SQLite e retorna um DataFrame com os dados transformados.
        
        - Calcula o total de vendas por dia
        - Altera a coluna 'data_venda' para o formato ISO
        - Remove duplicados
        """
        df = self._extract()

        try:
            total_sales_per_day = df.groupby('data_venda')['valor_total'].sum().reset_index() # Calcula o total de vendas por dia
            total_sales_per_day.columns = ['data_venda', 'total_vendas_dia']
            df = df.merge(total_sales_per_day, on='data_venda', how='left')
            df['data_venda'] = pd.to_datetime(df['data_venda'], format='%Y-%m-%d')
            df['data_venda'] = df['data_venda'].apply(lambda x: x.isoformat()) # Altera a data para o formato ISO (Linha a linha)
            df = df.drop_duplicates() #Remove duplicados
            
            sys_log.trasform()

            return df 
        except Exception as e:
            sys_log.error_log(sys_log.detail_error(e))

    def _create_storage_structure(self):
        """
        Cria a estrutura de armazenamento necessria para o carregamento dos dados no bucket simulado.
        
        Retorna o caminho da pasta criada.
        """
        try:
            mask_name_folder = os.path.join(self.dir_s3, datetime.now().strftime('%Y%m%d'))
            
            if not os.path.exists(mask_name_folder):
                os.makedirs(mask_name_folder, exist_ok=True)
                
            sys_log.create_folder(mask_name_folder)

            return mask_name_folder
        except Exception as e:
            sys_log.error_log(sys_log.detail_error(e))

    def load(self):
        """
        Carrega os dados transformados para o bucket simulado e chama o módulo que irá criar 2 dashboards:
        """
        try:
            df = self._transform()
            path = self._create_storage_structure()
            date_formated = datetime.now().strftime('D%Y%m%d_H%H%M%S')

            job = plot.CreateDashs(df)
            job.sales_by_region()
            job.sales_by_month()
            df.to_csv(os.path.join(path, f'TREATED_SALES_FILE_{date_formated}.csv'), sep=';', encoding='utf-8', header=True, index=False)
            
            sys_log.load(os.path.join(path, f'TREATED_SALES_FILE_{date_formated}.csv'))
        except Exception as e:
            sys_log.error_log(sys_log.detail_error(e))

if __name__ == '__main__':
    sys_log.start_log()
    job = ETLvendas()
    job.load()
    sys_log.end_log()
