# טריקים ודפוסים לבחינה - CS1001

מבוסס על תרגילי הבית, תרגולים ומבחנים קודמים.

---

## 1. טריקים בסיבוכיות

### טריק: לולאה פנימית לא תמיד O(n)

```python
# נראה O(n²) אבל בעצם O(n)!
for i in range(n):
    for j in range(i):
        print(j)

# סה"כ: 0+1+2+...+(n-1) = n(n-1)/2 = O(n²)
# זה כן O(n²)!

# אבל זה שונה:
i = 0
for j in range(n):
    while i < n and some_condition:
        i += 1
# i עולה רק n פעמים בסה"כ → O(n)
```

### טריק: חיבור מול כפל

```python
# חיבור מחרוזות בלולאה - O(n²)!
s = ""
for i in range(n):
    s = s + str(i)  # כל פעם יוצרים מחרוזת חדשה

# פתרון - O(n):
parts = []
for i in range(n):
    parts.append(str(i))
s = "".join(parts)
```

### טריק: פעולות מובנות

| פעולה | רשימה | מילון | קבוצה |
|-------|-------|-------|-------|
| `x in` | O(n) | **O(1)** | **O(1)** |
| `append` | O(1)* | - | - |
| `insert(0,x)` | O(n) | - | - |
| `pop()` | O(1) | - | - |
| `pop(0)` | O(n) | - | - |

**בבחינה:** אם יש `in` על רשימה בתוך לולאה → O(n²)!

---

## 2. טריקים ברקורסיה

### טריק: זיהוי מקרה בסיס חסר

```python
# שאלה: מה לא בסדר?
def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)

# בעיה: f(-1) → רקורסיה אינסופית!
# תיקון:
def f(n):
    if n <= 0:  # ≤ במקום ==
        return 0
    return n + f(n - 1)
```

### טריק: שכחת return

```python
# שאלה: למה מחזיר None?
def sum_list(lst):
    if len(lst) == 0:
        return 0
    sum_list(lst[1:]) + lst[0]  # חסר return!

# תיקון:
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return sum_list(lst[1:]) + lst[0]
```

### טריק: פיבונאצ'י ומספר קריאות

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# שאלה: כמה קריאות ל-fib(5)?
# תשובה: 15 קריאות
# fib(5)=1, fib(4)=1, fib(3)=2, fib(2)=3, fib(1)=5, fib(0)=3
```

### טריק: מה קורה אחרי הקריאה הרקורסיבית?

```python
def mystery(n):
    if n <= 0:
        return
    print(n, "before")
    mystery(n - 1)
    print(n, "after")

mystery(3)
# 3 before
# 2 before
# 1 before
# 1 after  ← חוזרים בסדר הפוך!
# 2 after
# 3 after
```

---

## 3. טריקים בייצוג מספרים

### טריק: Two's Complement - המספר השלילי ביותר

```
ב-8 ביטים:
-128 = 10000000
127 = 01111111

שים לב: -(-128) = 128 לא קיים בטווח!
```

### טריק: בינארי לעשרוני מהר

```
1101 = 8+4+1 = 13
במקום: 1×2³ + 1×2² + 0×2¹ + 1×2⁰
פשוט סכום החזקות שיש בהן 1
```

### טריק: Floating Point

```python
# שאלה קלאסית:
0.1 + 0.2 == 0.3  # False!

# תשובה נכונה:
abs(0.1 + 0.2 - 0.3) < 1e-9  # True
# או:
import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

---

## 4. טריקים ב-OOP

### טריק: self שכוח

```python
class Counter:
    def __init__(self):
        count = 0  # שגיאה! משתנה לוקאלי

    def increment(self):
        self.count += 1  # AttributeError!

# תיקון:
class Counter:
    def __init__(self):
        self.count = 0  # נכון
```

### טריק: משתנה מחלקה vs משתנה מופע

