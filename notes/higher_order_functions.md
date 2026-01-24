# פונקציות מסדר גבוה ו-Lambda - סיכום לבחינה

---

## מושגי יסוד

### פונקציה מסדר גבוה (Higher-Order Function)
פונקציה שמקיימת **לפחות אחד** מהתנאים:
1. **מקבלת** פונקציה כפרמטר
2. **מחזירה** פונקציה כערך

### פונקציות הן אזרחיות מדרגה ראשונה (First-Class Citizens)
בפייתון, פונקציות הן **אובייקטים** כמו כל דבר אחר:

```python
def greet(name):
    return f"Hello {name}"

# פונקציה היא אובייקט
print(type(greet))      # <class 'function'>

# אפשר להשים למשתנה
f = greet
print(f("World"))       # Hello World

# אפשר לשים ברשימה
funcs = [greet, len, max]

# אפשר להעביר כפרמטר
def call_twice(func, arg):
    return func(arg) + " " + func(arg)

call_twice(greet, "Hi")  # "Hello Hi Hello Hi"
```

---

## ביטויי Lambda

### מהו Lambda?
פונקציה **אנונימית** (ללא שם) בשורה אחת.

### תחביר
```python
lambda parameters: expression
```

### השוואה לפונקציה רגילה

```python
# פונקציה רגילה
def square(x):
    return x ** 2

# Lambda מקביל
square = lambda x: x ** 2

# שימוש זהה
square(5)  # 25
```

### דוגמאות

```python
# פרמטר אחד
double = lambda x: x * 2
double(5)  # 10

# שני פרמטרים
add = lambda x, y: x + y
add(3, 4)  # 7

# עם תנאי (ternary)
abs_val = lambda x: x if x >= 0 else -x
abs_val(-5)  # 5

# ללא פרמטרים
get_pi = lambda: 3.14159
get_pi()  # 3.14159
```

### מתי להשתמש ב-Lambda?
- פונקציות **קצרות וחד-פעמיות**
- כארגומנט ל-`map`, `filter`, `sorted`
- **לא** לפונקציות מורכבות - קשה לקריאה

```python
# טוב - קצר וברור
sorted(words, key=lambda w: len(w))

# רע - מסובך מדי
f = lambda x: x**2 if x > 0 else (-x)**2 if x < 0 else 0  # קשה לקרוא!
```

---

## map()

### מהו?
מפעיל פונקציה על **כל איבר** ב-iterable.

### תחביר
```python
map(function, iterable)
```

### דוגמאות

```python
# הכפלה
nums = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, nums)
list(doubled)  # [2, 4, 6, 8]

# עם פונקציה רגילה
def square(x):
    return x ** 2

squared = map(square, nums)
list(squared)  # [1, 4, 9, 16]

# המרת טיפוסים
strings = ['1', '2', '3']
numbers = list(map(int, strings))  # [1, 2, 3]

# על מחרוזת
list(map(str.upper, ['hello', 'world']))  # ['HELLO', 'WORLD']
```

### map עם מספר iterables

```python
a = [1, 2, 3]
b = [10, 20, 30]

# מחבר זוגות
result = map(lambda x, y: x + y, a, b)
list(result)  # [11, 22, 33]
```

### שקילות ל-List Comprehension

```python
# map
list(map(lambda x: x**2, nums))

# list comprehension - בד"כ יותר קריא
[x**2 for x in nums]
```

---

## filter()

### מהו?
מסנן איברים לפי **תנאי** (פונקציה שמחזירה True/False).

### תחביר
```python
filter(function, iterable)
```

### דוגמאות

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# רק זוגיים
evens = filter(lambda x: x % 2 == 0, nums)
list(evens)  # [2, 4, 6, 8, 10]

# רק חיוביים
numbers = [-2, -1, 0, 1, 2]
positives = filter(lambda x: x > 0, numbers)
list(positives)  # [1, 2]

# סינון מחרוזות ריקות
words = ['hello', '', 'world', '', 'python']
non_empty = filter(None, words)  # None = בודק truthiness
list(non_empty)  # ['hello', 'world', 'python']

