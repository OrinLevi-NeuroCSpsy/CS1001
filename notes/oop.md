# תכנות מונחה עצמים (OOP) - סיכום לבחינה

---

## מוטיבציה

### הבעיה
רוצים לייצג ישויות מורכבות עם:
- **נתונים** (מאפיינים/תכונות)
- **פעולות** (התנהגויות)

### דוגמה: ייצוג סטודנט

**בלי OOP:**
```python
# נתונים מפוזרים
student_name = "דני"
student_id = 123456
student_grades = [85, 90, 78]

def calculate_average(grades):
    return sum(grades) / len(grades)

avg = calculate_average(student_grades)
```

**עם OOP:**
```python
class Student:
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("דני", 123456, [85, 90, 78])
avg = student.average()
```

---

## מושגי יסוד

### מחלקה (Class)
**תבנית/שרטוט** ליצירת אובייקטים. מגדירה מה יהיו התכונות והמתודות.

### אובייקט (Object) / מופע (Instance)
**יצירה קונקרטית** לפי התבנית. לכל אובייקט יש ערכים משלו.

### אנלוגיה
- **מחלקה** = תבנית לעוגיות
- **אובייקט** = עוגייה ספציפית

```python
class Cookie:           # המחלקה (תבנית)
    pass

cookie1 = Cookie()      # אובייקט 1
cookie2 = Cookie()      # אובייקט 2 (שונה מ-cookie1)
```

---

## הגדרת מחלקה

### תחביר בסיסי

```python
class ClassName:
    """תיעוד המחלקה (אופציונלי)"""

    def __init__(self, param1, param2):
        """הבנאי - נקרא בעת יצירת אובייקט"""
        self.attribute1 = param1
        self.attribute2 = param2

    def method_name(self):
        """מתודה - פונקציה של המחלקה"""
        # קוד
        return something
```

### דוגמה מלאה: מחלקת Point

```python
class Point:
    """נקודה במישור דו-ממדי"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

# שימוש
p1 = Point(3, 4)
p2 = Point(0, 0)

print(p1.x)                    # 3
print(p1.distance_from_origin())  # 5.0
print(p1.distance_to(p2))      # 5.0
```

---

## הבנאי: `__init__`

### מהו?
מתודה מיוחדת שנקראת **אוטומטית** בעת יצירת אובייקט חדש.

### תפקיד
**אתחול** (initialization) של תכונות האובייקט.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width      # תכונה
        self.height = height    # תכונה

# כשכותבים:
r = Rectangle(5, 3)

# פייתון קורא מאחורי הקלעים:
# Rectangle.__init__(r, 5, 3)
```

### ערכי ברירת מחדל בבנאי

```python
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

r1 = Rectangle()        # width=1, height=1
r2 = Rectangle(5)       # width=5, height=1
r3 = Rectangle(5, 3)    # width=5, height=3
```

---

## self - הפניה לאובייקט עצמו

### מהו self?
פרמטר שמייצג את **האובייקט הספציפי** שעליו נקראת המתודה.

### למה צריך?
כדי לגשת לתכונות ומתודות של האובייקט מתוך המחלקה.

```python
class Counter:
    def __init__(self):
        self.count = 0      # self.count - תכונה של האובייקט

    def increment(self):
        self.count += 1     # גישה לתכונה דרך self

    def get_count(self):
        return self.count

c1 = Counter()
c2 = Counter()

c1.increment()
c1.increment()
c2.increment()

print(c1.get_count())  # 2
print(c2.get_count())  # 1 - כל אובייקט עם count משלו!
```

### חשוב!
- `self` **חייב** להיות הפרמטר הראשון בכל מתודה
- בקריאה למתודה, **לא** מעבירים את self - פייתון עושה זאת אוטומטית

```python
c1.increment()          # מה שכותבים
Counter.increment(c1)   # מה שקורה מאחורי הקלעים
```

---

## תכונות (Attributes)

### תכונות מופע (Instance Attributes)
שייכות **לאובייקט ספציפי**. כל אובייקט יכול לקבל ערכים שונים.

```python
class Dog:
    def __init__(self, name):
        self.name = name    # תכונת מופע

