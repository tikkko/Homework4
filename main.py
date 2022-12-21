LONG_TEXT = """asdlknfasldkmfasdfasdf"""

main_list = list()


def add_word(word):
    main_list.append(word)


def get_words(chars):
    new_list = list(filter(lambda el: el.startswith(chars), main_list))
    new_list.sort()
    new_list = new_list[:5]
    return new_list


def crop_text(length):
    f = 0
    while True:
        b = LONG_TEXT[f:length + f]
        yield b
        f += length


if __name__ == '__main__':
    assert get_words('') == []

    add_word('bat')
    add_word('batman')

    assert get_words('') == ['bat', 'batman']
    assert get_words('bat') == ['bat', 'batman']
    assert get_words('batm') == ['batman']
    assert get_words('x') == []

    add_word('bar')
    add_word('bartender')
    add_word('basket')
    add_word('band')

    assert get_words('ba') == ['band', 'bar', 'bartender', 'basket', 'bat']

    text_generator = crop_text(10)
    assert next(text_generator) == "asdlknfasl"
    assert next(text_generator) == "dkmfasdfas"
    assert next(text_generator) == "df"
