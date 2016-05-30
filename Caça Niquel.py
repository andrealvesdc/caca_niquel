import random

def gerar_opcoes(apostas,pesos):
    opcoes = []
    for i in range(len(apostas)):
        for peso in range(pesos[i]):
            opcoes.append(apostas[i])
    return opcoes


apostas = ['(@)','(#)','(%)','(&)','(7)','(A)','{$}','{*}']
pesos = [3,3,3,3,3,3,1,1]

moedas=10
iniciar='sim'
print('##########BEM VINDO AO CAÇA NIQUEL!##########')
print('Seu saldo inicial é de 10 moedas, boa sorte!')
while(iniciar=='sim')and(moedas>0):
    tipoaposta=str.lower(input('Gostaria de apostar em: Par ou Trinca? '))
    if(tipoaposta=='par')or(tipoaposta=='trinca'):
        valoraposta=int(input('Quanto deseja apostar? '))
        while(valoraposta>moedas)or(valoraposta<=0):
            valoraposta=int(input('Informe uma aposta valida: '))
        moedas=moedas-valoraposta
        opcoes = gerar_opcoes(apostas,pesos)

        sort1=random.choice(opcoes)
        sort2=random.choice(opcoes)
        sort3=random.choice(opcoes)
        
        if(sort1==sort2) and (sort2==sort3) and (tipoaposta=='trinca'):
            moedas=moedas+50
            print(sort1, sort2, sort3)
            print('você ganhou 50 moedas com a trinca,',sort1, sort2, sort3, 'o premio maximo, seu saldo é ',moedas,'moedas')
        elif(sort1==sort2) and (tipoaposta=='par'):
            moedas=moedas+15
            print(sort1, sort2, sort3)
            print('você ganhou 15 moedas, fez um par na combinação',sort1, sort2,'seu saldo é ',moedas,'moedas')
        elif(sort1==sort3) and (tipoaposta=='par'):
            moedas=moedas+15
            print(sort1, sort2, sort3)
            print('você ganhou 15 moedas, fez um par na combinação',sort1, sort3,'seu saldo é ',moedas,'moedas')
        elif(sort2==sort3) and (tipoaposta=='par'):
            moedas=moedas+15
            print(sort1, sort2, sort3)
            print('você ganhou 15 moedas, fez um par na combinação',sort2, sort3,'seu saldo é ',moedas,'moedas')
        elif(sort1==apostas[6]):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com o',apostas[6],'sifrão da prosperidade seu saldo é ',moedas,'moedas')
        elif(sort2==apostas[6]):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com o',apostas[6],'sifrão da prosperidade seu saldo é ',moedas,'moedas')
        elif(sort3==apostas[6]):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com o',apostas[6],'sifrão da prosperidade seu saldo é ',moedas,'moedas')
        elif(sort1==apostas[7]):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com a',apostas[7],'estrela da sorte seu saldo é ',moedas,'moedas')
        elif(sort2==apostas[7]):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com a',apostas[7],'estrela da sorte seu saldo é ',moedas,'moedas')
        elif(sort3==apostas[7]):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com a',apostas[7],'estrela da sorte seu saldo é ',moedas,'moedas')
        elif(sort1==apostas[6])and(sort2==apostas[6])and(sort3==apostas[6]):
            moedas=moedas+65
            print(sort1, sort2, sort3)
            print('você fez uma trinca com o',apostas[6],'sifrão da prosperidade, ganhou 50 moedas de premio e mais 15 moedas de bonus, seu saldo é ',moedas,'moedas')
        elif(sort1==apostas[7])and(sort2==apostas[7])and(sort3==apostas[7]):
            moedas=moedas+50
            print(sort1, sort2, sort3)
            print('você fez uma trinca com a',apostas[7],'estrela da sorte,ganhou 50 moedas de premio e mais 15 moedas de bonus, seu saldo é ',moedas,'moedas')
        elif(sort1!=sort2)and(sort2!=sort3)and(sort1!=sort3):
            print(sort1, sort2, sort3)
            print('infelizmente você não acertou sua aposta, seu saldo é ',moedas,'moedas')
    else:
        print('tipo de aposta invalida')
    iniciar=str.lower(input('para continuar digite sim e tecle enter ou tecle enter para sair: '))
else:
    print('seu saldo final foi: ',moedas,'moedas')
    print('Até a proxima!')
