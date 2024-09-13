SELECT
    strftime('%Y-%m', data_venda) AS mes,
    SUM(valor_total) AS total_vendas
FROM vendas
GROUP BY strftime('%Y-%m', data_venda)
ORDER BY mes;