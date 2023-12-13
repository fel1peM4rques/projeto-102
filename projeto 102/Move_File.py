import os
import shutil

from_dir = "C:/Users/55479/Downloads"
to_dir = "C:/Users/55479/Documents/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)

    if ext == '':
        continue
    elif ext.lower() in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, ext[1:])
        path3 = os.path.join(path2, file_name)

        if not os.path.exists(path2):
            os.makedirs(path2)

        print("Movendo", file_name)
        shutil.move(path1, path3)