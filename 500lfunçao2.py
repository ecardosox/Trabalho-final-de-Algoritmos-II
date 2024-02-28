import pandas as pd # importando os dados do arquivo pelo método 'import panda as pd'

comando = int(input('Informe um valor: 0 para sair, 1 para Relatório do Arquivo Completo, 2 para Relatório do Arquivo com 500 linhas: '))

sair = 0
arqu_total = 1
arq_500 = 2

sim = 1
nao = 2 


if comando not in [sair, arqu_total, arq_500]:
    print('Número digitado incorreto, tente novamente!')


# ARQUIVO COM TODAS AS LINHAS ABAIXO
#-------------------------------------------------------------------------------------------------------------------------------------------------
if comando == sair:
    print('A análise terminou!')