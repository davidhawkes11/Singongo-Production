CREATE DATABASE IF NOT EXISTS singongo;
GRANT ALL ON singongo.* TO admin;
USE singongo;

CREATE TABLE file_rec (
	name	VARCHAR(200)	NOT NULL,
	location	VARCHAR(1000)	NOT NULL,
	size	INT				NOT NULL,
	format	VARCHAR(10)		NOT NULL,
	date_added	DATE		NOT NULL,
    file_type	VARCHAR(5)			NOT NULL,
    length		int			NULL,
    num_pages	int			NULL,
    width		int			NULL,
    height		int			NULL,
	CONSTRAINT file_pkey PRIMARY KEY (name),
    CONSTRAINT type_check CHECK (file_type IN ('doc', 'img', 'audio', 'video'))
);