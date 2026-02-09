# Tradutor de Codigo Morse 
# Devido a ruídos na transmissão do código morse, 
# alguns dos sinais não são tão distinguíveis quanto outros e há momentos em que um [.] parece indistinguível de [-/]. 
# Nestes casos, você anota um [?] para que possa descobrir 
# quais são todas as possibilidades daquela letra para aquela palavra mais tarde

from typing import List

 #Dicionario para os codigos que serão traduzidos
dic_morse = {
    ".": "E",
    "-": "T",
    "..": "I",
    ".-": "A",
    "-.": "N",
    "--": "M",
    "...": "S",
    "..-": "U",
    ".-.": "R",
    ".--": "W",
    "-..": "D",
    "-.-": "K",
    "--.": "G",
    "---": "O"
    }
    
def possibilidades_codigo_morse (sinal: str) -> List[str]:
    
    resultados = [] 
    
    def volta_caminho(atual, i):
        if i == len(sinal):
            if atual in dic_morse:
                resultados.append(dic_morse[atual])
            return
        
        if sinal[i] == "?":
            volta_caminho(atual +".", i + 1)
            volta_caminho(atual +"-", i + 1)
        else:
            volta_caminho(atual+ sinal[i], i + 1)    
            
    volta_caminho("", 0)    
    
    return resultados


print(possibilidades_codigo_morse("."))    

print(possibilidades_codigo_morse("--"))    

print(possibilidades_codigo_morse(".?."))   
