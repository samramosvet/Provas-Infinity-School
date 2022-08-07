CREATE DATABASE clientes;

USE clientes;

DROP TABLE usuarios;

SELECT * FROM usuarios;

CREATE TABLE usuarios (
	cod_user INT PRIMARY KEY AUTO_INCREMENT,
    nome_user VARCHAR(55) NOT NULL,
    email_user VARCHAR(55) NOT NULL,
    senha_user VARCHAR(55) NOT NULL,
    data_user VARCHAR(20) NOT NULL
    );
    
INSERT INTO usuarios (nome_user, email_user, senha_user, data_user)
VALUES ('root', 'root@gmail.com', 'root@#123', '07/08/2022');
    




