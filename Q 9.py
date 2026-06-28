import math

try:
    sentence = input("Enter Sentence: ")

    words = set(sentence.split())

    print("Unique Words:")
    print(sorted(words))

    print("Power of Unique Words:")
    print(math.pow(len(words), 2))

except Exception as e:
    print("Error:", e)
