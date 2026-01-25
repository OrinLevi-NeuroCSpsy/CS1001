# זיכרון בפייתון

## 1. מודל הזיכרון של Python

### משתנים כמצביעים (References)

בפייתון, **משתנה הוא שם שמצביע לאובייקט בזיכרון**, לא תא זיכרון שמכיל ערך.

```python
x = [1, 2, 3]
```

מה קורה:
1. נוצר אובייקט רשימה `[1, 2, 3]` בזיכרון (ב-Heap)
2. המשתנה `x` מצביע לאובייקט הזה

```
x  ──────►  [1, 2, 3]
(שם)        (אובייקט בזיכרון)
```

### בדיקת זהות עם `id()`

```python
x = [1, 2, 3]
print(id(x))  # 140234567890 (כתובת בזיכרון)

y = x
print(id(y))  # 140234567890 (אותה כתובת!)

z = [1, 2, 3]
print(id(z))  # 140234567999 (כתובת אחרת!)
```

### `==` מול `is`

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

# == בודק שוויון ערכים
print(x == y)  # True
print(x == z)  # True

# is בודק זהות (אותו אובייקט)
print(x is y)  # True  (אותו אובייקט)
print(x is z)  # False (אובייקטים שונים עם אותו ערך)
```

---

## 2. Mutable מול Immutable

### טיפוסים Immutable (בלתי ניתנים לשינוי)

| טיפוס | דוגמה |
|-------|-------|
| `int` | `42` |
| `float` | `3.14` |
| `str` | `"hello"` |
| `tuple` | `(1, 2, 3)` |
| `bool` | `True` |
| `frozenset` | `frozenset({1, 2})` |

```python
x = 5
print(id(x))  # 140234500

x = x + 1     # לא משנה את 5, יוצר אובייקט חדש 6
print(id(x))  # 140234532 (כתובת חדשה!)
```

```python
s = "hello"
# s[0] = "H"  # TypeError! מחרוזות הן immutable
s = "H" + s[1:]  # יוצר מחרוזת חדשה
```

### טיפוסים Mutable (ניתנים לשינוי)

| טיפוס | דוגמה |
|-------|-------|
| `list` | `[1, 2, 3]` |
| `dict` | `{"a": 1}` |
| `set` | `{1, 2, 3}` |
| אובייקטים של מחלקות | `TreeNode()` |

```python
lst = [1, 2, 3]
print(id(lst))  # 140234567890

lst.append(4)   # משנה את האובייקט הקיים!
print(id(lst))  # 140234567890 (אותה כתובת!)
```

### למה זה חשוב?

```python
# Immutable - בטוח
def add_one(n):
    n = n + 1  # יוצר אובייקט חדש, לא משנה את המקורי
    return n

x = 5
add_one(x)
print(x)  # 5 (לא השתנה)

# Mutable - זהירות!
def add_element(lst):
    lst.append(4)  # משנה את האובייקט המקורי!

my_list = [1, 2, 3]
add_element(my_list)
print(my_list)  # [1, 2, 3, 4] (השתנה!)
```

---

## 3. Aliasing (כינויים)

כשמשתנה נוסף מצביע לאותו אובייקט.

### דוגמה בסיסית

```python
a = [1, 2, 3]
b = a  # b הוא כינוי ל-a (שניהם מצביעים לאותה רשימה)

b.append(4)
print(a)  # [1, 2, 3, 4] - גם a השתנה!
```

```
a  ──────┐
         ├──►  [1, 2, 3, 4]
b  ──────┘
```

### Aliasing בפונקציות

```python
def mystery(lst):
    lst[0] = 999

original = [1, 2, 3]
mystery(original)
print(original)  # [999, 2, 3] - השתנה!
```

### Aliasing ברשימות מקוננות

```python
row = [0, 0, 0]
matrix = [row, row, row]  # שלוש שורות - אותה רשימה!

matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - כולן השתנו!
```

**הדרך הנכונה:**
```python
matrix = [[0, 0, 0] for _ in range(3)]  # שלוש רשימות נפרדות
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]] - רק הראשונה השתנתה
```

---

## 4. Shallow Copy מול Deep Copy

### Shallow Copy (העתקה רדודה)

יוצר אובייקט חדש, אבל **לא מעתיק אובייקטים מקוננים**.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
# או: shallow = original[:]
# או: shallow = list(original)

print(original is shallow)  # False (רשימות חיצוניות שונות)
print(original[0] is shallow[0])  # True (רשימות פנימיות זהות!)

shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4]] - המקורית השתנתה!
```

```
original ──►  [ ● , ● ]
               │    │
shallow  ──►  [ ● , ● ]
               │    │
               ▼    ▼
            [1,2] [3,4]  ◄── אותם אובייקטים פנימיים!
```

### Deep Copy (העתקה עמוקה)

מעתיק **הכל** - גם אובייקטים מקוננים.

```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

print(original[0] is deep[0])  # False (רשימות פנימיות שונות!)

deep[0][0] = 999
print(original)  # [[1, 2], [3, 4]] - המקורית לא השתנתה!
```

```
original ──►  [ ● , ● ]
               │    │
               ▼    ▼
            [1,2] [3,4]

deep     ──►  [ ● , ● ]
               │    │
               ▼    ▼
            [1,2] [3,4]  ◄── אובייקטים נפרדים!
```

### סיכום השוואה

| פעולה | יוצר אובייקט חדש? | מעתיק אובייקטים מקוננים? |
|-------|-------------------|--------------------------|
| `b = a` | לא | לא (aliasing) |
| `copy.copy(a)` / `a[:]` | כן | לא (shallow) |
| `copy.deepcopy(a)` | כן | כן (deep) |

### מתי להשתמש במה?

```python
# רשימה פשוטה (ללא רשימות מקוננות) - shallow מספיק
numbers = [1, 2, 3]
backup = numbers[:]

# רשימה מקוננת - צריך deep copy
matrix = [[1, 2], [3, 4]]
backup = copy.deepcopy(matrix)
```

---

## 5. Call Stack ו-Stack Frames

### מה זה Call Stack?

**מחסנית הקריאות** - מבנה נתונים שמנהל קריאות לפונקציות.

כל קריאה לפונקציה יוצרת **Stack Frame** שמכיל:
- המשתנים המקומיים
- הפרמטרים
- כתובת החזרה (לאן לחזור אחרי הפונקציה)

### דוגמה פשוטה

```python
def multiply(a, b):
    result = a * b
    return result

def square(n):
    return multiply(n, n)

def main():
    x = 5
    y = square(x)
    print(y)

main()
```

**מצב ה-Stack:**

```
קריאה ל-main():
┌─────────────────┐
│ main()          │
│   x = 5         │
└─────────────────┘

קריאה ל-square(5):
┌─────────────────┐
│ square()        │
│   n = 5         │
├─────────────────┤
│ main()          │
│   x = 5         │
└─────────────────┘

קריאה ל-multiply(5, 5):
┌─────────────────┐
│ multiply()      │
│   a = 5, b = 5  │
│   result = 25   │
├─────────────────┤
│ square()        │
│   n = 5         │
├─────────────────┤
│ main()          │
│   x = 5         │
└─────────────────┘

חזרה מ-multiply (מחזיר 25):
┌─────────────────┐
│ square()        │
│   n = 5         │
│   return 25     │
├─────────────────┤
│ main()          │
│   x = 5         │
└─────────────────┘

חזרה מ-square:
┌─────────────────┐
│ main()          │
│   x = 5         │
│   y = 25        │
└─────────────────┘
```

### Stack Overflow

כשיש יותר מדי קריאות רקורסיביות, המחסנית מתמלאת:

```python
def infinite():
    return infinite()  # RecursionError: maximum recursion depth exceeded

infinite()
```

