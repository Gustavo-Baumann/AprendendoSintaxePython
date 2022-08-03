import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
database = cliente["bancoDados"]
pessoas = database["pessoas"]

listaInfo = [{"nome":"Felipe","peso": 66},{"nome":"Rafael","peso": 63},{"nome":"Leonardo","peso": 71}]

insert = pessoas.insert_many(listaInfo)
print(insert.inserted_ids)