from gematria_search import GematriaSearchEngine

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


def main():
    # Inicializar el motor de búsqueda
    engine = GematriaSearchEngine(data_directory=".")

    # Mostrar estadísticas
    engine.statistical_summary()

    # Menú interactivo
    while True:
        print("\n" + "=" * 50)
        print("BUSCADOR DE GEMATRÍA EN LA TORÁ")
        print("=" * 50)
        print("1. Buscar por valor numérico")
        print("2. Buscar por palabra hebrea")
        print("3. Buscar valores cercanos")
        print("4. Calcular gematría de una palabra")
        print("5. Salir")

        choice = input("\nSelecciona una opción (1-5): ")

        if choice == "1":
            try:
                value = int(input("Ingresa el valor de gematría a buscar: "))
                results = engine.search_by_gematria(value)

                print(f"\nSe encontraron {len(results)} palabras con gematría {value}:")
                for i, result in enumerate(results[:20], 1):  # Mostrar solo primeras 20
                    print(f"{i}. {result['word']} (גימטריה: {value})")
                    print(
                        f"   {result['book_hebrew']} {result['chapter']}:{result['verse']}"
                    )
                    print(f"   Texto: {result['full_text']}")
                    print()

                if len(results) > 20:  # si hay más de 20 resultados
                    print(f"... y {len(results) - 20} más.")

            except ValueError:
                print("Por favor ingresa un número válido.")

        elif choice == "2":
            word = input("Ingresa la palabra en hebreo: ")
            results = engine.search_by_word(word)

            print(f"\nSe encontraron {len(results)} ocurrencias de '{word}':")
            for i, result in enumerate(results[:10], 1):  # Mostrar solo primeras 10
                print(
                    f"{i}. {result['book_hebrew']} {result['chapter']}:{result['verse']}"
                )
                print(f"   {result['full_text']}")
                print()

            if len(results) > 10:  # si hay más de 10 resultados
                print(f"... y {len(results) - 10} más.")

        elif choice == "3":
            try:
                value = int(input("Ingresa el valor de gematría: "))
                tolerance = int(input("Ingresa el rango de tolerancia: "))

                results = engine.find_similar_gematria(value, tolerance)
                total_words = sum(len(occurrences) for occurrences in results.values())

                print(
                    f"\nSe encontraron {total_words} palabras con gematría entre {value - tolerance} y {value + tolerance}:"
                )

                for gematria, occurrences in sorted(results.items()):
                    print(f"\nGematría {gematria} ({len(occurrences)} palabras):")
                    for occ in occurrences[:3]:  # Mostrar solo 3 ejemplos por valor
                        print(
                            f"  - {occ['word']} en {occ['book_hebrew']} {occ['chapter']}:{occ['verse']}"
                        )

                    if len(occurrences) > 3:  # si hay más de 3 resultados
                        print(f"  ... y {len(occurrences) - 3} más")

            except ValueError:
                print("Por favor ingresa números válidos.")

        elif choice == "4":
            from gematria_calculator import calculate_gematria

            word = input("Ingresa la palabra en hebreo: ")
            value = calculate_gematria(word)
            print(f"La gematría de '{word}' es: {value}")

            # Mostrar desglose
            print("\nDesglose:")
            for char in word:
                if char in HEBREW_LETTERS:
                    print(f"  {char}: {HEBREW_LETTERS[char]}")

        elif choice == "5":
            print("¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Por favor selecciona 1-5.")


if __name__ == "__main__":
    main()
