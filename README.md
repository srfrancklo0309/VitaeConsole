# VitaeConsole
Sistema de Gestión de Hojas de Vida desde Consola

# Integrantes:
Esteban Gonzalez
Omar Uribe
Emmanuel Perez


# Descripción:
ViateConsole es una aplicación de consola que permite gestionar hojas de vida. Tiene funcionalidades como registrar, consultar, actualizar, generar reportes y exportar información sobre los candidatos. Toda la información se almacena en un archivo JSON llamado resumes.json

# Ejecución del sistema:
El usuario ingresa al archivo del menú principal "main.py" donde se abrirá el menú de la aplicación donde podrán: Registrar hojas de vida, buscar y actualizar información, generar reportes o salir del sistema.

"" Bienvenido al Sistema de Gestión de Hojas de Vida
1. Registrar hoja de vida
2. Buscar hoja de vida
3. Actualizar información
4. Generar reporte
5. Salir
Seleccione una opción:  ""

Elige una opción escribiendo el número correspondiente y sigue las instrucciones que el sistema te va indicando.

# Librerías utilizadas:

Utilizamos 3 librerías estándar:

JSON: Utilizada para leer y escribir el archivo 'resumes.json', que almacena toda la información de las hojas de vida en formato estructurado 
CSV: Exporta los reportes de hojas de vida en formato .csv, permitiendo que se pueda abrir facilmente en un excel 
Impresión: Imprime con buena estetica la información, mejorando la legibilidad 

# Ejemplos de uso:

{
  "resume": [
     {
      "personal_information": {
        "fullname": "Juan Pérez",
        "id": 12345678,
        "cel": 3001234567,
        "email": "juan.perez@correo.com",
        "birthdate": "1995-05-20"
      },
      "academic_education": ["Ingeniero de Sistemas", "Universidad Nacional", 60],
      "profesional_experience": ["Google", "Desarrollador Junior", "Desarrollo de aplicaciones web", 24],
      "personal_references": {
        "fullname": "Carlos Gómez",
        "relationship": "Amigo",
        "cel": 3009876543
      },
      "profesional_references": {
        "name_company": "Microsoft",
        "cel": 3012345678,
        "email": "referencia@microsoft.com"
      },
      "skills": "Python, JavaScript, Git",
      "additional_certificates": "Certificado en Desarrollo Web - Platzi"
    }
  ]
}


# Tablero Trello:

https://trello.com/invite/b/6826463c8e74d88367118c3f/ATTI75cb5febd41eca0e60033a71e78fe48c330E023D/vitaeconsole