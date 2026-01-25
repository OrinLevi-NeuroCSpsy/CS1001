# Memoization - שיפור ביצועי רקורסיה

---

## הבעיה

### פיבונאצ'י נאיבי - O(2ⁿ)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

**למה זה איטי?** אותם ערכים מחושבים שוב ושוב!

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1)
│   │   │   └── fib(0)
│   │   └── fib(1)
│   └── fib(2)         ← מחושב שוב!
│       ├── fib(1)
│       └── fib(0)
└── fib(3)             ← מחושב שוב!
    ├── fib(2)         ← מחושב שוב!
    │   ├── fib(1)
    │   └── fib(0)
    └── fib(1)
```

**fib(2)** מחושב **3 פעמים**!
עבור fib(40), יש כ-**331 מיליון** קריאות.

---

## הפתרון: Memoization

### מה זה?
**שמירת תוצאות** של חישובים קודמים כדי לא לחשב אותם שוב.

### אינטואיציה
כמו "פתק" - אם כבר חישבת תשובה, רשום אותה. בפעם הבאה שצריך אותה, פשוט תקרא מהפתק.

---

## מימוש עם מילון

### פיבונאצ'י עם Memoization - O(n)

```python
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}

    # בדוק אם כבר חישבנו
    if n in memo:
        return memo[n]

    # מקרה בסיס
    if n <= 1:
        return n

    # חשב ושמור בזיכרון
    result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = result

    return result

# עכשיו אפילו fib_memo(100) מהיר!
fib_memo(100)  # 354224848179261915075
```

### מעקב

```
fib_memo(5):
  memo = {}

  fib_memo(5) → צריך fib_memo(4) + fib_memo(3)
    fib_memo(4) → צריך fib_memo(3) + fib_memo(2)
      fib_memo(3) → צריך fib_memo(2) + fib_memo(1)
        fib_memo(2) → צריך fib_memo(1) + fib_memo(0)
          fib_memo(1) = 1
          fib_memo(0) = 0
        fib_memo(2) = 1, memo[2] = 1
        fib_memo(1) = 1 (בסיס)
      fib_memo(3) = 2, memo[3] = 2
      fib_memo(2) = 1 ← נלקח מ-memo!
    fib_memo(4) = 3, memo[4] = 3
    fib_memo(3) = 2 ← נלקח מ-memo!
  fib_memo(5) = 5
```

---

## מימוש עם Decorator

### lru_cache מובנה (הכי קל!)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

fib(100)  # מהיר!
```

### מה זה עושה?
`@lru_cache` אוטומטית שומר תוצאות של קריאות קודמות.

---

## דוגמאות נוספות

### עצרת עם Memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### ספירת דרכים במדרגות

**בעיה:** כמה דרכים לעלות n מדרגות אם בכל פעם אפשר לעלות 1 או 2?

```python
# נאיבי - O(2ⁿ)
def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)

# עם memoization - O(n)
@lru_cache(maxsize=None)
def climb_stairs_memo(n):
    if n <= 2:
        return n
    return climb_stairs_memo(n - 1) + climb_stairs_memo(n - 2)
```

### מטבעות (Coin Change)

**בעיה:** כמה דרכים לתת עודף של n אגורות עם מטבעות [1, 5, 10]?

```python
@lru_cache(maxsize=None)
def coin_ways(amount, coins_tuple):
    coins = list(coins_tuple)

    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0

    # או שמשתמשים במטבע הראשון, או לא
    return (coin_ways(amount - coins[0], coins_tuple) +
            coin_ways(amount, tuple(coins[1:])))

coin_ways(10, (1, 5, 10))  # 4 דרכים
```

---

## השוואת ביצועים

| n | fib נאיבי | fib עם memo |
|---|-----------|-------------|
| 10 | 0.0001s | 0.0001s |
| 30 | 0.5s | 0.0001s |
| 40 | 55s | 0.0001s |
| 50 | ~1 שעה | 0.0001s |
| 100 | ∞ | 0.0001s |

---

