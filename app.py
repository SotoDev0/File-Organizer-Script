import os
import shutil

# Obtener y mostrar directorio actual
cwd = os.getcwd()
print(f"Directorio Actual: {cwd}")

# Listar contenido del directorio actual
content = os.listdir(cwd)
print(content)

for i in content:
    if os.path.isfile(i):
        file = os.path.splitext(i)
        extension = file[1][1:]

        if extension == "":
            extension = "Archivos sin extension"

        
        if extension == "py": #or extension == ""
            continue
        
        if not os.path.exists(extension):
            os.mkdir(extension)
            print(f"Carpeta {extension} creada")
        
        shutil.move(i,extension)


        


        
        

        
    