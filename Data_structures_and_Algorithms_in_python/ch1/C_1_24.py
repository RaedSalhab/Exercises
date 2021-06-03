"""C-1.24 Write a short Python function that counts the number of vowels
 in a given character string."""

def vowels_count(text):
    vowel_count = 0
    for i in range(len(text)):
        if text[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1

    return vowel_count

if __name__ == '__main__':
    print(vowels_count('a short Python function'))
    print(vowels_count('any text'))
