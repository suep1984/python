import os
import shutil


ROOT_FOLDER = 'my_project'
DEST_FOLDER = os.path.join(ROOT_FOLDER, 'templates')

for folder in os.walk(ROOT_FOLDER):
    for sub_folder in folder[1]:
        if sub_folder == 'templates':
            src_folder = os.path.join(folder[0], sub_folder)
            if src_folder != DEST_FOLDER:
                shutil.copytree(src_folder, DEST_FOLDER, dirs_exist_ok=True)
