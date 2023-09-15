import openpyxl

STATIC_LOOKUP = {
    "x": 0,
    "h": 1,
    "d": 2,
    "c": 3,
    "b": 4,
    "a": 5,
    "f": 6,
    "g": 7,
    "m": 8,
    "n": 9
}

ENCODE_LOOKUP = dict()
DECODE_LOOKUP = dict()


def load(key, val, decode_delimiter_append=True):
    ENCODE_LOOKUP[str(key)] = str(val)
    DECODE_LOOKUP[str(val)] = str(key) + ('.' if decode_delimiter_append else '')


def load_lookup_table():
    for key, val in STATIC_LOOKUP.items():
        load(key, val, False)

    xlsx_file_path = 'Fidel Char with All Code.xlsx'
    workbook = openpyxl.load_workbook(xlsx_file_path)
    sheet = workbook['Sheet2']

    for row in sheet.iter_rows(values_only=True):
        val = None
        for cell_value in row:
            if val:
                load(cell_value, val)
                val = None
            else:
                val = cell_value
    workbook.close()


def decode(text):
    words = text.split()
    translated_words = []

    for word in words:
        translated_chars = []
        for char in word.split("."):
            if char.isnumeric():
                trans_char = ENCODE_LOOKUP.get(char, char)
                translated_chars.append(str(trans_char))
            else:
                for c in char:
                    if c != "/":
                        trans_char = ENCODE_LOOKUP.get(c, c)
                        translated_chars.append(str(trans_char))
        translated_words.append("".join(translated_chars))

    return " ".join(translated_words)


def encode(text):
    words = text.split()
    translated_words = []
    for word in words:
        translated_chars = []
        for char in word:
            trans_char = DECODE_LOOKUP.get(char, char)
            translated_chars.append(str(trans_char))
        translated_words.append("".join(translated_chars))
    return " / ".join(translated_words)


def start():
    while True:
        try:
            operation = input("Enter Operation:\nPress 1 for ENCODE\nPress 2 for DECODE\n")
            if operation == "1":
                text = input("Enter Input:")
                output = encode(text)
            elif operation == "2":
                text = input("Enter Input:")
                output = decode(text)
            else:
                output = "Invalid Option"
            print(output)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    load_lookup_table()
    start()
