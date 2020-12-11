"""
Exmplo 2.
Como escrever o log em um arquivo
"""

import logging

logging.basicConfig(filename='Exemplo_2.log',
                    filemode='a',
                    level=logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)
# logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                    datefmt='%m-%d %H:%M',
#                    filename='/temp/myapp.log',
#                    filemode='w')

try:
   1/0
   logging.info('ok')
except:
    logging.warning(' Deu merda')
    pass
finally:input()