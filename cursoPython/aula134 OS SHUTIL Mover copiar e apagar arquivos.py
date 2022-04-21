
import os
import shutil

caminho_original = 'C:\\Users\\004696631\\Documents\\adilson'
caminho_novo = 'C:\\Users\\004696631\\Documents\\adilson\\novo'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        if '.srt' in file:
            # shutil.move(old_file_path, new_file_path)
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} movido com sucesso!')
            os.remove(new_file_path)