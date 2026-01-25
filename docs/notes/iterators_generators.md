# איטרטורים וגנרטורים (Iterators & Generators) - סיכום לבחינה

---

## מוטיבציה

### הבעיה
רוצים לעבור על אוסף איברים **בלי לטעון הכל לזיכרון**.

```python
# בעייתי - טוען מיליון איברים לזיכרון
lst = list(range(1000000))
for x in lst:
    print(x)

# יעיל - מייצר איבר אחד בכל פעם
for x in range(1000000):
    print(x)
```

### הפתרון: Lazy Evaluation
**חישוב עצל** - מייצרים ערכים רק כשצריך אותם, לא מראש.

---

## מושגי יסוד

### Iterable (ניתן לאיטרציה)
אובייקט שאפשר לעבור עליו בלולאת `for`.

```python
# דוגמאות ל-Iterables:
[1, 2, 3]       # רשימה
"hello"         # מחרוזת
{1, 2, 3}       # קבוצה
{"a": 1}        # מילון
range(10)       # range
open("file")    # קובץ
```

### Iterator (איטרטור)
אובייקט שיודע **איפה הוא נמצא** באיטרציה ומה הערך **הבא**.

### ההבדל

| Iterable | Iterator |
|----------|----------|
| "ניתן למעבר" | "יודע לעבור" |
| יש לו `__iter__` | יש לו `__iter__` + `__next__` |
| אפשר ליצור ממנו iterator | הוא עצמו ה-iterator |
| רשימה, מחרוזת, range | iter(list), generator |

---

## פרוטוקול האיטרציה

### שתי מתודות

1. **`__iter__()`** - מחזיר את האיטרטור
2. **`__next__()`** - מחזיר את הערך הבא, או זורק `StopIteration`

### מה קורה בלולאת for?

```python
for x in [1, 2, 3]:
    print(x)
```

מאחורי הקלעים:
```python
# פייתון עושה:
iterator = iter([1, 2, 3])   # קורא ל-__iter__
while True:
    try:
        x = next(iterator)   # קורא ל-__next__
        print(x)
    except StopIteration:
        break
```

### דוגמה ידנית

```python
lst = [1, 2, 3]
it = iter(lst)      # יצירת איטרטור

next(it)    # 1
next(it)    # 2
next(it)    # 3
next(it)    # StopIteration!
```

---

## iter() ו-next()

### iter(iterable)
מחזיר איטרטור מאובייקט iterable.

```python
lst = [1, 2, 3]
it = iter(lst)
type(it)    # <class 'list_iterator'>
```

### next(iterator)
מחזיר את הערך הבא, או זורק `StopIteration`.

```python
it = iter([1, 2])
next(it)            # 1
next(it)            # 2
next(it)            # StopIteration

# עם ערך ברירת מחדל (לא זורק שגיאה):
next(it, "סוף")    # "סוף"
```

---

## יצירת Iterator עם מחלקה

```python
class CountUp:
    """איטרטור שסופר מ-start עד end"""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # האיטרטור הוא האובייקט עצמו

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# שימוש
for num in CountUp(1, 5):
    print(num)
# 1, 2, 3, 4
```

### דוגמה: איטרטור פיבונאצ'י

```python
class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

list(Fibonacci(8))  # [0, 1, 1, 2, 3, 5, 8, 13]
```

---

## גנרטורים (Generators)

### מהו גנרטור?
**דרך פשוטה ליצור איטרטור** באמצעות פונקציה עם `yield`.

### yield vs return

| return | yield |
|--------|-------|
| מסיים את הפונקציה | "משהה" את הפונקציה |
| מחזיר ערך אחד | יכול "להחזיר" ערכים רבים |
| - | זוכר את המצב בין קריאות |

### תחביר בסיסי

```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()  # יוצר אובייקט generator
type(gen)             # <class 'generator'>

next(gen)    # 1
next(gen)    # 2
next(gen)    # 3
next(gen)    # StopIteration
```

