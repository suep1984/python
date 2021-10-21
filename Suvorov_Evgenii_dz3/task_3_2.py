trans_num = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(english_num):
    """Translate english number with register"""
    if english_num.lower() in trans_num:
        return trans_num[english_num.lower()].capitalize() \
            if english_num == english_num.capitalize() else trans_num[english_num]
    else:
        return None
