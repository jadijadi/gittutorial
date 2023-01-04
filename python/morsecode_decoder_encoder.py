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
