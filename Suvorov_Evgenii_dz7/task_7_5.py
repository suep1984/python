import os
import json

TARGET_DIR = os.getcwd()
result = {}
dirs = os.walk(TARGET_DIR)
for dir in dirs:
    files = dir[2]
    for i in range(len(files)):
        file_path = os.path.join(dir[0], files[i])
        stat = os.stat(file_path).st_size
        file_res = files[i].split('.')[1]
        k, v = int(f'1{"0" * len(str(stat))}'), (0, [])
        result.setdefault(k, v)
        count = result[k][0] + 1
        result[k][1].append(file_res)
        result[k] = (count, list(set(result[k][1])))
with open(f'{TARGET_DIR.split("/")[-1]}_summary.json', 'w') as f:
    json.dump(result, f)
print(result)
