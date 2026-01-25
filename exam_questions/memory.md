# שאלות מבחן - זיכרון, Aliasing, Copy

שאלות ממבחנים על נושאי זיכרון בפייתון.

---

## שאלות "מה יודפס?"

### שאלה 1: Aliasing בסיסי

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

<details>
<summary>תשובה</summary>

```
[1, 2, 3, 4]
```

**הסבר:** `b = a` יוצר alias - שניהם מצביעים לאותה רשימה. שינוי דרך `b` משפיע על `a`.

</details>

---

### שאלה 2: Aliasing עם השמה חדשה

```python
a = [1, 2, 3]
b = a
b = [4, 5, 6]
print(a)
```

<details>
<summary>תשובה</summary>

```
[1, 2, 3]
```

**הסבר:** `b = [4, 5, 6]` יוצר רשימה **חדשה** ומצביע `b` אליה. `a` עדיין מצביע לרשימה המקורית.

</details>

---

### שאלה 3: Slicing יוצר עותק

```python
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)
print(b)
```

<details>
<summary>תשובה</summary>

```
[1, 2, 3]
[1, 2, 3, 4]
```

**הסבר:** `a[:]` יוצר **shallow copy** - רשימה חדשה. שינויים ב-`b` לא משפיעים על `a`.

</details>

---

### שאלה 4: Shallow Copy עם רשימות מקוננות

```python
a = [[1, 2], [3, 4]]
b = a[:]
b[0][0] = 999
print(a)
```

<details>
<summary>תשובה</summary>

```
[[999, 2], [3, 4]]
```

**הסבר:** `a[:]` הוא shallow copy - הרשימה החיצונית חדשה, אבל הרשימות הפנימיות **משותפות**.

</details>

---

### שאלה 5: Deep Copy

```python
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 999
print(a)
```

<details>
<summary>תשובה</summary>

```
[[1, 2], [3, 4]]
```

**הסבר:** `deepcopy` מעתיק **הכל** - גם הרשימות הפנימיות. `a` לא מושפע.

</details>

---

### שאלה 6: פונקציה עם Mutable

```python
def f(lst):
    lst.append(4)
    return lst

a = [1, 2, 3]
b = f(a)
print(a)
print(a is b)
```

<details>
<summary>תשובה</summary>

```
[1, 2, 3, 4]
True
```

**הסבר:** הפונקציה מקבלת **reference** לרשימה, לא עותק. `lst` ו-`a` מצביעים לאותו אובייקט.

</details>

---

### שאלה 7: פונקציה עם Immutable

```python
def f(n):
    n = n + 1
    return n

x = 5
y = f(x)
print(x)
print(y)
```

<details>
<summary>תשובה</summary>

```
5
6
```

**הסבר:** `int` הוא immutable. `n = n + 1` יוצר אובייקט **חדש**. `x` לא משתנה.

</details>

---

### שאלה 8: Default Mutable Argument

```python
def f(item, lst=[]):
    lst.append(item)
    return lst

print(f(1))
print(f(2))
print(f(3))
```

<details>
<summary>תשובה</summary>

```
[1]
[1, 2]
[1, 2, 3]
```

**הסבר:** הרשימה `[]` נוצרת **פעם אחת** כשהפונקציה מוגדרת, ומשותפת לכל הקריאות!

</details>

---

### שאלה 9: יצירת מטריצה שגויה

```python
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)
```

<details>
<summary>תשובה</summary>

```
[[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```

**הסבר:** `[[0] * 3] * 3` יוצר **שלוש הפניות לאותה רשימה**. שינוי אחד משפיע על כולן.

**תיקון:** `[[0] * 3 for _ in range(3)]`

</details>

---

