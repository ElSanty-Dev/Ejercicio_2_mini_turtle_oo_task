# mini_turtle_oo/turtle_class.py

class Tortuga:
    def __init__(self):
        # Estado interno de cada tortuga
        self.posicion_x = 0

    def adelante(self, n):
        # Dibuja el tramo horizontal desde su propia posición
        print(" " * self.posicion_x + "-" * n + ">")
        self.posicion_x += n

    def abajo(self, n):
        # Dibuja el descenso vertical alineado al final del escalón
        for _ in range(n):
            print(" " * self.posicion_x + "|")

    def reiniciar(self):
        self.posicion_x = 0
        print("🐢 Posición reiniciada")

    def mostrar(self):
        print(" " * self.posicion_x + "🐢")
