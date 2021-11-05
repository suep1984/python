import os

TARGET_DIR = os.getcwd()
result = {}
dirs = os.walk(TARGET_DIR)
for dir in dirs:
    for files in dir[2]:
        file_path = os.path.join(dir[0], files)
        stat = os.stat(file_path).st_size
        k, v = int(f'1{"0" * len(str(stat))}'), 0
        result.setdefault(k, v)
        result[k] = result[k] + 1

print(result)
