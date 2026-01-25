"""
איטרטורים וגנרטורים - דוגמאות והדגמות
מבוא למדעי המחשב
"""


# ========================================
# גנרטורים בסיסיים
# ========================================

def count_up(start, end):
    """גנרטור שסופר מ-start עד end"""
    current = start
    while current <= end:
        yield current
        current += 1


def fibonacci_gen(limit):
    """גנרטור פיבונאצ'י עד limit"""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def infinite_counter(start=0):
    """גנרטור אינסופי"""
    n = start
    while True:
        yield n
        n += 1


# ========================================
# גנרטורים מתקדמים
# ========================================

def pairs(lst):
    """גנרטור לכל הזוגות ברשימה"""
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            yield (lst[i], lst[j])


def flatten_gen(nested):
    """גנרטור לשיטוח רשימה מקוננת"""
    for item in nested:
        if isinstance(item, list):
            yield from flatten_gen(item)
        else:
            yield item


def permutations(lst):
    """גנרטור לכל הפרמוטציות"""
    if len(lst) <= 1:
        yield lst
        return

    for i in range(len(lst)):
        first = lst[i]
        rest = lst[:i] + lst[i+1:]
        for perm in permutations(rest):
            yield [first] + perm


def subsets(lst):
    """גנרטור לכל תתי-הקבוצות"""
    if not lst:
        yield []
        return

    first = lst[0]
    rest = lst[1:]

    for subset in subsets(rest):
        yield subset
        yield [first] + subset


# ========================================
# Generator Expressions
# ========================================

def demo_generator_expressions():
    """הדגמת generator expressions"""
    print("\n--- Generator Expressions ---")

    # השוואה בין list comprehension ל-generator expression
    print("\nList Comprehension vs Generator Expression:")
    print("squares_list = [x**2 for x in range(5)]  # רשימה בזיכרון")
    print("squares_gen = (x**2 for x in range(5))   # גנרטור עצלן")

    squares_list = [x**2 for x in range(5)]
    squares_gen = (x**2 for x in range(5))

    print(f"\nרשימה: {squares_list}")
    print(f"גנרטור: {squares_gen}")
    print(f"גנרטור לרשימה: {list(squares_gen)}")

    # שימוש עם sum, max, min
    print("\nשימוש עם פונקציות מובנות:")
    print(f"sum(x**2 for x in range(5)) = {sum(x**2 for x in range(5))}")
    print(f"max(x**2 for x in range(1, 5)) = {max(x**2 for x in range(1, 5))}")


# ========================================
# איטרטורים - מחלקות
# ========================================

class CountDown:
    """איטרטור לספירה לאחור"""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result


class Range:
    """מימוש פשוט של range"""

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step

    def __iter__(self):
        current = self.start
        while current < self.stop:
            yield current
            current += self.step


def main():
    print("=" * 60)
    print("איטרטורים וגנרטורים")
    print("=" * 60)

    # גנרטורים בסיסיים
    print("\n--- גנרטורים בסיסיים ---")

    print("\ncount_up(1, 5):")
    for n in count_up(1, 5):
        print(f"  {n}")

    print("\nfibonacci_gen(20):")
    print(f"  {list(fibonacci_gen(20))}")

    # גנרטורים מתקדמים
    print("\n--- גנרטורים מתקדמים ---")

    print("\npairs([1, 2, 3]):")
    print(f"  {list(pairs([1, 2, 3]))}")

    print("\nflatten_gen([1, [2, 3], [4, [5]]]):")
    print(f"  {list(flatten_gen([1, [2, 3], [4, [5]]]))}")

    print("\npermutations([1, 2, 3]):")
    for p in permutations([1, 2, 3]):
        print(f"  {p}")

    print("\nsubsets([1, 2]):")
    for s in subsets([1, 2]):
        print(f"  {s}")

    # Generator expressions
    demo_generator_expressions()

    # איטרטורים כמחלקות
    print("\n--- איטרטורים כמחלקות ---")

    print("\nCountDown(3):")
    for n in CountDown(3):
        print(f"  {n}")

    print("\nRange(1, 10, 2):")
    print(f"  {list(Range(1, 10, 2))}")

    # yield from
    print("\n--- yield from ---")
    print("""
    yield from iterable
    # שווה ערך ל:
    for item in iterable:
        yield item
    """)


if __name__ == "__main__":
    main()
