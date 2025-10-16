import random
import string
import nltk
from nltk.corpus import words

class PasswordGenerator:
    """Mother class for password generators,
    saves the password length as an argument
    """
    def __init__(self, pass_len):
        self.pass_len = pass_len
    
    def generate():
        pass

class RandomPasswordGenerator(PasswordGenerator):
    """Child class for generating passwords using random characters
    """
    def __init__(self, pass_len, numbers=True, special_chars=True):
        """Saves user's personal preferences for the password as arguments

        :param pass_len: length of the password
        :type pass_len: int
        :param numbers: whether the password includes numbers, defaults to True
        :type numbers: bool, optional
        :param special_chars: whether the password includes special characters, defaults to True
        :type special_chars: bool, optional
        :raises ValueError: if password length is not between 10 and 20 characters
        """
        if 10 <= pass_len <= 20:
            super().__init__(pass_len)
        else:
            raise ValueError("Password length must be between 10 and 20 characters.")
        self.numbers = numbers
        self.special_chars = special_chars

    def get_necessary_part(self):
        """Determines the necessary parts of the password based on user's input

        :return: a tuple containing the necessary characters and the number of remaining characters
        :rtype: tuple
        """
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
        """Password generator, adds the randomly generated part to the necessary part

        :return: final password
        :rtype: str
        """
        necessary_pool, char_num = self.get_necessary_part(self.pass_len)
        main_pool = string.ascii_letters + string.digits + string.punctuation
        rand_pool = ''.join(random.sample(main_pool, char_num))
        final_pool = list(necessary_pool + rand_pool)
        random.shuffle(final_pool)
        password = ''.join(final_pool)
        return password

class MemorablePasswordGenerator(PasswordGenerator):
    """Child class for generating memorable passwords using words from nltk corpus
    """
    def __init__(self, pass_len, separator='-', capitalize = False):
        if 3 <= pass_len <= 8:
            super().__init__(pass_len)
        else:
            raise ValueError("Password must be between 3 and 8 words long.")
        self.separator = separator
        self.capitalize = capitalize

    def get_memorable_list(self):
        """Gives access to a ready to use list of words

        :raises LookupError: if nltk words corpus is not found
        :return: List of words between 4 and 6 characters long
        :rtype: list
        """
        # This ensures the words are downloaded only once
        try:
            words_list = words.words()
        except LookupError:
            nltk.download('words')
            words_list = words.words()
        filtered_words = [word for word in words_list if 4 <= len(word) <= 6]
        return filtered_words

    def generate(self):
        """Generates a passwords using memorable words

        :return: final password with chosen separator and optional capitalization
        :rtype: str
        """
        initial_pool = self.get_memorable_list()
        if self.capitalize:
            initial_pool = [word.capitalize() for word in initial_pool]
        rand_words = random.choices(initial_pool, k=self.pass_len)
        password = self.separator.join(rand_words)
        return password

class PinNumberGenerator(PasswordGenerator):
    """Child class for generating pin numbers
    """
    def __init__(self, pass_len):
        if 8 <= pass_len <= 15:
            super().__init__(pass_len)
        else:
            raise ValueError("Pin number must be between 8 and 15 numbers long.")

    def generate(self):
        """Generates a random pin number

        :return: final pin number
        :rtype: str
        """
        pin_pool = string.digits
        pin_rand = random.choices(pin_pool, k=self.pass_len)
        pin = "".join(pin_rand)
        return pin
    