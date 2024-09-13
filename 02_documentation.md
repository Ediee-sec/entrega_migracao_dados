## Documentação entrega para o teste técnico, posição de Analista de Dados na empresa V4 Company - Emerson dos santos Pereira

### PRIMEIRO PASSO - INSTALAR O SQLITE MAIS RECENTE NO LINUX (INSTALAÇÃO)
* Instalar o sqllite no ambiente de desenvolvimento online (Linux)
    sudo apt-get update
    sudo apt-get install sqlite3

    > Versão instalada 3.45.3 

* Tomei a liberdade de aplimorar o script de criação da base de dados e estou inserindo o resultado no SQLite  
> Ele dropa a tabela caso exista
> Cria a tabela caso ela não exista
> Insere os dados gerados do script fornecido
> Local: /tools/

### SEGUNDO PASSO - CRIAR A CONEXÃO ENTRE O PYTHON E O DB (PYTHON)

* Aqui eu criei uma classe geral chamada de ETLvendas, e na ontrução dos objetos eu ja criei a conexão com o SQLite 

```python
    class ETLvendas:
        def __init__(self):
            self.con = sqlite3.connect('../db/teste_tecnico.db')
            self.cur = self.con.cursor()
```

### TERCEIRO PASSO - EXTRAIR O DADOS DO DB vendas PARA O PANDAS NO PYTHON (PYTHON)

* Passo simples, apenas usar a função read_sql_query do pandas para ler toda a base, aqui criei um método especifico para isso que retorna o próprio dataframe

    ```python
    def extract(self):
        df = pd.read_sql_query('SELECT * FROM vendas', self.con)
        
        return df
    ```

### QUARTO PASSO - TRANSFORMAÇÃO DOS DADOS (PYTHON)

* Transformei as datas para ISO de (YYYY-MM-DD) para (YYYY-MM-DDT00:00:00)
* Eu realizei o calculo de vendas por dia usando o pandas e em seguida adcionei o resuldado do calculo em uma coluna e esta coluna eu adcionei al final do meu dataframe
* adcionei a função drop_duplicates() do pandas para remover duplicados, apenas se houver
* Ao final é retornado o dataframe tratado

```python
    def _transform(self):
        df = self._extract()

        total_sales_per_day = df.groupby('data_venda')['valor_total'].sum().reset_index() # Calcula o total de vendas por dia
        total_sales_per_day.columns = ['data_venda', 'total_vendas_dia']
        df = df.merge(total_sales_per_day, on='data_venda', how='left')
        df['data_venda'] = pd.to_datetime(df['data_venda'], format='%Y-%m-%d')
        df['data_venda'] = df['data_venda'].apply(lambda x: x.isoformat()) # Altera a data para o formato ISO (Linha a linha)
        df = df.drop_duplicates() #Remove duplicados

        return df 
```

### QUINTO PASSO - CARREGAMENTO DOS DADOS (PYTHON)

* Para simular um bucket (data lake), eu criei o dirtório bucket_s3
* Fiquei em duvida neste ponto, decidi então criar um sistema que cria as pastas no bucket_s3 com base no dia do processamento
* Na etapa de carregamento eu uso a função to_csv() do pandas para criar um arquivo csv com base no dataframe tratado, mas poderia ser um tipo mais leve como o .parquet, deixei o csv apenas para visualizar os dados
* O arquivo sera armazenado dentro da pasta que foi criada
* EX da mascará do arquivo: TREATED_SALES_FILE_DYYYYMMDD_Hhh:mm:ss.csv

```python
    def load(self):
        df = self._transform()
        path = self._create_storage_structure()
        date_formated = datetime.now().strftime('D%Y%m%d_H%H%M%S')

        df.to_csv(os.path.join(path, f'TREATED_SALES_FILE_{date_formated}.csv'), sep=';', encoding='utf-8', header=True, index=False)
```


### SEXTO PASSO - CRIAR UM ARQUIVO .SQL COM A QUERY DE VENDAS DO MES (SQL)

* Abrir o terminal do sqlite3: ```sqlite3 teste_tecnico.db```
* Executar a query abaixo:
```SQL
        SELECT
        strftime('%Y-%m', data_venda) AS mes,
        SUM(valor_total) AS total_vendas
    FROM
        vendas
    GROUP BY
        strftime('%Y-%m', data_venda)
    ORDER BY
        mes;
```
* Como só possui dados do mês 1, será retornada apenas uma linhas com o resultado de 2023-01|807.0


### SÉTIMO PASSO - VISUALIZAÇÃO DOS DADOS (INSIGHTS)

* Criei um modelo mock-up para dar visualização ao conceito da visualiação do dados (Utilizei o Looker Studio da google por ser gratuito)
* Para uma melhor visualização criei um módulo para plotar dois tipos de insights (vendas por região) (vendas por mês)
* Caminho dos arquivos /dashs/
