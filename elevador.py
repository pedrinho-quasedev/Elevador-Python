# Sistema de Elevadores

andares_validos = [-2, -1, 0, 1, 2, 3, 4]

# Posição inicial dos elevadores

elevador1 = 0

elevador2 = 0

# Lista de chamadas pendentes

fila_chamadas = []

def escolher_elevador(origem):

    global elevador1, elevador2

    distancia1 = abs(elevador1 - origem)

    distancia2 = abs(elevador2 - origem)

    if distancia1 < distancia2:

        return 1

    elif distancia2 < distancia1:

        return 2

    else:

        # Se a distância for igual, escolhe o elevador 1

        return 1

def mover_elevador(numero, origem, destino):

    global elevador1, elevador2

    if numero == 1:

        print(f"\nElevador 1 está no andar {elevador1}.")

        print(f"Movendo até o andar {origem}...")

        elevador1 = origem

        print(f"Usuário entrou no Elevador 1.")

        print(f"Levando ao andar {destino}...")

        elevador1 = destino

        print(f"Elevador 1 chegou ao andar {destino}.")

    else:

        print(f"\nElevador 2 está no andar {elevador2}.")

        print(f"Movendo até o andar {origem}...")

        elevador2 = origem

        print(f"Usuário entrou no Elevador 2.")

        print(f"Levando ao andar {destino}...")

        elevador2 = destino

        print(f"Elevador 2 chegou ao andar {destino}.")

while True:

    print("\n===== SISTEMA DE ELEVADORES =====")

    print(f"Elevador 1: andar {elevador1}")

    print(f"Elevador 2: andar {elevador2}")

    entrada = input("\nDeseja fazer uma chamada? (S/N): ").upper()

    if entrada == "N":

        print("Sistema encerrado.")

        break

    if entrada != "S":

        print("Entrada inválida!")

        continue

    try:

        origem = int(input("Informe o andar de origem: "))

        destino = int(input("Informe o andar de destino: "))

        # Validação dos andares

        if origem not in andares_validos:

            print("Erro: andar de origem inválido!, andares válidos [-2, -1, 0, 1, 2, 3, 4]")

            continue

        if destino not in andares_validos:

            print("Erro: andar de destino inválido!")

            continue

        fila_chamadas.append((origem, destino))

    except ValueError:

        print("Erro: digite apenas números inteiros.")

        continue

    # Processa todas as chamadas da fila

    while len(fila_chamadas) > 0:

        origem, destino = fila_chamadas.pop(0)

        elevador = escolher_elevador(origem)

        print(f"\nMelhor elevador escolhido: Elevador {elevador}")

        mover_elevador(elevador, origem, destino)