## מתי להשתמש ב-Memoization?

### כן ✓

1. **חפיפה תת-בעיות (Overlapping Subproblems)**
   - אותה בעיה נפתרת כמה פעמים
   - דוגמה: פיבונאצ'י, מדרגות

2. **מבנה אופטימלי (Optimal Substructure)**
   - הפתרון מורכב מפתרונות של תת-בעיות
   - דוגמה: נתיב קצר ביותר

### לא ✗

1. **ללא חישובים חוזרים**
   ```python
   # אין צורך - כל n מחושב פעם אחת
   def factorial(n):
       if n <= 1:
           return 1
       return n * factorial(n - 1)
   ```

2. **הקלט לא hashable**
   - Memoization דורש שהפרמטרים יהיו מפתח למילון
   - רשימות לא עובדות (אבל tuples כן)

---

## Bottom-Up vs Top-Down

### Top-Down (Memoization)
מתחילים מלמעלה (n) ויורדים למטה (0).

```python
@lru_cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

### Bottom-Up (Tabulation)
מתחילים מלמטה (0) ועולים למעלה (n).

```python
def fib_bottom_up(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

### עוד יותר יעיל: O(1) זיכרון

```python
def fib_optimal(n):
    if n <= 1:
        return n

    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1
```

---

## טעויות נפוצות

### טעות 1: ערך ברירת מחדל משתנה

```python
# שגוי!
def fib(n, memo={}):  # מילון אחד לכל הקריאות!
    ...

# נכון
def fib(n, memo=None):
    if memo is None:
        memo = {}
    ...
```

### טעות 2: שכחה להעביר את memo

```python
# שגוי
def fib(n, memo=None):
    if memo is None:
        memo = {}
    ...
    return fib(n - 1) + fib(n - 2)  # שכחנו להעביר memo!

# נכון
def fib(n, memo=None):
    if memo is None:
        memo = {}
    ...
    return fib(n - 1, memo) + fib(n - 2, memo)
```

### טעות 3: רשימה כמפתח

```python
# שגוי - רשימות לא hashable
@lru_cache
def func(lst):  # TypeError!
    ...

# נכון - המר ל-tuple
@lru_cache
def func(tpl):
    ...

func(tuple([1, 2, 3]))
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: מהי הסיבוכיות?

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

**תשובה:** O(2ⁿ) - כל קריאה מתפצלת לשתיים.

---

### שאלה 2: מהי הסיבוכיות עם memo?

```python
@lru_cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

**תשובה:** O(n) - כל ערך מחושב פעם אחת.

---

### שאלה 3: הוסף Memoization

```python
def count_paths(m, n):
    """כמה דרכים להגיע מ-(0,0) ל-(m,n) בצעדים ימינה/למטה?"""
    if m == 0 or n == 0:
        return 1
    return count_paths(m - 1, n) + count_paths(m, n - 1)
```

**פתרון:**
```python
@lru_cache(maxsize=None)
def count_paths(m, n):
    if m == 0 or n == 0:
        return 1
    return count_paths(m - 1, n) + count_paths(m, n - 1)
```

---

### שאלה 4: למה נדרש memo?

```python
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)
```

**תשובה:** לא נדרש! אין חפיפה - כל n מחושב פעם אחת.

---

## סיכום נקודות חשובות

- [ ] **Memoization** = שמירת תוצאות חישוב לשימוש חוזר
- [ ] הופך O(2ⁿ) ל-O(n) בבעיות עם חפיפה
- [ ] `@lru_cache` - הדרך הקלה ביותר בפייתון
- [ ] משתמשים כש: **אותה בעיה נפתרת כמה פעמים**
- [ ] **Top-Down** = רקורסיה + memo
- [ ] **Bottom-Up** = לולאה + מערך
- [ ] זהירות: ערך ברירת מחדל משתנה (`memo={}`)
- [ ] רשימות לא hashable - המר ל-tuple

---

## קישורים נוספים

- **קוד:** [memoization_demo.py](../code/memoization_demo.py)
