from Student import Student;

class ClassS:
    def __init__(self):
        
        self.student = Student()

    def estudiante_registrado(self, nameSt, nameSub):
        try:
            subject = self.student.devolver_materias(nameSt)
            return nameSub in subject
        except Exception as e:
            print(e)
            return False

# Print
classExample = ClassS()
print(classExample.estudiante_registrado("Juan", "algebra"))  
print(classExample.estudiante_registrado("Pablo", "poo I"))   
print(classExample.estudiante_registrado("Susana", "aplicaciones moviles"))        

