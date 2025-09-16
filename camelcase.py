def camelcase(sentence):
    """Convert sentence to camelCase, e.g., 'Display all books' -> 'displayAllBooks'"""
    title_case = sentence.title()  # Capitalize each word
    upper_camel_cased = title_case.replace(' ', '')  # Remove spaces
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
    """ Display program name """
    message = 'Awesome camelcase program!!'
    stars = '*' * len(message)
    print(f'\n{stars}\n{message}\n{stars}\n')

def main():
    banner()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()