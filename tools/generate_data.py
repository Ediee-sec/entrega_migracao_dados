import sqlite3
from datetime import datetime, timedelta
import random
import os

def generate_sales_data(num_records=500):
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    products = list(range(101, 111))  # 10 produtos
    regions = ['Norte', 'Sul', 'Leste', 'Oeste', 'Centro']
    
    sales_data = []
    for i in range(1, num_records + 1):
        sale_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        product_id = random.choice(products)
        customer_id = random.randint(1001, 2000)
        quantity = random.randint(1, 10)
        unit_price = round(random.uniform(10.0, 100.0), 2)
        total_value = round(quantity * unit_price, 2)
        seller_id = random.randint(1, 20)
        region = random.choice(regions)
        
        sale = (i, sale_date.strftime('%Y-%m-%d'), product_id, customer_id, quantity, unit_price, total_value, seller_id, region)
        sales_data.append(sale)
    
    return sales_data


def drop_tb_sales():
    drop_table_sql = """
    DROP TABLE IF EXISTS vendas;
    """

    return drop_table_sql

def create_tb_sales():
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY,
        data_venda TEXT NOT NULL,
        id_produto INTEGER NOT NULL,
        id_cliente INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        valor_unitario REAL NOT NULL,
        valor_total REAL NOT NULL,
        id_vendedor INTEGER NOT NULL,
        regiao TEXT NOT NULL
    );
    """
    return create_table_sql

def load_data_to_data_base(qtd_reg):

    conn = sqlite3.connect(f'../db/teste_tecnico.db')
    cursor = conn.cursor()

    random_data = generate_sales_data(qtd_reg)

    conn.execute(drop_tb_sales())
    cursor.execute(create_tb_sales())


    insert_sql = """
    INSERT INTO vendas (id, data_venda, id_produto, id_cliente, quantidade, valor_unitario, valor_total, id_vendedor, regiao)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    cursor.executemany(insert_sql, random_data)

    conn.commit()
    cursor.close()


load_data_to_data_base(500)
