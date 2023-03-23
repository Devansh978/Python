'''
WAP to accept a character from the user and display whether it is a vowel or consonant.
Author: Bikramadittya Bagchi
Date: 11-03-2021
'''

def vowel_conso_check():
    character = input("Enter any character to check vowel or consonant: ")
    if character[0] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        print(f"Entered character {character[0]} is a VOWEL!")
    else:
        print(f"Entered character {character[0]} is a CONSONANT!")

def main():
    vowel_conso_check()

if __name__=="__main__":
    main()