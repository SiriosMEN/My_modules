def searching_vowels(word:str) ->set:
    '''Поиск гласных'''
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    #return bool(found)
    return vowels.intersection(set(word))


def searching_letters(phrase:str,letters:str = 'aieou') ->set: #Со значением по умолчанию
    '''Поиск одинаковых букв в двух множествах'''
    return set(letters).intersection(set(phrase))
