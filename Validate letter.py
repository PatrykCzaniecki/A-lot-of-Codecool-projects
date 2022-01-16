'''Implement the function validate_letter which receives 2 parameters: string user_input and integer options_amount.
This function is used for validating, whether given user_input is a valid one-letter answer, within given range, used by a quiz program.
The user is expected to input a one letter (upper or lowercase), which is then checked whether it is within acceptable range. 
The range is determined by the options_amount parameter, for example: if it's value is three, then the acceptable letters are A B C 
(the first 3 letters of the alphabet). If user has entered a valid letter input, the letter's index in the alphabet should be returned. 
Otherwise, for any invalid input, return None.'''

options_amount = int(input("Please provide range of validation: ")) 
user_letter = str(input("Please provide one letter: ").lower())
alphabet = [chr(i) for i in range(97, 123)]

def validate_letter(user_letter, options_amount):
    if user_letter in alphabet[:options_amount]:
        return alphabet.index(user_letter)
    else:
        return None

validate_letter(user_letter, options_amount)