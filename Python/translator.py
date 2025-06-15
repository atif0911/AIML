#turns vowel of a string to z
def translate(str):
    translation=""
    for letter in str:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation+="Z"
            else:
                translation+="z"
        else :
            translation+=letter
    return translation

result=translate(input("Enter a string "))
print(result)