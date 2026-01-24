# מחרוזות (Strings) - סיכום לבחינה

---

## הגדרה פורמלית

**מחרוזת (String)** היא רצף סדרתי ו**בלתי משתנה (Immutable)** של תווים.

```python
s = "Hello"
s = 'Hello'
s = """Multi
line"""
```

### מאפיינים
| מאפיין | ערך |
|--------|-----|
| סדר | כן - לתווים יש אינדקסים |
| שינוי (Mutable) | **לא** - לא ניתן לשנות אחרי יצירה |
| כפילויות | מותר |
| סוג איברים | תווים בלבד |

---

## הסבר אינטואיטיבי

מחרוזת היא כמו שרשרת חרוזים - כל חרוז הוא תו, והם מחוברים בסדר קבוע. **אי אפשר להחליף חרוז בודד**, רק ליצור שרשרת חדשה.

```
אינדקס:   0    1    2    3    4
        +----+----+----+----+----+
תו:     | H  | e  | l  | l  | o  |
        +----+----+----+----+----+
אינדקס:  -5   -4   -3   -2   -1
שלילי
```

---

## יצירת מחרוזות

```python
# גרשיים כפולים או בודדים
s1 = "Hello"
s2 = 'World'

# מחרוזת רב-שורתית
s3 = """שורה ראשונה
שורה שנייה"""

# מחרוזת ריקה
empty = ""

# המרה מטיפוסים אחרים
s = str(42)       # "42"
s = str(3.14)     # "3.14"
s = str([1,2,3])  # "[1, 2, 3]"
```

---

## תווים מיוחדים (Escape Characters)

| תו | משמעות |
|----|--------|
| `\n` | שורה חדשה |
| `\t` | טאב |
| `\\` | קו נטוי אחורי |
| `\'` | גרש בודד |
| `\"` | גרשיים |

```python
print("שורה 1\nשורה 2")
# שורה 1
# שורה 2

print("A\tB\tC")
# A    B    C
```

---

## גישה לתווים (Indexing)

```python
s = "Python"

s[0]    # 'P' - ראשון
s[2]    # 't'
s[-1]   # 'n' - אחרון
s[-2]   # 'o'
```

### ניסיון לשנות תו - שגיאה!
```python
s[0] = 'J'  # TypeError: 'str' object does not support item assignment
```

---

## חיתוך (Slicing)

```python
s = "Hello World"

s[0:5]      # "Hello"
s[6:]       # "World"
s[:5]       # "Hello"
s[::2]      # "HloWrd" - כל תו שני
s[::-1]     # "dlroW olleH" - הפוך
s[-5:]      # "World" - 5 אחרונים
```

---

## פעולות על מחרוזות

### אופרטורים

```python
# שרשור (+)
"Hello" + " " + "World"   # "Hello World"

# כפל (*)
"ab" * 3                  # "ababab"
"-" * 20                  # "--------------------"

# שייכות (in)
"ell" in "Hello"          # True
"xyz" in "Hello"          # False

# השוואה (לקסיקוגרפית)
"apple" < "banana"        # True
"abc" == "abc"            # True
```

### פונקציות מובנות

```python
s = "Hello"

len(s)        # 5 - אורך
min(s)        # 'H' (לפי ASCII)
max(s)        # 'o'
```

---

## מתודות של מחרוזות

### בדיקות (מחזירות True/False)

```python
s = "Hello123"

s.isalpha()     # False - רק אותיות?
s.isdigit()     # False - רק ספרות?
s.isalnum()     # True - אותיות או ספרות?
s.isupper()     # False - כולו אותיות גדולות?
s.islower()     # False - כולו אותיות קטנות?
s.isspace()     # False - רק רווחים?

"Hello".isalpha()   # True
"123".isdigit()     # True
"   ".isspace()     # True
```

### המרת רישיות

```python
s = "Hello World"

s.upper()       # "HELLO WORLD"
s.lower()       # "hello world"
s.capitalize()  # "Hello world" - רק ראשונה גדולה
s.title()       # "Hello World" - כל מילה
s.swapcase()    # "hELLO wORLD"
```

### חיפוש

```python
s = "Hello World"

s.find("o")       # 4 - אינדקס ראשון (או -1 אם אין)
s.find("o", 5)    # 7 - חיפוש מאינדקס 5
s.rfind("o")      # 7 - אינדקס אחרון
s.index("o")      # 4 - כמו find, אבל ValueError אם אין
s.count("o")      # 2 - כמה פעמים

s.startswith("He")  # True
s.endswith("ld")    # True
```

### החלפה

```python
s = "Hello World"

s.replace("o", "0")       # "Hell0 W0rld" - כל ההופעות
s.replace("o", "0", 1)    # "Hell0 World" - רק ראשונה
```

### פיצול ואיחוד

```python
# split - פיצול למילים
"a,b,c".split(",")        # ['a', 'b', 'c']
"Hello World".split()     # ['Hello', 'World'] - לפי רווחים
"a::b::c".split("::")     # ['a', 'b', 'c']

# join - איחוד רשימה למחרוזת
",".join(['a', 'b', 'c']) # "a,b,c"
" ".join(['Hello', 'World'])  # "Hello World"
"".join(['a', 'b', 'c'])  # "abc"
```

