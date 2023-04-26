
-- Tabela Clientes do ERP
SELECT * FROM db_erp.clientes c ;

SELECT
	id,
	nome ,
	sobrenome,
	email,
	telefone,
	DATE_FORMAT(data_nascimento, '%Y-%m-%d') data_nascimento,
	cidade,
	estado,
	pais,
	codigo_pais,
	DATE_FORMAT(datahora, '%Y-%m-%d %H:%i:%s') datahora
FROM db_erp.clientes
-- WHERE datahora >= NOW() - INTERVAL 1 MINUTE 
-- WHERE id >= False
ORDER BY id;


SELECT
	id,
	nome ,
	sobrenome,
	email,
	telefone,
	DATE_FORMAT(data_nascimento, '%Y-%m-%d') data_nascimento,
	cidade,
	estado,
	pais,
	codigo_pais,
	DATE_FORMAT(datahora, '%Y-%m-%d %H:%i:%s') datahora
FROM db_erp.clientes
${clausula_where_flow}
ORDER BY id;


-- Tabela Vendas do ERP
SELECT * FROM db_erp.vendas v ;

SELECT
	id,
	produto,
	DATE_FORMAT(data_compra, '%Y-%m-%d') data_compra,
	tipo_cartao,
	numero_cartao,
	quantidade,
	valor,
	DATE_FORMAT(datahora, '%Y-%m-%d %H:%i:%s') datahora
FROM db_erp.vendas
-- WHERE datahora >= NOW() - INTERVAL 1 MINUTE 
-- WHERE id >= False
ORDER BY id;

SELECT
	id,
	produto,
	DATE_FORMAT(data_compra, '%Y-%m-%d') data_compra,
	tipo_cartao,
	numero_cartao,
	quantidade,
	valor,
	DATE_FORMAT(datahora, '%Y-%m-%d %H:%i:%s') datahora
FROM db_erp.vendas
${clausula_where_flow}
ORDER BY id;


