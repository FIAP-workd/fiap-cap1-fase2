from modulos.modulo import Modulos, MGPEB

mgpeb = MGPEB()

# Aqui, estamos criando os módulos
modulo1 = Modulos("Hab-01", "Habitação", 45, 1200, "Alta")
modulo2 = Modulos("Energia-01", "Energia", 18, 2000, "Alta")
modulo3 = Modulos("Lab-01", "Laboratório", 60, 1500, "Média")
modulo4 = Modulos("Med-01", "Suporte Médico", 55, 1100, "Alta")
modulo5 = Modulos("Log-01", "Logística", 70, 2500, "Média")

# Classificando os módulos e adicionando no MGPEB
mgpeb.classificar_modulo(modulo1)
mgpeb.classificar_modulo(modulo2)
mgpeb.classificar_modulo(modulo3)
mgpeb.classificar_modulo(modulo4)
mgpeb.classificar_modulo(modulo5)

# Algoritmos de localização por maior ponto
prioridade_maxima = mgpeb.localiza_maior()
combustivel_maximo = mgpeb.localiza_maior('combustivel')
massa_maxima = mgpeb.localiza_maior('massa')

# Algoritmos de localização por menor ponto
prioridade_minima = mgpeb.localiza_menor()
combustivel_minimo = mgpeb.localiza_menor('combustivel')
massa_minima = mgpeb.localiza_menor('massa')
print(f"Prioridade máxima: {prioridade_maxima.nome} - {prioridade_maxima.prioridade}")
print(f"Combustível máximo: {combustivel_maximo.nome} - {combustivel_maximo.combustivel}%")
print(f"Massa máxima: {massa_maxima.nome} - {massa_maxima.massa} kg")
print(f"Prioridade mínima: {prioridade_minima.nome} - {prioridade_minima.prioridade}")
print(f"Combustível mínimo: {combustivel_minimo.nome} - {combustivel_minimo.combustivel}%")
print(f"Massa mínima: {massa_minima.nome} - {massa_minima.massa} kg")

# Algoritmo de localização por tipo
local_tipo = mgpeb.localiza_tipo_carga("Habitação")
print(f" Módulos do tipo 'Habitação': \n{'\n    -'.join([modulo.nome for modulo in local_tipo])}")

# Aqui apresentamos a estrutura encontrada na fila de pouso antes e depois do sort
mgpeb.display()
mgpeb.sort_by_priority()
mgpeb.display()

# Simulação de pouso dos módulos.
print("\n\nPouso dos módulos")
mgpeb.modulos_pousar()

# Funções Matemáticas

# Calculo da altura em função do tempo de descida
# Função utilizada: h(t) = h0 - (1/2) * g * t² (Função quadrática)
def calcular_altura(h0, g, t):
    altura = h0 - (1/2) * g * (t ** 2)
    return max(altura, 0)

# Calculo da variação de temperatura externa com o tempo
# Função utilizada: T(t) = T0 - k * (h0 - (1/2) * g * t²) (Função quadrática)
def calcular_temperatura(T0, k, h0, g, t):
    return T0 - k * (h0 - (1/2) * g * (t ** 2))


# Simulação de pouso ao longo do tempo
def simular_pouso_marte():
    print("\n--- Pouso em Marte ---\n")

    # Parâmetros de Marte
    h0 = 1000       # altura inicial da nave (m)
    g = 3.71        # gravidade de Marte
    T0 = -20        # temperatura próxima do solo
    k = 0.002       # variação térmica

    tempo = 0
    dt = 1

    paraquedas = False
    retrofoguete = False

    while True:
        altura = calcular_altura(h0, g, tempo)
        temperatura = calcular_temperatura(T0, k, h0, g, tempo)

        print(f"Tempo: {tempo}s | Altura: {altura:.2f} m | Temp: {temperatura:.2f}°C")

        # Decisões de engenharia
        # Abrir paraquedas
        if altura <= 400 and altura > 0 and not paraquedas:
            print(">> Abrir paraquedas (atmosfera fraca)")
            paraquedas = True

        # Acionar retrofoguetes
        if altura <= 150 and altura > 0 and not retrofoguete:
            print(">> Acionar retrofoguetes")
            retrofoguete = True

        # Pouso concluído
        if altura == 0:
            print("\n>> Pouso em Marte concluído!")
            break

        tempo += dt

# Executar a simulação
simular_pouso_marte()