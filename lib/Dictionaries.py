import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split the sentence into words and count frequencies using a dictionary comprehension
    word_freq = {word: cleaned_sentence.split().count(word) for word in cleaned_sentence.split()}

    return word_freq

# Test case
sentence = "This is a test sentence. This sentence is a test."
sentence = "Fine Boy Like me. Fine Boy Like me."
result = word_frequency(sentence)
print(result)
