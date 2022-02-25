# Importing required libraries
import string
import random
lower_case_strings=string.ascii_lowercase# Returns a list of lower case ascii letters
upper_case_strings=string.ascii_uppercase# Returns a list of upper case ascii letters
digits=string.digits# Returns a list of digits (0,1,2,3,4,5,6,7,8,9)
symbols=string.punctuation# Returns a list of all punctuations
keyboard=lower_case_strings +upper_case_strings + digits + symbols
def generate_password(length):
    '''
    Generates a random password with given length , length should not exceed 94 (as len of keyboard varible is 94), if it exceeds a valid output will not be given
    '''
    try:
        password_list=random.sample(keyboard,length)# sequence = list Keyboard , K=length
        '''
sample() is an inbuilt function of random module in Python that
returns a particular length list of items chosen from the sequence 
i.e. list, tuple, string or set. Used for random sampling without replacement.
It has no repeating elements
sequence: Can be a list, tuple, string, or set.
k: An Integer value, it specify the length of a sample.
Returns: k length new list of elements chosen from the sequence.
        '''
        password_string="".join(password_list)# The join functions joins all elements in password list and puts it in a string named password
    except:
        password_string="valid_password_not_generated"
    return password_string
