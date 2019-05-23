from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config

training_data = load_data('data/nlu')
trainer = Trainer(config.load("nlu_config.yml"))
trainer.train(training_data)
model_directory = trainer.persist('./models/current')  # Returns the directory the model is stored in
print(model_directory)
