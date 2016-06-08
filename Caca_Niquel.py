import random
import time
import verificar_apostas

def menu_cn():
    print(" ----------------------------------- ")
    print("       BEM VINDO AO CAÇA NIQUEL      ")
    print(" ----------------------------------- ")
    print("    [1] JOGAR      |   [2] HELP      ")
    print(" ----------------------------------- ")
    print("              [3]SAIR                ")
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
    print("em TRINCA ou PAR, se  você  escolher  PAR, só")
    print("ganhara  moedas se  aparecer um par dos  mesmos") 
    print("elementos na tela,Se escolher TRINCA só ganhara")
    print("moedas se aparecer um trio dos mesmos elementos")
    print("                                               ")
    print("depois  você vai dizer o quanto quer apostar, o")
    print("valor não  poderar ser  menor que zero ou maior")
    print("que a quantidade de moedas que você possui.    ")
    print("                                               ")
    print("Se você perder, sera descontado das suas moedas")
    print("a quantia que você  apostou,se for bem sucedido")
    print("no  sorteio podera ganhar  10 moedas, 15 moedas")
    print("ou 50 moedas. vai depender do resultado.       ")
    print("Se no  sorteio aparecer um [$] ou uma [☆] você")
    print("ganhara 10 moedas de bonus automatimente."      )
    print("                                               ")
    print("os pontos são o valor do premio em moedas vezes")
    print("o valor de moedas apostado.                    ")
    print("-----------------------------------------------")

apostas = ['[☺]','[♥]','[♬]','[☀]','[☎]','[☂]','[$]']
pesos = [2,2,2,2,2,2,1]
       
def gerar_opcoes(apostas,pesos):
    opcoes = []
    for i in range(len(apostas)):
        for peso in range(pesos[i]):
            opcoes.append(apostas[i])
    return opcoes


pontos = 0
moedas = 10

menu_cn()
print("")

iniciar = input("Escolha uma opção: ")

while iniciar != "1" and iniciar !="2" and iniciar!="3":
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
        tipoaposta=str.lower(input('Gostaria de apostar em Trinca ou Par?: '))
        
        if(tipoaposta=='trinca')or(tipoaposta=='par'):
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

            resultado = verificar_apostas.verificar(sort1,sort2,sort3,tipoaposta,apostas)

            if resultado=="trinca":
                moedas=moedas+50
                pontos=pontos+(50*valoraposta)
                print("sorteando...")
                time.sleep(2)
                print(sort1)
                time.sleep(2)
                print(sort2)
                time.sleep(3)
                print(sort3)
                time.sleep(2)
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 50 moedas com a trinca, o premio máximo, seu saldo é:',moedas,'moedas e',pontos,"pontos")

            elif resultado=="trincabonuscifrão":
                moedas=moedas+80
                pontos=pontos+(50*valoraposta)
                print("sorteando...")
                time.sleep(2)
                print(sort1)
                time.sleep(2)
                print(sort2)
                time.sleep(3)
                print(sort3)
                time.sleep(2)
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você fez uma trinca com o cifrão da prosperidade, ganhou 50 moedas de premio + 30 moedas de bonus, seu saldo é:',moedas,"moedas e",pontos,"pontos")


            elif resultado=="par":
                moedas=moedas+15
                pontos=pontos+(15*valoraposta)
                print("sorteando...")
                time.sleep(2)
                print(sort1)
                time.sleep(2)
                print(sort2)
                time.sleep(3)
                print(sort3)
                time.sleep(2)
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 15 moedas, fez um par, seu saldo é:',moedas,"moedas e",pontos,"pontos")

            elif resultado=="parbonuscifrão":
                moedas=moedas+20
                pontos=pontos+(20*valoraposta)
                print("sorteando...")
                time.sleep(2)
                print(sort1)
                time.sleep(2)
                print(sort2)
                time.sleep(3)
                print(sort3)
                time.sleep(2)
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 10 moedas de bonus com o cifrão da prosperidade + 15 moedas com um par, seu saldo é:',moedas,"moedas e",pontos,"pontos")
                

            elif resultado=="cifrão":
                moedas=moedas+10
                pontos=pontos+(10*valoraposta)
                print("sorteando...")
                time.sleep(2)
                print(sort1)
                time.sleep(2)
                print(sort2)
                time.sleep(3)
                print(sort3)
                time.sleep(2)
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('você ganhou 10 moedas de bonus com o cifrão da prosperidade seu saldo é:',moedas,"moedas e",pontos,"pontos")


            elif resultado=="perdeu":
                print("sorteando...")
                time.sleep(2)
                print(sort1)
                time.sleep(2)
                print(sort2)
                time.sleep(3)
                print(sort3)
                time.sleep(2)
                print("")
                print("-----RESULTADO-----")
                print("   ",sort1, sort2, sort3,"  ")
                print("-------------------")
                print("")
                print('infelizmente você não acertou sua aposta, seu saldo é:',moedas,"moedas e",pontos,"pontos")



        else:
            print('tipo de aposta invalida')
        if moedas==0:
            print("você perdeu tudo!")
        elif moedas>0:
            iniciar=str.lower(input('Tecle [1] para continuar ou [3] para sair:'))
    if pontos > 0:
        nome = input("Informe seu nome para nosso registro de jogadores:")
        arquivo = open('registro.txt', 'a')
        arquivo.write("jogador: ")
        arquivo.write(nome)
        arquivo.write(" | Pontos: ")
        arquivo.write(str(pontos))
        arquivo.write("\n")

        arquivo.close()
        
        
    else:
        print("")
        print('seu saldo final foi:%i moedas'%moedas,"e",pontos,"pontos")
        
print('Até a proxima!')            
