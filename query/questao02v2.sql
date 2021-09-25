CREATE TABLE `hackathon-a3-data.the_data_girls.q2_v2_estabelecimento_fechado` (
    tipo	STRING,	
    opcao	STRING,
    municipio	STRING,
    uf STRING,
    data_situacao_cadastro	STRING,	
    quantidade	INTEGER,	
);

INSERT INTO `hackathon-a3-data.the_data_girls.q2_v2_estabelecimento_fechado`
SELECT
    'SIMPLES' as tipo,
    opcao_pelo_simples as opcao,
    municipio,
    uf,
    FORMAT_DATE('%Y-%m',data_situ_cadastral) AS data_situacao_cadastro,
    COUNT(*) as quantidade
FROM `hackathon-a3-data.the_data_girls.empresa_estabelecimento`
WHERE data_situ_cadastral >= '2010-01-01'
AND data_situ_cadastral  <= '2021-06-30'
AND situacao_cadastral IN ('NULA','BAIXADA')
GROUP BY 1,2,3,4,5
UNION ALL 
SELECT 
    'MEI' as  tipo,
    opcao_pelo_mei AS opcao,
    municipio,
    uf,
    FORMAT_DATE('%Y-%m',data_situ_cadastral) AS data_situacao_cadastro,
    COUNT(*) as quantidade 
FROM `hackathon-a3-data.the_data_girls.empresa_estabelecimento`
WHERE data_situ_cadastral >= '2010-01-01'
AND data_situ_cadastral  <= '2021-06-30'
AND situacao_cadastral IN ('NULA','BAIXADA')
GROUP BY 1,2,3,4,5