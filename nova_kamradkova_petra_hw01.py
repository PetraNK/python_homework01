import json

with open('alice.txt', encoding='utf-8') as book:
    bookSample = book.read()

final_bookSample = bookSample.replace(" ","").replace("\n","").lower()
char_dictionary = dict()

for sign in final_bookSample:
    if sign in char_dictionary:
        char_dictionary[sign] += 1
    else:
        char_dictionary[sign] = 1

sorted_alfabeth = dict(sorted(char_dictionary.items()))

with open('hw01_output.json.', mode="w", encoding="utf-8") as new_file:
    json.dump(sorted_alfabeth, new_file, ensure_ascii=False, indent=4)





