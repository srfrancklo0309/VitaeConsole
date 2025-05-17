import json

def register_resumes():
    fullname, id, cel, email, birthdate = add_personal_info()
    academic_education=ask_academic_training()
    profesional_experience = ask_professional_experience()
    personal_references = ask_personal_references()
    profesional_references = ask_professional_references()
    skills = ask_skills()
    additional_certificates = ask_additional_certificates()
    
    dictionary = {
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
    
    return dictionary

def add_personal_info():
    print('DATOS PERSONALES\n')
    fullname = add_full_name()
    id = ask_number_int_positive('ID: ')
    cel = ask_number_int_positive("Celular: ")
    email = add_email()
    birthdate = input("Fecha de nacimiento: ").strip()
    return fullname,id,cel,email,birthdate
    
    
def ask_academic_training():
    print('FORMACION ACADEMICA\n')
    academic_title = input("Titulo academico: ").strip()
    institution = input("Institucion: ").strip()
    time = ask_number_int_positive("Meses en la institucion: ")
    
    academic_education = (academic_title, institution, time)
    
    return academic_education
    
def ask_professional_experience():
    print('EXPERIENCIA PROFESIONAL\n')
    company = input("Empresa: ").strip().title()
    position = input("Cargo: ").strip().title()
    functions = input("Funciones en la empresa: ").strip()
    time = ask_number_int_positive("Duracion(En meses): ")
    
    profesional_experience = (company, position, functions, time)
    return profesional_experience
    
    
def ask_personal_references():
    print('REFERENCIAS PERSONALES\n')
    fullname = add_full_name()
    relationship = input("Relacion: ").strip().title()
    cel = ask_number_int_positive("Celular: ")
    
    personal_references = {
        'fullname': fullname,
        'relationship': relationship,
        'cel': cel    
    }
    
    return personal_references
    
    
def ask_professional_references():
    print('REFERENCIAS PROFESIONALES\n')
    name_company = input("Nombre Empresa: ").strip().title()
    cel = ask_number_int_positive("Celular: ")
    email = add_email()  

    profesional_references = {
        'name_company': name_company,
        'cel': cel,    
        'email': email
    }
    print (email)
    return profesional_references

def add_email():
    while True:
        email = input("Correo electronico: ").strip().lower()
        if any(caracter.isspace() for caracter in email):
            print("Error: El texto contiene espacios en blanco.")
        else: 
            return email

def ask_skills():
    print('HABILIDADES \n')
    skills = input("Habilidades o otros certificados: ").strip()
    return skills
    
def ask_additional_certificates():
    print('CERTIFICADOS ADICIONALES\n')
    additional_certificates = input("Habilidades o otros certificados: ").strip()
    return additional_certificates

def add_full_name():
    while True:
        nombre = input("Nombre: ").strip().title()
        if nombre.isalpha():
            return nombre 
        else:
            print("Error: El nombre debe contener solo letras.")
    

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


def resume_add():
    dictionary=register_resumes()
    with open("resumes.json","r") as f:
        data=json.load(f)
        data["resume"].append(dictionary)
    with open("resumes.json", "w") as f:
        json.dump(data, f, indent=3)
    
resume_add()
    
    