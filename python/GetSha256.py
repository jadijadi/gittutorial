# hash your string to sha256
import hashlib
from encodings import utf_8 as utf8

def main(text):
    sha256 = hashlib.sha256()
    encodedText = utf8.encode(text)[0]
    sha256.update(encodedText)
    print(f"Your Hash\n{sha256.hexdigest()}")

if __name__ == "__main__":
    text = input('enter your text:')
    main(text)