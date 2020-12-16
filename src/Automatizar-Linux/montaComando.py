comando = 'spark-submit consumer_tbs_spark.py [ambiente] [interface] "" [data]'
data = '20201010'
ambiente = 'dev'

tabelas = [
 'loja_venda'
,'loja_venda_pgto'
,'loja_venda_parcelas'
,'loja_venda_produtos'
,'loja_venda_troca'
,'loja_venda_vendedores'
,'loja_cf_sat'
,'loja_cf_sat_item'
,'loja_cf_sat_imposto'
,'loja_nota_fiscal'
,'loja_nota_fiscal_item'
,'loja_nota_fiscal_imposto'
,'lojas_varejo'
,'cadastro_cli_for'
,'loja_formas_pgto'
,'loja_opercaoes_venda'
,'loja_vendedores'
,'produtos'
,'produtos_grupo'
,'produtos_subgrupo'
,'produtos_linhas'
,'produtos_tipo'
,'produtos_barra'
,'clientes_varejo'
]

for tabela in tabelas:
    comando = comando.replace('[ambiente]', ambiente)
    comando = comando.replace('[interface]', tabela)
    comando = comando.replace('[data]', data)
    print(comando)
    comando = 'spark-submit consumer_tbs_spark.py [ambiente] [interface] "" [data]'
    #spark-submit consumer_tbs_spark.py dev loja_nota_fiscal "" 20201010