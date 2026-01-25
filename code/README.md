# קוד לדוגמה - CS1001.py

קבצי Python עם מימושים ודוגמאות לכל נושא בקורס.

---

## הרצה

```bash
python <filename>.py
```

לדוגמה:
```bash
python sorting_demo.py
```

---

## רשימת קבצים

### יסודות פייתון

| קובץ | תוכן |
|------|------|
| [basics_demo.py](basics_demo.py) | משתנים, תנאים, לולאות, פונקציות בסיסיות |
| [lists_demo.py](lists_demo.py) | פעולות על רשימות, slicing, list comprehension |
| [strings_demo.py](strings_demo.py) | פעולות על מחרוזות, עיבוד טקסט |
| [dict_set_demo.py](dict_set_demo.py) | מילונים, קבוצות, פעולות נפוצות |

### רקורסיה ואלגוריתמים

| קובץ | תוכן |
|------|------|
| [recursion_demo.py](recursion_demo.py) | פיבונאצ'י, פקטוריאל, מגדלי האנוי, בעיות רקורסיביות |
| [sorting_demo.py](sorting_demo.py) | Bubble, Selection, Insertion, Merge, Quick Sort |
| [binary_search.py](binary_search.py) | חיפוש בינארי - איטרטיבי ורקורסיבי |
| [memoization_demo.py](memoization_demo.py) | פיבונאצ'י עם memoization, דוגמאות נוספות |

### פונקציות מתקדמות

| קובץ | תוכן |
|------|------|
| [higher_order_demo.py](higher_order_demo.py) | map, filter, reduce, lambda, closures |
| [iterators_generators_demo.py](iterators_generators_demo.py) | yield, גנרטורים, איטרטורים אינסופיים |

### תכנות מונחה עצמים

| קובץ | תוכן |
|------|------|
| [oop_demo.py](oop_demo.py) | מחלקות, ירושה, מתודות מיוחדות, BST |
| [linked_lists_demo.py](linked_lists_demo.py) | רשימה מקושרת חד/דו-כיוונית |
| [hash_tables_demo.py](hash_tables_demo.py) | טבלת גיבוב עם שרשראות |

### ייצוג מידע

| קובץ | תוכן |
|------|------|
| [binary_and_hex.py](binary_and_hex.py) | המרות בין בסיסים, פעולות ביטיות |
| [ascii_unicode.py](ascii_unicode.py) | קידוד ASCII ו-Unicode, ord/chr |

### דחיסה ותיקון שגיאות

| קובץ | תוכן |
|------|------|
| [compression_demo.py](compression_demo.py) | האפמן (בניית עץ, קידוד, פענוח), Lempel-Ziv |
| [error_correction_demo.py](error_correction_demo.py) | קודי המינג, זיהוי ותיקון שגיאות |

### קריפטוגרפיה

| קובץ | תוכן |
|------|------|
| [cryptography_demo.py](cryptography_demo.py) | RSA, Diffie-Hellman, בדיקת ראשוניות, modpower |

### נושאים נוספים

| קובץ | תוכן |
|------|------|
| [string_matching_demo.py](string_matching_demo.py) | חיפוש נאיבי, Rabin-Karp, KMP |
| [image_processing_demo.py](image_processing_demo.py) | מטריצות, פילטרים, עיבוד תמונות |
| [file_io_demo.py](file_io_demo.py) | קריאה וכתיבה לקבצים, with statement |

---

## דוגמאות שימושיות לבחינה

### מיון מהיר (Quicksort)
```python
# מתוך sorting_demo.py
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    smaller = [x for x in lst[1:] if x < pivot]
    equal = [x for x in lst if x == pivot]
    greater = [x for x in lst[1:] if x > pivot]
    return quicksort(smaller) + equal + quicksort(greater)
```

### גנרטור אינסופי
```python
# מתוך iterators_generators_demo.py
def naturals():
    n = 0
    while True:
        yield n
        n += 1
```

### BST - הכנסה
```python
# מתוך oop_demo.py
def insert(self, key, val):
    if self.root is None:
        self.root = TreeNode(key, val)
    else:
        self._insert_rec(self.root, key, val)
```

### Memoization
```python
# מתוך memoization_demo.py
def fib_mem(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_mem(n-1, memo) + fib_mem(n-2, memo)
    return memo[n]
```

---

## קישור לסיכומים

כל קובץ קוד מתאים לסיכום ב-[notes/](../notes/):

| קוד | סיכום |
|-----|-------|
| sorting_demo.py | [sorting.md](../notes/sorting.md) |
| recursion_demo.py | [functions_and_recursion.md](../notes/functions_and_recursion.md) |
| oop_demo.py | [oop.md](../notes/oop.md) |
| compression_demo.py | [compression.md](../notes/compression.md) |
| ... | ... |

---

*חלק מפרויקט [CS1001_sum](../README.md)*
