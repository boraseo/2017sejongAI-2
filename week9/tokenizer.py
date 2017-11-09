from nltk.tokenize import sent_tokenize, \
        word_tokenize, WordPunctTokenizer

# Define input text
input_text = "Only 30%of the tikets were sold, despite less then 100day is left till 2018 Pyung Chang Olympic. Many experts pick relationship between south and north, as the reason. But interesting fact is that the locals in South Korean don't think North Korea as a problem. " 

# Sentence tokenizer 
print("\nSentence tokenizer:")
print(sent_tokenize(input_text))

# Word tokenizer
print("\nWord tokenizer:")
print(word_tokenize(input_text))

# WordPunct tokenizer
print("\nWord punct tokenizer:")
print(WordPunctTokenizer().tokenize(input_text))
