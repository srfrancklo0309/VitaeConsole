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

def report_experience_greater_than_n(resumes_list):
    print("\n--- Reporte: Experiencia Superior a N Años ---")
    print("Nota: Dada la estructura actual de 'profesional_experience' (listas de cadenas/números sin fechas),")
    print("este reporte buscará si algún número dentro de esa lista es igual o superior a N.")
    
    try:
        n_years = int(input("Ingresa el número mínimo de años (N) para la experiencia: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
        return []

    found_resumes = []
    for resume in resumes_list:
        prof_exp_entries = resume.get("profesional_experience", [])
        
        has_enough_experience = False
        for entry in prof_exp_entries:
            try:
                exp_value = int(entry)
                if exp_value >= n_years:
                    has_enough_experience = True
                    break
            except (ValueError, TypeError):
                continue
        
        if has_enough_experience:
            found_resumes.append(resume)
    
    if not found_resumes:
        print(f"No se encontraron hojas de vida con experiencia >= {n_years} (según la interpretación actual de los datos).")
    else:
        print(f"\n--- Hojas de Vida con experiencia >= {n_years} años ---")
        for i, resume in enumerate(found_resumes):
            name = resume.get("personal_information", {}).get("fullname", "N/A")
            print(f"{i+1}. {name}")
            pprint.pprint(resume, indent=2)
            print("-" * 20)
    
    return found_resumes

def report_candidates_with_certification(resumes_list):
    print("\n--- Reporte: Candidatos con Certificación o Formación Específica ---")
    keyword = input("Ingresa la palabra clave a buscar en formación/certificaciones (ej. 'Python', 'Marketing', 'Ingeniería'): ").strip().lower()

    found_resumes = []
    if not keyword:
        print("La palabra clave no puede estar vacía.")
        return []

    for resume in resumes_list:
        found_match = False

        academic_edu = resume.get("academic_education", [])
        if isinstance(academic_edu, list):
            for entry in academic_edu:
                if isinstance(entry, str) and keyword in entry.lower():
                    found_match = True
                    break
                elif isinstance(entry, (int, float)) and keyword == str(entry).lower():
                    found_match = True
                    break
        
        additional_certs = resume.get("additional_certificates", "")
        if isinstance(additional_certs, str) and keyword in additional_certs.lower():
            found_match = True
        
        if found_match:
            found_resumes.append(resume)
    
    if not found_resumes:
        print(f"No se encontraron candidatos con certificación o formación que contenga '{keyword}'.")
    else:
        print(f"\n--- Candidatos con '{keyword}' en certificación/formación ---")
        for i, resume in enumerate(found_resumes):
            name = resume.get("personal_information", {}).get("fullname", "N/A")
            print(f"{i+1}. {name}")
            pprint.pprint(resume, indent=2)
            print("-" * 20)
            
    return found_resumes

def export_resumes(resumes_to_export, output_filename, format_choice, content_choice):
    if not resumes_to_export:
        print("No hay hojas de vida para exportar.")
        return

    print(f"\n--- Exportando Hojas de Vida a {output_filename}.{format_choice} ({content_choice} content) ---")

    summarized_fields = [
        ("personal_information.fullname", "Nombre Completo"),
        ("personal_information.email", "Email"),
        ("personal_information.cel", "Teléfono"),
        ("skills", "Habilidades"),
        ("academic_education", "Educación Académica (Resumen)"),
        ("profesional_experience", "Experiencia Profesional (Resumen)")
    ]

    try:
        if format_choice == 'json':
            full_path = f"{output_filename}.json"
            export_data = {"resume": []}
            if content_choice == 'complete':
                export_data["resume"] = resumes_to_export
            else:
                for resume in resumes_to_export:
                    summary = {}
                    for field_path, header in summarized_fields:
                        parts = field_path.split('.')
                        current_val = resume
                        for part in parts:
                            current_val = current_val.get(part, None)
                            if current_val is None:
                                break
                        
                        if field_path in ["academic_education", "profesional_experience"] and isinstance(current_val, list):
                            summary[header] = "; ".join(map(str, current_val))
                        else:
                            summary[header] = current_val if current_val is not None else "N/A"
                    export_data["resume"].append(summary)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=4)
            print(f"Exportación JSON completada: {full_path}")

        elif format_choice == 'csv':
            full_path = f"{output_filename}.csv"
            
            if content_choice == 'complete':
                print("Advertencia: La exportación CSV 'completa' puede no ser ideal para estructuras JSON anidadas. Los objetos/listas se exportarán como cadenas JSON en una celda.")
                
                headers = [
                    "fullname", "id", "cel", "email", "birthdate",
                    "academic_education", "profesional_experience",
                    "skills", "additional_certificates",
                    "personal_references.fullname", "personal_references.relationship", "personal_references.cel",
                    "profesional_references.name_company", "profesional_references.cel", "profesional_references.email"
                ]

                with open(full_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(headers)

                    for resume in resumes_to_export:
                        row_data = []
                        personal_info = resume.get("personal_information", {})
                        personal_refs = resume.get("personal_references", {})
                        prof_refs = resume.get("profesional_references", {})

                        for header in headers:
                            if header.startswith("personal_information."):
                                key = header.split('.')[1]
                                row_data.append(personal_info.get(key, ""))
                            elif header.startswith("personal_references."):
                                key = header.split('.')[1]
                                row_data.append(personal_refs.get(key, ""))
                            elif header.startswith("profesional_references."):
                                key = header.split('.')[1]
                                row_data.append(prof_refs.get(key, ""))
                            elif header in ["academic_education", "profesional_experience"]:
                                list_data = resume.get(header, [])
                                row_data.append("; ".join(map(str, list_data)) if isinstance(list_data, list) else str(list_data))
                            else:
                                value = resume.get(header, "")
                                if isinstance(value, (dict, list)):
                                    row_data.append(json.dumps(value))
                                else:
                                    row_data.append(value)
                        writer.writerow(row_data)

            else:
                headers = [header for _, header in summarized_fields]
                with open(full_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(headers)

                    for resume in resumes_to_export:
                        row_data = []
                        for field_path, _ in summarized_fields:
                            parts = field_path.split('.')
                            current_val = resume
                            for part in parts:
                                current_val = current_val.get(part, None)
                                if current_val is None:
                                    break
                            
                            if field_path in ["academic_education", "profesional_experience"] and isinstance(current_val, list):
                                row_data.append("; ".join(map(str, current_val)))
                            else:
                                row_data.append(current_val if current_val is not None else "N/A")
                        writer.writerow(row_data)
            print(f"Exportación CSV completada: {full_path}")

        elif format_choice == 'txt':
            full_path = f"{output_filename}.txt"
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(f"--- Reporte de Hojas de Vida ({content_choice.capitalize()}) ---\n\n")
                for i, resume in enumerate(resumes_to_export):
                    f.write(f"--- Hoja de Vida {i+1} ---\n")
                    if content_choice == 'complete':
                        pprint.pprint(resume, indent=2, stream=f)
                    else:
                        summary_lines = []
                        for field_path, header in summarized_fields:
                            parts = field_path.split('.')
                            current_val = resume
                            for part in parts:
                                current_val = current_val.get(part, None)
                                if current_val is None:
                                    break
                            
                            if field_path in ["academic_education", "profesional_experience"] and isinstance(current_val, list):
                                summary_lines.append(f"{header}: {'; '.join(map(str, current_val))}")
                            else:
                                summary_lines.append(f"{header}: {current_val if current_val is not None else 'N/A'}")
                        f.write("\n".join(summary_lines))
                    f.write("\n" + "="*40 + "\n\n")
            print(f"Exportación TXT completada: {full_path}")

        else:
            print("Formato de exportación no válido. Opciones: json, csv, txt.")
    except Exception as e:
        print(f"Error durante la exportación: {e}")

def main_reports_menu():
    data = call_json()
    resumes_list = data["resume"]

    last_report_results = []

    while True:
        print("\n" + "==" * 20)
        print("Menú de Reportes de Hojas de Vida")
        print("==" * 20)
        print("1. Listado de Hojas de Vida con Experiencia Superior a N años")
        print("2. Candidatos con Cierta Certificación o Formación Específica")
        print("3. Exportar Último Reporte o Todas las Hojas de Vida")
        print("4. Salir")
        report_option = input("Ingresa el número de la opción deseada: ")

        if report_option == "1":
            last_report_results = report_experience_greater_than_n(resumes_list)
        elif report_option == "2":
            last_report_results = report_candidates_with_certification(resumes_list)
        elif report_option == "3":
            if not resumes_list:
                print("No hay hojas de vida en el sistema para generar reportes o exportar.")
                continue

            export_choice = input("¿Deseas exportar (1) el último reporte generado o (2) todas las hojas de vida? (1/2): ")
            resumes_to_export_actual = []
            if export_choice == "1":
                if not last_report_results:
                    print("No hay resultados del último reporte para exportar. Por favor, genera un reporte primero.")
                    continue
                resumes_to_export_actual = last_report_results
                print(f"Exportando {len(resumes_to_export_actual)} hojas de vida del último reporte.")
            elif export_choice == "2":
                resumes_to_export_actual = resumes_list
                print(f"Exportando todas las {len(resumes_to_export_actual)} hojas de vida.")
            else:
                print("Opción inválida. Volviendo al menú de reportes.")
                continue
            
            format_choice = input("Elige el formato de exportación (json, csv, txt): ").lower()
            content_choice = input("Elige el contenido (completo, resumido): ").lower()
            filename = input("Ingresa el nombre del archivo de salida (sin extensión): ")

            export_resumes(resumes_to_export_actual, filename, format_choice, content_choice)

        elif report_option == "4":
            print("Saliendo del programa de reportes. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

