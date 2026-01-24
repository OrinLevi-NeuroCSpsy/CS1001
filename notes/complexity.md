# סיבוכיות זמן ומקום (Big-O) - סיכום לבחינה

---

## הגדרות פורמליות

### O (Big-O) - חסם עליון
**הגדרה:** f(n) = O(g(n)) אם קיימים c > 0 ו-n₀ כך שלכל n > n₀:
```
f(n) ≤ c · g(n)
```

**משמעות:** f גדלה **לכל היותר** כמו g (במקרה הגרוע).

### Ω (Omega) - חסם תחתון
**הגדרה:** f(n) = Ω(g(n)) אם קיימים c > 0 ו-n₀ כך שלכל n > n₀:
```
f(n) ≥ c · g(n)
```

**משמעות:** f גדלה **לפחות** כמו g (במקרה הטוב).

### Θ (Theta) - חסם הדוק
**הגדרה:** f(n) = Θ(g(n)) אם f(n) = O(g(n)) וגם f(n) = Ω(g(n))

**משמעות:** f גדלה **בדיוק** כמו g.

> **בקורס CS1001:** בדרך כלל משתמשים ב-O לתאר את המקרה הגרוע.

---

## כללי אצבע לספירת צעדים

### 1. רצף פעולות → חיבור (לוקחים את הגדול)
```python
x = 5           # O(1)
for i in range(n):  # O(n)
    print(i)
```
**סה"כ:** O(1) + O(n) = **O(n)**

### 2. לולאה → כפל
```python
for i in range(n):      # n פעמים
    print(i)            # O(1) כל פעם
```
**סה"כ:** n × O(1) = **O(n)**

### 3. לולאות מקוננות → כפל נוסף
```python
for i in range(n):          # n פעמים
    for j in range(n):      # n פעמים כל איטרציה
        print(i, j)         # O(1)
```
**סה"כ:** n × n × O(1) = **O(n²)**

### 4. לולאה עם חצי/כפול → O(log n)
```python
# חצי בכל צעד
i = n
while i > 1:
    print(i)
    i = i // 2      # n → n/2 → n/4 → ... → 1
```
**סה"כ:** log₂(n) צעדים = **O(log n)**

```python
# כפול בכל צעד
i = 1
while i < n:
    print(i)
    i = i * 2       # 1 → 2 → 4 → ... → n
```
**סה"כ:** log₂(n) צעדים = **O(log n)**

### 5. קריאה רקורסיבית → תלוי במבנה
- קריאה אחת עם n-1: O(n)
- שתי קריאות עם n-1: O(2ⁿ)
- קריאה אחת עם n/2: O(log n)

---

## טבלת סדרי גודל נפוצים

| סיבוכיות | שם | דוגמה | n=1000 |
|----------|-----|-------|--------|
| O(1) | קבוע | גישה לאיבר במערך | 1 |
| O(log n) | לוגריתמי | חיפוש בינארי | ~10 |
| O(n) | לינארי | חיפוש לינארי | 1,000 |
| O(n log n) | לינאריתמי | מיון יעיל (merge sort) | ~10,000 |
| O(n²) | ריבועי | לולאה כפולה | 1,000,000 |
| O(2ⁿ) | אקספוננציאלי | פיבונאצ'י רקורסיבי נאיבי | ~10³⁰⁰ |

**סדר מהיר לאיטי:**
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
```

---

## דוגמאות קוד

### O(1) - קבוע
```python
def get_first(lst):
    return lst[0]  # גישה ישירה לאינדקס
```

### O(log n) - לוגריתמי
```python
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### O(n) - לינארי
```python
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
```

### O(n²) - ריבועי
```python
def has_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False
```

### O(2ⁿ) - אקספוננציאלי
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)  # שתי קריאות רקורסיביות
```

---

## מלכודות בחינה (5 נפוצות)

### 1. לולאה כפולה ≠ תמיד O(n²)
```python
for i in range(n):
    for j in range(5):      # 5 קבוע, לא n!
        print(i, j)
```
**סיבוכיות:** O(n × 5) = **O(n)**, לא O(n²)

### 2. גבול פנימי תלוי בחיצוני
```python
for i in range(n):
    for j in range(i):      # j רץ עד i, לא עד n
        print(i, j)
```
**סיבוכיות:** 0 + 1 + 2 + ... + (n-1) = n(n-1)/2 = **O(n²)**

### 3. break יכול לשנות את הסיבוכיות
```python
def find_first_even(lst):
    for x in lst:
        if x % 2 == 0:
            return x    # מקרה טוב: O(1)
    return None         # מקרה גרוע: O(n)
```
**מקרה גרוע:** O(n), **מקרה טוב:** O(1)

### 4. פעולות על מחרוזות/רשימות עולות
```python
# שרשור מחרוזות בלולאה - לא O(n)!
s = ""
for i in range(n):
    s = s + str(i)      # כל שרשור הוא O(len(s))
```
**סיבוכיות:** O(1 + 2 + 3 + ... + n) = **O(n²)** !

### 5. פונקציות מובנות לא תמיד O(1)
```python
for i in range(n):
    if x in lst:        # in על רשימה הוא O(n)
        print("found")
```
**סיבוכיות:** O(n) × O(n) = **O(n²)**

---

## סיבוכיות מקום (Space Complexity)

### מה זה?
כמות הזיכרון הנוספת שהאלגוריתם צורך (לא כולל הקלט).

### דוגמאות

**O(1) - זיכרון קבוע:**
```python
def sum_list(lst):
    total = 0           # משתנה אחד בלבד
    for x in lst:
        total += x
    return total
```

**O(n) - זיכרון לינארי:**
```python
def double_list(lst):
    result = []         # רשימה חדשה בגודל n
    for x in lst:
        result.append(x * 2)
    return result
```

**O(n) - רקורסיה:**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # n קריאות ב-stack
```

### זמן מול מקום - Trade-off
לפעמים אפשר "לקנות" זמן במקום ולהפך:
- **Memoization:** שומרים תוצאות (יותר זיכרון) → פחות חישובים
- **In-place:** לא יוצרים מבנה חדש (פחות זיכרון) → לפעמים יותר איטי

---

## שאלות בחינה טיפוסיות

### שאלה 1: מהי הסיבוכיות?
```python
for i in range(n):
    for j in range(n):
        for k in range(10):
            print(i, j, k)
```
**תשובה:** O(n × n × 10) = **O(n²)**

---

### שאלה 2: מהי הסיבוכיות?
```python
i = n
while i > 0:
    for j in range(n):
        print(i, j)
    i = i // 2
```
**תשובה:** O(log n) × O(n) = **O(n log n)**

---

### שאלה 3: מהי הסיבוכיות?
```python
def func(n):
    if n <= 1:
        return 1
    return func(n // 2) + func(n // 2)
```
**תשובה:** שתי קריאות, כל אחת עם n/2 → עץ בעומק log n עם 2^(log n) = n עלים → **O(n)**

---

## סיכום נקודות חשובות

- [ ] O = חסם עליון (מקרה גרוע)
- [ ] רצף → מקסימום, לולאה → כפל
- [ ] לולאה עם חצי/כפול → O(log n)
- [ ] לבדוק מה באמת הגבול של הלולאה הפנימית
- [ ] פעולות על מחרוזות/רשימות עולות זמן
- [ ] `in` על רשימה הוא O(n)
- [ ] רקורסיה צורכת מקום ב-stack
