# <span class="chick-badge">🐣</span> סיכום קורס מבוא מורחב למדעי המחשב (CS1001.py) {: .main-title }

*by Orin Levi* {: .byline }

סיכום מקיף לקורס CS1001.py באוניברסיטת תל אביב, כולל סיכומי נושאים, שאלות מבחנים, מחברות Jupyter וקוד לדוגמה.

---

## ניווט באתר

| מדור | תוכן |
|------|------|
| **בית** | דף זה |
| **סיכומים** | נושאים + שאלות מבחנים |
| **מחברות** | מחברות Jupyter (תצוגה באתר) |
| **קוד** | קוד לדוגמה – [code/README.md](code/README.md) |
| **Colab** | כפתורי Open in Colab לכל מחברת |

---

## מבנה הפרויקט

```
CS1001_sum/
├── notes/              # סיכומי נושאים (26 קבצים)
├── exam_questions/     # שאלות מבחנים לפי נושאים (9 קבצים)
├── code/               # קוד לדוגמה (22 קבצים)
└── notebooks/          # מחברות Jupyter (10 מחברות)
```

---

## סיכומי נושאים (notes/)

| קובץ | נושא |
|------|------|
| [basics.md](notes/basics.md) | יסודות פייתון |
| [memory.md](notes/memory.md) | מודל הזיכרון, aliasing, copy |
| [lists.md](notes/lists.md) | רשימות |
| [strings.md](notes/strings.md) | מחרוזות |
| [dictionaries_and_sets.md](notes/dictionaries_and_sets.md) | מילונים וקבוצות |
| [functions_and_recursion.md](notes/functions_and_recursion.md) | פונקציות ורקורסיה |
| [higher_order_functions.md](notes/higher_order_functions.md) | פונקציות מסדר גבוה |
| [iterators_generators.md](notes/iterators_generators.md) | איטרטורים וגנרטורים |
| [complexity.md](notes/complexity.md) | סיבוכיות |
| [sorting.md](notes/sorting.md) | מיון |
| [search_binary.md](notes/search_binary.md) | חיפוש בינארי |
| [memoization.md](notes/memoization.md) | Memoization |
| [oop.md](notes/oop.md) | תכנות מונחה עצמים |
| [linked_lists.md](notes/linked_lists.md) | רשימות מקושרות |
| [hash_tables.md](notes/hash_tables.md) | טבלאות גיבוב |
| [number_representation.md](notes/number_representation.md) | ייצוג מספרים |
| [text_representation.md](notes/text_representation.md) | ייצוג טקסט |
| [compression.md](notes/compression.md) | דחיסה (האפמן, LZ) |
| [error_correction.md](notes/error_correction.md) | תיקון שגיאות |
| [cryptography.md](notes/cryptography.md) | קריפטוגרפיה |
| [string_matching.md](notes/string_matching.md) | התאמת מחרוזות |
| [image_processing.md](notes/image_processing.md) | עיבוד תמונות |
| [file_io.md](notes/file_io.md) | קריאה וכתיבה לקבצים |
| [exam_tricks.md](notes/exam_tricks.md) | טריקים לבחינה |
| [cheat_sheet.md](notes/cheat_sheet.md) | דף סיכום מרוכז |

---

## שאלות מבחנים (exam_questions/)

שאלות ממבחנים 2022-2025, מאורגנות לפי נושאים:

| קובץ | נושאים | מבחנים |
|------|--------|--------|
| [complexity.md](exam_questions/complexity.md) | סיבוכיות, ניתוח לולאות | 2022b-2025b |
| [data_structures.md](exam_questions/data_structures.md) | BST, Hash Tables | 2022b-2025b |
| [recursion_and_generators.md](exam_questions/recursion_and_generators.md) | רקורסיה, גנרטורים, LCS | 2022b-2025b |
| [compression.md](exam_questions/compression.md) | האפמן, LZ | 2022b-2025b |
| [error_correction.md](exam_questions/error_correction.md) | קודים לתיקון שגיאות | 2022b-2023b |
| [cryptography_and_primes.md](exam_questions/cryptography_and_primes.md) | ראשוניות, קריפטוגרפיה | 2022b |
| [memory.md](exam_questions/memory.md) | זיכרון, Aliasing, Copy | שאלות נפוצות |
| [misc_topics.md](exam_questions/misc_topics.md) | PageRank, Floating Point, CFG | 2023a-2025b |

