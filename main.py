from modulos.modulo import Modulos, MGPEB

mgpeb = MGPEB()

    # Modulos (nome, tipo, combustível, massa, criticidade)
modulo1 = Modulos("Hab-01", "Habitação", 45, 1200, "Alta")
modulo2 = Modulos("Energia-01", "Energia", 18, 2000, "Alta")
modulo3 = Modulos("Lab-01", "Laboratório", 60, 1500, "Média")
modulo4 = Modulos("Med-01", "Suporte Médico", 55, 1100, "Alta")
modulo5 = Modulos("Log-01", "Logística", 70, 2500, "Média")

mgpeb.classificar_modulo(modulo1)
mgpeb.classificar_modulo(modulo2)
mgpeb.classificar_modulo(modulo3)
mgpeb.classificar_modulo(modulo4)
mgpeb.classificar_modulo(modulo5)

print(mgpeb.count)
print()

prioridade_maxima = mgpeb.localiza_maior()
combustivel_maximo = mgpeb.localiza_maior('combustivel')
massa_maxima = mgpeb.localiza_maior('massa')

prioridade_minima = mgpeb.localiza_menor()
combustivel_minimo = mgpeb.localiza_menor('combustivel')
massa_minima = mgpeb.localiza_menor('massa')
print(f"Prioridade máxima: {prioridade_maxima.nome} - {prioridade_maxima.prioridade}")
print(f"Combustível máximo: {combustivel_maximo.nome} - {combustivel_maximo.combustivel}%")
print(f"Massa máxima: {massa_maxima.nome} - {massa_maxima.massa} kg")
print(f"Prioridade mínima: {prioridade_minima.nome} - {prioridade_minima.prioridade}")
print(f"Combustível mínimo: {combustivel_minimo.nome} - {combustivel_minimo.combustivel}%")
print(f"Massa mínima: {massa_minima.nome} - {massa_minima.massa} kg")

local_tipo = mgpeb.localiza_tipo_carga("Habitação")
print(f" Módulos do tipo 'Habitação': \n{'\n    -'.join([modulo.nome for modulo in local_tipo])}")

#print(mgpeb.peek())
mgpeb.display()
mgpeb.sort_by_priority()
mgpeb.display()