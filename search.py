import json
def call_json():
    resumes_json="resumes.json"

    try:
        with open("resumes.json", "r") as f:
            data=json.load(f)
    except FileNotFoundError:
        print("")
        exit()
        
    if "resume" in data:
        resumes_json=data["resume"]
        
    if isinstance(resumes_json, list):
        resumes=resumes_json
    return resumes

def search_id(resumes):
    id=input("Ingrese el Id que deseas buscar: ")
    try:
        id=int(id)
    except ValueError:
        print("El id debe ser numérico.")
        
    for i in resumes:
        if i.get("personal_information", {}).get("id") == id:
            print("=" * 30)
            print("Información Personal:")
            personal_info = i.get("personal_information", {})
            print(f"  Nombre completo: {personal_info.get('fullname', 'N/A')}")
            print(f"  ID: {personal_info.get('id', 'N/A')}")
            print(f"  Celular: {personal_info.get('cel', 'N/A')}")
            print(f"  Email: {personal_info.get('email', 'N/A')}")
            print(f"  Fecha de Nacimiento: {personal_info.get('birthdate', 'N/A')}")
            print("-" * 30)

            print("Educación Académica:")
            academic_education = i.get("academic_education", [])
            if academic_education:
                for item in academic_education:
                    print(f"  - {item}")
            else:
                print("  N/A")
            print("-" * 30)

            print("Experiencia Profesional:")
            profesional_experience = i.get("profesional_experience", [])
            if profesional_experience:
                for item in profesional_experience:
                    print(f"  - {item}")
            else:
                print("  N/A")
            print("-" * 30)

            print("Referencias Personales:")
            personal_references = i.get("personal_references", {})
            print(f"  Nombre completo: {personal_references.get('fullname', 'N/A')}")
            print(f"  Relación: {personal_references.get('relationship', 'N/A')}")
            print(f"  Celular: {personal_references.get('cel', 'N/A')}")
            print("-" * 30)

            print("Referencias Profesionales:")
            profesional_references = i.get("profesional_references", {})
            print(f"  Nombre de la compañía: {profesional_references.get('name_company', 'N/A')}")
            print(f"  Celular: {profesional_references.get('cel', 'N/A')}")
            print(f"  Email: {profesional_references.get('email', 'N/A')}")
            print("-" * 30)

            print(f"Habilidades: {i.get('skills', 'N/A')}")
            print("-" * 30)
            print(f"Certificados Adicionales: {i.get('additional_certificates', 'N/A')}")
            print("=" * 30)
            print("\n")
            break
        else:
            print(f"No se encontró ningún currículum con el ID: {id}")

def search_email(resumes):
    email=input("Ingresa el Email del usuario que deseas buscar: ")
    for i in resumes:
        if i.get("personal_information", {}).get("email") == email:
            print("=" * 30)
            print("Información Personal:")
            personal_info = i.get("personal_information", {})
            print(f"  Nombre completo: {personal_info.get('fullname', 'N/A')}")
            print(f"  ID: {personal_info.get('id', 'N/A')}")
            print(f"  Celular: {personal_info.get('cel', 'N/A')}")
            print(f"  Email: {personal_info.get('email', 'N/A')}")
            print(f"  Fecha de Nacimiento: {personal_info.get('birthdate', 'N/A')}")
            print("-" * 30)

            print("Educación Académica:")
            academic_education = i.get("academic_education", [])
            if academic_education:
                for item in academic_education:
                    print(f"  - {item}")
            else:
                print("  N/A")
            print("-" * 30)

            print("Experiencia Profesional:")
            profesional_experience = i.get("profesional_experience", [])
            if profesional_experience:
                for item in profesional_experience:
                    print(f"  - {item}")
            else:
                print("  N/A")
            print("-" * 30)

            print("Referencias Personales:")
            personal_references = i.get("personal_references", {})
            print(f"  Nombre completo: {personal_references.get('fullname', 'N/A')}")
            print(f"  Relación: {personal_references.get('relationship', 'N/A')}")
            print(f"  Celular: {personal_references.get('cel', 'N/A')}")
            print("-" * 30)

            print("Referencias Profesionales:")
            profesional_references = i.get("profesional_references", {})
            print(f"  Nombre de la compañía: {profesional_references.get('name_company', 'N/A')}")
            print(f"  Celular: {profesional_references.get('cel', 'N/A')}")
            print(f"  Email: {profesional_references.get('email', 'N/A')}")
            print("-" * 30)

            print(f"Habilidades: {i.get('skills', 'N/A')}")
            print("-" * 30)
            print(f"Certificados Adicionales: {i.get('additional_certificates', 'N/A')}")
            print("=" * 30)
            print("\n")
            break
    else:
        print(f"No se encontró ningún currículum con el Email: {email}")

def search_fullname(resumes):
    fullname=input("Ingresa el nombre completo del usuario que deseas buscar: ")
    for i in resumes:
        if i.get("personal_information", {}).get("fullname") == fullname:
            print("=" * 30)
            print("Información Personal:")
            personal_info = i.get("personal_information", {})
            print(f"  Nombre completo: {personal_info.get('fullname', 'N/A')}")
            print(f"  ID: {personal_info.get('id', 'N/A')}")
            print(f"  Celular: {personal_info.get('cel', 'N/A')}")
            print(f"  Email: {personal_info.get('email', 'N/A')}")
            print(f"  Fecha de Nacimiento: {personal_info.get('birthdate', 'N/A')}")
            print("-" * 30)

            print("Educación Académica:")
            academic_education = i.get("academic_education", [])
            if academic_education:
                for item in academic_education:
                    print(f"  - {item}")
            else:
                print("  N/A")
            print("-" * 30)

            print("Experiencia Profesional:")
            profesional_experience = i.get("profesional_experience", [])
            if profesional_experience:
                for item in profesional_experience:
                    print(f"  - {item}")
            else:
                print("  N/A")
            print("-" * 30)

            print("Referencias Personales:")
            personal_references = i.get("personal_references", {})
            print(f"  Nombre completo: {personal_references.get('fullname', 'N/A')}")
            print(f"  Relación: {personal_references.get('relationship', 'N/A')}")
            print(f"  Celular: {personal_references.get('cel', 'N/A')}")
            print("-" * 30)

            print("Referencias Profesionales:")
            profesional_references = i.get("profesional_references", {})
            print(f"  Nombre de la compañía: {profesional_references.get('name_company', 'N/A')}")
            print(f"  Celular: {profesional_references.get('cel', 'N/A')}")
            print(f"  Email: {profesional_references.get('email', 'N/A')}")
            print("-" * 30)

            print(f"Habilidades: {i.get('skills', 'N/A')}")
            print("-" * 30)
            print(f"Certificados Adicionales: {i.get('additional_certificates', 'N/A')}")
            print("=" * 30)
            print("\n")
            break
    else:
        print(f"No se encontró ningún currículum con el Nombre: {fullname}")

def menu():
    resumes=call_json()       
    print("=="*20)
    print("Menú de busqueda CV")
    print("=="*20)
    print("1. Opción de busqueda por Id")
    print("2. Opción de busqueda por Email")
    print("3. Opción de busqueda por Nombre completo")
    option=input("Ingresa el número de la opción por la que deseas buscar: ")
    match option:
        case "1":
            search_id(resumes)
        case "2":
            search_email(resumes)
        case "3":
            search_fullname(resumes)
        case _:
            print("Por favor ingresa una opción válida")
            
            
        
