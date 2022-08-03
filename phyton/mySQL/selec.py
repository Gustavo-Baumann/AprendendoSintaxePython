import mysql.connector 

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

console = database.cursor()
console.execute('use teste')
console.execute('create table if not exists pessoas(id int auto_increment primary key, nome varchar(100) not null, nascimento date not null)')

console.execute('select * from pessoas order by nome')
resultSet = console.fetchall()  #ou console.fetchone() para apenas 1 resultado

for result in resultSet:
    print(result)