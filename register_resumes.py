resumes = [   
]

def register_resumes():
    print('DATOS PERSONALES\n')
    fullname = input('Nombre Completo: ')
    id = ask_number_int_positive('ID: ')
    cel = ask_number_int_positive("Celular: ")
    email = input('Correo Electronico: ')
    birthdate = input("Fecha de nacimiento: ")
    
    academic_education=ask_academic_training()
    profesional_experience = ask_professional_experience()
    personal_references = ask_personal_references()
    profesional_references = ask_professional_references()
    skills = ask_skills()
    additional_certificates = ask_additional_certificates()
    
    id = {
        'personal_information':{'fullname': fullname,
        'id': id,
        'cel': cel,
        'email': email,
        'birthdate': birthdate },
        'academic_education':academic_education,
        'profesional_experience': profesional_experience,
        'personal_references': personal_references,
        'profesional_references': profesional_references,
        'skills': skills,
        'additional_certificates': additional_certificates
        
    }
    
    resumes.append(id)
    
    
def ask_academic_training():
    print('FORMACION ACADEMICA\n')
    academic_title = input("Titulo academico: ")
    institution = input("Institucion: ")
    time = ask_number_int_positive("Meses en la institucion: ")
    
    academic_education = (academic_title, institution, time)
    
    return academic_education
    
        

def ask_professional_experience():
    print('EXPERIENCIA PROFESIONAL\n')
    company = input("Empresa: ")
    position = input("Cargo: ")
    functions = input("Funciones en la empresa: ")
    time = ask_number_int_positive("Duracion(En meses): ")
    
    profesional_experience = (company, position, functions, time)
    return profesional_experience
    
    
def ask_personal_references():
    print('REFERENCIAS PERSONALES\n')
    fullname = input("Nombre completo de persona referencia: ")
    relationship = input("Relacion: ")
    cel = ask_number_int_positive("Celular: ")
    
    personal_references = {
        'fullname': fullname,
        'relationship': relationship,
        'cel': cel    
    }
    
    return personal_references
    
    
def ask_professional_references():
    print('REFERENCIAS PROFESIONALES\n')
    name_company = input("Nombre Empresa: ")
    cel = ask_number_int_positive("Celular: ")
    email = input("Correo electronico: ")
    
    profesional_references = {
        'name_company': name_company,
        'cel': cel,    
        'email': email
    }
    
    return profesional_references
    

def ask_skills():
    print('HABILIDADES \n')
    skills = input("Habilidades o otros certificados: ")
    return skills
    
def ask_additional_certificates():
    print('CERTIFICADOS ADICIONALES\n')
    additional_certificates = input("Habilidades o otros certificados: ")
    return additional_certificates
    
def ask_number_float_positive(prompt):
    while(True):
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("\n||El numero no es positivo|| \n")
        except ValueError:
            print("\n||El numero es invalido|| \n")

def ask_number_int_positive(prompt):
    while(True):
        try:
            number = int(input(prompt))
            if number >= 0:
                return number
            else:
                print("\n||El numero no es positivo|| \n")
        except ValueError:
            print("\n||Ingresa un dato valido|| \n")

def print_row(a, b, c):
    print('{:<12}  {:<12}  {:<12}'.format(a, b, c) )
    
register_resumes()
print()
print(resumes)
    
print("HEllo")