"""
יסודות פייתון - משתנים, תנאים, לולאות
מבוא למדעי המחשב
"""


# ========================================
# משתנים וטיפוסים
# ========================================

def demo_variables():
    """משתנים וטיפוסים בסיסיים"""
    print("--- משתנים וטיפוסים ---")

    # מספרים שלמים
    x = 42
    print(f"int: x = {x}, type = {type(x).__name__}")

    # מספרים עשרוניים
    pi = 3.14159
    print(f"float: pi = {pi}, type = {type(pi).__name__}")

    # בוליאני
    is_valid = True
    print(f"bool: is_valid = {is_valid}, type = {type(is_valid).__name__}")

    # מחרוזת
    name = "Python"
    print(f"str: name = {name!r}, type = {type(name).__name__}")

    # None
    result = None
    print(f"NoneType: result = {result}, type = {type(result).__name__}")


# ========================================
# אופרטורים
# ========================================

def demo_operators():
    """אופרטורים"""
    print("\n--- אופרטורים ---")

    # אריתמטיים
    print("אריתמטיים:")
    print(f"  5 + 3 = {5 + 3}")
    print(f"  5 - 3 = {5 - 3}")
    print(f"  5 * 3 = {5 * 3}")
    print(f"  5 / 3 = {5 / 3}")      # חילוק עשרוני
    print(f"  5 // 3 = {5 // 3}")    # חילוק שלם
    print(f"  5 % 3 = {5 % 3}")      # שארית
    print(f"  5 ** 3 = {5 ** 3}")    # חזקה

    # השוואה
    print("\nהשוואה:")
    print(f"  5 == 5: {5 == 5}")
    print(f"  5 != 3: {5 != 3}")
    print(f"  5 > 3: {5 > 3}")
    print(f"  5 <= 5: {5 <= 5}")

    # לוגיים
    print("\nלוגיים:")
    print(f"  True and False: {True and False}")
    print(f"  True or False: {True or False}")
    print(f"  not True: {not True}")


# ========================================
# תנאים
# ========================================

def demo_conditionals():
    """משפטי תנאי"""
    print("\n--- תנאים ---")

    x = 10

    # if-else בסיסי
    if x > 0:
        print(f"  {x} הוא חיובי")
    else:
        print(f"  {x} אינו חיובי")

    # if-elif-else
    grade = 85
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    else:
        letter = "F"
    print(f"  ציון {grade} = {letter}")

    # ביטוי תנאי (ternary)
    result = "זוגי" if x % 2 == 0 else "אי-זוגי"
    print(f"  {x} הוא {result}")


# ========================================
# לולאות
# ========================================

def demo_loops():
    """לולאות"""
    print("\n--- לולאות ---")

    # for עם range
    print("for i in range(5):")
    for i in range(5):
        print(f"  i = {i}")

    # for על רשימה
    print("\nfor item in ['a', 'b', 'c']:")
    for item in ['a', 'b', 'c']:
        print(f"  item = {item}")

    # while
    print("\nwhile n > 0:")
    n = 3
    while n > 0:
        print(f"  n = {n}")
        n -= 1

    # break ו-continue
    print("\nbreak ו-continue:")
    for i in range(10):
        if i == 3:
            continue  # דלג
        if i == 7:
            break     # עצור
        print(f"  {i}", end=" ")
    print()


# ========================================
# פונקציות
# ========================================

def demo_functions():
    """פונקציות"""
    print("\n--- פונקציות ---")

    # פונקציה בסיסית
    def greet(name):
        return f"שלום, {name}!"

    print(greet("עולם"))

    # ערכי ברירת מחדל
    def power(base, exp=2):
        return base ** exp

    print(f"power(3) = {power(3)}")
    print(f"power(3, 3) = {power(3, 3)}")

    # מספר ארגומנטים משתנה
    def sum_all(*args):
        return sum(args)

    print(f"sum_all(1, 2, 3, 4) = {sum_all(1, 2, 3, 4)}")

    # ארגומנטים עם שם
    def describe(name, age, city="תל אביב"):
        return f"{name}, {age}, מ{city}"

    print(describe("דני", 25))
    print(describe(age=30, name="רוני", city="ירושלים"))


# ========================================
# קלט ופלט
# ========================================

def demo_io():
    """קלט ופלט"""
    print("\n--- קלט ופלט ---")

    # print עם פרמטרים
    print("print עם פרמטרים:")
    print("a", "b", "c", sep="-")
    print("שורה 1", end=" | ")
    print("שורה 2")

    # f-strings
    name = "פייתון"
    version = 3.11
    print(f"\nf-string: {name} גרסה {version}")

    # עיצוב מספרים
    pi = 3.14159265
    print(f"עיצוב: {pi:.2f}")
    print(f"רוחב: {42:>10}")


# ========================================
# טיפול בשגיאות
# ========================================

def demo_errors():
    """טיפול בשגיאות"""
    print("\n--- טיפול בשגיאות ---")

    # try-except
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("  שגיאה: חילוק באפס")

    # מספר שגיאות
    try:
        x = int("abc")
    except ValueError:
        print("  שגיאה: לא ניתן להמיר למספר")

    # raise
    def check_positive(n):
        if n < 0:
            raise ValueError("המספר חייב להיות חיובי")
        return n

    try:
        check_positive(-5)
    except ValueError as e:
        print(f"  שגיאה: {e}")


def main():
    print("=" * 60)
    print("יסודות פייתון")
    print("=" * 60)

    demo_variables()
    demo_operators()
    demo_conditionals()
    demo_loops()
    demo_functions()
    demo_io()
    demo_errors()

    print("\n" + "=" * 60)
    print("טיפוסי נתונים מובנים")
    print("=" * 60)
    print("""
    | טיפוס  | דוגמה          | Mutable | Ordered |
    |--------|----------------|---------|---------|
    | int    | 42             | -       | -       |
    | float  | 3.14           | -       | -       |
    | bool   | True           | -       | -       |
    | str    | "hello"        | No      | Yes     |
    | list   | [1, 2, 3]      | Yes     | Yes     |
    | tuple  | (1, 2, 3)      | No      | Yes     |
    | dict   | {"a": 1}       | Yes     | Yes*    |
    | set    | {1, 2, 3}      | Yes     | No      |

    * dict שומר סדר הכנסה מ-Python 3.7
    """)


if __name__ == "__main__":
    main()