פייתון מגביל ל-~1000 קריאות רקורסיביות (ניתן לשנות עם `sys.setrecursionlimit`).

---

## 6. Trace (מעקב ריצה)

### Trace ברקורסיה

מעקב אחרי הקריאות הרקורסיביות וערכי החזרה.

**דוגמה: פקטוריאל**

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

**Trace של `factorial(4)`:**

```
factorial(4)
│
├── 4 * factorial(3)
│       │
│       ├── 3 * factorial(2)
│       │       │
│       │       ├── 2 * factorial(1)
│       │       │       │
│       │       │       └── return 1    ← מקרה בסיס
│       │       │
│       │       └── return 2 * 1 = 2
│       │
│       └── return 3 * 2 = 6
│
└── return 4 * 6 = 24
```

**Trace של `fib(5)`:**

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   └── fib(0) → 0
│   │   │   └── return 1
│   │   └── fib(1) → 1
│   │   └── return 2
│   └── fib(2)
│       ├── fib(1) → 1
│       └── fib(0) → 0
│       └── return 1
│   └── return 3
└── fib(3)
    ├── fib(2)
    │   ├── fib(1) → 1
    │   └── fib(0) → 0
    │   └── return 1
    └── fib(1) → 1
    └── return 2
└── return 5
```

### Trace ב-Backtracking

**דוגמה: כל התמורות של מחרוזת**

```python
def permutations(s, prefix=""):
    if len(s) == 0:
        print(prefix)
        return
    for i in range(len(s)):
        permutations(s[:i] + s[i+1:], prefix + s[i])
```

**Trace של `permutations("ABC")`:**

```
permutations("ABC", "")
│
├── permutations("BC", "A")
│   ├── permutations("C", "AB")
│   │   └── permutations("", "ABC") → print "ABC"
│   │
│   └── permutations("B", "AC")
│       └── permutations("", "ACB") → print "ACB"
│
├── permutations("AC", "B")
│   ├── permutations("C", "BA")
│   │   └── permutations("", "BAC") → print "BAC"
│   │
│   └── permutations("A", "BC")
│       └── permutations("", "BCA") → print "BCA"
│
└── permutations("AB", "C")
    ├── permutations("B", "CA")
    │   └── permutations("", "CAB") → print "CAB"
    │
    └── permutations("A", "CB")
        └── permutations("", "CBA") → print "CBA"
```

**דוגמה: N-Queens (ציור פשוט)**

```python
def solve_n_queens(n, row=0, cols=set(), diag1=set(), diag2=set()):
    if row == n:
        return 1  # מצאנו פתרון

    count = 0
    for col in range(n):
        if col in cols or (row-col) in diag1 or (row+col) in diag2:
            continue  # לא חוקי - backtrack

        # נסה למקם מלכה
        count += solve_n_queens(n, row+1,
                                cols | {col},
                                diag1 | {row-col},
                                diag2 | {row+col})
    return count
```

**Trace מקוצר ל-4 מלכות:**

```
row=0: נסה col=0
  row=1: col=0 ✗, col=1 ✗, נסה col=2
    row=2: col=0 ✗, col=1 ✗, col=2 ✗, col=3 ✗
    ← backtrack
  row=1: נסה col=3
    row=2: נסה col=1
      row=3: col=0 ✗, col=1 ✗, col=2 ✗, col=3 ✗
      ← backtrack
    ...
← backtrack
row=0: נסה col=1
  row=1: col=0 ✗, col=1 ✗, col=2 ✗, נסה col=3
    row=2: נסה col=0
      row=3: col=0 ✗, col=1 ✗, נסה col=2
        ✓ פתרון! (1,3,0,2)
