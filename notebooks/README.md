# מחברות Jupyter - CS1001.py

מחברות אינטראקטיביות להבנה מעמיקה של נושאי הקורס.

---

## רשימת מחברות

| מחברת | נושאים | קישור לסיכום |
|-------|--------|--------------|
| [binary_search_and_complexity.ipynb](binary_search_and_complexity.ipynb) | חיפוש בינארי, ניתוח סיבוכיות | [complexity.md](../notes/complexity.md) |
| [recursion_and_memoization.ipynb](recursion_and_memoization.ipynb) | פיבונאצ'י, Subset Sum, LIS, LCS | [memoization.md](../notes/memoization.md) |
| [data_structures.ipynb](data_structures.ipynb) | BST, Hash Tables | [oop.md](../notes/oop.md), [hash_tables.md](../notes/hash_tables.md) |
| [compression.ipynb](compression.ipynb) | האפמן, Lempel-Ziv | [compression.md](../notes/compression.md) |
| [sorting.ipynb](sorting.ipynb) | Bubble, Selection, Merge, Quick | [sorting.md](../notes/sorting.md) |

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

---

## טיפים

1. **הריצו את התאים בסדר** - חלק מהתאים תלויים בתאים קודמים
2. **שנו פרמטרים** - נסו לשנות את גודל הקלט ולראות את ההשפעה
3. **הוסיפו תאים** - אל תפחדו להוסיף תאים משלכם לניסויים

---

*חלק מפרויקט [CS1001_sum](../README.md)*