### מה קורה?

```python
def countdown(n):
    print("מתחיל!")
    while n > 0:
        print(f"לפני yield {n}")
        yield n
        print(f"אחרי yield {n}")
        n -= 1
    print("סיום!")

gen = countdown(3)
# כלום לא קורה עדיין!

next(gen)
# מדפיס: "מתחיל!", "לפני yield 3"
# מחזיר: 3
# (הפונקציה "קפואה" אחרי yield)

next(gen)
# מדפיס: "אחרי yield 3", "לפני yield 2"
# מחזיר: 2

next(gen)
# מדפיס: "אחרי yield 2", "לפני yield 1"
# מחזיר: 1

next(gen)
# מדפיס: "אחרי yield 1", "סיום!"
# זורק: StopIteration
```

---

## דוגמאות גנרטורים

### גנרטור פשוט: טווח

```python
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

list(my_range(1, 5))  # [1, 2, 3, 4]
```

### גנרטור אינסופי

```python
def count_forever(start=0):
    n = start
    while True:
        yield n
        n += 1

gen = count_forever()
next(gen)  # 0
next(gen)  # 1
next(gen)  # 2
# ... לעולם לא נגמר!
```

### גנרטור פיבונאצ'י

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
[next(fib) for _ in range(10)]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### גנרטור שקורא קובץ שורה-שורה

```python
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# יעיל לקבצים גדולים - שורה אחת בזיכרון בכל רגע
for line in read_lines("big_file.txt"):
    process(line)
```

---

## Generator Expressions

### תחביר
כמו list comprehension, אבל עם **סוגריים עגולים**.

```python
# List comprehension - יוצר רשימה בזיכרון
squares_list = [x**2 for x in range(1000000)]

# Generator expression - יוצר generator (עצלן)
squares_gen = (x**2 for x in range(1000000))
```

### השוואה

```python
import sys

lst = [x**2 for x in range(10000)]
gen = (x**2 for x in range(10000))

sys.getsizeof(lst)  # ~87,616 bytes
sys.getsizeof(gen)  # ~112 bytes (!)
```

### שימוש

```python
# עם פונקציות שמקבלות iterable
sum(x**2 for x in range(100))      # 328350
max(len(w) for w in words)          # המילה הארוכה ביותר
any(x > 100 for x in numbers)       # האם יש מספר > 100?
```

---

## פונקציות מובנות שעובדות עם Iterators

### enumerate
```python
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)
# 0 a
# 1 b
# 2 c
```

### zip
```python
names = ['דני', 'רוני']
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name}: {age}")
# דני: 25
# רוני: 30
```

### map
```python
nums = [1, 2, 3, 4]
squares = map(lambda x: x**2, nums)
list(squares)  # [1, 4, 9, 16]
```

### filter
```python
nums = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, nums)
list(evens)  # [2, 4, 6]
```

> **שים לב:** `map`, `filter`, `zip`, `enumerate` מחזירים **איטרטורים**, לא רשימות!

---

## yield from

### מה זה?
דרך קצרה ל-yield על כל איברי iterable אחר.

```python
# במקום:
def gen():
    for x in [1, 2, 3]:
        yield x
    for x in [4, 5, 6]:
        yield x

# אפשר:
def gen():
    yield from [1, 2, 3]
    yield from [4, 5, 6]

list(gen())  # [1, 2, 3, 4, 5, 6]
```

### שימושי לרקורסיה

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # רקורסיה
        else:
            yield item

