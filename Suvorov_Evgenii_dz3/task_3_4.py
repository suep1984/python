def thesaurus_adv(*peoples):
    """Dictionary of surnames and names"""
    peoples = list(peoples)
    surname_value = []
    surname_key = sorted([surname[surname.index(' ') + 1] for surname in peoples])
    surnames_dict = {}
    for k in surname_key:
        _surnames = []
        for surname in peoples:
            if k == surname[surname.index(' ') + 1]:
                _surnames.append(surname)
        surname_value.append(_surnames)
        name_value = []
        name_key = sorted([name[0] for name in _surnames])
        for n_k in name_key:
            _names = []
            for name in _surnames:
                if n_k == name[0]:
                    _names.append(name)
            name_value.append(_names)
        names_dict = {n_k: n_v for n_k, n_v in zip(name_key, name_value)}
        surnames_dict.setdefault(k, names_dict)
    return surnames_dict


a = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(a)
