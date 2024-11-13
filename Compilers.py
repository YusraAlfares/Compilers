# Define keywords, relational operators, other operators, and delimiters for the toy programming language

keywords = {'start', 'finish', 'then', 'if', 'repeat', 'var', 'int', 'float', 'do', 'read', 'print', 'void', 'return'}

relational_operators = {'==', '<', '>', '!=', '>=', '<='}

other_operators = {'=', '+', '-', '*', '/', '%'}

delimiters = {'.', '(', ')', ',', '{', '}', ';'}


def is_identifier(token):  # a method for finding identifiers in the token

    if not (token[0].isalpha() or token[0] == '_'):  # an identifier should start with either a letter or _, else false
        return False
    if len(token) > 8:  # If the length of the identifier larger than 8, then return false
        return False
    if token[-1] == '_':  # If the identifier ends with " _ ", then return false
        return False
    if token in keywords:  # If the identifier is itself also a keyword, then return false
        return False

    return all(c.isalnum() or c == '_' for c in token)  # Return true if all the characters is alphanumeric or _


def is_number(token):  # a method for finding numbers in the token
    if len(token) > 8:  # If the length exceeds 8, then return false
        return False
    return token.isdigit() or (token[0] == '-' and token[1:].isdigit())  # check if the token is a digit, or negative


def is_delimiter(token):  # Check if the token is a delimiter
    return token in delimiters


def is_whitespace(token):  # Check if the token is a whitespace
    return token.isspace()


def is_string(token):  # Check if the token is a string, including the double quotation marks
    return len(token) >= 2 and token[0] == '"' and token[-1] == '"'


def lexical_analyzer(program):  # Lexical analyzer function that will scan the input
    # Initialize a list of tokens, an empty string (current_token), i for iterations over the program
    # and an in_string for tracking inside the string, which is a boolean value.
    tokens = []
    current_token = ""
    i = 0
    in_string = False

    while i < len(program):  # Iterate over the program character by character
        char = program[i]

        if char == '/' and i + 1 < len(program) and program[i + 1] == '/':  # check if the character is a comment "//"
            while i < len(program) and program[i] != '\n':  # skip over all characters in comment, until new line
                i += 1  # move past new line character
            i += 1
            continue

        if char == '"':  # Check whether the character is a double quotation mark
            in_string = not in_string  # for checking whether the character is inside the string
            current_token += char  # The current character will be added to the current token
            if not in_string:  # checks if in_string is false or not, if it is false, it will execute the code below
                tokens.append(current_token)  # append the completed string into the tokens list
                current_token = ""  # Reset to empty string, to continue using it correctly
            i += 1  # Move to the next character in the program
            continue

        if in_string:  # If the string is inside the double quotation marks ""
            current_token += char  # add the char to the current token, collect the characters of the string
        else:  # If not inside the string
            if is_whitespace(char) or is_delimiter(char):  # If the current char is a whitespace or delimiter
                if current_token:  # if current token is not empty, prevent empty tokens from being added to token list
                    tokens.append(current_token)  # append the current token into the tokens list
                    current_token = ""  # Reset to empty string
                if is_delimiter(char):  # If the character is a delimiter
                    tokens.append(char)  # append the delimiters to the tokens list
            else:  # If the character is not a delimiter or a whitespace
                current_token += char  # character is not a delimiter or a whitespace, add to the current token

        # Any remaining tokens will be added to the tokens list, while also returning the tokens list
        i += 1

    if current_token:
        tokens.append(current_token)

    return tokens


def detect_keyword_as_identifier(tokens):  # error handling for keyword followed by another keyword, or invalid forms.
    for i in range(1, len(tokens)):  # starts from the second token in the list
        if tokens[i - 1] in keywords and tokens[i] in keywords:  # if two consecutive tokens are both keywords
            print(f"Error: Cannot use keyword '{tokens[i]}' after keyword '{tokens[i - 1]}'.")
            # If the token is not in a valid form
        elif tokens[i - 1] in keywords and not (
                is_identifier(tokens[i]) or tokens[i] in other_operators or tokens[i] in delimiters):
            print(f"Error: Invalid token '{tokens[i]}' used after keyword '{tokens[i - 1]}'.")


def classify_token(token):  # Method to classify a token into a class, if it wasn't able to be classified, then error
    token_lower = token.lower()

    if token in keywords:
        return 'keyword'
    elif is_identifier(token):
        return 'identifier'
    elif is_number(token):
        return 'number'
    elif is_string(token):
        return 'string'
    elif token in relational_operators:
        return 'relational operator'
    elif token in other_operators:
        return 'operator'
    elif is_delimiter(token):
        return 'delimiter'
    else:
        return 'error'


def main():  # Output program
    with open('input.txt', 'r') as file:
        program = file.read()

    print("Lexical Analysis Output:")
    print("***********************")
    tokens = lexical_analyzer(program)

    for token in tokens:
        token_class = classify_token(token)
        if token_class != 'error':
            print(f"'{token}' is a {token_class}")
        else:
            print(f"Error: '{token}' is not a valid token")

    detect_keyword_as_identifier(tokens)


if __name__ == "__main__":
    main()