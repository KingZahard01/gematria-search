from collections import defaultdict

from gematria_calculator import get_word_gematria_pairs
from torah_loader import TorahLoader


class GematriaSearchEngine:
    def __init__(self, data_directory="."):
        self.loader = TorahLoader(data_directory)
        self.loader.load_all_books()
        self.index = defaultdict(list)  # gematría -> lista de ocurrencias
        self.build_index()

    def build_index(self):
        """Construye un índice inverso de gematría."""
        print("Construyendo índice de gematría...")

        for verse_info in self.loader.iterate_all_verses():
            words_pairs = get_word_gematria_pairs(verse_info["text"])

            for word, gematria in words_pairs:
                self.index[gematria].append(
                    {
                        "word": word,
                        "book": verse_info["book"],
                        "book_hebrew": verse_info["book_hebrew"],
                        "chapter": verse_info["chapter"],
                        "verse": verse_info["verse"],
                        "full_text": verse_info["text"],
                    }
                )

        print(
            f"Índice construido. {len(self.index)} valores gematría únicos encontrados."
        )

    def search_by_gematria(self, target_value):
        """
        Busca todas las palabras con una gematría específica.

        Args:
            target_value (int): Valor de gematría a buscar

        Returns:
            list: Todas las ocurrencias con esa gematría
        """
        return self.index.get(target_value, [])

    def search_by_word(self, word):
        """
        Busca todas las ocurrencias de una palabra específica.

        Args:
            word (str): Palabra en hebreo a buscar

        Returns:
            list: Todas las ocurrencias de la palabra
        """
        from gematria_calculator import calculate_gematria

        target_value = calculate_gematria(word)
        occurrences = self.search_by_gematria(target_value)

        # Filtrar para obtener solo la palabra exacta (puede haber colisiones)
        exact_matches = [occ for occ in occurrences if occ["word"] == word]
        return exact_matches

    def find_similar_gematria(self, target_value, tolerance=0):
        """
        Encuentra palabras con gematría cercana al valor objetivo.

        Args:
            target_value (int): Valor objetivo
            tolerance (int): Rango de variación permitida

        Returns:
            dict: Diccionario con gematrías cercanas y sus ocurrencias
        """
        results = {}
        for gematria, occurrences in self.index.items():
            if abs(gematria - target_value) <= tolerance:
                results[gematria] = occurrences
        return results

    def statistical_summary(self):
        """Muestra estadísticas del índice."""
        total_words = sum(len(occurrences) for occurrences in self.index.values())
        avg_occurrences = total_words / len(self.index) if self.index else 0

        print("=== ESTADÍSTICAS DEL ÍNDICE ===")
        print(f"Valores gematría únicos: {len(self.index)}")
        print(f"Total de palabras indexadas: {total_words}")
        print(f"Promedio de palabras por valor: {avg_occurrences:.2f}")

        # Mostrar los valores más comunes
        sorted_gematrias = sorted(
            self.index.items(), key=lambda x: len(x[1]), reverse=True
        )
        print("\nTop 10 valores gematría más frecuentes:")
        for gematria, occurrences in sorted_gematrias[:10]:
            print(f"  {gematria}: {len(occurrences)} palabras")