### ניקוי רווחים

```python
s = "  Hello World  "

s.strip()       # "Hello World" - משני הצדדים
s.lstrip()      # "Hello World  " - משמאל
s.rstrip()      # "  Hello World" - מימין

"***Hello***".strip("*")  # "Hello"
```

---

## טבלת מתודות (לשנן!)

| מתודה | פעולה | מחזירה |
|-------|-------|--------|
| `upper()` | כל האותיות גדולות | str חדש |
| `lower()` | כל האותיות קטנות | str חדש |
| `strip()` | הסר רווחים מהקצוות | str חדש |
| `split(sep)` | פצל לרשימה | list |
| `join(lst)` | אחד רשימה | str |
| `replace(old, new)` | החלף | str חדש |
| `find(sub)` | מצא אינדקס | int (-1 אם אין) |
| `count(sub)` | ספור הופעות | int |
| `startswith(s)` | מתחיל ב-? | bool |
| `endswith(s)` | מסתיים ב-? | bool |
| `isdigit()` | רק ספרות? | bool |
| `isalpha()` | רק אותיות? | bool |

> **חשוב:** כל המתודות מחזירות ערך **חדש** - המחרוזת המקורית לא משתנה!

---

## עיצוב מחרוזות (Formatting)

### f-strings (מומלץ)
```python
name = "דני"
age = 25
print(f"שמי {name} ואני בן {age}")
# שמי דני ואני בן 25

# עם חישובים
print(f"2 + 3 = {2 + 3}")  # 2 + 3 = 5

# עיצוב מספרים
pi = 3.14159
print(f"Pi = {pi:.2f}")    # Pi = 3.14
```

### format()
```python
"שמי {} ואני בן {}".format("דני", 25)
"{name} - {age}".format(name="דני", age=25)
```

### אופרטור % (ישן)
```python
"שמי %s ואני בן %d" % ("דני", 25)
```

---

## לולאות על מחרוזות

```python
s = "Hello"

# לולאה על תווים
for char in s:
    print(char)

# לולאה על אינדקסים
for i in range(len(s)):
    print(i, s[i])

# עם enumerate
for i, char in enumerate(s):
    print(i, char)
```

---

## טעויות נפוצות

### טעות 1: ניסיון לשנות תו
```python
s = "Hello"
s[0] = 'J'  # TypeError!

# נכון - יצירת מחרוזת חדשה
s = 'J' + s[1:]  # "Jello"
```

### טעות 2: שכחת ש-replace מחזיר מחרוזת חדשה
```python
s = "Hello"
s.replace("e", "a")  # לא עשינו כלום עם התוצאה!
print(s)             # "Hello" - לא השתנה

# נכון
s = s.replace("e", "a")
print(s)             # "Hallo"
```

### טעות 3: שרשור בלולאה (לא יעיל)
```python
# לא יעיל - O(n²)
result = ""
for i in range(1000):
    result += str(i)

# יעיל - O(n)
result = "".join(str(i) for i in range(1000))
```

### טעות 4: בלבול בין find ל-index
```python
s = "Hello"
s.find("x")   # -1 (לא נמצא)
s.index("x")  # ValueError!
```

### טעות 5: split ללא ארגומנט
```python
"a  b  c".split(" ")   # ['a', '', 'b', '', 'c'] - רווחים ריקים!
"a  b  c".split()      # ['a', 'b', 'c'] - מתעלם מרווחים מרובים
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: מה יודפס?
```python
s = "Python"
print(s[1:4])
```
**תשובה:** `"yth"`

---

### שאלה 2: מה יודפס?
```python
s = "Hello"
s.upper()
print(s)
```
**תשובה:** `"Hello"` (המקורית לא משתנה!)

---

### שאלה 3: כתוב פונקציה שסופרת תווים
```python
def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

# או בקיצור:
def count_char(s, char):
    return s.count(char)
```

---

### שאלה 4: כתוב פונקציה שבודקת פלינדרום
```python
def is_palindrome(s):
    return s == s[::-1]

# או עם לולאה:
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            return False
    return True
```

---

### שאלה 5: מה יודפס?
```python
print("-".join(["a", "b", "c"]))
```
**תשובה:** `"a-b-c"`

---

## השוואה: רשימה מול מחרוזת

| תכונה | רשימה | מחרוזת |
|-------|-------|--------|
| Mutable | כן | **לא** |
| אינדקס | כן | כן |
| Slicing | כן | כן |
| `len()` | כן | כן |
| שינוי איבר | `lst[0] = x` | **לא אפשרי** |
| שרשור | `+` | `+` |
| כפל | `*` | `*` |

---

## סיכום נקודות חשובות

- [ ] מחרוזות הן **Immutable** - לא ניתן לשנות
- [ ] מתודות מחזירות מחרוזת **חדשה**
- [ ] `find()` מחזיר -1 אם לא נמצא, `index()` זורק שגיאה
- [ ] `split()` ללא ארגומנט מתעלם מרווחים מרובים
- [ ] `s[::-1]` - היפוך מחרוזת
- [ ] f-strings: `f"Hello {name}"` - עיצוב נוח
- [ ] `join()` יעיל יותר משרשור בלולאה