[מידע נוסף על שאלות המבחנים](exam_questions/README.md)

---

## קוד לדוגמה (code/)

קבצי Python עם מימושים ודוגמאות לכל נושא:

| קובץ | נושא |
|------|------|
| [basics_demo.py](code/basics_demo.py) | יסודות פייתון |
| [memory_demo.py](code/memory_demo.py) | זיכרון, aliasing, copy |
| [lists_demo.py](code/lists_demo.py) | פעולות על רשימות |
| [strings_demo.py](code/strings_demo.py) | פעולות על מחרוזות |
| [dict_set_demo.py](code/dict_set_demo.py) | מילונים וקבוצות |
| [recursion_demo.py](code/recursion_demo.py) | פונקציות רקורסיביות |
| [sorting_demo.py](code/sorting_demo.py) | אלגוריתמי מיון |
| [binary_search.py](code/binary_search.py) | חיפוש בינארי |
| [higher_order_demo.py](code/higher_order_demo.py) | map, filter, lambda |
| [iterators_generators_demo.py](code/iterators_generators_demo.py) | yield וגנרטורים |
| [memoization_demo.py](code/memoization_demo.py) | Memoization |
| [oop_demo.py](code/oop_demo.py) | מחלקות ואובייקטים |
| [linked_lists_demo.py](code/linked_lists_demo.py) | רשימות מקושרות |
| [hash_tables_demo.py](code/hash_tables_demo.py) | טבלאות גיבוב |
| [binary_and_hex.py](code/binary_and_hex.py) | המרות בסיסים |
| [ascii_unicode.py](code/ascii_unicode.py) | קידוד תווים |
| [compression_demo.py](code/compression_demo.py) | האפמן ו-LZ |
| [error_correction_demo.py](code/error_correction_demo.py) | קודי המינג |
| [cryptography_demo.py](code/cryptography_demo.py) | RSA, Diffie-Hellman |
| [string_matching_demo.py](code/string_matching_demo.py) | התאמת מחרוזות |
| [image_processing_demo.py](code/image_processing_demo.py) | עיבוד תמונות |
| [file_io_demo.py](code/file_io_demo.py) | קריאה/כתיבה לקבצים |

### הרצת הקוד

```bash
cd code
python basics_demo.py
```

---

## סדר לימוד מומלץ

### שלב 1: יסודות
1. basics → lists → strings → dictionaries_and_sets
2. functions_and_recursion → complexity

### שלב 2: אלגוריתמים
3. sorting → search_binary
4. higher_order_functions → iterators_generators → memoization

### שלב 3: מבני נתונים
5. oop → linked_lists → hash_tables

### שלב 4: ייצוג מידע
6. number_representation → text_representation
7. compression → error_correction → cryptography

### שלב 5: נושאים נוספים
8. string_matching → image_processing → file_io

---

## הכנה לבחינה

1. **קרא את הסיכומים** ב-notes/
2. **תרגל שאלות** מ-exam_questions/
3. **הרץ את הקוד** ב-[code/](code/README.md) להבנה מעמיקה
4. **עבור על הטריקים** ב-[exam_tricks.md](notes/exam_tricks.md)
5. **פתח מחברות ב-Colab** מתפריט **Colab** או מ-[מחברות](notebooks/README.md)

---

## קישורים שימושיים

- [Colab – פתיחת מחברת (דוגמה: חיפוש בינארי)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/binary_search_and_complexity.ipynb) (או מתפריט **Colab** בצד)
- [אתר הקורס](http://tau-cs1001-py.wikidot.com/)
- [מבחנים קודמים](http://tau-cs1001-py.wikidot.com/exams)
- [Python Documentation](https://docs.python.org/3/)

---

## תרומה

מצאתם טעות? רוצים להוסיף חומר? פתחו Issue או Pull Request — או שלחו מייל ל־[orinl@mail.tau.ac.il](mailto:orinl@mail.tau.ac.il).

---

*נוצר לקורס CS1001.py, אוניברסיטת תל אביב. המרצה: אמיר רובינשטיין.*
