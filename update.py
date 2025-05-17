import json
import pprint
import csv

def call_json():
    resumes_file = "resumes.json"
    try:
        with open(resumes_file, "r", encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"El archivo '{resumes_file}' no se encontró. Creando uno vacío con la estructura esperada.")
        data = {"resume": []}
        with open(resumes_file, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except json.JSONDecodeError:
        print(f"Error al decodificar '{resumes_file}'. El archivo puede estar corrupto. Inicializando con una estructura vacía.")
        data = {"resume": []}
        with open(resumes_file, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    if "resume" not in data or not isinstance(data["resume"], list):
        print(f"Advertencia: Estructura inválida en '{resumes_file}'. Asegurando que 'resume' sea una lista.")
        data["resume"] = []

    return data

def save_json(data):
    resumes_file = "resumes.json"
    try:
        with open(resumes_file, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print("Datos actualizados guardados exitosamente en resumes.json")
    except Exception as e:
        print(f"Error al guardar los datos en '{resumes_file}': {e}")

def search_by_id(resumes_list):
    print("\n--- Búsqueda por ID ---")
    search_id_val = input("Ingresa el ID del usuario que deseas buscar: ")
    for i, resume in enumerate(resumes_list):
        personal_info = resume.get("personal_information", {})
        if str(personal_info.get("id", "")).strip().lower() == str(search_id_val).strip().lower():
            return i
    return None

def search_by_email(resumes_list):
    print("\n--- Búsqueda por Email ---")
    email = input("Ingresa el Email del usuario que deseas buscar: ")
    for i, resume in enumerate(resumes_list):
        personal_info = resume.get("personal_information", {})
        if personal_info.get("email", "").strip().lower() == email.strip().lower():
            return i
    return None

def search_by_fullname(resumes_list):
    print("\n--- Búsqueda por Nombre Completo ---")
    full_name = input("Ingresa el Nombre Completo del usuario que deseas buscar: ")
    for i, resume in enumerate(resumes_list):
        personal_info = resume.get("personal_information", {})
        if personal_info.get("fullname", "").strip().lower() == full_name.strip().lower():
            return i
    return None

def add_experience_or_education(resume_data):
    print("\n--- Añadir Experiencia o Formación ---")
    category_choice = input("¿Deseas añadir (1) Experiencia Profesional o (2) Formación Académica? (1/2): ")

    if category_choice == "1":
        if "profesional_experience" not in resume_data or not isinstance(resume_data["profesional_experience"], list):
            resume_data["profesional_experience"] = []

        print("\n--- Nueva Experiencia Profesional ---")
        new_exp_entry = input("Ingresa la nueva experiencia profesional (ej. 'Desarrollador en EmpresaX, 2023-2024'): ")
        resume_data["profesional_experience"].append(new_exp_entry)
        print("Experiencia profesional añadida exitosamente.")

    elif category_choice == "2":
        if "academic_education" not in resume_data or not isinstance(resume_data["academic_education"], list):
            resume_data["academic_education"] = []

        print("\n--- Nueva Formación Académica ---")
        new_edu_entry = input("Ingresa la nueva formación académica (ej. 'Ingeniería en UniversidadY, 2018-2022'): ")
        resume_data["academic_education"].append(new_edu_entry)
        print("Formación académica añadida exitosamente.")
    else:
        print("Opción no válida. Por favor, selecciona 1 o 2.")

def edit_personal_contact_info(resume_data):
    print("\n--- Editar Datos Personales o de Contacto ---")
    if "personal_information" not in resume_data:
        resume_data["personal_information"] = {}
        print("No se encontró la sección 'personal_information'. Creando una nueva.")

    current_info = resume_data["personal_information"]
    print("Datos personales y de contacto actuales:")
    if current_info:
        for key, value in current_info.items():
            print(f"  - {key.replace('_', ' ').title()}: {value}")
    else:
        print("  Ningún dato personal o de contacto registrado.")

    print("\nCampos disponibles para editar/añadir: fullname, id, cel, email, birthdate")
    field_to_edit = input("Ingresa el nombre del campo que deseas editar o añadir: ").lower()
    
    if field_to_edit:
        new_value = input(f"Ingresa el nuevo valor para '{field_to_edit}': ")
        current_info[field_to_edit] = new_value
        print(f"Campo '{field_to_edit}' actualizado/añadido.")
    else:
        print("No se especificó ningún campo para editar.")

def add_skills_references(resume_data):
    print("\n--- Cambiar o Agregar Habilidades y Referencias ---")
    category_choice = input("¿Deseas actualizar (1) Habilidades, (2) Referencias Personales o (3) Referencias Profesionales? (1/2/3): ")

    if category_choice == "1":
        print(f"Habilidad actual: {resume_data.get('skills', 'Ninguna')}")
        new_skill = input("Ingresa la nueva habilidad (esta sobrescribirá la actual): ")
        resume_data["skills"] = new_skill
        print("Habilidad actualizada.")
    elif category_choice == "2":
        if "personal_references" not in resume_data:
            resume_data["personal_references"] = {}
            print("No se encontró la sección 'personal_references'. Creando una nueva.")
        
        current_ref_info = resume_data["personal_references"]
        print("Datos actuales de Referencia Personal:")
        if current_ref_info:
            for key, value in current_ref_info.items():
                print(f"  - {key.replace('_', ' ').title()}: {value}")
        else:
            print("  Ninguna referencia personal registrada.")

        print("Campos disponibles: fullname, relationship, cel")
        field_to_edit = input("Ingresa el campo a editar/añadir en referencias personales: ").lower()
        new_value = input(f"Ingresa el nuevo valor para '{field_to_edit}': ")
        current_ref_info[field_to_edit] = new_value
        print("Referencia personal actualizada.")
    elif category_choice == "3":
        if "profesional_references" not in resume_data:
            resume_data["profesional_references"] = {}
            print("No se encontró la sección 'profesional_references'. Creando una nueva.")

        current_prof_ref_info = resume_data["profesional_references"]
        print("Datos actuales de Referencia Profesional:")
        if current_prof_ref_info:
            for key, value in current_prof_ref_info.items():
                print(f"  - {key.replace('_', ' ').title()}: {value}")
        else:
            print("  Ninguna referencia profesional registrada.")

        print("Campos disponibles: name_company, cel, email")
        field_to_edit = input("Ingresa el campo a editar/añadir en referencias profesionales: ").lower()
        new_value = input(f"Ingresa el nuevo valor para '{field_to_edit}': ")
        current_prof_ref_info[field_to_edit] = new_value
        print("Referencia profesional actualizada.")
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

def update_resume_menu(all_data, found_index):
    resume_to_update = all_data["resume"][found_index]

    while True:
        print("\n" + "==" * 20)
        full_name_display = resume_to_update.get('personal_information', {}).get('fullname', 'N/A')
        print(f"Menú de Actualización para: {full_name_display}")
        print("==" * 20)
        print("1. Añadir nueva experiencia o formación")
        print("2. Editar datos personales o de contacto")
        print("3. Cambiar o agregar habilidades y referencias")
        print("4. Volver al menú principal")
        update_option = input("Ingresa el número de la opción para actualizar: ")

        match update_option:
            case "1":
                add_experience_or_education(resume_to_update)
            case "2":
                edit_personal_contact_info(resume_to_update)
            case "3":
                add_skills_references(resume_to_update)
            case "4":
                print("Volviendo al menú principal.")
                break
            case _:
                print("Opción no válida. Por favor, intenta de nuevo.")
        
        save_json(all_data)

def menu_updates():
    data = call_json()
    resumes_list = data["resume"]

    while True:
        print("\n" + "==" * 20)
        print("Menú Principal de Currículums")
        print("==" * 20)
        print("1. Buscar y Actualizar Currículum por ID")
        print("2. Buscar y Actualizar Currículum por Email")
        print("3. Buscar y Actualizar Currículum por Nombre completo")
        print("4. Salir")
        option = input("Ingresa el número de la opción deseada: ")

        found_index = None
        match option:
            case "1":
                found_index = search_by_id(resumes_list)
            case "2":
                found_index = search_by_email(resumes_list)
            case "3":
                found_index = search_by_fullname(resumes_list)
            case "4":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            case _:
                print("Por favor ingresa una opción válida.")
                continue

        if found_index is not None:
            print("\n--- Currículum encontrado ---")
            pprint.pprint(resumes_list[found_index], indent=4)
            update_resume_menu(data, found_index)
        else:
            print("Currículum no encontrado con los criterios especificados.")

def run_application():
    print("\nIniciando el programa de Gestión de Hojas de Vida...")
    menu_updates()

if __name__ == "__main__":
    run_application()

