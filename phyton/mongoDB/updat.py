import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
database = cliente["bancoDados"]
pessoas = database["pessoas"]

query = {"nome" : "Felipe"}
updatedNome= { "$set" : {"nome" : "Fernando"}}

pessoas.update_one(query,updatedNome)

buscarTodos = pessoas.find({},{"_id" : 0,"nome" : 1,"peso" : 1}).limit(10)

for resultado in buscarTodos:
    print(resultado)