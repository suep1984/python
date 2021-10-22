from random import choice as chc

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count_jokes=3, repeat=True):
    """Jokes generator"""
    return [f'{chc(nouns)} {chc(adverbs)} {chc(adjectives)}' for i in range(count_jokes)] \
        if repeat else [f'{nouns.pop(nouns.index(chc(nouns)))} {adverbs.pop(adverbs.index(chc(adverbs)))} ' \
                        f'{adjectives.pop(adjectives.index(chc(adjectives)))}' for i in range(count_jokes)]
