### Como eu implementaria um modelo de ML no SageMaker da AWS

* Não possuo um conhecimento muito abrangente nesta área de ciência de dados, então muito do que coloquei aqui foi meu conhecimento teórico nas ferramentas de ML da GCP, e vi alguns videos sobre o SageMaker para dar sentido aos meus raciocinios.

1. Estrutura dos Dados 
* Os principais campos que serão úteis para o modelo poderão ser:

> data_venda 
> quantidade 
> valor_total
> regiao 

2. Pré-processamento dos Dados
* Conversão de Data: Extração de características como o mês, dia, e o ano da data.

3. Fonte dos dados
* Amazon S3

4. Seleção de Modelo
* A regressão linear pode ser implementado para prever o valor vendido (coluna valor_total).

5. Implementação no SageMaker
* Pré-processamento dos dados:

> Carregar os dados.
> Transformar a coluna de data em componentes como year, month, e day.
> Codificar variáveis categóricas EX: Centro, Norte

* Divisão dos Dados:
> Separar os dados em treinamento e teste.
> Configuração do SageMaker:

* Treinamento:
> Iniciar o treinamento 
> Definir a variável-alvo como a quantidade vendida (target).

* Avaliação:
> Avaliar a performance do modelo.

* Implantação:
> Uma vez treinado, o modelo pode ser implantado usando endpoints do SageMaker para prever valores futuros com base em novos dados.