# סינון לפי אורך
words = ['a', 'bb', 'ccc', 'dddd']
long_words = filter(lambda w: len(w) > 2, words)
list(long_words)  # ['ccc', 'dddd']
```

### שקילות ל-List Comprehension

```python
# filter
list(filter(lambda x: x % 2 == 0, nums))

# list comprehension - בד"כ יותר קריא
[x for x in nums if x % 2 == 0]
```

---

## reduce()

### מהו?
מצמצם iterable ל**ערך אחד** על ידי הפעלת פונקציה מצטברת.

### תחביר
```python
from functools import reduce
reduce(function, iterable, initial)  # initial אופציונלי
```

### איך זה עובד?

```python
reduce(f, [a, b, c, d])
# שקול ל:
f(f(f(a, b), c), d)
```

**ויזואליזציה:**
```
[1, 2, 3, 4] עם חיבור:

שלב 1: 1 + 2 = 3
שלב 2: 3 + 3 = 6
שלב 3: 6 + 4 = 10

תוצאה: 10
```

### דוגמאות

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

# סכום
total = reduce(lambda acc, x: acc + x, nums)
# 15

# מכפלה
product = reduce(lambda acc, x: acc * x, nums)
# 120

# מקסימום
maximum = reduce(lambda acc, x: acc if acc > x else x, nums)
# 5

# עם ערך התחלתי
total = reduce(lambda acc, x: acc + x, nums, 10)
# 10 + 1 + 2 + 3 + 4 + 5 = 25

# שרשור מחרוזות
words = ['Hello', ' ', 'World']
sentence = reduce(lambda acc, w: acc + w, words)
# 'Hello World'
```

### שימושים נפוצים

```python
from functools import reduce

# flatten רשימה מקוננת
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda acc, lst: acc + lst, nested, [])
# [1, 2, 3, 4, 5, 6]

# מציאת המחרוזת הארוכה ביותר
words = ['cat', 'elephant', 'dog']
longest = reduce(lambda a, b: a if len(a) > len(b) else b, words)
# 'elephant'
```

---

## sorted() עם key

### תחביר
```python
sorted(iterable, key=function, reverse=False)
```

### דוגמאות

```python
# מיון לפי אורך
words = ['banana', 'pie', 'apple', 'a']
sorted(words, key=len)
# ['a', 'pie', 'apple', 'banana']

# מיון לפי האות האחרונה
sorted(words, key=lambda w: w[-1])
# ['banana', 'apple', 'pie', 'a']

# מיון מילון לפי ערכים
d = {'a': 3, 'b': 1, 'c': 2}
sorted(d.items(), key=lambda item: item[1])
# [('b', 1), ('c', 2), ('a', 3)]

# מיון רשימת tuples לפי איבר שני
students = [('דני', 85), ('רוני', 92), ('יוסי', 78)]
sorted(students, key=lambda s: s[1], reverse=True)
# [('רוני', 92), ('דני', 85), ('יוסי', 78)]

# מיון case-insensitive
words = ['Banana', 'apple', 'Cherry']
sorted(words, key=str.lower)
# ['apple', 'Banana', 'Cherry']
```

---

## פונקציות שמחזירות פונקציות

### Closure (סגור)
פונקציה פנימית ש"זוכרת" משתנים מהפונקציה החיצונית.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n    # n "נזכר" מהפונקציה החיצונית
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

double(5)   # 10
triple(5)   # 15
```

### מפעל פונקציות (Function Factory)

```python
def make_power(exp):
    return lambda x: x ** exp

square = make_power(2)
cube = make_power(3)

square(4)   # 16
cube(4)     # 64
```

### דקורטור פשוט (לידיעה)

```python
def log_calls(func):
    def wrapper(*args):
        print(f"Calling {func.__name__} with {args}")
        return func(*args)
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(2, 3)
# Calling add with (2, 3)
# 5
```

---

## שילוב map, filter, reduce

### Pipeline עיבוד נתונים

```python
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# סכום ריבועי הזוגיים
result = reduce(
    lambda acc, x: acc + x,         # צעד 3: סכום
    map(
        lambda x: x ** 2,            # צעד 2: ריבוע
        filter(
            lambda x: x % 2 == 0,    # צעד 1: רק זוגיים
            nums
        )
    )
)
# 2² + 4² + 6² + 8² + 10² = 4 + 16 + 36 + 64 + 100 = 220

