import logging
import logging.config

logging.config.fileConfig('loggin_com_cmd.ini')

logger = logging.getLogger('root')

logging.info('Peixes')
