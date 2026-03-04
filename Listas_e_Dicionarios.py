# ================================
# DICIONÃRIOS E LISTAS DE DADOS EM PYTHON
# ================================

# Lista chamada 'escola' que contÃ©m dicionÃ¡rios
# Cada dicionÃ¡rio representa uma aluna com seus atributos
escola = [
    {
        "nome": "Ana",
        "idade": 45,
        "curso": "Python",
        "status": True  # True significa ativa, False inativa
    },
    {
        "nome": "Cynthia",
        "idade": 34,
        "curso": "C#",
        "status": True
    },
    {
        "nome": "Clarice",
        "idade": 23,
        "curso": "Dados",
        "status": False
    }
]

# ================================
# ACESSANDO ELEMENTOS
# ================================

# Podemos acessar uma aluna pelo Ã­ndice da lista
# aluna = escola[2]
# print(aluna)

# Mostra toda a lista de dicionÃ¡rios
# print(escola)

# ================================
# PERCORRENDO A LISTA COM FOR
# ================================

# Aqui usamos um for para percorrer cada dicionÃ¡rio dentro da lista
for aluna in escola:
    # Verifica se o nome da aluna Ã© "Cynthia"
    if aluna["nome"] == "Cynthia":
        # Exibe informaÃ§Ãµes da aluna encontrada
        print(f"Nome: {aluna['nome']}")
        print(f"Curso: {aluna['curso']}")

# ================================
# EXPLICAÇÕES DIDÁTICAS
# ================================

# 1. Cada item da lista 'escola' Ã© um dicionÃ¡rio
# 2. Cada dicionÃ¡rio contÃ©m pares chave:valor (ex: "nome":"Ana")
# 3. Para acessar um valor, usamos aluna["nome"] ou aluna["curso"]
# 4. Podemos filtrar ou aplicar condiÃ§Ãµes usando if dentro do for