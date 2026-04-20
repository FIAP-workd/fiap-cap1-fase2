from modulos.fila import Queue
from typing import List
from __future__ import annotations

class Modulos:
    def __init__(self, nome, tipo, combustivel, massa, criticidade, hora_pouso=None):
        self.nome = nome
        self.tipo = tipo
        self.combustivel = combustivel
        self.massa = massa
        self.criticidade = criticidade
        self.pouso = False
        self.pronto_pouso = False
        self.hora_pouso = hora_pouso
        self.prioridade = None

    def definir_prioridade(self):
        return None


class MGPEB:
    def __init__(self):
        self.fila_pouso: Queue()  # queue FIFO
        self.pousados: List[Modulos] = []
        self.em_alerta: List[Modulos] = []
        self.em_espera: List[Modulos] = []
        
    def adicionar_modulo(self, modulo: Modulos):
        self.fila_pouso.push(modulo)
    