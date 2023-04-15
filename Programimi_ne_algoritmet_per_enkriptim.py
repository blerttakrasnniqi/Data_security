import os

plaintext = "The quick brown fox jumps over the lazy dog"

cyphertext = "012-011-007-018-024-003-020-019-013-004-009-015-002-006-009-023-024-001-022-014-009-021-007-004-012-011-007-016-005-008-017-009-010"

book_file = "book.txt"

# Read the book

if not os.path.isfile(book_file):
    print(f"Error: File '{book_file}' not found.")
else:
    with open(book_file, "r", encoding='utf-8') as f:
        book = f.read()
        
# Shnderrimi i tekstit ne liste qe te mund te kontrollohet fjale per fjale


book_words = book.split(" ")

key = {}



# Kontrollo shkronjen e pare te cdo fjale dhe bashkangjite ne dictionary nese nuk eshte
for word in book_words:
    first_letter = word[0].upper()
    if not first_letter.isalpha():
        continue
    if first_letter not in key:
        key[first_letter] = str(book_words.index(word)+1).zfill(3)

        #key[first_letter] = str(word_position).zfill(3)
        #word_position += 1


# enkriptimi:

ciphertext = ""
for word in plaintext.upper():
    first_letter = word[0]
    if first_letter in key:
        ciphertext += key[first_letter] + "-"
    else:
        continue
        
        
 #dekriptimi
listaciphetext = ciphertext.split("-")
plaintext = ""
swapped_key = {value: key for key, value in key.items()}


for number in listaciphetext:
    if number in swapped_key:
        plaintext += swapped_key[number]



# largoje - (vizen e fundit)
ciphertext = ciphertext[:-1]


print("Key:")
print(key)
print("encryption:\n")
print("\nCiphertext:")
print(ciphertext)
print("decryption:\n")
print("\nPlaintext:")
print(plaintext)

