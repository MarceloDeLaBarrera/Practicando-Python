import os

#fullpath = "D:\\RESPALDO\\Desktop\\SERIES VIENDO AHORA\\The Big Bang Theory"
#fullpath = "D:\\RESPALDO\\Desktop\\SERIES VIENDO AHORA\\TBBT"
fullpath = "D:\\RESPALDO\\Desktop\\SERIES VIENDO AHORA\\ssssssssssssje"


def make_directory(full_path):

    if os.path.exists(full_path):
        array = os.listdir(full_path)
        print(array)
        for j in array:
            for i in range(1, 9):
                if i < 10:
                    new_path = os.path.join(full_path, j, "0"+str(i))
                else:
                    new_path = os.path.join(full_path, j, str(i))

                try:
                    os.makedirs(new_path, exist_ok=True)
                except Exception as e:
                    print(
                        f"No se encontró la ruta especificada, por lo que no se pudo crear directorios. Excepcion: {e}")

            if "S12" in j:
                new_path = os.path.join(full_path, j, str(25))
                os.makedirs(new_path, exist_ok=True)


def move_files_to_directory(full_path):
    array = os.listdir(full_path)

    for seasion in array:
        pathh = os.path.join(full_path, seasion)
        new_array = os.listdir(pathh)

        for element in new_array:
            if os.path.isfile(os.path.join(pathh, element)):
                for j in range(1, 11):
                    # Hacer referencia al episodio no a sesion
                    if 'e' + str(j).zfill(2) in element:
                        directory = os.path.join(pathh, str(j).zfill(2))
                        print(directory)
                        os.replace(os.path.join(pathh, element),
                                   os.path.join(directory, element))


def move_files_to_directory_inverse(full_path):
    array = os.listdir(full_path)
    os.chdir(full_path)

    for seasion in array:
        pathh = os.path.join(full_path, seasion)
        newpath = os.listdir(pathh)

        for element in newpath:
            if os.path.isdir(os.path.join(pathh, element)):
                pathhhh = os.path.join(pathh, element)
                directory = os.listdir(pathhhh)
                for file in directory:
                    print(os.path.join(pathhhh, file))
                    os.replace(
                        os.path.join(pathhhh, file), os.path.join(pathh, file))


def rename_files(full_path):
    array = os.listdir(full_path)

    for seasion in array:
        pathh = os.path.join(full_path, seasion)
        newpath = os.listdir(pathh)

        for element in newpath:
            if os.path.isdir(os.path.join(pathh, element)):
                pathhh = os.path.join(pathh, element)
                directorys = os.listdir(os.path.join(pathh, element))

                for file in directorys:
                    if file.endswith("mkv") or file.endswith("mp4"):
                        file_name = file
                        name, extmkvmp4 = os.path.splitext(file_name)

                    if file.endswith("srt"):
                        os.rename(os.path.join(pathhh, file),
                                  os.path.join(pathhh, 'zzzz.srt'))

                        os.rename(os.path.join(pathhh, 'zzzz.srt'),
                                  os.path.join(pathhh, name+'.srt'))


def rename_files_version_mejorada(full_path):
    array = os.listdir(full_path)

    for seasion in array:
        pathh = os.path.join(full_path, seasion)
        newpath = os.listdir(pathh)

        for element in newpath:
            if os.path.isdir(os.path.join(pathh, element)):
                pathhh = os.path.join(pathh, element)
                directorys = os.listdir(os.path.join(pathh, element))
                namestr = ""
                namemkv = ""
                for i in range(2):
                    if i == 0 and directorys[i].endswith("mkv") or directorys[i].endswith("mp4"):
                        file_name = directorys[i]
                        namemkv, extmkvmp4 = os.path.splitext(file_name)
                        file_name_str = directorys[i+1]
                        namestr, extstr = os.path.splitext(file_name_str)

                        os.rename(os.path.join(pathhh, directorys[i+1]),
                                  os.path.join(pathhh, 'zzzz.srt'))

                        os.rename(os.path.join(pathhh, 'zzzz.srt'),
                                  os.path.join(pathhh, namemkv+extstr))

                    if i == 0 and directorys[i].endswith("srt"):
                        file_name_str = directorys[i]
                        namestr, extstr = os.path.splitext(file_name_str)
                        file_name_mkv = directorys[i+1]
                        namemkv, extmkvmp4 = os.path.splitext(file_name_mkv)

                        os.rename(os.path.join(pathhh, directorys[i+1]),
                                  os.path.join(pathhh, 'zzzz.'+extmkvmp4))

                        os.rename(os.path.join(pathhh, 'zzzz.'+extmkvmp4),
                                  os.path.join(pathhh, namestr+extmkvmp4))


# make_directory(fullpath)
# move_files_to_directory(fullpath)
rename_files_version_mejorada(fullpath)
