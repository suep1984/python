import os
import yaml

START_DIR = 'my_project'
with open('config.yaml', 'r') as f:
    dirs = yaml.safe_load(f)
for i in range(len(dirs)):
    dir_path = os.path.join(START_DIR, dirs[i])
    file_extension = ('.py', '.html')
    if not os.path.exists(dir_path) and not dirs[i].endswith(file_extension):
        os.makedirs(dir_path)
    elif not os.path.exists(dir_path):
        with open(dir_path, 'w'):
            pass
