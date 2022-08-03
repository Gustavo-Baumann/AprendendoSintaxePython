import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
database = cliente["bancoDados"]
pessoas = database["pessoas"]

pessoa1 = {"nome":"Gustavo","peso": 58}
insert = pessoas.insert_one(pessoa1)
print(insert.inserted_id)

listaDBs = cliente.list_database_names()
print(listaDBs)
listaCollections = database.list_collection_names()
print(listaCollections)