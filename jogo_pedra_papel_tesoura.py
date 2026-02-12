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

imprimir = [pedra, papel, tesoura]
 

print(f'''
        JOGO DO PEDRA, PAPEL E TESOURAls
        
            
            Escolha:
            0 para PEDRA
            1 para PAPEL 
            2 para TESOURA
            
            ''')
continuar = "s"
while continuar == "s":
    
    escolha_usuario = int(input("Escolha uma opção: "))
    print(imprimir[escolha_usuario])
    
    #Escolha Aleatoria do computador (0, 1 ou 2)

    escolha_computador = random.randint(0,2)
    print(f"Computador Escolheu: {imprimir[escolha_computador]}")
    
    #Jogo
    if escolha_usuario >= 3:
        print("Você escolheu uma opção errada.")
        break
    
    elif escolha_usuario == 0 and escolha_computador == 2:
        print("Você Ganhou!!")
        
    elif escolha_usuario > escolha_computador:
        print("Você Ganhou!!")
        
    elif escolha_computador == escolha_usuario:
        print("Empate!!")
        
    else:
        print("Você Perdeu!!")
        
    continuar = input("Quer continuar?(S/N): ")

 
