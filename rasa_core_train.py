import asyncio

from rasa_core import train, utils
from rasa_core.training import interactive
import logging

logger = logging.getLogger(__name__)


def train_agent(domain_file='domain.yml',
                         stories_file='./data/dialogue/stories.md',
                         model_path='models/current/dialogue',
                         policy_config='config.yml'):
    return  train(domain_file=domain_file,
                       stories_file=stories_file,
                       output_path=model_path,
                       policy_config=policy_config,
                       kwargs={'augmentation_factor': 50,
                               'validation_split': 0.2})


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    agent = train_agent()
    logger.info("Training Success")
