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


class MGPEB:
    def __init__():
        self.fila_pouso: deque[Modulo] = deque()  # queue FIFO
        self.pousados: List[Modulo] = []
        self.em_alerta: List[Modulo] = []
        self.em_espera: List[Modulo] = []
        self._index: Dict[str, Modulo] = {}
        self._pilha_logs: List[str] = []  # pilha = registra eventos LIFO