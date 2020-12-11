import logging
import time
#<M/D/Y> <H M S AM/PM> <thread number> < file name> <logging level> <message>
#logging.basicConfig(name='meu_projeto_logger',
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(process)d %(filename)s'
                           '%(levelname)s %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    filename='log_info.log',
                    filemode='a')
logging.info('Deu ruim alguma coisa')

LOG = logging.getLogger('meu_projeto_logger')
LOG.info('this is coming from my new logger')
LOG.error('this is an error')
LOG.warning('this is warning')

            




                    