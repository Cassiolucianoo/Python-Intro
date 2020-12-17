
#aws s3 cp s3://natura-datalake-dev/landing/linx.loja_cf_sat_imposto-20201010/ 
# /home/237435195/linx.loja_cf_sat_imposto-20201010/ --recursive

comando = 'aws s4 cp s4://natural-datalake-dev/landing/linx.[interface]-[data]/ /home/237435195/linx.[interface]-[data]/ --recursive'
data = '20201010'
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
    comando = comando.replace('[interface]', tabela)
    comando = comando.replace('[data]', data)
    print(comando)
    comando = 'aws s4 cp s4://natural-datalake-dev/landing/linx.[interface]-[data]/ /home/237435195/linx.[interface]-[data]/ --recursive'
    #spark-submit consumer_tbs_spark.py dev loja_nota_fiscal "" 20201010