def word_length(text):
    total = len(text.split())
    print('\nКол-во слов в тексте: {}\n'.format(total))
    for num, word in enumerate(text.split(), 1):
        word = word.replace(',', '').replace('.', '').replace(':', '').replace('-', '').replace('(', '').replace(')', '')
        yield '{}: {}'.format(word, len(word))


def main():
  text = input('Введите текст:\n')
  for word in word_length(text):
    print(word)

main()
