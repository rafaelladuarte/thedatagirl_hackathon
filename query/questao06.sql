--6. Qual a média do capital social das empresas de pequeno porte por natureza jurídica
 
CREATE TABLE `hackathon-a3-data.the_data_girls.q06_capital_social_pequeno_porte` (
   media_capital_social FLOAT64,
   natureza_juridica STRING
);
 
INSERT INTO `hackathon-a3-data.the_data_girls.q06_capital_social_pequeno_porte`
SELECT AVG(CAST(REPLACE(capital_social, ',', '.') AS float64)) AS media_capital_social, natureza_juridica
FROM `hackathon-a3-data.the_data_girls.empresa_estabelecimento`
WHERE porte_empresa = 'EMPRESA DE PEQUENO PORTE'
GROUP BY natureza_juridica