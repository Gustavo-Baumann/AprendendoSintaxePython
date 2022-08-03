import mysql.connector 

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

console = database.cursor()
console.execute('use teste')
console.execute('create table if not exists pessoas(id int auto_increment primary key, nome varchar(100) not null, nascimento date not null)')

sql = 'select * from pessoas where nome = (%s)'
nome = ["Gustavo"]
console.execute(sql,nome)
resultSet = console.fetchone()

print(resultSet)