```python
class Dog:
    legs = 4  # משתנה מחלקה - משותף לכולם!

    def __init__(self, name):
        self.name = name  # משתנה מופע

d1 = Dog("Rex")
d2 = Dog("Max")
Dog.legs = 3  # משנה לכל הכלבים!
```

### טריק: __repr__ vs __str__

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(p)        # (3, 4) - קורא ל-__str__
print([p])      # [Point(3, 4)] - קורא ל-__repr__
```

---

## 5. טריקים ברשימות מקושרות

### טריק: איבוד הראש

```python
# שגוי - איבדנו את הרשימה!
def add_first(self, val):
    self.head = Node(val)  # הראש הישן אבד!
    self.head.next = ???

# נכון:
def add_first(self, val):
    new_node = Node(val)
    new_node.next = self.head  # קודם מחברים
    self.head = new_node       # אז מעדכנים
```

### טריק: current vs current.next

```python
# למחוק את האיבר ה-i:
# צריך להגיע לאיבר ה-(i-1)!

current = self.head
for _ in range(i - 1):  # i-1, לא i!
    current = current.next
current.next = current.next.next  # דילוג
```

### טריק: רשימה ריקה

```python
# תמיד לבדוק!
def add_last(self, val):
    if self.head is None:  # רשימה ריקה
        self.head = Node(val)
        return
    # ... המשך הקוד
```

---

## 6. טריקים ב-Hash

### טריק: hash של רשימה

```python
# רשימות לא hashable!
d = {}
d[[1,2,3]] = "value"  # TypeError!

# פתרון: המר ל-tuple
d[(1,2,3)] = "value"  # עובד!
```

### טריק: התנגשויות

```python
# שאלה: מה קורה כש-hash("ab") == hash("ba")?
# תשובה: שניהם נכנסים לאותה "שרשרת" (chaining)

# זה למה dict מהיר ב-average case אבל לא worst case
# Average: O(1), Worst: O(n)
```

---

## 7. טריקים באיטרטורים וגנרטורים

### טריק: איטרטור חד-פעמי

```python
gen = (x**2 for x in range(5))
list(gen)  # [0, 1, 4, 9, 16]
list(gen)  # [] - נגמר!

# אותו דבר עם map, filter, zip
```

### טריק: yield vs return

```python
def gen():
    yield 1
    yield 2
    return 3  # לא מוחזר! רק StopIteration

list(gen())  # [1, 2] - בלי ה-3!
```

### טריק: generator function vs generator object

```python
def gen():
    yield 1

gen       # פונקציה
gen()     # generator object

# שגוי:
for x in gen:    # TypeError!
    print(x)

# נכון:
for x in gen():  # צריך לקרוא לפונקציה
    print(x)
```

---

## 8. טריקים בקריפטוגרפיה

### טריק: Diffie-Hellman - מה ציבורי ומה סודי?

```
ציבורי: p, g, A=g^a mod p, B=g^b mod p
סודי:   a, b, K=g^(ab) mod p

האקר רואה: p, g, A, B
האקר לא יכול לחשב: a, b, K
```

### טריק: משפט פרמה לחישוב מהיר

```python
# חשב 5^100 mod 7
# לפי פרמה: 5^6 ≡ 1 (mod 7)
# 100 = 6×16 + 4
# 5^100 = (5^6)^16 × 5^4 ≡ 1 × 5^4 (mod 7)
# 5^4 = 625 = 89×7 + 2
# תשובה: 2
```

### טריק: pow עם 3 פרמטרים

```python
# יעיל!
pow(base, exp, mod)

# לא יעיל!
(base ** exp) % mod  # overflow אפשרי
```

---

## 9. טריקים בדחיסה

### טריק: Huffman - מי נמזג קודם?

```
תמיד שני הצמתים עם התדירות הנמוכה ביותר!
אם יש שוויון - לא משנה מי קודם.
```

### טריק: Prefix-free

```python
# בדוק אם קוד הוא prefix של אחר:
codes = ["0", "10", "110", "111"]
# 0 הוא prefix של 01? לא, אין 01
# תקין!

