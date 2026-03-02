import random
import palavras_jogo_forca

forca = [
            '''   
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
''', 
        '''   
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
''', 
        '''   
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
''',
        '''   
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
''', 
'''   
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
''',
         '''   
        +---+
        |   |
        O   |
            |
            |
            |
        =========
''' ,        
'''
        +---+
        |   |
            |
            |
            |
            |
        =========
         
'''

]

palavra_escohida= random.choice(palavras_jogo_forca.palavra)


desenho_palavra =""
for espaco in range(len(palavra_escohida)):
    desenho_palavra += "_"
print(desenho_palavra)

game_over = False
lifes = 6
letras_corretas = []

while not game_over:
                
    print(f"You have {lifes}/6 LIVES LEFT")
    
    #inserção do palpite do usuario
    letra = input("Digite uma letra: ").lower()

    #Teste para saber se a letra que o usuario digitou esta na palavra escolhida aleatoriamente pelo programa
    display = ""
    for let in palavra_escohida:
        if let == letra:
            display += letra
            letras_corretas.append(letra)
        elif let in letras_corretas:
            display += let
        else:
            display += "_"
        
    print(display)              
        
    if "_" not in display:
        game_over = True
        print("You Win!")

    if letra in palavra_escohida:
        print(f"A Letra {letra.upper()} está CERTA")
        print(f"{forca[lifes]}")        
    else:
        lifes -= 1
        print(f"{forca[lifes]}")   
        if lifes == 0:
            game_over = True
            print("You Lose")
            print(f"A palavra correta era {palavra_escohida.upper()}")
    
    

    