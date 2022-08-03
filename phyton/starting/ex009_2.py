import starting.ex009_1 as ex009_1
import datetime

print(datetime.datetime.now().year)
print(ex009_1.somar(5,10))
print(ex009_1.gritar("banana"))
print(ex009_1.converterParaInt(3.3))

umDiaQualquer = datetime.datetime(1,1,1)
print(umDiaQualquer)
print(umDiaQualquer.strftime("%A"))