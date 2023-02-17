def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
             translation = translation + "LSB"
            else:
             translation = translation + "lsb"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a Word:")))