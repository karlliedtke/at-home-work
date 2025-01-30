# def remove_comma(word):
#     return word.replace(',', '')

# word = "ste,ve"
# cleaned_word = remove_comma(word)
# print(cleaned_word)  

# def combine(word):
#     return word.concatenate("e,v")

# word = "ste,ve"
# cleaned_word = combine(word)
# print(cleaned_word)

def reomve_comma(word):
    return word
word = "ste,ve"
find_comma = word.find(",")
print(word[0:find_comma] + word[find_comma+1:])
    

# mystr =  "dented"
# print(mystr.strip("d"))
# print(mystr.strip("de"))
# print(mystr.strip("end"))
# mystr = " so i love a good olive"
# print(mystr.strip("evils"))
# print(mystr.strip("evils "))

