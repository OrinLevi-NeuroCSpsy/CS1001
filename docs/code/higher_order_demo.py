"""
פונקציות מסדר גבוה - map, filter, reduce, lambda
מבוא למדעי המחשב
"""

from functools import reduce


# ========================================
# פונקציות Lambda
# ========================================

def demo_lambda():
    """הדגמת פונקציות lambda"""
    print("--- Lambda Functions ---")

    # פונקציה רגילה
    def square(x):
        return x ** 2

    # פונקציית lambda שקולה
    square_lambda = lambda x: x ** 2

    print(f"square(5) = {square(5)}")
    print(f"square_lambda(5) = {square_lambda(5)}")

    # דוגמאות נוספות
    add = lambda a, b: a + b
    is_even = lambda x: x % 2 == 0
    first_char = lambda s: s[0] if s else ''

    print(f"\nadd(3, 4) = {add(3, 4)}")
    print(f"is_even(6) = {is_even(6)}")
    print(f"first_char('hello') = {first_char('hello')!r}")


# ========================================
# map
# ========================================

def demo_map():
    """הדגמת map"""
    print("\n--- map ---")

    numbers = [1, 2, 3, 4, 5]
    print(f"רשימה: {numbers}")

    # ריבוע
    squared = list(map(lambda x: x**2, numbers))
    print(f"map(lambda x: x**2, ...) = {squared}")

    # המרה לסטרינג
    strings = list(map(str, numbers))
    print(f"map(str, ...) = {strings}")

    # עם שתי רשימות
    a = [1, 2, 3]
    b = [10, 20, 30]
    sums = list(map(lambda x, y: x + y, a, b))
    print(f"\nmap עם שתי רשימות:")
    print(f"  a = {a}, b = {b}")
    print(f"  map(lambda x,y: x+y, a, b) = {sums}")


# ========================================
# filter
# ========================================

def demo_filter():
    """הדגמת filter"""
    print("\n--- filter ---")

    numbers = list(range(1, 11))
    print(f"רשימה: {numbers}")

    # מספרים זוגיים
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filter(lambda x: x%2==0, ...) = {evens}")

    # מספרים גדולים מ-5
    large = list(filter(lambda x: x > 5, numbers))
    print(f"filter(lambda x: x>5, ...) = {large}")

    # מחרוזות לא ריקות
    strings = ["hello", "", "world", "", "!"]
    non_empty = list(filter(None, strings))  # None = בדיקת truthiness
    print(f"\nstrings = {strings}")
    print(f"filter(None, strings) = {non_empty}")


# ========================================
# reduce
# ========================================

def demo_reduce():
    """הדגמת reduce"""
    print("\n--- reduce ---")

    numbers = [1, 2, 3, 4, 5]
    print(f"רשימה: {numbers}")

    # סכום
    total = reduce(lambda acc, x: acc + x, numbers)
    print(f"reduce(lambda acc,x: acc+x, ...) = {total}")

    # מכפלה
    product = reduce(lambda acc, x: acc * x, numbers)
    print(f"reduce(lambda acc,x: acc*x, ...) = {product}")

    # מקסימום
    maximum = reduce(lambda acc, x: acc if acc > x else x, numbers)
    print(f"reduce(max, ...) = {maximum}")

    # עם ערך התחלתי
    total_with_init = reduce(lambda acc, x: acc + x, numbers, 100)
    print(f"reduce(..., init=100) = {total_with_init}")

    # הסבר ויזואלי
    print("\nתהליך reduce לסכום:")
    print("  ((((1 + 2) + 3) + 4) + 5)")
    print("  = (((3 + 3) + 4) + 5)")
    print("  = ((6 + 4) + 5)")
    print("  = (10 + 5)")
    print("  = 15")


# ========================================
# שילובים
# ========================================

def demo_combinations():
    """שילוב map, filter, reduce"""
    print("\n--- שילובים ---")

    numbers = list(range(1, 11))
    print(f"רשימה: {numbers}")

    # סכום ריבועי הזוגיים
    result = reduce(
        lambda acc, x: acc + x,
        map(lambda x: x**2,
            filter(lambda x: x % 2 == 0, numbers))
    )
    print(f"סכום ריבועי הזוגיים: {result}")

    # שווה ערך עם list comprehension
    result2 = sum(x**2 for x in numbers if x % 2 == 0)
    print(f"עם comprehension: {result2}")


# ========================================
# פונקציות שמחזירות פונקציות
# ========================================

def demo_higher_order():
    """פונקציות שמחזירות פונקציות"""
    print("\n--- פונקציות שמחזירות פונקציות ---")

    def make_multiplier(n):
        """יוצר פונקציה שמכפילה ב-n"""
        return lambda x: x * n

    double = make_multiplier(2)
    triple = make_multiplier(3)

    print(f"double = make_multiplier(2)")
    print(f"double(5) = {double(5)}")
    print(f"triple(5) = {triple(5)}")

    def compose(f, g):
        """הרכבת פונקציות: (f ∘ g)(x) = f(g(x))"""
        return lambda x: f(g(x))

    add_one = lambda x: x + 1
    square = lambda x: x ** 2

    # (x + 1)^2
    f = compose(square, add_one)
    print(f"\ncompose(square, add_one)(5) = (5+1)² = {f(5)}")

    # x^2 + 1
    g = compose(add_one, square)
    print(f"compose(add_one, square)(5) = 5²+1 = {g(5)}")


def main():
    print("=" * 60)
    print("פונקציות מסדר גבוה")
    print("=" * 60)

    demo_lambda()
    demo_map()
    demo_filter()
    demo_reduce()
    demo_combinations()
    demo_higher_order()

    print("\n" + "=" * 60)
    print("סיכום")
    print("=" * 60)
    print("""
    lambda x: expr    - פונקציה אנונימית
    map(f, iter)      - החל f על כל איבר
    filter(pred, iter) - סנן לפי תנאי
    reduce(f, iter)   - צבור לערך יחיד

    שווה ערך ל-comprehension:
    map(f, lst)       ↔  [f(x) for x in lst]
    filter(p, lst)    ↔  [x for x in lst if p(x)]
    """)


if __name__ == "__main__":
    main()
