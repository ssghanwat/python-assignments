# 1. Check vowel or consonant
def check_vowel(ch, Vowels = ['a', 'e', 'i', 'o', 'u']):
        if ch in Vowels:
             return True
        else:
             return False
    
def main():
    char = input("Enter a character: ")
    result = check_vowel(char)
    if result == True:
        print(f"{char} is a Vowel")
    else:
        print(f"{char} is a consonant")


if __name__ == "__main__":
    main()