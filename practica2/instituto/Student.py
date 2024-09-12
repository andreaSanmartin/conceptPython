class Student:
    def __init__(self):
        self.dic = {
            "Juan": ["ia", "aplicaciones seguras", "aplicaciones nube"],
            "Pablo": ["algebra", "poo I", "diseño de aplicaicones"],
            "Susana": ["aplicaciones web", "aplicaciones moviles"],
        }

    def devolver_materias(self, estudent):
        return self.dic.get(estudent, [])


#Print
studentI = Student()
print(studentI.devolver_materias("Pablo"))  
print(studentI.devolver_materias("Susana"))   