d1 = Dog("רקס")
d2 = Dog("בובי")
print(d1.name)  # רקס
print(d2.name)  # בובי
```

### תכונות מחלקה (Class Attributes)
שייכות **למחלקה עצמה**. משותפות לכל האובייקטים.

```python
class Dog:
    species = "Canis familiaris"  # תכונת מחלקה

    def __init__(self, name):
        self.name = name          # תכונת מופע

d1 = Dog("רקס")
d2 = Dog("בובי")

print(d1.species)  # Canis familiaris
print(d2.species)  # Canis familiaris
print(Dog.species) # Canis familiaris - גישה דרך המחלקה
```

### ספירת אובייקטים עם תכונת מחלקה

```python
class Student:
    count = 0  # תכונת מחלקה - סופרת כמה סטודנטים נוצרו

    def __init__(self, name):
        self.name = name
        Student.count += 1  # עדכון תכונת המחלקה

s1 = Student("דני")
s2 = Student("רוני")
print(Student.count)  # 2
```

---

## מתודות (Methods)

### מתודות מופע (Instance Methods)
פועלות על **אובייקט ספציפי**. מקבלות `self`.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):      # מתודת מופע
        self.balance += amount

    def withdraw(self, amount):     # מתודת מופע
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
```

### מתודות מיוחדות (Magic/Dunder Methods)

מתודות עם `__שם__` שפייתון קורא להן אוטומטית במצבים מסוימים.

#### `__str__` - ייצוג למשתמש
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(p)        # (3, 4) - קורא ל-__str__
str(p)          # "(3, 4)"
```

#### `__repr__` - ייצוג "רשמי"
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
repr(p)         # "Point(3, 4)"
```

#### `__eq__` - השוואה
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 2)

p1 == p2   # True (בזכות __eq__)
p1 == p3   # False
```

#### `__len__` - אורך
```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

pl = Playlist(["שיר1", "שיר2", "שיר3"])
len(pl)    # 3
```

### טבלת מתודות מיוחדות

| מתודה | נקראת כש... | דוגמה |
|-------|-------------|-------|
| `__init__` | יוצרים אובייקט | `obj = Class()` |
| `__str__` | `print()` או `str()` | `print(obj)` |
| `__repr__` | הצגה בקונסול | `repr(obj)` |
| `__eq__` | משווים עם `==` | `obj1 == obj2` |
| `__len__` | `len()` | `len(obj)` |
| `__add__` | חיבור עם `+` | `obj1 + obj2` |
| `__lt__` | השוואה עם `<` | `obj1 < obj2` |
| `__getitem__` | גישה עם `[]` | `obj[i]` |
| `__contains__` | בדיקה עם `in` | `x in obj` |

---

## דוגמה מלאה: מחלקת Fraction

```python
class Fraction:
    """מחלקה לייצוג שבר"""

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("מכנה לא יכול להיות 0")
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __eq__(self, other):
        # a/b == c/d if a*d == b*c
        return self.num * other.den == self.den * other.num

    def __add__(self, other):
        # a/b + c/d = (ad + bc) / bd
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def value(self):
        return self.num / self.den

# שימוש
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f1)           # 1/2
print(f1 + f2)      # 5/6
print(f1 * f2)      # 1/6
print(f1 == Fraction(2, 4))  # True
```

---

## הורשה (Inheritance)

### מהי הורשה?
מנגנון שמאפשר ליצור מחלקה חדשה **על בסיס** מחלקה קיימת.

### מונחים
- **מחלקת אב/בסיס (Parent/Base)** - המחלקה המקורית
- **מחלקת בן/נגזרת (Child/Derived)** - המחלקה שיורשת

### תחביר

```python
class Parent:
    # ...

class Child(Parent):  # Child יורש מ-Parent
    # ...
```

### דוגמה

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "קול כלשהו"

class Dog(Animal):
    def speak(self):        # דריסה (Override)
        return "הב הב!"

class Cat(Animal):
    def speak(self):        # דריסה
        return "מיאו!"

# שימוש
d = Dog("רקס")
c = Cat("מיצי")

print(d.name)       # רקס (ירש מ-Animal)
print(d.speak())    # הב הב!
print(c.speak())    # מיאו!
```

