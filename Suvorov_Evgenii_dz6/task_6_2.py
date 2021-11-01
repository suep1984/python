with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    ip_list = list(line[:line.find(' ')] for line in f)

requests_count_list = list(ip_list.count(ip) for ip in ip_list)
spammer = f'{ip_list[requests_count_list.index(max(requests_count_list))]}: {max(requests_count_list)}'

print(spammer)