```

### איך לצייר Trace בבחינה

1. **רשום את הקריאה הראשונה עם הפרמטרים**
2. **הכנס פנימה (indentation) לכל קריאה רקורסיבית**
3. **רשום את ערך ההחזרה**
4. **ב-backtracking: סמן איפה חוזרים אחורה**

---

## 7. טעויות נפוצות בנושא זיכרון

### טעות 1: Default Mutable Argument

```python
# שגוי!
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - לא [2]!
print(add_item(3))  # [1, 2, 3] - לא [3]!
```

**למה?** הרשימה הריקה נוצרת **פעם אחת** כשהפונקציה מוגדרת.

**תיקון:**
```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### טעות 2: יצירת מטריצה עם כפל

```python
# שגוי!
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```

**תיקון:**
```python
matrix = [[0] * 3 for _ in range(3)]
```

### טעות 3: שינוי רשימה תוך כדי איטרציה

```python
# שגוי!
lst = [1, 2, 3, 4, 5]
for x in lst:
    if x % 2 == 0:
        lst.remove(x)  # משנה את הרשימה תוך כדי!
print(lst)  # [1, 3, 5]? לא בטוח...
```

**תיקון:**
```python
lst = [x for x in lst if x % 2 != 0]
# או:
lst = [1, 2, 3, 4, 5]
for x in lst[:]:  # עובר על עותק
    if x % 2 == 0:
        lst.remove(x)
```

### טעות 4: השוואה עם `is` במקום `==`

```python
# שגוי לפעמים!
a = 1000
b = 1000
print(a is b)  # עשוי להיות False!

# נכון:
print(a == b)  # True
```

**הערה:** פייתון שומר cache למספרים קטנים (-5 עד 256), אז `is` עובד להם, אבל לא למספרים גדולים.

### טעות 5: שכחה שמחרוזות הן Immutable

```python
def make_uppercase(s):
    s.upper()  # לא משנה את s!
    return s

text = "hello"
print(make_uppercase(text))  # "hello" (לא השתנה)

# תיקון:
def make_uppercase(s):
    return s.upper()
```

### טעות 6: Aliasing לא מכוון בפונקציה

```python
def process(data):
    data.sort()  # משנה את הרשימה המקורית!
    return data[0]

original = [3, 1, 2]
smallest = process(original)
print(original)  # [1, 2, 3] - סודר! לא רצינו

# תיקון:
def process(data):
    sorted_data = sorted(data)  # יוצר רשימה חדשה
    return sorted_data[0]
```

---

## 8. סיכום מהיר לבחינה

### חוקים לזכור:

1. **משתנה = מצביע** - לא מכיל ערך, מצביע לאובייקט

2. **`=` לא מעתיק** - יוצר alias (כינוי)

3. **Immutable בטוח** - `int`, `str`, `tuple` לא משתנים

4. **Mutable מסוכן** - `list`, `dict`, `set` יכולים להשתנות

5. **Default arguments** - אף פעם לא `[]` או `{}`

6. **רשימה מקוננת** - צריך `deepcopy`

7. **`==` לערך, `is` לזהות**

### טבלת פעולות:

| פעולה | מה היא עושה |
|-------|-------------|
| `b = a` | כינוי (alias) |
| `b = a[:]` | shallow copy לרשימה |
| `b = list(a)` | shallow copy לרשימה |
| `b = a.copy()` | shallow copy |
| `b = copy.deepcopy(a)` | deep copy |

### בדיקה מהירה:

```python
import copy

original = [[1, 2], [3, 4]]

# מה ישתנה אחרי כל פעולה?
alias = original
shallow = original[:]
deep = copy.deepcopy(original)

original[0][0] = 999

print(alias[0][0])    # 999 (הושפע)
print(shallow[0][0])  # 999 (הושפע - shallow!)
print(deep[0][0])     # 1   (לא הושפע)
```

---

## קישורים

- [יסודות](basics.md) - משתנים וטיפוסים
- [רשימות](lists.md) - עבודה עם רשימות
- [פונקציות ורקורסיה](functions_and_recursion.md) - קריאות ו-stack
- [Memoization](memoization.md) - שמירת תוצאות בזיכרון

---

*חלק מפרויקט [CS1001_sum](../README.md)*
