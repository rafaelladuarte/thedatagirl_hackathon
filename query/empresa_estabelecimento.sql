CREATE TABLE OR REPLACE `hackathon-a3-data.the_data_girls.empresa_estabelecimento` (
    cnpj_basico	STRING	NULLABLE	
    municipio	STRING	NULLABLE	
    uf	STRING	NULLABLE	
    pais	STRING	NULLABLE	
    situacao_cadastral	STRING	NULLABLE	
    data_situ_cadastral	DATE	NULLABLE	
    motivo_situacao_cadastral	STRING	NULLABLE	
    data_inicio_atividade	DATE	NULLABLE	
    situacao_especial	STRING	NULLABLE	
    data_situ_especial	DATE	NULLABLE	
    atividade_economica_principal	STRING	NULLABLE	
    atividade_economica_secundaria	STRING	NULLABLE	
    socio	STRING	NULLABLE	
    qualificacao_socio	STRING	NULLABLE	
    capital_social	STRING	NULLABLE	
    porte_empresa	STRING	NULLABLE	
    natureza_juridica	STRING	NULLABLE	
    opcao_pelo_simples	STRING	NULLABLE	
    data_opcao_simples	DATE	NULLABLE	
    data_exclusao_simples	DATE	NULLABLE	
    opcao_pelo_mei	STRING	NULLABLE	
    data_opcao_mei	DATE	NULLABLE	
    data_exclusao_mei	DATE	NULLABLE	
);

