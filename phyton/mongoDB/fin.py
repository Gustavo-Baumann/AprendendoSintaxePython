import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
database = cliente["bancoDados"]
pessoas = database["pessoas"]

busca = pessoas.find_one()
print(busca)

buscarTodos = pessoas.find({},{"_id" : 0,"nome" : 1,"peso" : 1}).sort('nome',1)

for resultado in buscarTodos:
    print(resultado)