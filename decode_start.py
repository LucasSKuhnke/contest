alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""

with open("secret.txt") as f:
    for line in f:
        vowel_count = sum(1 for char in line if char.lower() in vowel)
        if 0 <= vowel_count < len(alphabet):
            message += alphabet[vowel_count]
        else:
            message += "?"

print("Decoded message:", message)
