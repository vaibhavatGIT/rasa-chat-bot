from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")
message = "i am from delhi"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))


message = "from Rajasthan"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))

message = "Delhi please"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))


message = "i am searching for Telangana"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))
