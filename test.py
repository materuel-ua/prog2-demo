from Estudiante import Estudiante

# Ejemplo de uso
if __name__ == "__main__":
    estudiante1 = Estudiante("Carlos", 20, ["Matemáticas", "Física"])
    if estudiante1.inscribir_curso("Programación"):
        print("Curso añadido exitosamente.")
    else:
        print("El curso ya estaba inscrito.")

    estudiante1.mostrar_informacion()
    print(estudiante1)
    print(repr(estudiante1))

    try:
        estudiante2 = Estudiante.desde_tupla(("Ana", 17, ["Historia"]))
        estudiante2.mostrar_informacion()
        print(Estudiante.es_mayor_de_edad(estudiante2.edad))  # False
    except ValueError as e:
        print(f"Error al crear estudiante desde tupla: {e}")