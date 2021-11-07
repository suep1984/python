import re


def email_parse(value):
    pattern = re.match(r"^(?P<username>[\w.+-]+)@(?P<domain>[a-zA-Z0-9-]+(?:\.[a-zA-Z]+)+)$", value)
    if pattern:
        return pattern.groupdict()
    msg = f'wrong email: {value}'
    raise ValueError(msg)


print(email_parse('qwe_rtytdy@geekbr.ains.ru'))
