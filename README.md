# Password Generator

<img src="images/banner.jpg" alt="Password Generator" height="210" width="1100">

## Introduction
Here's a simple password generator implemented in Python, hope you enjoy it!
It provides three different choices for generating passwords, using: random characters, dictionary words, and numbers (to produce a pin number). The code is organized using a mother class and subclasses for each password generation method. The password specifications can be adjusted based on the user's needs. This includes options for password length, character types, separators, and capitalization.

### Project Structure
```
Password-Generator/
│
├── src/
│   ├── main.py
│   
└── README.md
```

### How to run
to run the project, make sure you have Python installed on your machine. Then, follow these steps:
```
python src/main.py
```

## Features
- Generate passwords using random characters, dictionary words, or numbers.
- Customize password length and character types.
- Easy-to-use command-line interface.
- Makes use of NLTK library for dictionary word generation.

## Requirements
- Python 3.6 or higher
- NLTK library