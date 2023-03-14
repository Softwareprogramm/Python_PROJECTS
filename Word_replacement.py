# Word replacement
def word_replacement():
    sentence_or_word = input("enter a word/sentence: ")
    original_word = input("Enter the word you wish to replace: ")
    replacement_word = input("Enter the replacement word: ")
    print(sentence_or_word.replace(original_word, replacement_word))


word_replacement()