INSERT INTO `hackathon-a3-data.the_data_girls.empresa_estabelecimento`
SELECT 
    a.`cnpj_basico`,
    b.nome AS municipio,
    a.uf,
    c.pais,
    CASE a.situacao_cadastral 
        WHEN '01' THEN 'NULA'
        WHEN '02' THEN 'ATIVA'
        WHEN '03' THEN 'SUSPENSA'
        WHEN '04' THEN 'INAPTA'
        WHEN '08' THEN 'BAIXADA'
        ELSE NULL END  situacao_cadastral,
    CASE a.data_situ_cadastral
        WHEN NULL THEN NULL
        WHEN '00000000'  THEN NULL
        WHEN '0' THEN NULL
        WHEN '' THEN NULL
        ELSE CAST( 
            CONCAT(
                SUBSTR(a.data_situ_cadastral, 0 , 4), '-' ,
                SUBSTR(a.data_situ_cadastral, 5 , 2), '-' , 
                SUBSTR(a.data_situ_cadastral, 7 , 2) 
            ) AS DATE
        ) END data_situ_cadastral,
    e.nome AS motivo_situacao_cadastral,
    CASE a.data_inicio_atividade
        WHEN NULL THEN NULL
        WHEN '00000000' THEN NULL
        WHEN '0' THEN NULL
        WHEN '' THEN NULL
        ELSE CAST( 
            CONCAT(
                SUBSTR(a.data_inicio_atividade, 0 , 4), '-' ,
                SUBSTR( a.data_inicio_atividade, 5 , 2),'-' , 
                SUBSTR( a.data_inicio_atividade, 7 , 2) 
            ) AS DATE 
        ) END data_inicio_atividade,
    a.situacao_especial,
    CASE a.data_situ_especial
        WHEN NULL THEN NULL
        WHEN '00000000' THEN NULL
        WHEN '0' THEN NULL
        WHEN '' THEN NULL
        ELSE CAST( 
            CONCAT(
                SUBSTR(a.data_situ_especial, 0 , 4), '-' ,
                SUBSTR(a.data_situ_especial, 5 , 2), '-' , 
                SUBSTR(a.data_situ_especial, 7 , 2) 
            ) AS DATE 
        ) END data_situ_especial,
    d.nome AS atividade_economica_principal,
    d2.nome AS atividade_economica_secundaria,
    CASE f.id_de_socio
        WHEN '1' THEN 'PESSOA JURIDICA'
        WHEN '2' THEN 'PESSOA FISICA'
        WHEN '3' THEN 'ESTRANGEIRO'
        ELSE NULL END socio,
    g.nome AS qualificacao_socio,
    h.capital_social,
    CASE h.porte_empresa
        WHEN '01' THEN 'NÃO INFORMADO'
        WHEN '02' THEN 'MICRO EMPRESA'
        WHEN '03' THEN 'EMPRESA DE PEQUENO PORTE'
        WHEN '05' THEN 'DEMAIS'
        ELSE NULL END porte_empresa,
    j.nome AS natureza_juridica,
    i.opcao_pelo_simples,
    CASE i.data_opcao_simples
        WHEN NULL THEN NULL
        WHEN '00000000' THEN NULL
        WHEN '0' THEN NULL
        WHEN '' THEN NULL
        ELSE CAST( 
        CONCAT(
            SUBSTR(i.data_opcao_simples, 0 , 4), '-' ,
            SUBSTR(i.data_opcao_simples, 5 , 2), '-' , 
            SUBSTR(i.data_opcao_simples, 7 , 2) 
        ) AS DATE 
    ) END data_opcao_simples,
    CASE i.data_exclusao_simples
        WHEN NULL THEN NULL
        WHEN '00000000' THEN NULL
        WHEN '0' THEN NULL
        WHEN '' THEN NULL
        ELSE CAST( 
            CONCAT(
                SUBSTR(i.data_exclusao_simples, 0 , 4), '-' ,
                SUBSTR(i.data_exclusao_simples, 5 , 2), '-' , 
                SUBSTR(i.data_exclusao_simples, 7 , 2) 
            ) AS DATE 
        ) END data_exclusao_simples,
    i.opcao_pelo_mei,
    CASE data_opcao_mei
        WHEN NULL THEN NULL
        WHEN '00000000' THEN NULL
        WHEN '0' THEN NULL
        WHEN '' THEN NULL
        ELSE CAST(  
            CONCAT(
                SUBSTR(i.data_opcao_mei, 0 , 4), '-' ,
                SUBSTR(i.data_opcao_mei, 5 , 2), '-' , 
                SUBSTR(i.data_opcao_mei, 7 , 2) 
            ) AS DATE 
        ) END data_opcao_mei,
    CASE i.data_exclusao_mei
        WHEN NULL  THEN NULL
        WHEN '00000000' THEN NULL
        WHEN '0' THEN NULL
        WHEN '' THEN NULL
        ELSE CAST( 
            CONCAT(
                SUBSTR(i.data_exclusao_mei, 0 , 4), '-' ,
                SUBSTR(i.data_exclusao_mei, 5 , 2), '-' , 
                SUBSTR(i.data_exclusao_mei, 7 , 2) 
            ) AS DATE 
    ) END data_exclusao_mei,   
FROM `hackathon-a3-data.the_data_girls.estabelecimentos`  a
inner join `hackathon-a3-data.the_data_girls.socios` f on a.cnpj_basico = f.cnpj_basico
inner join `hackathon-a3-data.the_data_girls.empresas` h on  a.cnpj_basico = h.cnpj_basico
inner join `hackathon-a3-data.the_data_girls.simples` i on a.cnpj_basico = i.cnpj_basico
left join `hackathon-a3-data.the_data_girls.municipios`  b on a.municipio = b.codigo
left join `hackathon-a3-data.the_data_girls.pais` c on a.pais = c.codigo
left join `hackathon-a3-data.the_data_girls.cnae` d on a.cnae_principal = d.codigo 
left join `hackathon-a3-data.the_data_girls.cnae` d2 on a.cnae_secundario = d2.codigo
left join `hackathon-a3-data.the_data_girls.motivo` e on a.motivo_situ_cadastral = e.codigo
left join `hackathon-a3-data.the_data_girls.qualificacao_socio` g on f.qualificacao_do_socio = g.codigo
left join `hackathon-a3-data.the_data_girls.atuacao_juridica` j on h.natureza_juridica = j.codigo;