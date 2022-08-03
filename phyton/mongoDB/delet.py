import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
database = cliente["bancoDados"]
pessoas = database["pessoas"]

nome = {"nome" : "Gustavo"}
deletar = pessoas.delete_many(nome)

print(deletar.deleted_count,"instancias excluidas")

#pessoas.drop()  --para deletar a collection