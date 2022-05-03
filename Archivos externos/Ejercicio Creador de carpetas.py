import os

#fullpath = "D:\\RESPALDO\\Desktop\\SERIES VIENDO AHORA\\The Big Bang Theory"
#fullpath = "D:\\RESPALDO\\Desktop\\SERIES VIENDO AHORA\\TBBT"
fullpath = "D:\\Documentos\\Mipony\\Series\\Shingeki no Kyojin\\wea"


def make_directory(full_path):

    if os.path.exists(full_path):
        array = os.listdir(full_path)

        for j in array:
            for i in range(1, 26):
                if "S4" in j:
                    if i > 16:
                        break
                if "S2" in j or "S3" in j:
                    if i > 12:
                        break

                if i < 10:
                    new_path = os.path.join(full_path, j, "0"+str(i))
                else:
                    new_path = os.path.join(full_path, j, str(i))

                os.makedirs(new_path, exist_ok=True)

            if "S12" in j:
                new_path = os.path.join(full_path, j, str(25))
                os.makedirs(new_path, exist_ok=True)


def move_files_to_directory(full_path):
    array = os.listdir(full_path)
    os.chdir(full_path)

    for seasion in array:
        pathh = os.path.join(full_path, seasion)
        new_array = os.listdir(pathh)
        for element in new_array:
            if os.path.isfile(os.path.join(pathh, element)):
                for j in range(1, 26):
                    if " - "+str(j).zfill(2) in element:
                        directory = os.path.join(pathh, str(j).zfill(2))
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


# make_directory(fullpath)
# move_files_to_directory(fullpath)
rename_files(fullpath)
