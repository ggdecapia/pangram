def is_pangram(sentence):
    import re
    # remove non-alphabetic characters, spaces
    alpha_chars = re.sub("[^a-zA-Z]+", '', sentence)

    # convert string to lower case
    lower_case = alpha_chars.lower()

    # convert string to list of characters
    string_to_chars = [char for char in lower_case]

    # remove duplicates
    no_dupe = set((string_to_chars))

    # count the number of chars
    char_len = len(no_dupe)

    # check if length is 26 and return True/False
    if char_len == 26:
       return True
    else:
       return False
