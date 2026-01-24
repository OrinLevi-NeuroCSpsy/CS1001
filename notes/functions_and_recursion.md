# פונקציות ורקורסיה - סיכום לבחינה

---

## חלק א': פונקציות

### 1. הגדרה פורמלית

**פונקציה** היא בלוק קוד בעל שם, שמבצע משימה מוגדרת, יכול לקבל קלט (פרמטרים) ולהחזיר פלט (ערך מוחזר).

```python
def function_name(parameter1, parameter2, ...):
    """תיעוד הפונקציה (אופציונלי)"""
    # גוף הפונקציה
    return value  # אופציונלי
```

### 2. הסבר אינטואיטיבי

פונקציה היא כמו "מכונה" שמקבלת חומרי גלם (קלט), מעבדת אותם, ומוציאה מוצר מוגמר (פלט).

**למה משתמשים בפונקציות?**
- **מודולריות** - חלוקת הקוד ליחידות לוגיות
- **שימוש חוזר** - כתיבה פעם אחת, שימוש מספר פעמים
- **קריאות** - קוד ברור ומאורגן
- **תחזוקה** - קל לתקן ולשנות

---

### 3. פרמטרים וארגומנטים

#### הגדרה פורמלית
- **פרמטר (Parameter)** - משתנה המוגדר בחתימת הפונקציה
- **ארגומנט (Argument)** - הערך שמועבר בפועל בקריאה לפונקציה

```python
def greet(name):      # name הוא פרמטר
    print(f"שלום {name}")

greet("דני")          # "דני" הוא ארגומנט
```

#### סוגי העברת ארגומנטים

**א. ארגומנטים פוזיציוניים (Positional)**
```python
def divide(a, b):
    return a / b

result = divide(10, 2)  # a=10, b=2, result=5.0
```

**ב. ארגומנטים עם שם (Keyword)**
```python
result = divide(b=2, a=10)  # סדר לא משנה
```

**ג. ערכי ברירת מחדל (Default Values)**
```python
def power(base, exponent=2):
    return base ** exponent

power(3)      # 9 (exponent=2 כברירת מחדל)
power(3, 3)   # 27
```

> **כלל חשוב:** פרמטרים עם ברירת מחדל חייבים לבוא **אחרי** פרמטרים ללא ברירת מחדל.

---

### 4. החזרת ערכים (return)

#### הגדרה פורמלית
פקודת `return` מסיימת את ביצוע הפונקציה ומחזירה ערך לקוד הקורא.

```python
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8
```

#### פונקציה ללא return
```python
def print_hello():
    print("Hello")
    # אין return - מחזירה None באופן אוטומטי

x = print_hello()  # מדפיס "Hello", x = None
```

#### החזרת מספר ערכים
```python
def min_max(lst):
    return min(lst), max(lst)  # מחזיר tuple

minimum, maximum = min_max([3, 1, 4, 1, 5])
# minimum = 1, maximum = 5
```

---

### 5. Scope - תחום הכרה של משתנים

#### משתנים מקומיים (Local)
```python
def func():
    x = 10  # משתנה מקומי - קיים רק בתוך הפונקציה
    print(x)

func()
print(x)  # Error! x לא קיים מחוץ לפונקציה
```

#### משתנים גלובליים (Global)
```python
y = 20  # משתנה גלובלי

def func():
    print(y)  # ניתן לקרוא משתנה גלובלי

func()  # מדפיס 20
```

#### שינוי משתנה גלובלי (נדיר - להימנע!)
```python
counter = 0

def increment():
    global counter  # הכרזה מפורשת
    counter += 1
```

---

### 6. טעויות נפוצות בפונקציות

#### טעות 1: בלבול בין print ל-return
```python
# שגוי - מדפיס אבל לא מחזיר
def add_wrong(a, b):
    print(a + b)

result = add_wrong(3, 5)  # result = None!

# נכון
def add_correct(a, b):
    return a + b

result = add_correct(3, 5)  # result = 8
```

#### טעות 2: שינוי רשימה בתוך פונקציה
```python
def add_element(lst):
    lst.append(4)  # משנה את הרשימה המקורית!

my_list = [1, 2, 3]
add_element(my_list)
print(my_list)  # [1, 2, 3, 4] - הרשימה השתנתה!
```

