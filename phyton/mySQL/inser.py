import mysql.connector 

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

console = database.cursor()
console.execute('use teste')
console.execute('create table if not exists pessoas(id int auto_increment primary key, nome varchar(100) not null, nascimento date not null)')

sql = 'insert into pessoas(nome,nascimento) values (%s,%s)'
info = ("Gustavo", '2002-01-01')

console.execute(sql,info)
database.commit()

sql = 'insert into pessoas(nome,nascimento) values (%s,%s)'
info = [("Ana", '2000-02-15'),("Bruno","1997-10-05"),("Carla","2003-07-23")]

console.executemany(sql,info)
database.commit()