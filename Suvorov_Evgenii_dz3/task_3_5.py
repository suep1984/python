from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count_jokes=3, repeat=True):
    """Jokes generator"""
    jokes = []
    if not repeat:
        for i in range(count_jokes):
            word1 = choice(nouns)
            word2 = choice(adverbs)
            word3 = choice(adjectives)
            jokes.append(f'{word1} {word2} {word3}')
            nouns.pop(nouns.index(word1))
            adverbs.pop(adverbs.index(word2))
            adjectives.pop(adjectives.index(word3))
    else:
        jokes = [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for i in range(count_jokes)]

    return jokes
