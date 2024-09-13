import logging
from datetime import datetime,timedelta
import os
import traceback

log_folder = os.path.join(os.getcwd(), '../logs')
os.makedirs(log_folder, exist_ok=True)
log_file = os.path.join(log_folder, f'log_sales_{datetime.now().strftime("%Y%m%d%H%M%S")}.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start_log():
    logging.info('Processo iniciado')
    
def extract():
    logging.info('Dados extraidos com sucesso!')
    
def trasform():
    logging.info('Dados transformados com sucesso!')
    
def create_folder(p):
    logging.info(f'Pasta {p} criada com sucesso!')
    
def load(p):
    logging.info('Dados carregados com sucesso!')
    logging.info('Dashboards criados com sucesso!')
    logging.info(f'Arquivo {p} criado com sucesso!')
    
def end_log():
    logging.info('Processo finalizado')
    
def detail_error(e):
    tb_str = traceback.format_exception(type(e), value=e, tb=e.__traceback__)
    tb_str = ''.join(tb_str)
    
    return tb_str

def error_log(e):
    logging.critical(e)
