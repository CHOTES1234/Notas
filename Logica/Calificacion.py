class Calificacion():
    def __init__(self, calificacion):
        self.calificacion = calificacion
        self.nota = ""


    def CalificacionNueva(self):
        if self.calificacion > 9:
           self.nota = "A"
        elif self.calificacion > 8:
             self.nota = "B"
        elif self.calificacion >= 7.5:
             self.nota = "C"
        else:
             self.nota = "R"

    def imprimirCalificacion(self):
        print(f"La calificacion es: {self.nota}")