comando = 'spark-submit consumer_tbs_spark.py [ambiente] [interface] "" [data]'
data = '20201010'
ambiente = 'dev'

tabelas = [
 
'loja_venda_parcelas'
,'loja_formas_pgto'
,'loja_opercaoes_venda'
,'loja_vendedores'
,'produtos'
,'produtos_grupo'
,'produtos_subgrupo'
,'produtos_linhas'
,'produtos_tipo'
,'produtos_barra'
]

for tabela in tabelas:
    comando = comando.replace('[ambiente]', ambiente)
    comando = comando.replace('[interface]', tabela)
    comando = comando.replace('[data]', data)
    print(comando)
    comando = 'spark-submit consumer_tbs_spark.py -e [ambiente] -a [interface] -b "" -d[data]'
    #spark-submit consumer_tbs_spark.py dev loja_nota_fiscal "" 20201010
    #spark-submit consumer_tbs_spark.py -e dev -a loja_nota_fiscal -b "" -d 20201010