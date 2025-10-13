import random
import string
import nltk

class PasswordGenerator:
    def __init__(self, pass_len):
        self.pass_len = pass_len
    
    def generate():
        pass

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, pass_len, numbers=True, special_chars=True):
        super().__init__(pass_len)
        self.numbers = numbers
        self.special_chars = special_chars

    def get_necessary_part(self, pass_len):
        necessary_lowercase = random.choice(string.ascii_lowercase)
        necessary_uppercase = random.choice(string.ascii_uppercase)
        necessary_pool = necessary_lowercase + necessary_uppercase
        char_num = self.pass_len - 2
        if self.numbers:
            necessary_number = random.choice(string.digits)
            necessary_pool += necessary_number
            char_num -= 1
        if self.special_chars:
            necessary_special_char = random.choice(string.punctuation)
            necessary_pool += necessary_special_char
            char_num -= 1
        return necessary_pool, char_num

    def generate(self):
        necessary_pool, char_num = self.get_necessary_part(self.pass_len)
        print(necessary_pool, char_num)
        main_pool = string.ascii_letters + string.digits + string.punctuation
        rand_pool = ''.join(random.sample(main_pool, char_num))
        print(rand_pool)
        final_pool = list(necessary_pool + rand_pool)
        print(final_pool)
        random.shuffle(final_pool)
        password = ''.join(final_pool)
        return password

class PinNumberGenerator(PasswordGenerator):
    def __init__(self, pass_len):
        super().__init__(pass_len)

    def generate(self):
        pin_pool = string.digits
        pin_rand = random.choices(pin_pool, k=self.pass_len)
        pin = "".join(pin_rand)
        return pin