from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Callable
from collections import deque

# ============================
# Modelos de dados
# ============================
@dataclass
class Modulo:
    nome: str
    tipo: str
    prioridade: int  # 1-10 (10 = mais urgente)
    combustivel: int  # percentual restante
    massa: float  # kg
    criticidade: str  # baixa, media, alta
    horario_chegada: str  # HH:MM
    sensores_ok: bool = True
    integridade_carga: bool = True

    def __post_init__(self):
        self.criticidade = self.criticidade.lower()


# ============================
# Regras booleanas de autorizacao de pouso
# ============================
def regra_autorizacao(modulo: Modulo, clima_ok: bool, area_disponivel: bool) -> bool:
    """
    Exemplo de expressao booleana combinando AND / OR / NOT:
    - combustivel suficiente AND sensores ok AND area disponivel AND clima ok
    - bloqueia pouso se criticidade alta e combustivel < 15%
    """
    combustivel_ok = modulo.combustivel >= 15
    criticidade_bloqueio = modulo.criticidade == "alta" and modulo.combustivel < 15

    return (
        combustivel_ok
        and modulo.sensores_ok
        and modulo.integridade_carga
        and area_disponivel
        and clima_ok
        and not criticidade_bloqueio
    )


# ============================
# Gerenciador principal
# ============================
class MGPEB:
    def __init__(self):
        self.fila_pouso: deque[Modulo] = deque()  # queue FIFO
        self.pousados: List[Modulo] = []
        self.em_alerta: List[Modulo] = []
        self.em_espera: List[Modulo] = []
        self._index: Dict[str, Modulo] = {}
        self._pilha_logs: List[str] = []  # pilha = registra eventos LIFO

    def registrar_modulo(self, modulo: Modulo):
        if modulo.nome in self._index:
            raise ValueError(f"Modulo {modulo.nome} ja existe")
        self._index[modulo.nome] = modulo
        self._classificar(modulo)
        self._log(f"registrado {modulo.nome} ({modulo.tipo})")

    def _classificar(self, modulo: Modulo):
        if modulo.combustivel < 20:
            self.em_alerta.append(modulo)
        elif modulo.criticidade == "alta":
            self.em_espera.append(modulo)
        else:
            self.fila_pouso.append(modulo)

    # --------- buscas e ordenacao ---------
    def buscar_por_tipo(self, tipo: str) -> List[Modulo]:
        return [m for m in self._index.values() if m.tipo.lower() == tipo.lower()]

    def modulo_menor_combustivel(self) -> Modulo | None:
        return min(self._index.values(), key=lambda m: m.combustivel, default=None)

    def modulo_maior_prioridade(self) -> Modulo | None:
        return max(self._index.values(), key=lambda m: m.prioridade, default=None)

    def ordenar_fila(self, chave: Callable[[Modulo], int] | None = None, reverso: bool = True):
        """Reordena a fila principal de pouso (default: maior prioridade primeiro)."""
        chave = chave or (lambda m: m.prioridade)
        ordenada = sorted(list(self.fila_pouso), key=chave, reverse=reverso)
        self.fila_pouso = deque(ordenada)
        self._log("fila_pouso reordenada")

    # --------- simulacao de pouso ---------
    def autorizar_proximo(self, clima_ok: bool, area_disponivel: bool) -> bool:
        if not self.fila_pouso:
            return False
        modulo = self.fila_pouso[0]
        if regra_autorizacao(modulo, clima_ok, area_disponivel):
            self._executar_pouso(modulo)
            return True
        else:
            # move para espera se nao autorizado
            self.fila_pouso.popleft()
            self.em_espera.append(modulo)
            self._log(f"adiado {modulo.nome}")
            return False

    def _executar_pouso(self, modulo: Modulo):
        self.fila_pouso.popleft()
        self.pousados.append(modulo)
        self._log(f"pouso ok {modulo.nome}")

    # --------- logs e status ---------
    def _log(self, msg: str):
        self._pilha_logs.append(msg)

    def logs(self, limite: int = 10) -> List[str]:
        return list(reversed(self._pilha_logs[-limite:]))

    def snapshot(self) -> Dict[str, int]:
        return {
            "fila_pouso": len(self.fila_pouso),
            "em_alerta": len(self.em_alerta),
            "em_espera": len(self.em_espera),
            "pousados": len(self.pousados),
            "total": len(self._index),
        }


# ============================
# Funcoes matematicas aplicadas
# ============================
def combustivel_em_funcao_velocidade(v: float, c0: float, k: float) -> float:
    """
    Modelo simples: consumo cresce linearmente com a velocidade de reentrada.
    c(v) = c0 - k * v  (c0 em %, v em m/s, k em % por m/s)
    """
    return max(c0 - k * v, 0)


def altura_em_funcao_tempo(h0: float, v: float, t: float) -> float:
    """Queda controlada: h(t) = h0 - v*t (v constante simplificada)."""
    return max(h0 - v * t, 0)


# ============================
# Exemplo de uso / demonstracao rapida
# ============================
def demo():
    mg = MGPEB()
    exemplos = [
        Modulo("Hab-01", "Habitacao", 9, 45, 1200, "alta", "10:30"),
        Modulo("Energia-01", "Energia", 10, 18, 2000, "alta", "10:40"),
        Modulo("Lab-01", "Laboratorio", 7, 60, 1500, "media", "11:00"),
        Modulo("Med-01", "Suporte Medico", 8, 55, 1100, "alta", "11:10"),
        Modulo("Log-01", "Logistica", 5, 70, 2500, "media", "11:20"),
    ]

    for m in exemplos:
        mg.registrar_modulo(m)

    mg.ordenar_fila()

    # Simula 3 ciclos de decisao com clima e area disponivel
    cenarios = [(True, True), (False, True), (True, True)]
    for clima_ok, area_ok in cenarios:
        mg.autorizar_proximo(clima_ok, area_ok)

    print("Snapshot:", mg.snapshot())
    print("Logs recentes:", mg.logs())

    # Exemplos de funcoes matematicas
    print("Combustivel restante a 120 m/s:", combustivel_em_funcao_velocidade(120, 60, 0.05))
    print("Altura apos 80s a 15 m/s:", altura_em_funcao_tempo(1500, 15, 80))


if __name__ == "__main__":
    demo()
