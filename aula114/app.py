"""
Pillow: redimensionando várias imagens automaticamente
"""
import os
from PIL import Image


def main(main_images_folder, delete_converted=False, delete_original=False, new_width=800):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError("esse diretório não existe")

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extesion = os.path.splitext(file)

            converted_tag = '_CONVERTIDO'

            new_file = file_name + converted_tag + extesion
            new_file_full_path = os.path.join(root, new_file)

            if delete_converted:
                if converted_tag in file_full_path:
                    os.remove(file_full_path)
                    continue
                continue

            if os.path.isfile(new_file_full_path):
                print(f'arquivo {new_file_full_path} já existe')
                continue

            if converted_tag in file_full_path:
                print('imagem já convertida')
                continue

            img_pillow = Image.open(file_full_path)
            width, heigth = img_pillow.size
            new_heigth = round(new_width * heigth / width)

            new_image = img_pillow.resize((new_width, new_heigth), Image.LANCZOS)
            new_image.save(
                new_file_full_path,
                optimaze=True,
                quality=60
            )

            print(f'{file_full_path} convertido com sucesso!')
            new_image.close()
            img_pillow.close()

            if delete_original:
                os.remove(file_full_path)


if __name__ == '__main__':
    main_images_folder = r'\Users\user\Pictures\animais'
    main(main_images_folder, new_width=640, delete_converted=False, delete_original=True)
