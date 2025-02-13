from typing import List, Tuple


class Estudiante:
    # Atributo de clase (contador de instancias)
    total_estudiantes = 0

    def __init__(self, nombre: str, edad: int, cursos_inscritos: List[str] = None):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos if cursos_inscritos else []
        Estudiante.total_estudiantes += 1  # Incrementar el contador de instancias

    def inscribir_curso(self, curso: str):
        """Añade un curso a la lista de cursos inscritos."""
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)

    def mostrar_informacion(self):
        """Muestra la información del estudiante."""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Cursos: {', '.join(self.cursos_inscritos)}")

    def __str__(self):
        """Representación legible de la instancia."""
        return f"Estudiante(nombre={self.nombre}, edad={self.edad}, cursos={self.cursos_inscritos})"

    def __repr__(self):
        """Representación oficial de la instancia."""
        return f"Estudiante('{self.nombre}', {self.edad}, {self.cursos_inscritos})"

    @classmethod
    def desde_tupla(cls, tupla: Tuple[str, int, List[str]]):
        """Crea una instancia de Estudiante a partir de una tupla."""
        return cls(tupla[0], tupla[1], tupla[2])

    @staticmethod
    def es_mayor_de_edad(edad: int) -> bool:
        """Verifica si una edad dada corresponde a un mayor de edad."""
        return edad >= 18


# Ejemplo de uso
if __name__ == "__main__":
    estudiante1 = Estudiante("Carlos", 20, ["Matemáticas", "Física"])
    estudiante1.inscribir_curso("Programación")
    estudiante1.mostrar_informacion()

    print(estudiante1)
    print(repr(estudiante1))

    estudiante2 = Estudiante.desde_tupla(("Ana", 17, ["Historia"]))
    estudiante2.mostrar_informacion()

    print(Estudiante.es_mayor_de_edad(estudiante2.edad))  # False