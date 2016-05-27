import random
ap1='(@)'
ap2='(#)'
ap3='(%)'
ap4='(&)'
ap5='(7)'
ap6='(A)'
ap7='{$}'
ap8='{*}'
moedas=7
iniciar='sim'
print('##########BEM VINDO AO CAÇA NIQUEL!##########')
print('Seu saldo inicial é de 7 moedas, boa sorte!')
while(iniciar=='sim')and(moedas>0):
    tipoaposta=str.lower(input('Gostaria de apostar em: Par ou Trinca? '))
    if(tipoaposta=='par')or(tipoaposta=='trinca'):
        valoraposta=int(input('Quanto deseja apostar? '))
        moedas=moedas-valoraposta
        sort1=random.choice([ap1,ap2,ap3,ap4,ap5,ap6,ap1,ap2,ap3,ap4,ap5,ap6,ap1,ap2,ap3,ap4,ap5,ap6,ap7,ap8])
        sort2=random.choice([ap1,ap2,ap3,ap4,ap5,ap6,ap1,ap2,ap3,ap4,ap5,ap6,ap1,ap2,ap3,ap4,ap5,ap6,ap7,ap8])
        sort3=random.choice([ap1,ap2,ap3,ap4,ap5,ap6,ap1,ap2,ap3,ap4,ap5,ap6,ap1,ap2,ap3,ap4,ap5,ap6,ap7,ap8])
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
        elif(sort1==ap7):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com o',ap7,'sifrão da prosperidade seu saldo é ',moedas,'moedas')
        elif(sort2==ap7):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com o',ap7,'sifrão da prosperidade seu saldo é ',moedas,'moedas')
        elif(sort3==ap7):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com o',ap7,'sifrão da prosperidade seu saldo é ',moedas,'moedas')
        elif(sort1==ap8):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com a',ap8,'estrela da sorte seu saldo é ',moedas,'moedas')
        elif(sort2==ap8):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com a',ap8,'estrela da sorte seu saldo é ',moedas,'moedas')
        elif(sort3==ap8):
            moedas=moedas+5
            print(sort1, sort2, sort3)
            print('você ganhou 5 moedas de bonus com a',ap8,'estrela da sorte seu saldo é ',moedas,'moedas')
        elif(sort1==ap7)and(sort2==ap7)and(sort3==ap7):
            moedas=moedas+65
            print(sort1, sort2, sort3)
            print('você fez uma trinca com o',ap7,'sifrão da prosperidade, ganhou 50 moedas de premio e mais 15 moedas de bonus, seu saldo é ',moedas,'moedas')
        elif(sort1==ap8)and(sort2==ap8)and(sort3==ap8):
            moedas=moedas+50
            print(sort1, sort2, sort3)
            print('você fez uma trinca com a',ap8,'estrela da sorte,ganhou 50 moedas de premio e mais 15 moedas de bonus, seu saldo é ',moedas,'moedas')
        elif(sort1!=sort2)and(sort2!=sort3)and(sort1!=sort3):
            print(sort1, sort2, sort3)
            print('infelizmente você não acertou sua aposta, seu saldo é ',moedas,'moedas')
    else:
        print('tipo de aposta invalida')
    iniciar=str.lower(input('para continuar digite sim e tecle enter ou tecle enter para sair: '))
else:
    print('seu saldo final foi: ',moedas,'moedas')
    print('Até a proxima!')
