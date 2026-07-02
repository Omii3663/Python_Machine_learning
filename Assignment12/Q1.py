<<<<<<< HEAD
def CheckVowel(char):
    if char in ['a', 'e', 'i', 'o', 'u']:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")

def main():
    print('-'*30)
    print("------Check Vowel ------")
    print('-'*30)

    char = input("Enter a character :")
    if len(char) == 1:
        CheckVowel(char.lower())
    else:
        print("Please enter a single character.")

if __name__ == "__main__":
    main()
=======
def CheckVowel(char):
    if char in ['a', 'e', 'i', 'o', 'u']:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")

def main():
    print('-'*30)
    print("------Check Vowel ------")
    print('-'*30)

    char = input("Enter a character :")
    if len(char) == 1:
        CheckVowel(char.lower())
    else:
        print("Please enter a single character.")

if __name__ == "__main__":
    main()
>>>>>>> c5e63c5 (ok)
