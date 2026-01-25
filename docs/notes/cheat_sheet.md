# Cheat Sheet - CS1001.py

דף סיכום מרוכז לבחינה.

---

## סיבוכיות

### סימונים
| סימון | משמעות |
|-------|--------|
| O(f) | חסם עליון (≤) |
| Ω(f) | חסם תחתון (≥) |
| Θ(f) | חסם הדוק (=) |

### סיבוכיויות נפוצות
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

### לולאות
```python
for i in range(n):        # O(n)
for i in range(n):
    for j in range(n):    # O(n²)
for i in range(n):
    for j in range(i):    # O(n²) - סכום 0+1+...+(n-1) = n(n-1)/2
while n > 0:
    n = n // 2            # O(log n)
```

### רקורסיה
```python
T(n) = T(n-1) + O(1)      → O(n)
T(n) = T(n-1) + O(n)      → O(n²)
T(n) = 2T(n-1) + O(1)     → O(2ⁿ)
T(n) = T(n/2) + O(1)      → O(log n)
T(n) = T(n/2) + O(n)      → O(n)
T(n) = 2T(n/2) + O(n)     → O(n log n)
```

---

## מבני נתונים

### רשימה (list)
| פעולה | סיבוכיות |
|-------|----------|
| `lst[i]` | O(1) |
| `lst.append(x)` | O(1) |
| `lst.pop()` | O(1) |
| `lst.pop(0)` | O(n) |
| `x in lst` | O(n) |
| `lst[i:j]` | O(j-i) |

### מילון (dict) / קבוצה (set)
| פעולה | ממוצע | גרוע |
|-------|-------|------|
| `d[key]` | O(1) | O(n) |
| `key in d` | O(1) | O(n) |
| `d[key] = val` | O(1) | O(n) |

### BST
| פעולה | ממוצע | גרוע |
|-------|-------|------|
| lookup | O(log n) | O(n) |
| insert | O(log n) | O(n) |
| min/max | O(log n) | O(n) |

### Hash Table
| פעולה | ממוצע | גרוע |
|-------|-------|------|
| lookup | O(1) | O(n) |
| insert | O(1) | O(n) |

---

## מיון

| אלגוריתם | ממוצע | גרוע | מקום | יציב |
|----------|-------|------|------|------|
| Bubble | O(n²) | O(n²) | O(1) | כן |
| Selection | O(n²) | O(n²) | O(1) | לא |
| Insertion | O(n²) | O(n²) | O(1) | כן |
| Merge | O(n log n) | O(n log n) | O(n) | כן |
| Quick | O(n log n) | O(n²) | O(log n) | לא |

---

## רקורסיה

### מבנה בסיסי
```python
def f(n):
    if n <= base:        # מקרה בסיס
        return value
    return ... f(n-1) ...  # קריאה רקורסיבית
```

### Memoization
```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

---

## פונקציות מסדר גבוה

```python
# Lambda
f = lambda x: x * 2

# Map - הפעלה על כל איבר
list(map(lambda x: x*2, [1,2,3]))  # [2,4,6]

# Filter - סינון
list(filter(lambda x: x>2, [1,2,3,4]))  # [3,4]

# Reduce - צמצום
from functools import reduce
reduce(lambda a,b: a+b, [1,2,3,4])  # 10

# Sorted עם key
sorted(lst, key=len)
sorted(lst, key=lambda x: x[1])
```

---

## גנרטורים

```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
next(g)  # 1
next(g)  # 2

# Generator expression
(x**2 for x in range(10))
```

---

## זיכרון

### Mutable vs Immutable
- **Immutable:** int, float, str, tuple, bool
- **Mutable:** list, dict, set

### Aliasing
```python
a = [1, 2, 3]
b = a          # alias - אותו אובייקט!
b.append(4)    # a גם משתנה
```

### Copy
```python
import copy
b = a[:]              # shallow copy
b = copy.deepcopy(a)  # deep copy
```

### טעות נפוצה
```python
# שגוי!
def f(lst=[]):  # רשימה משותפת!
    lst.append(1)
    return lst

# נכון
def f(lst=None):
    if lst is None:
        lst = []
```

---

## דחיסה

### האפמן
1. ספור תדירויות
2. בנה עץ (מזג שני קטנים)
3. צור קודים (0=שמאל, 1=ימין)

**תכונה:** Prefix-free - אין קוד שהוא תחילית של אחר

### Lempel-Ziv
- מחליף חזרות ב-`[offset, length]`
- כדאי לדחוס אם: `bits(ref) < bits(chars)`

---

## תיקון שגיאות

### מרחק המינג
- מספר הביטים השונים בין שתי מילים
- זיהוי k שגיאות: d ≥ k + 1
- תיקון k שגיאות: d ≥ 2k + 1

### קוד המינג
- ביטי בדיקה במיקומים: 1, 2, 4, 8, ...
- כל ביט בדיקה בודק מיקומים ספציפיים

---

## קריפטוגרפיה

### בדיקת ראשוניות
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### חזקה מודולרית
```python
def modpower(a, b, m):
    if b == 0:
        return 1
    if b % 2 == 0:
        t = modpower(a, b//2, m)
        return (t * t) % m
    return (a * modpower(a, b-1, m)) % m
```

### פרמה הקטנה
אם p ראשוני ו-gcd(a,p)=1: `a^(p-1) ≡ 1 (mod p)`

---

## ייצוג מספרים

### המרות
```python
bin(10)      # '0b1010'
int('1010', 2)  # 10
hex(255)     # '0xff'
int('ff', 16)   # 255
```

### Floating Point (IEEE 754)
- 32 ביט: 1 סימן + 8 מעריך + 23 מנטיסה
- ערך: (-1)^s × 1.M × 2^(E-127)

---

## חיפוש בינארי

```python
def binary_search(lst, x):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**סיבוכיות:** O(log n)

---

## התאמת מחרוזות

### Rabin-Karp
- Rolling hash: הסר תו ראשון, הוסף אחרון
- סיבוכיות: O(n+m) ממוצע, O(nm) גרוע

---

## OOP

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"Node({self.val})"

    def __eq__(self, other):
        return self.val == other.val
```

### מתודות מיוחדות
| מתודה | שימוש |
|-------|-------|
| `__init__` | בנאי |
| `__repr__` | ייצוג מחרוזת |
| `__str__` | print |
| `__eq__` | == |
| `__lt__` | < |
| `__len__` | len() |
| `__getitem__` | [] |

---

## טריקים

1. **חיתוך רשימה יוצר עותק** (shallow)
2. **`in` במילון/קבוצה = O(1)**
3. **`in` ברשימה = O(n)**
4. **Default argument נוצר פעם אחת**
5. **מחרוזות הן immutable**
6. **`sort()` מחזיר None**
7. **`sorted()` מחזיר רשימה חדשה**
8. **map/filter מחזירים iterator חד-פעמי**

---

*חלק מפרויקט [CS1001_sum](../README.md)*
