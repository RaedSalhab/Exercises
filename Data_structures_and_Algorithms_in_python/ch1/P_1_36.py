"""P-1.36 Write a Python program that inputs a list of words, separated by
whitespace,  and outputs how many times each word appears in the list.  You
need  not  worry  about  efficiency  at  this  point,  however,  as  this
topic  is something that will be addressed later in this book."""

def Words_counter(text):
    Words_count = {}
    words_list = text.split()
    for word in words_list:
        value = words_list.count(word)
        Words_count.update({word: value})

    return Words_count


if __name__ == '__main__':
    text = 'Just tell the truth and you will never have to worry about what you say'
    print(Words_counter(text))
