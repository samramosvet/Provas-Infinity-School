#CRIANDO A BASE DE DADOS DA LOJA
CREATE DATABASE magazine;

#DEFININDO A BASE DE DADOS COMO PRINCIPAL
USE magazine

#CRIANDO A TABELA DE PRODUTOS
CREATE TABLE produtos(
	cod_produto INT PRIMARY KEY AUTO_INCREMENT,
    produto VARCHAR(50) NOT NULL,
    preco FLOAT NOT NULL,
    descricao VARCHAR(50) NOT NULL,
    categoria VARCHAR(50) NOT NULL
);

#CRIANDO A TABELA DE USUÁRIOS
CREATE TABLE usuarios(
	cod_user INT PRIMARY KEY AUTO_INCREMENT,
    usuario VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
);

#CRIANDO A TABELA DO CARRINHO
CREATE TABLE carrinho(
	cod_produto INT NOT NULL,
    produto VARCHAR(50) NOT NULL,
    preco FLOAT NOT NULL,
    descricao VARCHAR(50) NOT NULL,
    categoria VARCHAR(50) NOT NULL
);

#POPULANDO A TABELA PRODUTOS
INSERT INTO produtos (produto, preco, descricao, categoria) 
VALUES ('TV Samsung 43', '2000', 'TV 4k', 'Eletrônicos'), 
	('TV Samsung 60', '4000', 'TV 8k', 'Eletrônicos'), 
    ('Sanduícheira Arno', '100', 'Série Especial', 'Eletrodomésticos'), 
    ('Ventilador Arno', '150', 'Active Y', 'Eletrodomésticos'), 
    ('Ferro Black & Decker', '200', 'Top Black', 'Eletrodomésticos'),
    ('Microondas Brastemp', '500', 'Active X', 'Eletrodomésticos'), 
    ('Lavadora Brastemp', '1500', 'Active X', 'Eletrodomésticos');
    
#POPULANDO A TABELA USUÁRIOS
INSERT INTO usuarios (usuario, senha, email) 
VALUES ('root', '12345', 'root@gmail.com'), 
	('joseaderaldo', '235689', 'joseaderaldo@gmail.com'), 
    ('aceraspire', '200000', 'aceraspire@gmail.com'), 
    ('samuca', '654321', 'samuca@gmail.com');
    
INSERT INTO usuarios (usuario, senha, email) 
VALUES ('root', '232323', 'root@gmail.com');

SELECT * FROM produtos WHERE cod_produto = 1;

SELECT * FROM usuarios;

SELECT * FROM produtos;

DELETE FROM produtos;

SELECT * FROM carrinho;

DELETE FROM carrinho WHERE cod_produto;

UPDATE usuarios SET usuario = 'root', senha = '12345', email = 'root@gmail.com' WHERE cod_user = 1;
    


