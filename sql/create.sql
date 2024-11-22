CREATE SCHEMA IF NOT EXISTS exercicio;

CREATE TABLE if not exists "exercicio".clube (
	idClube INTEGER NOT NULL,
	cnpjClube VARCHAR(18),
	nomeClube VARCHAR(50),
	apelidoClube VARCHAR(50),
	
	CONSTRAINT PK_CLUBE 
		PRIMARY KEY (idClube)
);

CREATE TABLE if not exists "exercicio".jogador (
	idJogador INTEGER NOT NULL,
	cpfJogador VARCHAR(14),
	nomeJogador VARCHAR(50),
	apelidoJogador VARCHAR(50),
	
	CONSTRAINT PK_MEMBRO
		PRIMARY KEY (idJogador)
);

CREATE table if not exists "exercicio".joga (
	idJogador INTEGER NOT NULL,
	idClube INTEGER NOT NULL,
	dataInicioJoga DATE NOT NULL,
	dataFimJoga DATE,
	salario NUMERIC(10,2),
	CONSTRAINT PK_JOGA 
		PRIMARY KEY (idClube, idJogador, dataInicioJoga),
	CONSTRAINT FK_CLUBE 
		FOREIGN KEY (idClube)
			REFERENCES "exercicio".clube(idClube) 
				ON DELETE CASCADE,
	CONSTRAINT FK_JOGADOR 
		FOREIGN KEY (idJogador)
			REFERENCES "exercicio".jogador(idJogador)
				ON DELETE cascade
);