#### טעות 3: ערך ברירת מחדל משתנה (Mutable Default)
```python
# שגוי!
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - לא [2]!

# נכון
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

#### טעות 4: קוד אחרי return
```python
def func():
    return 5
    print("זה לא ירוץ לעולם")  # Dead code
```

---

## חלק ב': רקורסיה

### 1. הגדרה פורמלית

**רקורסיה** היא טכניקה בה פונקציה קוראת לעצמה, תוך הקטנת הבעיה בכל קריאה, עד הגעה למקרה בסיס (תנאי עצירה).

**שני מרכיבים הכרחיים:**
1. **מקרה בסיס (Base Case)** - תנאי עצירה שמחזיר ערך ללא קריאה רקורסיבית
2. **מקרה רקורסיבי (Recursive Case)** - קריאה לפונקציה עם קלט "קטן יותר"

### 2. הסבר אינטואיטיבי

רקורסיה היא כמו בבושקות רוסיות - כל בובה מכילה בובה קטנה יותר, עד לבובה הקטנה ביותר (מקרה הבסיס).

**או:** לפתור בעיה גדולה על ידי פתרון בעיה קטנה יותר מאותו סוג.

---

### 3. דוגמאות קוד קלאסיות

#### עצרת (Factorial)
```python
def factorial(n):
    # מקרה בסיס
    if n == 0 or n == 1:
        return 1
    # מקרה רקורסיבי
    return n * factorial(n - 1)

# מעקב: factorial(4)
# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * 1 = 24
```

#### פיבונאצ'י
```python
def fibonacci(n):
    # מקרה בסיס
    if n <= 1:
        return n
    # מקרה רקורסיבי
    return fibonacci(n - 1) + fibonacci(n - 2)

# fib(0)=0, fib(1)=1, fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5
```

#### סכום ספרות
```python
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

# digit_sum(123) = 3 + digit_sum(12) = 3 + 2 + digit_sum(1) = 3 + 2 + 1 = 6
```

#### סכום רשימה
```python
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])

# sum_list([1,2,3]) = 1 + sum_list([2,3]) = 1 + 2 + sum_list([3]) = 1 + 2 + 3 = 6
```

#### חזקה
```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# power(2, 3) = 2 * power(2, 2) = 2 * 2 * power(2, 1) = 2 * 2 * 2 * 1 = 8
```

#### בדיקת פלינדרום
```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# is_palindrome("abba") -> is_palindrome("bb") -> is_palindrome("") -> True
```

#### חיפוש בינארי רקורסיבי
```python
def binary_search(lst, target, low, high):
    if low > high:
        return -1  # לא נמצא

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, low, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, high)
```

---

### 4. תנאי עצירה - עקרונות

**תנאי עצירה תקין חייב:**
1. להיות **ניתן להשגה** - הרקורסיה חייבת להתכנס אליו
2. להחזיר ערך **ללא קריאה רקורסיבית**
3. לטפל ב**כל מקרי הקצה**

```python
# תבנית כללית
def recursive_func(input):
    # בדיקת תנאי עצירה קודם!
    if base_condition(input):
        return base_value

    # הקטנת הבעיה וקריאה רקורסיבית
    smaller_input = reduce(input)
    return combine(recursive_func(smaller_input))
```

---

### 5. שגיאות נפוצות ברקורסיה

#### שגיאה 1: חסר תנאי עצירה
```python
# שגוי - רקורסיה אינסופית!
def infinite(n):
    return infinite(n - 1)  # RecursionError: maximum recursion depth exceeded
```

#### שגיאה 2: תנאי עצירה לא מושג
```python
# שגוי - מספר שלילי לא יגיע ל-0
def bad_factorial(n):
    if n == 0:
        return 1
    return n * bad_factorial(n - 1)

bad_factorial(-5)  # רקורסיה אינסופית!

# נכון
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

#### שגיאה 3: שכחת return בקריאה הרקורסיבית
```python
# שגוי
def sum_wrong(n):
    if n == 0:
        return 0
    sum_wrong(n - 1) + n  # חסר return!

# נכון
def sum_correct(n):
    if n == 0:
        return 0
    return sum_correct(n - 1) + n
```

