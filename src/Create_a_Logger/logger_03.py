"""
Exemplo 3.
Personalizando alerta de mesangem

"""

import logging

log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s:%(lineno)d'

logging.basicConfig(filename='Exemplo_3.log',
                    filemode='a',
                    level=logging.DEBUG,
                    format=log_format)

logger = logging.getLogger('root')

def add(x: int, y: int) -> int:
    """ Função que efetua a soma de dois números inteiros."""
    if isinstance(x, int) and isinstance(y, int):
        logger.info(f'x: {x} - y: {y}')
        return x + y
    else:
        logger.warning(
            f'x: {x} type: {type(x)} - y: {y} type: {type(y)}'
        )
add(7,7)
add(7.5,9)