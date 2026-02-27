import random
palavra = ["carro", "moto", "estuda", "menino", "dinheiro", "deus"]
forca = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========
         
''',         '''   
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
        O   |
        |   |
            |
            |
        =========
''',        '''   
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
''',        '''   
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
       / \  |
            |
        =========
'''
]

palavra_escohida= random.choice(palavra)
print(palavra_escohida)

desenho_palavra =""
for espaco in range(len(palavra_escohida)):
    desenho_palavra += "_"
print(desenho_palavra)

game_over = False
letras_corretas = []

while not game_over:
            
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
        
    if "_" not in display:
        game_over = True
        print("You Win!")
    
    print(display)
    