import json

# 1. Cargar el JSON (asumiendo que está guardado como 'genesis.json')
with open("data/genesis.json", "r", encoding="utf-8") as file:
    genesis_data = json.load(file)

# 2. Mostrar metadatos
print("=== METADATOS ===")
print(f"Título: {genesis_data['title']}")
print(f"Idioma: {genesis_data['language']}")
print(f"Versión: {genesis_data['versionTitle']}")
print(f"Categorías: {', '.join(genesis_data['categories'])}")
print(
    f"Estructura: {genesis_data['sectionNames'][0]} -> {genesis_data['sectionNames'][1]}"
)
print()

# 3. Contar capítulos y versículos
chapters = genesis_data["text"]
print(f"Total de capítulos: {len(chapters)}")

# Contar versículos por capítulo
for i, chapter in enumerate(chapters, 1):
    print(f"Capítulo {i}: {len(chapter)} versículos")

print()


# 4. Acceder a versículos específicos
def get_verse(chapter_num, verse_num):
    """Obtiene un versículo específico (capítulo y versículo son números base-1)"""
    try:
        chapter_index = chapter_num - 1
        verse_index = verse_num - 1
        return genesis_data["text"][chapter_index][verse_index]
    except IndexError:
        return "Versículo no encontrado"


# Ejemplos:
print("=== EJEMPLOS DE VERSÍCULOS ===")

# Génesis 1:1 (primer versículo de la Biblia)
print("Génesis 1:1:")
print(get_verse(1, 1))
print()

# Génesis 1:26 (creación del hombre)
print("Génesis 1:26:")
print(get_verse(1, 26))
print()

# Génesis 3:15 (primera promesa mesiánica)
print("Génesis 3:15:")
print(get_verse(3, 15))
print()


# 5. Buscar palabras específicas (ejemplo simple)
def search_word(word, max_results=5):
    """Busca una palabra en todos los versículos"""
    results = []
    for chap_idx, chapter in enumerate(genesis_data["text"], 1):
        for verse_idx, verse in enumerate(chapter, 1):
            if word in verse:
                results.append((chap_idx, verse_idx, verse))
                if len(results) >= max_results:
                    return results
    return results


# Buscar la palabra "אלהים" (Dios)
print("=== BÚSQUEDA DE PALABRA 'אלהים' (primeras 5 ocurrencias) ===")
search_results = search_word("אלהים", 5)

for chap, verse, text in search_results:
    print(f"Génesis {chap}:{verse}: {text[:50]}...")

print()


# 6. Extraer todo el texto de un capítulo
def get_chapter_text(chapter_num):
    """Obtiene todo el texto de un capítulo"""
    try:
        chapter_index = chapter_num - 1
        verses = genesis_data["text"][chapter_index]
        return "\n".join([f"{i + 1}. {verse}" for i, verse in enumerate(verses)])
    except IndexError:
        return "Capítulo no encontrado"


# Mostrar el primer capítulo completo
print("=== GÉNESIS CAPÍTULO 1 (completo) ===")
print(get_chapter_text(1)[:1000] + "...")  # Mostrar solo los primeros 1000 caracteres

# 7. Estadísticas básicas
print("\n=== ESTADÍSTICAS ===")
total_verses = sum(len(chapter) for chapter in chapters)
print(f"Total de versículos en Génesis: {total_verses}")

# Contar caracteres
all_text = " ".join([" ".join(chapter) for chapter in chapters])
print(f"Total de caracteres en hebreo: {len(all_text)}")
print(f"Total de palabras (aproximado): {len(all_text.split())}")
