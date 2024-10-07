# Escritura de Archivo de Texto
# Crear o abrir el archivo "my_notes.txt" para escribir

with open("my_notes.txt", "w") as file:  # Modo "w" para escribir
    file.write("My nombre es John Franco.\n")  # Aqui se escribe la primera linea
    file.write("Estudio la carrera de tecnologia de la informacion.\n")  # Aqui se escribe la segunda linea
    file.write("Estoy en primer semestre.\n")  # Aqui se escribe la tercera  linea

# Lectura de Archivo de Texto
# Abrir el archivo "my_notes.txt" para leer

with open("my_notes.txt", "r") as file:  # Modo "r" para leer
    lines = file.readlines()  # Leer todas las líneas
    for line in lines:
        print(line.strip())  # Mostrar cada línea sin saltos de línea adicionales
