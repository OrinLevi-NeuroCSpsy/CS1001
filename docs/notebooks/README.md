# מחברות Jupyter - CS1001.py

מחברות אינטראקטיביות להבנה מעמיקה של נושאי הקורס.

---

## רשימת מחברות

| מחברת | נושאים | Open in Colab | קישור לסיכום |
|-------|--------|---------------|--------------|
| [binary_search_and_complexity.ipynb](binary_search_and_complexity.ipynb) | חיפוש בינארי, ניתוח סיבוכיות | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/binary_search_and_complexity.ipynb) | [complexity.md](../notes/complexity.md) |
| [recursion_and_memoization.ipynb](recursion_and_memoization.ipynb) | פיבונאצ'י, Subset Sum, LIS, LCS | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/recursion_and_memoization.ipynb) | [memoization.md](../notes/memoization.md) |
| [data_structures.ipynb](data_structures.ipynb) | BST, Hash Tables | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/data_structures.ipynb) | [oop.md](../notes/oop.md), [hash_tables.md](../notes/hash_tables.md) |
| [compression.ipynb](compression.ipynb) | האפמן, Lempel-Ziv | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/compression.ipynb) | [compression.md](../notes/compression.md) |
| [sorting.ipynb](sorting.ipynb) | Bubble, Selection, Merge, Quick | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/sorting.ipynb) | [sorting.md](../notes/sorting.md) |
| [higher_order.ipynb](higher_order.ipynb) | Lambda, Map, Filter, Reduce | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/higher_order.ipynb) | [higher_order_functions.md](../notes/higher_order_functions.md) |
| [memory.ipynb](memory.ipynb) | זיכרון, Aliasing, Copy | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/memory.ipynb) | [memory.md](../notes/memory.md) |
| [cryptography.ipynb](cryptography.ipynb) | ראשוניות, Diffie-Hellman, RSA | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/cryptography.ipynb) | [cryptography.md](../notes/cryptography.md) |
| [error_correction.ipynb](error_correction.ipynb) | המינג, קודים לתיקון שגיאות | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/error_correction.ipynb) | [error_correction.md](../notes/error_correction.md) |
| [string_matching.ipynb](string_matching.ipynb) | Naive, Rabin-Karp, KMP | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orinlevi/CS1001_sum/blob/master/notebooks/string_matching.ipynb) | [string_matching.md](../notes/string_matching.md) |

---

## הרצה

### אפשרות 1: Jupyter Notebook
```bash
cd notebooks
jupyter notebook
```

### אפשרות 2: JupyterLab
```bash
cd notebooks
jupyter lab
```

### אפשרות 3: VS Code
פתח את הקובץ `.ipynb` ב-VS Code עם התוסף Python/Jupyter.

### אפשרות 4: Google Colab
העלה את הקובץ ל-[Google Colab](https://colab.research.google.com/).

---

## מה יש בכל מחברת?

### recursion_and_memoization.ipynb
- פיבונאצ'י: נאיבי vs memoization
- ספירת קריאות רקורסיביות
- Subset Sum
- LIS (Longest Increasing Subsequence)
- LCS (Longest Common Subsequence)
- טבלת "מתי memoization עוזר?"

### data_structures.ipynb
- BST: הכנסה, חיפוש, סריקות
- ויזואליזציה של עצים
- Hash Table עם שרשראות
- השוואת ביצועים BST vs Hash

### compression.ipynb
- בניית עץ האפמן
- יצירת קודים וקידוד/פענוח
- ויזואליזציה של עץ האפמן
- Lempel-Ziv: דחיסה ופענוח
- חישוב ביטים ומתי כדאי לדחוס

### sorting.ipynb
- מימוש 5 אלגוריתמי מיון
- השוואת ביצועים על קלטים שונים
- הדגמת מקרה גרוע ל-Quicksort
- טבלת סיבוכיויות

### cryptography.ipynb
- בדיקת ראשוניות (naive ויעיל)
- נפה של ארטוסתנס
- חשבון מודולרי ו-GCD
- Diffie-Hellman Key Exchange
- RSA: יצירת מפתחות, הצפנה ופענוח
- חתימה דיגיטלית

### error_correction.ipynb
- מרחק המינג
- סיבית זוגיות
- קוד המינג (7,4)
- קוד המינג מורחב (8,4) - SECDED
- חישוב ביטי בדיקה

### string_matching.ipynb
- חיפוש נאיבי
- Rabin-Karp עם rolling hash
- KMP ובניית טבלת failure
- השוואת ביצועים

---

## טיפים

1. **הריצו את התאים בסדר** - חלק מהתאים תלויים בתאים קודמים
2. **שנו פרמטרים** - נסו לשנות את גודל הקלט ולראות את ההשפעה
3. **הוסיפו תאים** - אל תפחדו להוסיף תאים משלכם לניסויים

---

*חלק מפרויקט [CS1001_sum](../README.md)*
