import os

START_DIR = 'my_project'
with open('templates.txt', 'r', encoding='utf-8') as f:
    dirs = [dir_name.replace('\n', '') for dir_name in f.readlines()]
for i in range(len(dirs)):
    dir_path = os.path.join(START_DIR, dirs[i])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
