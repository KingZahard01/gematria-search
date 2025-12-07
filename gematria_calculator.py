HEBREW_LETTERS = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 10,
    "כ": 20,
    "ל": 30,
    "מ": 40,
    "נ": 50,
    "ס": 60,
    "ע": 70,
    "פ": 80,
    "צ": 90,
    "ק": 100,
    "ר": 200,
    "ש": 300,
    "ת": 400,
    "ך": 20,
    "ם": 40,
    "ן": 50,
    "ף": 80,
    "ץ": 90,
}


def calculate_gematria(word):
    """
    Calcula el valor numérico de una palabra hebrea.

    Args:
        word (str): Palabra en hebreo

    Returns:
        int: Valor de gematría
    """
    total = 0
    for char in word:
        if char in HEBREW_LETTERS:
            total += HEBREW_LETTERS[char]
        else:
            # Caracteres no hebreos (espacios, puntuación, etc.)
            continue
    return total


def extract_hebrew_words(text):
    """
    Extrae palabras hebreas puras de un texto.
    Elimina puntuación, números, etc.
    """
    import re

    # Encuentra secuencias de caracteres hebreos
    hebrew_pattern = re.compile(r"[\u0590-\u05FF]+")
    return hebrew_pattern.findall(text)


def get_word_gematria_pairs(text):
    """
    Extrae todas las palabras de un texto y calcula su gematría.

    Returns:
        list: Tuplas (palabra, gematría)
    """
    words = extract_hebrew_words(text)
    return [(word, calculate_gematria(word)) for word in words]