#### שגיאה 4: סדר שגוי - קריאה רקורסיבית לפני בדיקת תנאי עצירה
```python
# שגוי
def wrong_order(lst):
    return lst[0] + wrong_order(lst[1:])  # יקרוס ברשימה ריקה!
    if len(lst) == 0:
        return 0

# נכון - תנאי עצירה קודם
def correct_order(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + correct_order(lst[1:])
```

#### שגיאה 5: הקטנה לא נכונה של הבעיה
```python
# שגוי - הבעיה לא קטנה
def stuck(n):
    if n == 0:
        return 0
    return stuck(n)  # n לא משתנה!
```

---

### 6. מעקב (Trace) - כלי חיוני לבחינה

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# מעקב עבור factorial(4):
"""
factorial(4)
├── 4 * factorial(3)
│   ├── 3 * factorial(2)
│   │   ├── 2 * factorial(1)
│   │   │   └── return 1
│   │   └── return 2 * 1 = 2
│   └── return 3 * 2 = 6
└── return 4 * 6 = 24
"""
```

---

## חלק ג': דוגמאות בחינתיות

### שאלה 1: מה יודפס?
```python
def mystery(n):
    if n <= 0:
        return
    print(n)
    mystery(n - 2)
    print(n)

mystery(5)
```

**פתרון:**
```
5
3
1
1
3
5
```
**הסבר:** הפונקציה מדפיסה n, קוראת רקורסיבית, ואז מדפיסה n שוב (בחזרה מהרקורסיה).

---

### שאלה 2: מה מחזירה הפונקציה?
```python
def what(lst):
    if len(lst) == 0:
        return 0
    if lst[0] % 2 == 0:
        return 1 + what(lst[1:])
    return what(lst[1:])

print(what([1, 2, 3, 4, 5, 6]))
```

**פתרון:** `3`

**הסבר:** הפונקציה סופרת מספרים זוגיים ברשימה.

---

### שאלה 3: השלם את הפונקציה
```python
def count_occurrences(lst, target):
    """מחזירה כמה פעמים target מופיע ב-lst"""
    # השלם כאן
```

**פתרון:**
```python
def count_occurrences(lst, target):
    if len(lst) == 0:
        return 0
    count = 1 if lst[0] == target else 0
    return count + count_occurrences(lst[1:], target)
```

---

### שאלה 4: מצא את הבאג
```python
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))
```

**פתרון:** אין באג! הפונקציה תקינה ומחזירה `"olleh"`.

---

### שאלה 5: כתוב פונקציה רקורסיבית
**משימה:** כתוב פונקציה `flatten(lst)` שמקבלת רשימה מקוננת ומחזירה רשימה שטוחה.

```python
def flatten(lst):
    if len(lst) == 0:
        return []

    first = lst[0]
    rest = flatten(lst[1:])

    if isinstance(first, list):
        return flatten(first) + rest
    else:
        return [first] + rest

# דוגמה:
# flatten([1, [2, 3], [4, [5, 6]]]) -> [1, 2, 3, 4, 5, 6]
```

---

### שאלה 6: חשב סיבוכיות
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

**פתרון:** סיבוכיות זמן: **O(2^n)** (אקספוננציאלית - לא יעיל!)

**הסבר:** כל קריאה מתפצלת לשתי קריאות נוספות.

---

## סיכום נקודות חשובות לבחינה

### פונקציות:
- [ ] הבדל בין `print` ל-`return`
- [ ] פרמטרים עם ברירת מחדל - תמיד בסוף
- [ ] Scope - משתנים מקומיים לא קיימים מחוץ לפונקציה
- [ ] רשימות מועברות by reference - שינוי משפיע על המקור
- [ ] `return` מסיים את הפונקציה מיידית

### רקורסיה:
- [ ] **תמיד** תנאי עצירה ראשון
- [ ] הבעיה **חייבת** להקטן בכל קריאה
- [ ] **לא לשכוח** `return` בקריאה הרקורסיבית
- [ ] לדעת לעשות **מעקב (trace)** ידני
- [ ] להכיר את הדוגמאות הקלאסיות: עצרת, פיבונאצ'י, סכום ספרות