### שאלה 10: == מול is

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a == c)
print(a is c)
```

<details>
<summary>תשובה</summary>

```
True
False
True
True
```

**הסבר:**
- `==` בודק **שוויון ערכים**
- `is` בודק **זהות** (אותו אובייקט בזיכרון)

</details>

---

### שאלה 11: Tuple עם רשימה בפנים

```python
t = ([1, 2], [3, 4])
t[0].append(5)
print(t)
```

<details>
<summary>תשובה</summary>

```
([1, 2, 5], [3, 4])
```

**הסבר:** `tuple` הוא immutable - לא ניתן לשנות **את ה-tuple עצמו**. אבל הרשימות בפנים הן mutable ואפשר לשנות אותן.

</details>

---

### שאלה 12: מחרוזות הן Immutable

```python
s = "hello"
s.upper()
print(s)
```

<details>
<summary>תשובה</summary>

```
hello
```

**הסבר:** מחרוזות הן immutable. `s.upper()` מחזיר מחרוזת **חדשה**, לא משנה את `s`.

**תיקון:** `s = s.upper()`

</details>

---

### שאלה 13: sort() מול sorted()

```python
a = [3, 1, 2]
b = a.sort()
print(a)
print(b)
```

<details>
<summary>תשובה</summary>

```
[1, 2, 3]
None
```

**הסבר:**
- `a.sort()` ממיין **in-place** ומחזיר `None`
- `sorted(a)` מחזיר רשימה **חדשה** ממוינת

</details>

---

### שאלה 14: רשימה בתוך עצמה

```python
a = [1, 2]
a.append(a)
print(len(a))
print(a[2][2][0])
```

<details>
<summary>תשובה</summary>

```
3
1
```

**הסבר:** `a` מכיל את עצמו! `a[2]` הוא `a`, אז `a[2][2]` גם `a`, ו-`a[2][2][0]` הוא `1`.

</details>

---

## שאלות עם Trace

### שאלה 15: Trace של רקורסיה

צייר את עץ הקריאות של:
```python
def f(n):
    if n <= 0:
        return 0
    return n + f(n - 1)

f(3)
```

<details>
<summary>תשובה</summary>

```
f(3)
├── return 3 + f(2)
│   ├── return 2 + f(1)
│   │   ├── return 1 + f(0)
│   │   │   └── return 0
│   │   └── return 1 + 0 = 1
│   └── return 2 + 1 = 3
└── return 3 + 3 = 6
```

**תוצאה:** `6`

</details>

---

### שאלה 16: Stack Frames

מה מצב ה-stack כש-`g` מתבצעת?

```python
def f(x):
    y = x + 1
    return g(y)

def g(a):
    b = a * 2
    return b  # <-- כאן

f(5)
```

<details>
<summary>תשובה</summary>

```
┌─────────────────┐
│ g(a=6)          │
│   b = 12        │
├─────────────────┤
│ f(x=5)          │
│   y = 6         │
├─────────────────┤
│ <module>        │
└─────────────────┘
```

</details>

---

## שאלות "מה השגיאה?"

### שאלה 17: מצא את הבאג

```python
def remove_negatives(lst):
    for x in lst:
        if x < 0:
            lst.remove(x)
    return lst

print(remove_negatives([-1, -2, -3, -4]))
```

<details>
<summary>תשובה</summary>

**פלט:** `[-2, -4]` (לא רשימה ריקה!)

**הבעיה:** שינוי רשימה תוך כדי איטרציה עליה.

**תיקון:**
```python
def remove_negatives(lst):
    return [x for x in lst if x >= 0]
```

</details>

---

### שאלה 18: מצא את הבאג

```python
def make_uppercase(s):
    s.upper()
    return s

print(make_uppercase("hello"))
```

<details>
<summary>תשובה</summary>

**פלט:** `hello`

**הבעיה:** מחרוזות הן immutable. `s.upper()` לא משנה את `s`.

**תיקון:**
```python
def make_uppercase(s):
    return s.upper()
```

</details>

---

## שאלות תיאורטיות

### שאלה 19: נכון/לא נכון

1. `list` הוא טיפוס mutable
2. `tuple` הוא טיפוס mutable
3. `a = b` יוצר עותק של `b`
4. `a[:]` יוצר deep copy
5. `copy.deepcopy()` מעתיק גם אובייקטים מקוננים

<details>
<summary>תשובה</summary>

1. **נכון** - אפשר לשנות רשימות
2. **לא נכון** - tuple הוא immutable
3. **לא נכון** - יוצר alias (הפניה לאותו אובייקט)
4. **לא נכון** - יוצר shallow copy
5. **נכון** - deepcopy מעתיק הכל

</details>

---

### שאלה 20: השלם את הטבלה

| פעולה | מה היא עושה? |
|-------|-------------|
| `b = a` | ? |
| `b = a[:]` | ? |
| `b = copy.deepcopy(a)` | ? |

<details>
<summary>תשובה</summary>

| פעולה | מה היא עושה? |
|-------|-------------|
| `b = a` | Alias - שתי הפניות לאותו אובייקט |
| `b = a[:]` | Shallow copy - אובייקט חדש, תוכן משותף |
| `b = copy.deepcopy(a)` | Deep copy - הכל מועתק |

</details>

---

## קישורים

- [סיכום זיכרון](../notes/memory.md)
- [קוד דוגמה](../code/memory_demo.py)
- [מחברת אינטראקטיבית](../notebooks/memory.ipynb)
