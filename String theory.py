#Make a function to check if a string is a palindrome or isogram or pangram or anagram

def is_palindrome(text):
    text_lower = text.lower()
    only_letters = ''.join(c for c in text_lower if c.isalpha())
    text_reversed = only_letters[::-1]
    if only_letters == text_reversed:        
        return True
    else:
        return False   

def is_isogram(text):
    text_lower = text.lower()
    only_letters = ''.join(i for i in text_lower if i.isalpha())
    letter_list = []
    for letter in only_letters:
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)     
    return True

def is_pangram(text):
    only_letters = ''.join(i for i in text if i.isalpha())
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    for i in alphabet:
        if i not in only_letters.lower():
            return False    
    return True

def is_anagram(text1, text2):
    text1_lower = text1.lower()
    text2_lower = text2.lower()
    only_letters1 = ''.join(i for i in text1_lower if i.isalpha())
    only_letters2 = ''.join(i for i in text2_lower if i.isalpha())
    if sorted(only_letters1) == sorted(only_letters2):
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_palindrome("Mr. Owl ate my metal worm"))
    print(is_palindrome("Eva, can I see bees in a cave?"))
    print(is_isogram("uncopyrightables")) 
    print(is_pangram("The quick brown fox jumps over the lazy dog"))
    print(is_anagram("Justin Timberlake", "I'm a jerk but listen"))