#Definição de funções


# Implementação de fila
def adicionar_consumo(material, horario, fila):
    fila.append({"material": material, "horario": horario})

    return fila


def ler_consumos(fila):
    while fila != []:
        print(f"Material: {fila[0]['material']}\nHorário: {fila[0]['horario']}")
        fila.pop(0)


#Implementação de pilha
def adicionar_consulta(consulta, consumo, pilha):
    pilha.append({"consulta": consulta, "consumo": consumo})

    return pilha


def ler_consultas(pilha):
    while pilha != []:
        info = pilha.pop()
        print(f"Consulta: {info['consulta']}\nConsumo: {info['consumo']}")


def busca_linear(lista, alvo):
    
    for x, y in enumerate(lista):
        if y == alvo:
            return x

    return -1


def busca_binaria(lista, alvo):
    f = len(lista) - 1
    c = 0
    while f > c:
        i_atual = (c+f)//2
        if lista[i_atual] == alvo:
            return i_atual
        elif lista[i_atual] > alvo:
            f = i_atual-1
        elif lista[i_atual] < alvo:
            c = i_atual+1
    return -1


def merge_sort(lista, variavel):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], variavel)
    direita = merge_sort(lista[meio:], variavel)

    return merge(esquerda, direita, variavel)


def merge(esquerda, direita, variavel):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i][variavel] <= direita[j][variavel]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


def quick_sort(lista, variavel):
    if len(lista) <= 1:
        return lista
    menor = []
    maior = []

    for x in lista[1:]:
        if x[variavel] > lista[0][variavel]:
            maior.append(x)
        else:
            menor.append(x)
    final = quick_sort(menor, variavel) + [lista[0]] + quick_sort(maior, variavel)

    return final

#Testes de funções
def testar():
    print("Teste da fila:")
    consumos = []
    adicionar_consumo("gaze", "2:00", consumos)
    adicionar_consumo("seringa", "6:00", consumos)
    adicionar_consumo("agulha", "12:00", consumos)

    ler_consumos(consumos)

    print("\n---------------------\n")

    print("Teste da pilha:")
    consultas = []
    adicionar_consulta("Exame de sangue", "seringa", consultas)
    adicionar_consulta("Ultrassom,", "gel", consultas)
    adicionar_consulta("Exame de urina", "potinho", consultas)

    ler_consultas(consultas)

    print("\n---------------------\n")

    insumos = ["seringa", "agulha", "gaze", "pipeta"]

    print(f"Resultado busca linear: {busca_linear(insumos, 'gaze')}")
    print(f"Resultado busca binária: {busca_binaria(insumos, 'gaze')}")

    print("\n---------------------\n")

    insumos = [
    {"nome": "Álcool", "quantidade": 50, "validade": "2025-12-31"},
    {"nome": "Luvas", "quantidade": 200, "validade": "2024-06-30"},
    {"nome": "Máscara", "quantidade": 150, "validade": "2023-11-15"},
    {"nome": "Água oxigenada", "quantidade": 75, "validade": "2025-01-20"}
    ]

    insumos_ordenados1 = merge_sort(insumos, "quantidade")
    insumos_ordenados2 = quick_sort(insumos, "quantidade")


    print("Resultado do merge sort")
    for x in insumos_ordenados1:
        print(x)
    print("\nResultado do quick sort:")
    for x in insumos_ordenados2:
        print(x)

testar()