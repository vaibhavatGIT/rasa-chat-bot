from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)
input_channel = SlackInput('xoxb-551832269860-627021224770-Po2SZsbMxw9bzc3cY1jS7FhS' #your bot user authentication token
)
agent.handle_channels([input_channel], 5004, serve_forever=True)
