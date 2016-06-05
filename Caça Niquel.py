import random

def menu_cn():
    print(" ----------------------------------- ")
    print("       BEM VINDO AO CAÇA NIQUEL      ")
    print(" ----------------------------------- ")
    print("    [1] JOGAR      |   [2] HELP      ")
    print(" ----------------------------------- ")

def helP():
    print("-------------------------------------")
    print("               |HELP|                ")
    print("-------------------------------------")
    print("     |INSTRUÇÕES DE COMO JOGAR|      ")
    print("-----------------------------------------------")
    print("Ao iniciar o jogo você  já começa com 10 moedas")
    print("                                               ")
    print("em seguida você  podera escolhe se quer apostar")
    print("em  PAR ou TRINCAR, se  você  escolher  PAR, só")
    print("ganhara  moedas se  aparecer um par dos  mesmos") 
    print("elementos na tela, Se escolher TRINCA só ganhara")
    print("moedas se aparecer um trio dos mesmos elementos")
    print("                                               ")
    print("depois  você vai dizer o quanto quer apostar, o")
    print("valor não  poderar ser  menor que zero ou maior")
    print("que a quantidade de moedas que você possui.    ")
    print("                                               ")
    print("Se você perder, sera descontado das suas moedas")
    print("a quantia que você  apostou,se for bem sucedido")
    print("no  sorteio  podera ganhar  5 moedas, 15 moedas")
    print("ou 50 moedas. vai depender do resultado.       ")
    print("Se no  sorteio aparecer um [$] ou uma [☆] você")
    print("ganhara 5 moedas automatimente.                ")
    print("-----------------------------------------------")
    
    
def gerar_opcoes(apostas,pesos):
    opcoes = []
    for i in range(len(apostas)):
        for peso in range(pesos[i]):
            opcoes.append(apostas[i])
    return opcoes


apostas = ['[☺]','[♥]','[♬]','[☀]','[☎]','[☂]','[$]','[☆]']
pesos = [3,3,3,3,3,3,1,1]

moedas = 10
menu_cn()
print("")

iniciar = input("Escolha uma opção: ")

while iniciar != "1" and iniciar !="2":
    print("opção invalida, escolha uma opção valida")
    menu_cn()
    iniciar = input("Escolha uma opção: ")
    
while iniciar == "2":
    helP()
    menu_cn()
    print("")
    iniciar = input("Escolha uma opção: ")
    
if iniciar == "1":
    print("")
    print('SEU SALDO INICIAL É DE 10 MOEDAS, BOA SORTE!')
    while(iniciar=='1')and(moedas>0):
        print("")
        tipoaposta=str.lower(input('Gostaria de apostar em: Par ou Trinca? '))
        
        if(tipoaposta=='par')or(tipoaposta=='trinca'):
            valoraposta=0
            while valoraposta==0:
                try:
                    valoraposta=int(input('Quanto deseja apostar? '))
                except ValueError:
                    print("Informe um valor valido")
                
            while(valoraposta>moedas)or(valoraposta<=0):
                print("Atenção você tem %i moedas!" % moedas)
                valoraposta=int(input('Faça uma aposta valida: '))
                
            moedas = moedas-valoraposta
            opcoes = gerar_opcoes(apostas,pesos)

            sort1=random.choice(opcoes)
            sort2=random.choice(opcoes)
            sort3=random.choice(opcoes)

            if(sort1==sort2) and (sort2==sort3) and (tipoaposta=='trinca'):
                moedas=moedas+50
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 50 moedas com a trinca,',sort1, sort2, sort3, 'o premio maximo, seu saldo é ',moedas,'moedas')
                
            elif(sort1==sort2) and (tipoaposta=='par'):
                moedas=moedas+15
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 15 moedas, fez um par na combinação',sort1, sort2,'seu saldo é ',moedas,'moedas')
                
            elif(sort1==sort3) and (tipoaposta=='par'):
                moedas=moedas+15
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 15 moedas, fez um par na combinação',sort1, sort3,'seu saldo é ',moedas,'moedas')
                
            elif(sort2==sort3) and (tipoaposta=='par'):
                moedas=moedas+15
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 15 moedas, fez um par na combinação',sort2, sort3,'seu saldo é ',moedas,'moedas')
                
            elif(sort1==apostas[6]):
                moedas=moedas+5
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 5 moedas de bonus com o',apostas[6],'sifrão da prosperidade seu saldo é ',moedas,'moedas')
                
            elif(sort2==apostas[6]):
                moedas=moedas+5
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 5 moedas de bonus com o',apostas[6],'sifrão da prosperidade seu saldo é ',moedas,'moedas')
                
            elif(sort3==apostas[6]):
                moedas=moedas+5
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 5 moedas de bonus com o',apostas[6],'sifrão da prosperidade seu saldo é ',moedas,'moedas')
                
            elif(sort1==apostas[7]):
                moedas=moedas+5
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 5 moedas de bonus com a',apostas[7],'estrela da sorte seu saldo é ',moedas,'moedas')
                
            elif(sort2==apostas[7]):
                moedas=moedas+5
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 5 moedas de bonus com a',apostas[7],'estrela da sorte seu saldo é ',moedas,'moedas')
                
            elif(sort3==apostas[7]):
                moedas=moedas+5
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 5 moedas de bonus com a',apostas[7],'estrela da sorte seu saldo é ',moedas,'moedas')
                
            elif(sort1==apostas[6])and(sort2==apostas[6])and(sort3==apostas[6]):
                moedas=moedas+65
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você fez uma trinca com o',apostas[6],'sifrão da prosperidade, ganhou 50 moedas de premio e mais 15 moedas de bonus, seu saldo é ',moedas,'moedas')
                
            elif(sort1==apostas[7])and(sort2==apostas[7])and(sort3==apostas[7]):
                moedas=moedas+50
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você fez uma trinca com a',apostas[7],'estrela da sorte,ganhou 50 moedas de premio e mais 15 moedas de bonus, seu saldo é ',moedas,'moedas')
                
            elif(sort1!=sort2)and(sort2!=sort3)and(sort1!=sort3):
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('infelizmente você não acertou sua aposta, seu saldo é ',moedas,'moedas')
                
        else:
            print('tipo de aposta invalida')
        iniciar=str.lower(input('para continuar digite 1 e tecle enter ou apenas tecle enter para sair: '))
        
    else:
        print("")
        print('seu saldo final foi:%i moedas'%moedas)
        
print('Até a proxima!')
            
