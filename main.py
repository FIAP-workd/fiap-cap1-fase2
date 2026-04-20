from modulos.modulo import Modulos, MGPEB

mgpeb = MGPEB()

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


prioridade_maxima = mgpeb.localiza_maior()
print("Minimo")
print(prioridade_maxima)

prioridade_minima = mgpeb.localiza_menor()
print("Máximo")
print(prioridade_minima)

local_tipo = mgpeb.localiza_tipo_carga("Habitação")
print("Tipo")
print(", ".join([modulo.__str__() for modulo in local_tipo]))

