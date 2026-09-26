def word_frequency(sentence):
    frequency = {}

    words = sentence.lower().split()

    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    return frequency


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    print("Word frequency:", word_frequency(sentence))