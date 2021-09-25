CREATE TABLE OR REPLACE `hackathon-a3-data.the_data_girls.q01_industria_ativa_opcao` (
    tipo	STRING,	
    opcao	STRING,
    municipio	STRING,	
    data_situacao_cadastro	STRING,	
    quantidade	INTEGER,	
)


INSERT INTO `hackathon-a3-data.the_data_girls.q01_industria_ativa_opcao`
SELECT
    'SIMPLES' as tipo,
    opcao_pelo_simples as opcao,
    municipio,
    FORMAT_DATE('%Y-%m',data_situ_cadastral) AS data_situacao_cadastro,
    COUNT(*) as quantidade
FROM `hackathon-a3-data.the_data_girls.empresa_estabelecimento`
WHERE situacao_cadastral = 'ATIVA'
AND data_situ_cadastral >= '2010-01-01'
AND data_situ_cadastral  <= '2021-06-30'
GROUP BY 1,2,3,4
UNION ALL 
SELECT 
    'MEI' as  tipo,
    opcao_pelo_mei AS opcao,
    municipio,
    FORMAT_DATE('%Y-%m',data_situ_cadastral) AS data_situacao_cadastro,
    COUNT(*) as quantidade 
FROM `hackathon-a3-data.the_data_girls.empresa_estabelecimento`
WHERE situacao_cadastral = 'ATIVA'
AND data_situ_cadastral >= '2010-01-01'
AND data_situ_cadastral  <= '2021-06-30'
GROUP BY 1,2,3,4