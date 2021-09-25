--4. Qual o número de CNPJ que surgiram do grupo de educação superior, entre 2015 e 2021, discriminado por ano, em cada estado brasileiro?

CREATE TABLE `hackathon-a3-data.the_data_girls.q04_cnpj_educacao_superior` (
    quantidade INTEGER,
    atividade_economica_principal STRING,
    atividade_economica_secundaria STRING,
    ano_surgimento STRING,
    uf STRING
);

INSERT INTO `hackathon-a3-data.the_data_girls.q04_cnpj_educacao_superior`
SELECT
    COUNT(*) as quantidade,
    atividade_economica_principal,
    atividade_economica_secundaria,
    FORMAT_DATE('%Y', data_situ_cadastral) AS ano_surgimento,
    uf
FROM `hackathon-a3-data.the_data_girls.empresa_estabelecimento`
WHERE data_situ_cadastral >= '2015-01-01'
AND data_situ_cadastral <= '2021-06-30'
AND situacao_cadastral = 'ATIVA'
AND (atividade_economica_principal = 'Educação superior - graduação e pós-graduação'
OR atividade_economica_secundaria = 'Educação superior - graduação e pós-graduação')
GROUP BY
    atividade_economica_principal,
    atividade_economica_secundaria,
    ano_surgimento,
    uf