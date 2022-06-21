
import logging
import os
import sys
from typing import Dict

import yaml

logger = logging.getLogger(__name__)


def load_config(config_file_name: str) -> Dict:
    with open(config_file_name, 'r') as config_file:
        try:
            config = yaml.safe_load(config_file) or {}

        except yaml.YAMLError as ex:
            logger.error(ex)
            raise
    return config
