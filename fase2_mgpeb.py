# MGPEB
# Gerenciamento de Pouso e Estabilização de Base
# Projeto Aurora Siger

# Cada módulo será representado por um dicionário
def criar_modulo(nome, tipo, prioridade, combustivel, massa, criticidade, horario_chegada):
    modulo = {
        "nome": nome,
        "tipo": tipo,
        "prioridade": prioridade,
        "combustivel": combustivel,
        "massa": massa,
        "criticidade": criticidade,
        "horario_chegada": horario_chegada
    }
    return modulo


# Fila principal de módulos aguardando pouso
fila_pouso = []

# Listas auxiliares
modulos_pousados = []
modulos_espera = []
modulos_alerta = []


# Função para adicionar módulo na fila principal
def adicionar_na_fila(modulo):
    fila_pouso.append(modulo)


# Função para mostrar módulos de uma estrutura
def exibir_modulos(lista, titulo):
    print(f"\n--- {titulo} ---")
    if len(lista) == 0:
        print("Nenhum módulo nesta estrutura.")
    else:
        for i, modulo in enumerate(lista, start=1):
            print(f"{i}. Nome: {modulo['nome']}")
            print(f"   Tipo: {modulo['tipo']}")
            print(f"   Prioridade: {modulo['prioridade']}")
            print(f"   Combustível: {modulo['combustivel']}%")
            print(f"   Massa: {modulo['massa']} kg")
            print(f"   Criticidade: {modulo['criticidade']}")
            print(f"   Horário de chegada: {modulo['horario_chegada']}")
            print()


# Função simples para analisar situação do módulo
def classificar_modulo(modulo):
    if modulo["combustivel"] < 20:
        modulos_alerta.append(modulo)
    elif modulo["prioridade"] >= 8:
        modulos_espera.append(modulo)
    else:
        adicionar_na_fila(modulo)


# Cadastro inicial de módulos
modulo1 = criar_modulo("Hab-01", "Habitação", 9, 45, 1200, "Alta", "10:30")
modulo2 = criar_modulo("Energia-01", "Energia", 10, 18, 2000, "Alta", "10:40")
modulo3 = criar_modulo("Lab-01", "Laboratório", 7, 60, 1500, "Média", "11:00")
modulo4 = criar_modulo("Med-01", "Suporte Médico", 8, 55, 1100, "Alta", "11:10")
modulo5 = criar_modulo("Log-01", "Logística", 5, 70, 2500, "Média", "11:20")


# Classificação inicial
classificar_modulo(modulo1)
classificar_modulo(modulo2)
classificar_modulo(modulo3)
classificar_modulo(modulo4)
classificar_modulo(modulo5)


# Exibição dos dados
exibir_modulos(fila_pouso, "Fila Principal de Pouso")
exibir_modulos(modulos_espera, "Módulos em Espera")
exibir_modulos(modulos_alerta, "Módulos em Alerta")
exibir_modulos(modulos_pousados, "Módulos Já Pousados")