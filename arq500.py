import pandas as pd # importando os dados do arquivo pelo método 'import as panda'

comando = int(input('Informe um valor: 0 para sair, 1 para Relatório do Arquivo Completo, 2 para Relatório do Arquivo com 500 linhas: '))

sair = 0
arqu_total = 1
arq_500 = 2

sim = 1
nao = 2 

if comando != sair or arqu_total or arq_500:
    print('Número digitado incorreto, tente novamente!')

if comando == arq_500:
    arq = 'dengue500.csv' #ARQUIVO 500 LINHAS
    dados = pd.read_csv(arq) # lendo o arquivo CSV especificado pelo caminho fornecido
    num_linhas = len(dados) 
    colunas_nome = dados.columns.tolist() # transformando os dados em listas

    print('Relatório com número de linhas e o nome das colunas do arquivo:')
    print('------------------------------------------------------------------------------------------------------------------------------------')
    print(f"- Número de linhas: {num_linhas}")
    print("- Nomes das colunas:")
    for coluna in colunas_nome:
        print('•', coluna)
    print('------------------------------------------------------------------------------------------------------------------------------------')

    comando_ssounn = int(input('Para continuar a análise, informe 1 para Sim ou 2 para Não: '))
    if comando_ssounn == nao:
        print('A análise terminou!')
    if comando_ssounn == sim: # se o usuario digitar SIM, irá aparecer tudo o que está indentado
        arq = pd.read_csv('dengue500.csv')
        area = arq['Area de Abrangencia']
        cont = area.value_counts() # conta o numero de vezes que um certo dado aparece
        mais_casos = cont.index[0] # está pegando o dado mais frequente
        print(f'A Área de Abrangência com mais casos é: {mais_casos}')
        print('------------------------------------------------------------------------------------------------------------------------------------')

        arquivo = pd.read_csv('dengue500.csv')
        area = arquivo['Status']
        total_posi = 'POSITIVO'
        quan_total = (area == total_posi).sum() # somatorio da quantidade total de positivos
        print(f'A quantidade total de {total_posi} em Status é: {quan_total}')

        arq = pd.read_csv('dengue500.csv')
        area1 = arq['Status']
        total_nega = 'NEGATIVO' 

        quan_total1 = (area1 == total_nega).sum()
        print(f'A quantidade total de {total_nega} em Status é {quan_total1}')
        print('------------------------------------------------------------------------------------------------------------------------------------')
#------------------------------------------------------------------------------------------------------------------------------------')

        arq = pd.read_csv('dengue500.csv')
        area = arq['Status']
        posi = 'POSITIVO'
        porcen_posi =(area[area == posi].count() / len(area)) * 100 # numero de vezes q tem positivo e multiplica por 100
        print(f'A porcentagem de {posi} é: {porcen_posi:.2f}%')

        arq = pd.read_csv('dengue500.csv')
        area = arq['Status']
        nega = 'NEGATIVO'
        porcen_nega =(area[area == nega].count() / len(area)) * 100
        print(f'A porcentagem de {nega} é: {porcen_nega:.2f}%')
        print('------------------------------------------------------------------------------------------------------------------------------------')
#------------------------------------------------------------------------------------------------------------------------------------')

        arq = pd.read_csv('dengue500.csv')
        print('Para saber a quantidade de casos positivos e negativos entre os dias 09/01/2017 até 11/01/2017: ')

        posi_nega = input('Digite POSITIVO ou NEGATIVO (em maiusculo): ')
        data = input('Digite o dia (entre 09/01/2017 até 11/01/2017): ')

        resul = arq[(arq['Status'] == posi_nega) & (arq['Data da Coleta'] == data)]
        quantidade = len(resul)

        print(f'A quantidade de casos {posi_nega} no dia {data} é de: {quantidade}')

#---------------------------------------------------------------------------------------------------------------------------------------------------------
        dia_citado = int(input('Quer saber o dia mais citado com casos positivos? Informe 1 para Sim ou 2 para Não: '))
        if dia_citado == sim:
            arq = 'dengue500.csv'
            dados = pd.read_csv(arq)
            casos_positivos = dados[dados['Status'] == 'POSITIVO']
            cont_data = casos_positivos['Data da Coleta'].value_counts()
            data_maiscit = cont_data.idxmax()
            print(f'Dia mais citado com casos positivos: {data_maiscit}')
        else:
            print('Número digitado incorreto, tente novamente!')