CREATE DATABASE IF NOT EXISTS singongo;
CREATE USER admin IDENTIFIED BY 'singongo2019';
GRANT ALL ON singongo.* TO admin;
USE singongo;
CREATE TABLE user_rec (
	email	VARCHAR(500)	NOT NULL,
	password	VARCHAR(16)	NOT NULL,
	fname	VARCHAR(100)	NOT NULL,
	lname	VARCHAR(100)	NOT NULL,
	phone_number	CHAR(10)	NULL,
	dob		DATE			NULL,
	CONSTRAINT user_pkey PRIMARY KEY (email),
	CONSTRAINT dob_future CHECK (dob < sysdate())
);

CREATE TABLE admin_rec (
	email	VARCHAR(500)	NOT NULL,
	CONSTRAINT admin_pkey PRIMARY KEY (email),
	CONSTRAINT admin_fkey FOREIGN KEY (email) REFERENCES user_rec(email)
);

CREATE TABLE singer_rec (
	email	VARCHAR(500)	NOT NULL,
	type	VARCHAR(7)	NOT NULL,
	CONSTRAINT singer_pkey PRIMARY KEY (email),
	CONSTRAINT singer_fkey FOREIGN KEY (email) REFERENCES user_rec(email),
	CONSTRAINT singer_type CHECK (type IN ('bass', 'tenor', 'alto', 'soprano'))
);

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

CREATE TABLE access_rec(
	user_email	VARCHAR(500)	NOT NULL,
	file_name	VARCHAR(200)	NOT NULL,
	access_stamp	TIMESTAMP	NOT NULL,
	query_type	VARCHAR(500)	NOT NULL,
	CONSTRAINT acc_pkey PRIMARY KEY (user_email, file_name, access_stamp),
	CONSTRAINT acc_fkey1 FOREIGN KEY (user_email) REFERENCES user_rec(email),
	CONSTRAINT acc_fkey2 FOREIGN KEY (file_name) REFERENCES file_rec(name)
);

CREATE TABLE verification (
	code	CHAR(10)	NOT NULL,
	in_use	BOOLEAN		NOT NULL,
    user_type	VARCHAR(6)	NOT NULL,
	CONSTRAINT verif_pkey PRIMARY KEY(code)
)
