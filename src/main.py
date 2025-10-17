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
        super().__init__(pass_len)
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
        necessary_pool, char_num = self.get_necessary_part()
        main_pool = string.ascii_letters
        if self.numbers:
            main_pool += string.digits
        if self.special_chars:
            main_pool += string.punctuation
        rand_pool = ''.join(random.sample(main_pool, char_num))
        final_pool = list(necessary_pool + rand_pool)
        random.shuffle(final_pool)
        password = ''.join(final_pool)
        return password

class MemorablePasswordGenerator(PasswordGenerator):
    """Child class for generating memorable passwords using words from nltk corpus
    """
    def __init__(self, pass_len, separator='-', capitalize = False):
        super().__init__(pass_len)
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
        super().__init__(pass_len)

    def generate(self):
        """Generates a random pin number

        :return: final pin number
        :rtype: str
        """
        pin_pool = string.digits
        pin_rand = random.choices(pin_pool, k=self.pass_len)
        pin = "".join(pin_rand)
        return pin

while True:
    try:
        pass_type = input("Please type in wich kind of password you need: 'Random', 'Memorable' or 'Pin'(r/m/p): ").lower()
        if not pass_type in ["random", "memorable", "pin", "r", "m", "p"]:
            raise ValueError("Invalid password type. Please choose 'Random', 'Memorable', or 'Pin'.")
        break
    except ValueError as ve:
        print(ve)

def test(inp_message, error_message, type):
    user_input = input(inp_message)
    if type == int and user_input.isdigit():
        user_input = int(user_input)
        return user_input
    elif type == str and user_input in ["yes", "no", "y", "n"]:
        if user_input in ["yes", "y"]:
            return True
        else:
            return False
    elif type == str and user_input in string.punctuation:
            return user_input
    else:
        raise ValueError(f"Invalid input. {error_message}")

if pass_type in ["random", "r"]:
    while True:
        try:
            pass_length = test("How long should the password be? (10-20 characters): ", "Please type in a number between 10 and 20.", int)
            if not 10 <= pass_length <= 20:
                raise ValueError("Password length must be between 10 and 20 characters.")
            break
        except ValueError as ve:
            print(ve)
    while True:
        try:
            numbers = test("Should the password include numbers? (yes/no): ", "Please type in 'yes' or 'no'.", str)
            break
        except ValueError as ve:
            print(ve)
    while True:
        try:
            special_chars = test("Should the password include special characters? (yes/no): ", "Please type in 'yes' or 'no'.", str)
            break
        except ValueError as ve:
            print(ve)
    password = RandomPasswordGenerator(pass_length, numbers, special_chars)

if pass_type in ["memorable", "m"]:
    while True:
        try:
            pass_length = test("How many words long should the password be? (3-8 words): ", "Please type in a number between 3 and 8.", int)
            if not 3 <= pass_length <= 8:
                raise ValueError("Password length must be between 3 and 8 words.")
            break
        except ValueError as ve:
            print(ve)
    while True:
        try:
            separator = test(f"Please choose the separator for your password from these options: {string.punctuation} ", f"Please type in a separator ({string.punctuation}).", str)
            break
        except ValueError as ve:
            print(ve)
    while True:
        try:
            capitalized = test("Should the words in the password be capitalized? (yes/no): ", "Please type in 'yes' or 'no'.", str)
            break
        except ValueError as ve:
            print(ve)
    password = MemorablePasswordGenerator(pass_length, separator, capitalized)

if pass_type in ["pin", "p"]:
    while True:
        try:
            pass_length = test("How long should the password be? (3-8 characters): ", "Please type in a number between 3 and 8.", int)
            if not 3 <= pass_length <= 8:
                raise ValueError("Password length must be between 3 and 8.")
            break
        except ValueError as ve:
            print(ve)
    password = PinNumberGenerator(pass_length)

if __name__ == "__main__":
    password_generated = password.generate()
    print(f"Generated password: {password_generated}")