codes = ["0", "01", "10"]
# 0 הוא prefix של 01!
# לא תקין!
```

### טריק: אנטרופיה vs אורך ממוצע

```
אנטרופיה = גבול תחתון תיאורטי
אורך ממוצע Huffman ≥ אנטרופיה
(אבל קרוב מאוד)
```

---

## 10. טריקים בהתאמת מחרוזות

### טריק: Rolling Hash - עדכון

```python
# מעבר מ-"ABC" ל-"BCD":
# new = (old - 'A'×base²) × base + 'D'

# חשוב: לטפל במספרים שליליים!
if new_hash < 0:
    new_hash += mod
```

### טריק: התנגשויות

```python
# hash זהה ≠ מחרוזות זהות!
if hash_match:
    if text[i:i+m] == pattern:  # חובה לבדוק!
        found.append(i)
```

---

## 11. טריקים בתיקון שגיאות

### טריק: מרחק Hamming לעומת קוד Hamming

```
מרחק Hamming = כמה ביטים שונים בין שתי מילים
קוד Hamming = שיטת קידוד לתיקון שגיאות
```

### טריק: ביטי בדיקה במיקומים

```
מיקומים 1, 2, 4, 8, 16, ... (חזקות של 2)
שאר המיקומים = ביטי מידע
```

### טריק: סינדרום = מיקום השגיאה

```
סינדרום = 0 → אין שגיאה
סינדרום = 5 → ביט 5 שגוי
```

---

## 12. טריקים בעיבוד תמונות

### טריק: גבולות התמונה

```python
# פילטר 3×3 לא יכול לפעול על הקצוות!
for i in range(1, height - 1):
    for j in range(1, width - 1):
        # ... apply filter
```

### טריק: חריגה מטווח

```python
# תמיד לוודא 0 ≤ pixel ≤ 255
new_pixel = max(0, min(255, calculated_value))
```

### טריק: RGB לאפור

```python
# לא ממוצע פשוט!
gray = int(0.299*R + 0.587*G + 0.114*B)
# (משקולות לפי רגישות העין)
```

---

## 13. שאלות "מה יודפס?"

### דפוס 1: Short-circuit

```python
x = 5
y = 0
if y != 0 and x/y > 2:
    print("A")
else:
    print("B")
# תשובה: B (לא קורסים!)
```

### דפוס 2: רשימות ו-aliasing

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
# תשובה: [1, 2, 3, 4] - אותה רשימה!
```

### דפוס 3: ערך ברירת מחדל משתנה

```python
def f(x, lst=[]):
    lst.append(x)
    return lst

print(f(1))  # [1]
print(f(2))  # [1, 2] - לא [2]!
```

### דפוס 4: רקורסיה עם הדפסות

```python
def f(n):
    if n == 0:
        return
    print(n)
    f(n-1)
    print(n)

f(2)
# 2, 1, 1, 2
```

---

## 14. שאלות "מה הסיבוכיות?"

### דפוס 1: לולאה כפולה מטעה

```python
for i in range(n):
    for j in range(5):  # קבוע!
        print(i, j)
# O(5n) = O(n), לא O(n²)
```

### דפוס 2: לולאה עם חצי

```python
i = n
while i > 1:
    i = i // 2
# O(log n)
```

### דפוס 3: שתי לולאות עוקבות

```python
for i in range(n):
    print(i)
for j in range(n):
    print(j)
# O(n) + O(n) = O(n), לא O(n²)
```

---

## 15. מקורות

- [אתר הקורס](http://tau-cs1001-py.wikidot.com/)
- [תרגולים ב-GitHub](https://github.com/yoavram/CS1001.py)
- [מבחנים קודמים](http://tau-cs1001-py.wikidot.com/exams)
