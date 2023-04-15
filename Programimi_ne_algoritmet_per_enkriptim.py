import os

plaintext = "What a curious feeling!' said Alice; `I must be shutting up like a telescope."

ciphertext2 = "002-011-001-004-001-041-048-034-028-008-048-009-070-107-107-145-028-019-005-009-001-028-021-001-145-028-041-107-028-064-048-009-004-003-107-009-011-048-004-004-028-019-005-048-027-145-028-432-107-001-004-107-145-107-009-041-008-027-107"

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
listaciphetext = ciphertext2.split("-")
plaintext = ""
swapped_key = {value: key for key, value in key.items()}


for number in listaciphetext:
    if number in swapped_key:
        plaintext += swapped_key[number]



# largoje - (vizen e fundit)
ciphertext = ciphertext[:-1]


print("Key:")
print(key)
print("\n\n*********************ENCRYPTION*********************\n")
print("Ciphertext:")
print(ciphertext)
print("\n\n*********************DECRYPTION*********************\n")
print("Plaintext:")
print(plaintext)

