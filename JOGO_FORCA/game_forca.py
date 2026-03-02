import random
#Ou "from palavras_jogo_forca import palavra " Nao precisava colocar na linha 73 "palavras_jogo_forca.palavra" colocaria apenas "palavra"
import palavras_jogo_forca
from logo_jogo_forca import logo_forca

forca = ['''   
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
''','''   
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========
''','''   
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========
''','''   
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
''','''   
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
''','''   
        +---+
        |   |
        O   |
            |
            |
            |
        =========
''','''
        +---+
        |   |
            |
            |
            |
            |
        =========         
'''
]

print(logo_forca)
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
    
    if letra in  letras_corretas:
        print(f"A Letra {letra.upper()} já foi escolhida. Digite OUTRA letra")
        print(f"{forca[lifes]}")
    elif letra in palavra_escohida:
        print(f"A Letra {letra.upper()} está CERTA")
        print(f"{forca[lifes]}")
    else:
        lifes -= 1
        print(f"{forca[lifes]}")   
        if lifes == 0:
            game_over = True
            print("************************You Lose************************")
            print(f"A palavra correta era {palavra_escohida.upper()}")
            break
    
    
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
        print("************************You Win!************************")
        break

    
    
    

    