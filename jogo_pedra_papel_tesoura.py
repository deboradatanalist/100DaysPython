import random


pedra = '''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def imprimir(escolha):
    if escolha == 0:
        print(pedra)
    elif escolha == 1:
        print(papel)
    else:
        print(tesoura)
 
def resultado ():
    print("O Computador escolheu: ")
    imprimir(escolha_computador)
    print("Você escolheu: ")
    imprimir(escolha_usuario)

print(f'''
        JOGO DO PEDRA, PAPEL E TESOURA
            
            Escolha:
            0 para PEDRA
            1 para PAPEL 
            2 para TESOURA
            
            ''')
continuar = "s"
while continuar == "s":
    
    #Escolha Aleatoria do computador (0, 1 ou 2)
    escolha_computador = random.randint(0,2)
    escolha_usuario = int(input("Escolha uma opção: "))
    if escolha_usuario >= 3:
        print("Você escolheu uma opção errada.")
        break
    elif escolha_usuario == 0 and escolha_computador == 2:
        resultado()
        print("Você Ganhou!!")
    elif escolha_usuario > escolha_computador:
        resultado()
        print("Você Ganhou!!")
    elif escolha_computador == escolha_usuario:
        resultado()
        print("Empate!!")
    else:
        resultado()
        print("Você Perdeu!!")
    continuar = input("Quer continuar?(S/N): ")

 
