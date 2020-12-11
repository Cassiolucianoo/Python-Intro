"""
Exmplo 2.
Como escrever o log em um arquivo

"""

import logging

logging.basicConfig(filename='Exemplo_2.log',
                    filemode='a',
                    level=logging.INFO)

try:
   1/0
   logging.info('ok')
except:
    logging.warning(' Deu merda')
    pass
finally:input()