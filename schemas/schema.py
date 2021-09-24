all_schemas = [
    {
        'schema': {
                'cnpj_basico' :"STRING",
                'razao_social' :"STRING",
                'natureza_juridica' :"STRING",
                'qualificacao_responsavel' :"STRING",
                'capital_social' :"STRING",
                'porte_empresa' :"STRING",
                'ente_responsavel' :"STRING",
            },
        'table': 'empresa',
        'csv': 'EMPRESAS*'
    }, {
        'schema': {
            "cnpj_basico": "STRING",
            "id_de_socio": "STRING",
            "nome_socio_razao_social": "STRING",
            "cnpj_cpf_socio" : "STRING",
            "qualificacao_do_socio": "STRING",
            "data_entrada_sociedade": "STRING",
            "pais": "STRING",
            "cpf_representante_legal": "STRING",
            'nome_representante': "STRING",
            'qualificacao_representante': "STRING",
            'faixa_etaria': "STRING"
        },
        'table': 'socios',
        'csv': 'SOCIO*'
    }, {
        'schema': {
            'cnpj_basico' :"STRING",
            'cnpj_ordem' :"STRING",
            'cnpj_dv' :"STRING",
            'id_matriz_filial' :"STRING",
            'nome_fantasia':"STRING",
            'situacao_cadastral' :"STRING",
            'data_situ_cadastral' :"STRING",
            'motivo_situ_cadastral' :"STRING",
            'nome_cidade_exterior' :"STRING",
            'pais' :"STRING",
            'data_inicio_atividade':"STRING",
            'cnae_principal':"STRING",
            'cnae_secundario':"STRING",
            'tipo_logradouro':"STRING",
            'logradouro':"STRING",
            'numero':"STRING",
            'complemento':"STRING",
            'bairro':"STRING",
            'cep':"STRING",
            'uf':"STRING",
            'municipio':"STRING",
            'ddd1':"STRING",
            'telefone1':"STRING",
            'ddd2':"STRING",
            'telefone2':"STRING",
            'ddd_fax':"STRING",
            'fax':"STRING",
            'email':"STRING",
            'situacao_especial':"STRING",
            'data_situ_especial':"STRING"
        },
        'table': 'estabelecimento',
        'csv': 'ESTABELECIMENTO*'
    }, {
        'schema': {
            'cnpj_basico': "STRING",
            'opcao_pelo_simples': "STRING",
            'data_opcao_simples': "STRING",
            'data_exclusao_simples': "STRING",
            'opcao_pelo_mei': "STRING",
            'data_opcao_mei': "STRING",
            'data_exclusao_mei': "STRING"
        },
        'table': 'simples',
        'csv': '.D10*'
    },{
        'schema': {
            'codigo':"STRING",
            'nome':"STRING",
        },
        'table': 'paises',
        'csv': 'PAIS*'
    }, {
        'schema': {
            'codigo':"STRING",
            'nome':"STRING",
        },
        'table': 'motivo',
        'csv': 'MOT*'
    },{
        'schema': {
            'codigo':"STRING",
            'nome':"STRING",
        },
        'table': 'atuacao_juridica',
        'csv': 'ATJU*'
    },{
        'schema': {
            'codigo':"STRING",
            'nome':"STRING",
        },
        'table': 'qualificacao_socio',
        'csv': 'UALS*'
    },{
        'schema': {
            'codigo':"STRING",
            'nome':"STRING",
        },
        'table': 'municipio',
        'csv': 'UNIC*'
    },{
        'schema': {
            'codigo':"STRING",
            'nome':"STRING",
        },
        'table': 'cnae',
        'csv': 'CNAE*'
    }
]

