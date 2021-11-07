import re

result = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pattern = re.match(
            r'^([\d.]+|[\w:]+)[\s-]+\[([\w+/]+[\d:]+\s[+0]+)][\s"]+([A-Z]+)\s(/\w+/\w+)\s[\w/."]+\s(\d+)\s(\d+)',
            line)
        result.append(pattern.groups())
print(result)
