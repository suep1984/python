from requests import get

URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(get(URL).text)
result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = line[:line.find(' ')]
        request_type = line[line.find('"') + 1: line.find('"') + 4]
        requested_resource = line[line.find('"') + 4: line.find('HTTP') - 1]
        result.append((remote_addr, request_type, requested_resource))

print(result)
