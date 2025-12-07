# Tanach Text Processor

Un proyecto minimalista para procesar y analizar textos bíblicos en hebreo del Tanaj (Antiguo Testamento) en formato JSON.

## 📖 Contenido

Este proyecto incluye el texto completo del **Pentateuco** (Génesis, Éxodo, Levítico, Números, Deuteronomio) en hebreo original, estructurado en formato JSON para fácil acceso y análisis computacional.

## 🚀 Características

- **Texto completo** en hebreo del Pentateuco
- **Estructura organizada**: Capítulos → Versículos
- **Metadatos completos**: fuente, licencia, categorías
- **Formato limpio**: Solo texto, sin comentarios ni traducciones
- **Fácil de usar**: Acceso directo por capítulo y versículo

## 📂 Estructura del JSON

```json
{
  "language": "he",
  "title": "Genesis",
  "text": [
    ["versículo 1:1", "versículo 1:2", ...], // Capítulo 1
    ["versículo 2:1", "versículo 2:2", ...]  // Capítulo 2
  ]
}
```

## 📝 Aplicaciones posibles

- Análisis textual del hebreo bíblico
- Estudios de frecuencia de palabras
- Herramientas de estudio bíblico
- Proyectos de aprendizaje de hebreo
- Investigación académica

## 📄 Licencia

Los textos están en **Dominio Público**. El código de procesamiento es de uso libre.

## 🙏 Agradecimientos

Texto obtenido de [Tanach.us](http://www.tanach.us/Tanach.xml).

---

*Un proyecto modesto para explorar el texto bíblico desde una perspectiva computacional.*
