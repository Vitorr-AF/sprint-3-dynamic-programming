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