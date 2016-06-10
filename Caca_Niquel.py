import random
import verificar_apostas
import dificulta_bonus
from menu import *
from ajuda import *
from exibir_sorteio import *

apostas = ['[☺]','[♥]','[♬]','[☀]','[☎]','[☂]','[$]']
pesos = [2,2,2,2,2,2,1]
pontos = 0
moedas = 10
arquivo = open("registro.txt")

menu_cn()
print("")

iniciar = input("Escolha uma opção: ")

while iniciar != "1" and iniciar !="2" and iniciar!="3" and iniciar!="4":
    print("opção invalida, escolha uma opção valida")
    menu_cn()
    iniciar = input("Escolha uma opção: ")

if iniciar == "2":
    helP()
    print("")
    iniciar = input("Digite [1] para jogar ou [3] para sair: ")
    while iniciar!="1" and iniciar!="3":
        iniciar = input("Digite uma opção válida, [1] para jogar ou [3] para sair:")

elif iniciar == "4":
    print("")
    print("REGISTRO DE JOGADORES:")
    open("registro.txt", "r")
    print(arquivo.read())

    arquivo.close()

    print("")
    iniciar = input("Digite [1] para jogar ou [3] para sair: ")
    while iniciar!="1" and iniciar!="3":
        iniciar = input("Digite uma opção válida, [1] para jogar ou [3] para sair:")
        
if iniciar == "1":
    print("")
    print('SEU SALDO INICIAL É DE 10 MOEDAS, BOA SORTE!')
    while(iniciar=='1')and(moedas>0):
        print("")
        tipoaposta=str.lower(input('Digite [T] para apostar trinca ou [P} para apostar par: '))
        while tipoaposta!="t" and tipoaposta!="p":
            tipoaposta=str.lower(input("Informe uma aposta válida, digite [T] para trinca ou [P] para par:"))
        
        if tipoaposta == "t" or tipoaposta == "p":
            valoraposta=0
            while valoraposta == 0:
                try:
                    valoraposta=int(input('Quanto deseja apostar?: '))
                except ValueError:
                    print("Informe um valor válido!")
                
            while valoraposta > moedas or valoraposta < 0:
                print("Atenção: você não pode apostar nem mais, nem menos moedas do que possui")
                print("Nem digitar nada além de números inteiros positivos")
                print("Você tem:",moedas,"moedas")
                try:
                   valoraposta=int(input("Quanto deseja apostar?: "))
                except:
                    print("Informe um valor válido!")
                
            moedas = moedas-valoraposta
            opcoes = dificulta_bonus.gerar_opcoes(apostas,pesos)

            sort1=random.choice(opcoes)
            sort2=random.choice(opcoes)
            sort3=random.choice(opcoes)

            resultado = verificar_apostas.verificar(sort1,sort2,sort3,tipoaposta,apostas)

            if resultado=="trinca":
                moedas=moedas+50
                pontos=pontos+(50*valoraposta)
                sorteio= exibir_resultado(resultado,sort1,sort2,sort3)
                print('você ganhou 50 moedas com a trinca, o premio máximo, seu saldo é:',moedas,'moedas e',pontos,"pontos")

            elif resultado=="trincabonuscifrão":
                moedas=moedas+80
                pontos=pontos+(50*valoraposta)
                sorteio= exibir_resultado(resultado,sort1,sort2,sort3)
                print('você fez uma trinca com o cifrão da prosperidade, ganhou 50 moedas de premio + 30 moedas de bonus, seu saldo é:',moedas,"moedas e",pontos,"pontos")

            elif resultado=="par":
                moedas=moedas+15
                pontos=pontos+(15*valoraposta)
                sorteio= exibir_resultado(resultado,sort1,sort2,sort3)
                print('você ganhou 15 moedas, fez um par, seu saldo é:',moedas,"moedas e",pontos,"pontos")

            elif resultado=="parbonuscifrão":
                moedas=moedas+20
                pontos=pontos+(20*valoraposta)
                sorteio= exibir_resultado(resultado,sort1,sort2,sort3)
                print('você ganhou 10 moedas de bonus com o cifrão da prosperidade + 15 moedas com um par, seu saldo é:',moedas,"moedas e",pontos,"pontos")

            elif resultado=="cifrão":
                moedas=moedas+10
                pontos=pontos+(10*valoraposta)
                sorteio= exibir_resultado(resultado,sort1,sort2,sort3)
                print('você ganhou 10 moedas de bonus com o cifrão da prosperidade seu saldo é:',moedas,"moedas e",pontos,"pontos")

            elif resultado=="perdeu":
                sorteio= exibir_resultado(resultado,sort1,sort2,sort3)
                print('infelizmente você não acertou sua aposta, seu saldo é:',moedas,"moedas e",pontos,"pontos")
                print('')

        if moedas==0:
            print("você perdeu tudo!")
            print("")

        elif moedas > 0:
            iniciar=input('Tecle [1] para continuar ou [3] para sair:')
            while iniciar!="1" and iniciar!="3":
                iniciar=input('Informe uma opção valida, [1] para continuar ou [3] para sair:')

    if pontos > 0:
        print("")
        nome = input("Informe seu nome para nosso registro de jogadores:")
        arquivo = open('registro.txt', 'a')
        arquivo.write("jogador: ")
        arquivo.write(nome)
        arquivo.write(" | Pontos: ")
        arquivo.write(str(pontos))
        arquivo.write("\n")

        arquivo.close()

    print("")
    print("Registro de Jogadores:")
    arquivo = open('registro.txt', 'r')
    print(arquivo.read())

    arquivo.close()
    print("")
    print('seu saldo final foi:%i moedas'%moedas,"e",pontos,"pontos")

        
print('Até a proxima!')            
