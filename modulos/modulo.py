from __future__ import annotations
from modulos.fila import Queue
import numpy as np
from typing import List
import datetime

class Modulos:
    def __init__(self, nome, tipo, combustivel, massa, criticidade, hora_pouso=None):
        self.nome: str = nome
        self.tipo: str = tipo
        self.combustivel: int = combustivel
        self.massa: int = massa
        self.criticidade: str = criticidade
        self.pouso: bool = False
        self.pronto_pouso: bool = False
        self.hora_pouso: datetime = hora_pouso
        self.prioridade: int = self.prioridade()

    def prioridade(self):
        def limitar_0_10(valor):
            return max(0.0, min(10.0, float(valor)))

        # Criticidade aceita texto (baixa/média/alta) ou valor numérico.
        if isinstance(self.criticidade, str):
            mapa_criticidade = {
                "baixa": 3,
                "media": 7,
                "média": 7,
                "alta": 10,
            }
            nota_criticidade = mapa_criticidade.get(self.criticidade.strip().lower(), 5)
        else:
            nota_criticidade = limitar_0_10(self.criticidade)

        # Quanto menos combustível, maior a urgência.
        nota_combustivel = limitar_0_10(10 - (float(self.combustivel) / 10))

        # Normalização simples de massa (0 kg -> 0, 3000 kg ou mais -> 10)
        nota_massa = limitar_0_10((float(self.massa) / 3000) * 10)

        prioridade = (
            (nota_criticidade * 0.5)
            + (nota_combustivel * 0.3)
            + (nota_massa * 0.2)
        )

        return int(round(limitar_0_10(prioridade)))

    def __str__(self):
        return self.nome


class MGPEB:
    def __init__(self):
        self.lista_modulos: List[Modulos] = []
        self.fila_pouso: Queue = Queue()  # queue FIFO
        self.pousados: List[Modulos] = []
        self.em_alerta: List[Modulos] = []
        self.em_espera: List[Modulos] = []
        
    def adicionar_modulo(self, modulo: Modulos):
        self.fila_pouso.push(modulo)
        self.lista_modulos.append(modulo)

    def classificar_modulo(self, modulo: Modulos):
        if modulo.combustivel < 20:
            self.em_alerta.append(modulo)
        elif modulo.prioridade >= 8:
            self.em_espera.append(modulo)
        else:
            self.adicionar_modulo(modulo)

    def localiza_menor(self, atributo = 'prioridade'):
        """Algoritmo com complexidade O(n)"""
        if atributo not in ['combustivel', 'massa', 'prioridade']:
            raise Exception(f"Atributo {atributo} não possui formas de se capturar o menor valor.")
        
        menor_valor = np.inf
        modulo_menor = None
        for modulo in self.lista_modulos:
            valor_atributo = getattr(modulo, atributo)
            if valor_atributo < menor_valor:
                menor_valor = valor_atributo
                modulo_menor = modulo
        return modulo_menor
    
    def localiza_maior(self, atributo = 'prioridade'):
        """Algoritmo com complexidade O(n)"""
        if atributo not in ['combustivel', 'massa', 'prioridade']:
            raise Exception(f"Atributo {atributo} não possui formas de se capturar o menor valor.")
        
        maior_valor = 0
        modulo_maior = None
        for modulo in self.lista_modulos:
            valor_atributo = getattr(modulo, atributo)
            if valor_atributo > maior_valor:
                maior_valor = valor_atributo
                modulo_maior = modulo
        return modulo_maior

    def localiza_tipo_carga(self, tipo_carga):
        """Algoritmo com complexidade O(n)"""
        lista_modulos_carga = []
        
        for modulo in self.lista_modulos:
            valor_atributo = modulo.tipo
            if valor_atributo == tipo_carga:
                lista_modulos_carga.append(modulo)

        if lista_modulos_carga:
            return lista_modulos_carga
        else:
            raise Exception(f"Tipo de carga {tipo_carga} não encontrado nos módulos.")

