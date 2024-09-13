## COMO EXECUTAR A APLICAÇÃO

* Glossário de pastas
    > **bucket** : Armazenará os arquivos csv, separados por subpastas com a mascara YYYYMMDD
    > **dashs**: Irá armazenas os .png que serão plotados durante o processamento, e também contém o mock-up
    > **db**: Conterá o banco de dados SQLite
    > **logs**: Armazenrá os arquivos de logs das execuções dos processos

    > **python**: Conterá os principais scripts responsáveis pela execução do processo
        > **main.py**: Script principal responsável por realizar todo o ETL
        > **plot.py**: Módulo responsável por plotar os dashs
        > **sys_log.py**: Módulo responsável por gerar o arquivo de log da execução do processo

    > **sql**: Conterá a query de vendas por Ano Mês
    
    > **tools**: Conterá a adptação que eu fiz, após gerar as 500 linhas o script irá inserir os dados diretamente na tabela **vendas**
        > **generate_data.py**: Script responsável por gerar uma base aleatoria com 500 linhas e inserir no banco de dados criado

* Pré requisitos  
    > Ter o python instalado versão 3.9.X ou superior
    > Instalar a biblioteca pandas ```pip install pandas```

* Como gerar dados massivos para os testes
    > Acessar o caminho ```coodesh-data-engineering/tools```
    > No terminal executar o comando ```python generate_data.py```

* Como executar
    > Acessar o caminho ```coodesh-data-engineering/python```
    > No terminal executar o seguinte comando ```python main.py```

* Gráficos
    > Acessar o caminho ```coodesh-data-engineering/dashs```
    > Terá os gráficos com insghts sobre o negócio

* Resultado
    > Verificar se o arquivo ```TREATED_SALES_FILE_Dyyyymmdd_Hhh:mm:ss.csv``` foi criado no diretório ```bucket_s3```