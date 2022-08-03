import json
import re

x = '{"nome":"Felipe","peso":72,"cidade":"Belo Horizonte"}'
x = re.sub("Felipe","Bruno",x)
y = json.loads(x)

print(y['nome'],y['peso'],y['cidade'])

x = {"nome":"Felipe", "peso":72, "cidade":"Belo Horizonte"}
y = json.dumps(x)
print("JSON:", y)