list(flatten([1, [2, 3], [4, [5, 6]]]))
# [1, 2, 3, 4, 5, 6]
```

---

## יתרונות Generators

| יתרון | הסבר |
|-------|------|
| **חיסכון בזיכרון** | לא טוענים הכל מראש |
| **ביצועים** | מתחילים לעבד מיד, לא ממתינים |
| **אינסוף** | אפשר לייצג רצפים אינסופיים |
| **קריאות** | קוד פשוט יותר ממחלקת iterator |
| **Pipeline** | קל לשרשר עיבודים |

---

## טעויות נפוצות

### טעות 1: איטרטור נגמר אחרי שימוש אחד

```python
gen = (x for x in [1, 2, 3])

list(gen)  # [1, 2, 3]
list(gen)  # [] - ריק! האיטרטור נגמר

# פתרון: ליצור מחדש
gen = (x for x in [1, 2, 3])
```

### טעות 2: בלבול בין generator function ל-generator object

```python
def gen_func():
    yield 1
    yield 2

gen_func        # פונקציה
gen_func()      # generator object

# צריך לקרוא לפונקציה!
for x in gen_func:     # שגוי!
    print(x)

for x in gen_func():   # נכון
    print(x)
```

### טעות 3: שכחה שגנרטור הוא חד-פעמי

```python
def nums():
    yield 1
    yield 2

g = nums()
print(1 in g)   # True
print(2 in g)   # True
print(1 in g)   # False! הגנרטור כבר עבר על 1
```

### טעות 4: ניסיון לגשת לאינדקס

```python
gen = (x for x in [1, 2, 3])
gen[0]   # TypeError! generators don't support indexing
```

### טעות 5: return בגנרטור

```python
def bad_gen():
    return [1, 2, 3]  # מחזיר רשימה, לא generator!

def good_gen():
    yield from [1, 2, 3]  # או: for x in [1,2,3]: yield x
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: מה יודפס?

```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))
```

**תשובה:**
```
1
2
```

---

### שאלה 2: מה יודפס?

```python
def gen():
    for i in range(3):
        yield i * 2

print(list(gen()))
```

**תשובה:** `[0, 2, 4]`

---

### שאלה 3: כתוב גנרטור

כתוב גנרטור `evens(n)` שמייצר את כל הזוגיים עד n.

**פתרון:**
```python
def evens(n):
    for i in range(0, n + 1, 2):
        yield i

# או:
def evens(n):
    i = 0
    while i <= n:
        yield i
        i += 2

list(evens(10))  # [0, 2, 4, 6, 8, 10]
```

---

### שאלה 4: מה ההבדל?

```python
a = [x**2 for x in range(5)]
b = (x**2 for x in range(5))
```

**תשובה:**
- `a` הוא **רשימה** - כל הערכים מחושבים מיד ונשמרים בזיכרון
- `b` הוא **generator** - ערכים מחושבים "בעצלתיים" רק כשצריך

---

### שאלה 5: השלם את הקוד

```python
class EvenNumbers:
    """איטרטור שמחזיר מספרים זוגיים עד limit"""
    def __init__(self, limit):
        # השלם

    def __iter__(self):
        # השלם

    def __next__(self):
        # השלם
```

**פתרון:**
```python
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value
```

---

## סיכום נקודות חשובות

- [ ] **Iterable** = יש לו `__iter__`, **Iterator** = יש לו גם `__next__`
- [ ] `iter()` יוצר iterator, `next()` מקבל ערך הבא
- [ ] **Generator** = פונקציה עם `yield` (דרך קלה ליצור iterator)
- [ ] `yield` משהה את הפונקציה, `return` מסיים אותה
- [ ] **Generator expression**: `(x for x in ...)` - חוסך זיכרון
- [ ] איטרטור הוא **חד-פעמי** - אחרי שנגמר, צריך ליצור חדש
- [ ] `map`, `filter`, `zip`, `enumerate` מחזירים איטרטורים
- [ ] `yield from` - קיצור ל-yield על iterable

---

## קישורים נוספים

- **קוד:** [iterators_generators_demo.py](../code/iterators_generators_demo.py)
- **שאלות בחינה:** [recursion_and_generators.md](../exam_questions/recursion_and_generators.md)
