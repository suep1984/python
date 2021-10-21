def thesaurus(*names):
    """Dictionary of names"""
    names = sorted(list(names))
    value = []
    key = [name[0] for name in names]
    for k in key:
        _names = []
        for name in names:
            if k == name[0]:
                _names.append(name)
        value.append(_names)
    names_dict = {k: v for k, v in zip(key, value)}
    return names_dict


a = thesaurus("Иван", "Мария", "Петр", "Илья", "Анна", "Аристарх", "Михаил")
print(a)