# אותו דבר עם list comprehension:
sum(x**2 for x in nums if x % 2 == 0)  # 220
```

---

## any() ו-all()

### any()
מחזיר `True` אם **לפחות איבר אחד** הוא True.

```python
any([False, False, True])   # True
any([False, False, False])  # False
any([])                     # False

# עם generator
nums = [1, 3, 5, 7, 8, 9]
any(x % 2 == 0 for x in nums)  # True (יש זוגי)
```

### all()
מחזיר `True` אם **כל האיברים** הם True.

```python
all([True, True, True])    # True
all([True, False, True])   # False
all([])                    # True (vacuous truth)

# עם generator
nums = [2, 4, 6, 8]
all(x % 2 == 0 for x in nums)  # True (כולם זוגיים)
```

---

## zip עם פונקציות

```python
names = ['דני', 'רוני', 'יוסי']
scores = [85, 92, 78]

# יצירת מילון
dict(zip(names, scores))
# {'דני': 85, 'רוני': 92, 'יוסי': 78}

# עיבוד מקביל
list(map(lambda pair: f"{pair[0]}: {pair[1]}", zip(names, scores)))
# ['דני: 85', 'רוני: 92', 'יוסי: 78']
```

---

## טעויות נפוצות

### טעות 1: שכחה ש-map/filter מחזירים iterator

```python
nums = [1, 2, 3]
doubled = map(lambda x: x * 2, nums)

list(doubled)  # [2, 4, 6]
list(doubled)  # [] - נגמר!

# פתרון: להמיר לרשימה מיד אם צריך כמה פעמים
doubled = list(map(lambda x: x * 2, nums))
```

### טעות 2: Lambda עם statements

```python
# שגוי - lambda לא תומך ב-statements
f = lambda x: if x > 0: return x  # SyntaxError!

# נכון - רק expressions
f = lambda x: x if x > 0 else 0
```

### טעות 3: שכחת import ל-reduce

```python
reduce(lambda a, b: a + b, [1, 2, 3])  # NameError!

from functools import reduce  # צריך לייבא!
```

### טעות 4: שימוש ב-lambda כשיש פונקציה מובנית

```python
# מיותר
list(map(lambda x: str(x), nums))

# פשוט יותר
list(map(str, nums))

# מיותר
list(map(lambda x: x.upper(), words))

# פשוט יותר
list(map(str.upper, words))
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: מה יודפס?

```python
f = lambda x, y: x + y
print(f(2, 3))
```

**תשובה:** `5`

---

### שאלה 2: מה יודפס?

```python
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 3, nums))
print(result)
```

**תשובה:** `[4, 5]`

---

### שאלה 3: מה יודפס?

```python
from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda a, b: a * b, nums)
print(result)
```

**תשובה:** `24` (1×2×3×4)

---

### שאלה 4: כתוב בשורה אחת

מצא את סכום המספרים החיוביים ברשימה.

```python
nums = [-2, 3, -1, 5, -4, 2]
```

**פתרון:**
```python
sum(filter(lambda x: x > 0, nums))  # 10
# או:
sum(x for x in nums if x > 0)  # 10
```

---

### שאלה 5: מה עושה הקוד?

```python
def f(n):
    return lambda x: x ** n

g = f(3)
print(g(2))
```

**תשובה:** `8`

**הסבר:** `f(3)` מחזיר פונקציה שמעלה בחזקת 3. `g(2)` = 2³ = 8

---

## סיכום נקודות חשובות

- [ ] **Lambda** = פונקציה אנונימית: `lambda x: x * 2`
- [ ] **map** = הפעלה על כל איבר: `map(func, iterable)`
- [ ] **filter** = סינון לפי תנאי: `filter(func, iterable)`
- [ ] **reduce** = צמצום לערך אחד (צריך import!)
- [ ] **sorted עם key** = מיון לפי פונקציה
- [ ] **map/filter** מחזירים **iterator** - חד-פעמי!
- [ ] **Closure** = פונקציה פנימית שזוכרת משתנים חיצוניים
- [ ] list comprehension בד"כ קריא יותר מ-map/filter
