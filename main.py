from Logica.Calificacion import Calificacion
if __name__ == '__main__':
   notaLetra = float(input("Ingrese calificacion en numero: "))
   nota=Calificacion(notaLetra)
   nota.CalificacionNueva()
   nota.imprimirCalificacion()
