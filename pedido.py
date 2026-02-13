n = int(input())

# Dicionário para armazenar totais por tipo de embalagem
totais = {
    "saco": 0,
    "papelao ondulado": 0,
    "papel kraft":0
}

# Processa cada pedido
for _ in range(n):
    linha = input()
    cliente, embalagem, quantidade = linha.split(", ")
    quantidade = float(quantidade)
    
    # TODO: Some a quantidade ao tipo de embalagem correspondente
    totais[embalagem] += quantidade
    

# Imprime o resultado no formato solicitado, mantendo a ordem "saco", "papelao ondulado", "papel kraft"
for tipo in ["saco", "papelao ondulado", "papel kraft"]:
    print(f"{tipo}: {int(totais[tipo]) if tipo in totais and totais[tipo].is_integer() else totais.get(tipo, 0)}")