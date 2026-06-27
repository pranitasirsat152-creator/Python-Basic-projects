def analyze_string(text):
    if text == "":
        print("Empty String")
        return

    print("Length :", len(text))
    print("Reverse :", text[::-1])

    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch in vowels:
            count += 1

    print("Vowels :", count)

    print("\nCharacter  Positive  Negative")
    for i in range(len(text)):
        print(text[i], "\t", i, "\t", i-len(text))

s = input("Enter String : ")
analyze_string(s)
