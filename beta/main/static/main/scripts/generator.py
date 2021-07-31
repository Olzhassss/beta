import random
import string

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))


def generate_word(length):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word

def generate_phone_number():
    number='7'
    for i in range(11):
        number+= str(random.randint(0,9))
    return number

def generate_email(length):
    email = ''
    for i in range(length):
        email += random.choice(string.ascii_letters + string.digits)
    email += '@' + random.choice(['gmail.com', 'gmail.com', 'gmail.com', 'ast.nis.edu.kz', 'atree.kz', 'mail.ru', 'mail.ru', 'yahoo.org'])
    return email

# def generate_name(count, length):
#     if __name__ == "__main__":
#         try:
#             count = int(count)
#         except:
#             count = 2

#         try:
#             length = int(length)
#         except:
#             length = 6

#         for i in range(count):
#             return (generate_word(length))