--5. Qual a classe de CNAE com o maior capital social médio no Brasil no último ano?

CREATE TABLE `hackathon-a3-data.the_data_girls.q05_capital_social_cnae` (
    media_capital_social FLOAT64,
    classe_de_cnae STRING
);

INSERT INTO `hackathon-a3-data.the_data_girls.q05_capital_social_cnae`
SELECT AVG(CAST(REPLACE(capital_social, ',', '.') AS float64)) AS media_capital_social, atividade_economica_principal as classe_de_cnae
FROM `hackathon-a3-data.the_data_girls.empresa_estabelecimento`
WHERE situacao_cadastral = 'ATIVA'
GROUP BY classe_de_cnae
ORDER BY media_capital_social DESC