### super() - קריאה למחלקת האב

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # קריאה לבנאי של Animal
        self.breed = breed      # תכונה נוספת

d = Dog("רקס", "לברדור")
print(d.name)   # רקס
print(d.breed)  # לברדור
```

---

## isinstance ו-type

```python
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

# type - הטיפוס המדויק
type(d)             # <class 'Dog'>
type(d) == Dog      # True
type(d) == Animal   # False

# isinstance - בודק גם הורשה
isinstance(d, Dog)      # True
isinstance(d, Animal)   # True (כי Dog יורש מ-Animal)
isinstance(d, str)      # False
```

---

## טעויות נפוצות

### טעות 1: שכחת self

```python
class Counter:
    def __init__(self):
        count = 0       # שגוי! משתנה לוקאלי, לא תכונה

    # נכון:
    def __init__(self):
        self.count = 0  # תכונה של האובייקט
```

### טעות 2: שכחת self בקריאה למתודה

```python
class Example:
    def method1(self):
        method2()       # שגוי! צריך self.method2()

    def method2(self):
        pass

    # נכון:
    def method1(self):
        self.method2()
```

### טעות 3: שינוי תכונת מחלקה דרך מופע

```python
class Dog:
    count = 0

d = Dog()
d.count = 5         # יוצר תכונת מופע חדשה! לא משנה את תכונת המחלקה
print(Dog.count)    # עדיין 0

# נכון - גישה דרך שם המחלקה:
Dog.count = 5
```

### טעות 4: השוואת אובייקטים בלי `__eq__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(3, 4)
p2 = Point(3, 4)
p1 == p2    # False! (בלי __eq__ משווה זהות, לא ערכים)
```

### טעות 5: שכחת super().__init__

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        # שכחנו super().__init__(name)
        self.breed = breed

d = Dog("רקס", "לברדור")
print(d.name)   # AttributeError! אין תכונת name
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: מה יודפס?

```python
class A:
    x = 1
    def __init__(self):
        self.y = 2

a1 = A()
a2 = A()
a1.x = 10
A.x = 100

print(a1.x, a2.x, A.x)
```

**תשובה:** `10 100 100`

**הסבר:** `a1.x = 10` יצר תכונת מופע חדשה ל-a1. `A.x = 100` שינה את תכונת המחלקה. a2 עדיין ניגש לתכונת המחלקה.

---

### שאלה 2: השלם את המחלקה

```python
class Rectangle:
    def __init__(self, width, height):
        # השלם

    def area(self):
        # השלם

    def __str__(self):
        # השלם - יחזיר "Rectangle: 5x3"
```

**פתרון:**
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle: {self.width}x{self.height}"
```

---

### שאלה 3: מה השגיאה?

```python
class BankAccount:
    def __init__(self, balance):
        balance = balance

    def deposit(self, amount):
        self.balance += amount

acc = BankAccount(100)
acc.deposit(50)
```

**תשובה:** `AttributeError: 'BankAccount' object has no attribute 'balance'`

**הסבר:** בבנאי כתוב `balance = balance` במקום `self.balance = balance`

---

## סיכום נקודות חשובות

- [ ] **מחלקה** = תבנית, **אובייקט** = מופע ספציפי
- [ ] `__init__` = בנאי, נקרא אוטומטית ביצירת אובייקט
- [ ] `self` = הפניה לאובייקט עצמו, **חייב** בכל מתודה
- [ ] תכונת מופע: `self.x` | תכונת מחלקה: `Class.x`
- [ ] מתודות מיוחדות: `__str__`, `__eq__`, `__add__`, `__len__`
- [ ] הורשה: `class Child(Parent):`
- [ ] `super()` לקריאה למתודות האב
- [ ] `isinstance(obj, Class)` בודק גם הורשה

---

## קישורים נוספים

- **קוד:** [oop_demo.py](../code/oop_demo.py)
- **שאלות בחינה:** [data_structures.md](../exam_questions/data_structures.md)
