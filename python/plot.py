import matplotlib.pyplot as plt
import pandas as pd

class CreateDashs:
    def __init__(self, data):
        self.data = data

    def sales_by_region(self):
        """
            Gera um gráfico de barras com as vendas por região.
            
            O gráfico salvo em um arquivo png na pasta '../dashs' com o nome 'sales_by_region.png'.
        """
        df = pd.DataFrame(self.data)
        df_sum = df.groupby('regiao')['valor_total'].sum().reset_index()
        df_sum.plot.bar(x='regiao', y='valor_total', legend=False, color='skyblue')
        plt.title('Vendas por Região')
        plt.xlabel('regiao')
        plt.ylabel('valor_total')
        plt.savefig('../dashs/sales_by_region.png')

    def sales_by_month(self):
        """
            Gera um gráfico de barras com as vendas por mês.
            
            O gráfico salvo em um arquivo png na pasta '../dashs' com o nome 'sales_by_month.png'.
        """
        df = pd.DataFrame(self.data)
        df['data_venda'] = pd.to_datetime(df['data_venda'], errors='coerce')
        df_sum = df.groupby(df['data_venda'].dt.to_period('M'))['valor_total'].sum().reset_index()
        df_sum.plot.bar(x='data_venda', y='valor_total', legend=False, color='skyblue')
        plt.title('Vendas por Mês')
        plt.xlabel('data_venda')
        plt.ylabel('valor_total')
        plt.savefig('../dashs/sales_by_month.png')


