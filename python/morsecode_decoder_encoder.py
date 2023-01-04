from morsecode_dicts import ENCODE_DICT, DECODE_DICT


def get_user_selection() -> int:
    """
    Receive user selection, encode or decode user input?

    retrun : int user selection
    """

    print(
    """
    Encode text to morse code => 1

    Decode morse code to text => 2
    
    """
    )
    user_selection = int(input("Enter your choice[1 or 2]:"))

    return user_selection


def encode_morse_code(text: str) -> str:
    """
    Convert the user's English text to Morse code.

    param : text : user english text

    retrun : morse code
    """

    morse_code = str()

    for char in text:

        if char not in ENCODE_DICT:
            print(f"I cannot encode the {char} character :(")
            quit()

        morse_code += ENCODE_DICT[char]

    return char
