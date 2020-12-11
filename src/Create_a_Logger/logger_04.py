"""
Exemplo 4.

todas as etas do logger

"""

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s'

)

# Console Handle

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# file Handle

fh = logging.FileHandler('log.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
logger.debug(' Teste de log ')