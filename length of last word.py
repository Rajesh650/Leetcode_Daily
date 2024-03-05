def length_of_lastWord(sentence):

    words = sentence.split()

    if words :

        last_word = words[-1]

        length_of_lastWord = len(last_word)

        return length_of_lastWord
    else :
        return 0
    
sentence = "Hello World"

result = length_of_lastWord(sentence)
print(result)



