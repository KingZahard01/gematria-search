import json
import os


class TorahLoader:
    def __init__(self, data_directory="."):
        self.data_directory = data_directory
        self.books = {
            "genesis": "בראשית",
            "exodus": "שמות",
            "leviticus": "ויקרא",
            "numbers": "במדבר",
            "deuteronomy": "דברים",
        }
        self.texts = {}

    def load_all_books(self):
        """Carga todos los libros de la Torá desde archivos JSON."""
        for eng_name, he_name in self.books.items():
            filename = f"data/{eng_name}.json"
            filepath = os.path.join(self.data_directory, filename)

            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.texts[eng_name] = {
                        "hebrew_name": he_name,
                        "chapters": data["text"],
                    }
                print(f"Cargado: {eng_name} ({he_name})")
            else:
                print(f"Archivo no encontrado: {filename}")

    def get_verse(self, book, chapter, verse):
        """Obtiene un versículo específico."""
        try:
            return self.texts[book]["chapters"][chapter - 1][verse - 1]
        except (KeyError, IndexError):
            return None

    def iterate_all_verses(self):
        """Itera sobre todos los versículos de la Torá."""
        for book_name, book_data in self.texts.items():
            for chapter_idx, chapter in enumerate(book_data["chapters"], 1):
                for verse_idx, verse in enumerate(chapter, 1):
                    yield {
                        "book": book_name,
                        "book_hebrew": book_data["hebrew_name"],
                        "chapter": chapter_idx,
                        "verse": verse_idx,
                        "text": verse,
                    }
