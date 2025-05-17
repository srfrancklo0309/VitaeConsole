import register_resumes, search, update, generator_reports

def main_menu():
        while True:
                print('-------------------------------------------------------------')
                print('VitaeConsole')
                print('Sistema de Gestión de Hojas de Vida desde Consola\n')
                
                print('1. Registrar hoja de vida')
                print('2. Consultar hoja de vida')
                print('3. Actualizar informacion registrada')
                print('4. Generar reportes')
                print("5. Salir")
                print('-------------------------------------------------------------')

                opt=input("Ingrese su opción: ")

                match opt:
                        case '1':
                                register_resumes.resume_add()
                                continue
                        case '2':
                                search.menu()
                                continue
                        case '3':
                                update.run_application()
                                continue
                        case '4':
                                generator_reports.main_reports_menu()
                                continue
                        case '5':
                                print('\nTenga un feliz día')
                                break
                        case _:
                                print("Opción no válida")

main_menu()




