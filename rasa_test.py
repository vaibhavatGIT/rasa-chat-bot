from rasa_nlu.model import Interpreter

# where model_directory points to the model folder
interpreter = Interpreter.load('./model/example/default/model_20190517-115533')
result = interpreter.parse(u"I am sad")
print(result)
