from typing import List, Tuple, Optional

class Estudiante:
    # Atributo de clase (contador de instancias)
    total_estudiantes = 0

    def __init__(self, nombre: str, edad: int, cursos_inscritos: Optional[List[str]] = None):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos if cursos_inscritos is not None else []
        Estudiante.total_estudiantes += 1  # Incrementar el contador de instancias

    def inscribir_curso(self, curso: str) -> bool:
        """Añade un curso a la lista de cursos inscritos si aún no está presente."""
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            return True
        return False

    def mostrar_informacion(self) -> None:
        """Muestra la información del estudiante."""
        cursos = ', '.join(self.cursos_inscritos) if self.cursos_inscritos else "No inscrito en ningún curso"
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Cursos: {cursos}")

    def __str__(self) -> str:
        """Representación legible de la instancia."""
        return f"Estudiante(nombre={self.nombre}, edad={self.edad}, cursos={self.cursos_inscritos})"

    def __repr__(self) -> str:
        """Representación oficial de la instancia."""
        return f"Estudiante('{self.nombre}', {self.edad}, {self.cursos_inscritos})"

    @classmethod
    def desde_tupla(cls, tupla: Tuple[str, int, List[str]]):
        """Crea una instancia de Estudiante a partir de una tupla."""
        if not (isinstance(tupla, tuple) and len(tupla) == 3 and
                isinstance(tupla[0], str) and isinstance(tupla[1], int) and isinstance(tupla[2], list)):
            raise ValueError(
                "El formato de la tupla no es válido. Se espera (nombre: str, edad: int, cursos: List[str])")
        return cls(*tupla)

    @staticmethod
    def es_mayor_de_edad(edad: int) -> bool:
        """Verifica si una edad dada corresponde a un mayor de edad."""
        return edad >= 18


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