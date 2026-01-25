"""
מילונים וקבוצות - דוגמאות והדגמות
מבוא למדעי המחשב
"""


# ========================================
# מילונים (Dictionaries)
# ========================================

def demo_dict_basics():
    """יסודות מילונים"""
    print("--- מילונים - יסודות ---")

    # יצירה
    grades = {"alice": 90, "bob": 85, "charlie": 92}
    print(f"grades = {grades}")

    # גישה
    print(f"\ngrades['alice'] = {grades['alice']}")
    print(f"grades.get('david', 0) = {grades.get('david', 0)}")

    # הוספה ועדכון
    grades["david"] = 88
    grades["alice"] = 95
    print(f"אחרי הוספה ועדכון: {grades}")

    # מחיקה
    del grades["bob"]
    print(f"אחרי מחיקת bob: {grades}")

    # איטרציה
    print("\nאיטרציה:")
    print(f"  keys: {list(grades.keys())}")
    print(f"  values: {list(grades.values())}")
    print(f"  items: {list(grades.items())}")


def demo_dict_methods():
    """מתודות מילון"""
    print("\n--- מתודות מילון ---")

    d = {"a": 1, "b": 2}
    print(f"d = {d}")

    # get עם ברירת מחדל
    print(f"d.get('c', 0) = {d.get('c', 0)}")

    # setdefault
    d.setdefault("c", 3)
    print(f"d.setdefault('c', 3) → d = {d}")

    # update
    d.update({"d": 4, "e": 5})
    print(f"d.update(...) → d = {d}")

    # pop
    val = d.pop("e")
    print(f"d.pop('e') = {val}, d = {d}")

    # ספירת תדירויות
    print("\n--- ספירת תדירויות ---")
    text = "hello world"
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    print(f"תדירויות ב-'{text}': {freq}")


def demo_dict_comprehension():
    """Dictionary Comprehension"""
    print("\n--- Dictionary Comprehension ---")

    # ריבועים
    squares = {x: x**2 for x in range(6)}
    print(f"{{x: x**2 for x in range(6)}} = {squares}")

    # סינון
    even_squares = {x: x**2 for x in range(6) if x % 2 == 0}
    print(f"רק זוגיים: {even_squares}")

    # היפוך מילון
    original = {"a": 1, "b": 2, "c": 3}
    inverted = {v: k for k, v in original.items()}
    print(f"היפוך {original} = {inverted}")


# ========================================
# קבוצות (Sets)
# ========================================

def demo_set_basics():
    """יסודות קבוצות"""
    print("\n--- קבוצות - יסודות ---")

    # יצירה
    s1 = {1, 2, 3, 4, 5}
    s2 = set([3, 4, 5, 6, 7])
    empty = set()  # לא {} - זה מילון ריק!

    print(f"s1 = {s1}")
    print(f"s2 = {s2}")

    # הוספה ומחיקה
    s1.add(6)
    s1.discard(1)  # לא זורק שגיאה אם לא קיים
    print(f"אחרי add(6), discard(1): {s1}")

    # בדיקת שייכות - O(1)!
    print(f"3 in s1: {3 in s1}")
    print(f"10 in s1: {10 in s1}")


def demo_set_operations():
    """פעולות קבוצות"""
    print("\n--- פעולות קבוצות ---")

    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(f"a = {a}")
    print(f"b = {b}")

    print(f"\nאיחוד (union):")
    print(f"  a | b = {a | b}")
    print(f"  a.union(b) = {a.union(b)}")

    print(f"\nחיתוך (intersection):")
    print(f"  a & b = {a & b}")
    print(f"  a.intersection(b) = {a.intersection(b)}")

    print(f"\nהפרש (difference):")
    print(f"  a - b = {a - b}")
    print(f"  b - a = {b - a}")

    print(f"\nהפרש סימטרי (symmetric difference):")
    print(f"  a ^ b = {a ^ b}")

    print(f"\nהכלה:")
    print(f"  {{1, 2}} <= {{1, 2, 3}}: {({1, 2} <= {1, 2, 3})}")
    print(f"  {{1, 2}}.issubset({{1, 2, 3}}): {({1, 2}.issubset({1, 2, 3}))}")


def demo_set_use_cases():
    """שימושים נפוצים בקבוצות"""
    print("\n--- שימושים נפוצים ---")

    # הסרת כפילויות
    lst = [1, 2, 2, 3, 3, 3, 4]
    unique = list(set(lst))
    print(f"הסרת כפילויות: {lst} → {unique}")

    # בדיקת כפילויות
    def has_duplicates(lst):
        return len(lst) != len(set(lst))

    print(f"has_duplicates([1,2,3]): {has_duplicates([1,2,3])}")
    print(f"has_duplicates([1,2,2]): {has_duplicates([1,2,2])}")

    # מציאת משותף
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    common = set(list1) & set(list2)
    print(f"איברים משותפים: {common}")


# ========================================
# frozenset
# ========================================

def demo_frozenset():
    """Frozenset - קבוצה בלתי משתנה"""
    print("\n--- frozenset ---")

    fs = frozenset([1, 2, 3])
    print(f"frozenset([1,2,3]) = {fs}")

    # יכול לשמש כמפתח במילון
    d = {fs: "קבוצה קפואה"}
    print(f"מילון עם frozenset כמפתח: {d}")


def main():
    print("=" * 60)
    print("מילונים וקבוצות")
    print("=" * 60)

    demo_dict_basics()
    demo_dict_methods()
    demo_dict_comprehension()
    demo_set_basics()
    demo_set_operations()
    demo_set_use_cases()
    demo_frozenset()

    print("\n" + "=" * 60)
    print("סיבוכיויות")
    print("=" * 60)
    print("""
    מילון (dict):           קבוצה (set):
    ─────────────────       ─────────────
    d[key]      O(1)*       x in s    O(1)*
    d[key] = v  O(1)*       s.add(x)  O(1)*
    del d[key]  O(1)*       s.remove  O(1)*
    key in d    O(1)*       s | t     O(len(s)+len(t))
    len(d)      O(1)        s & t     O(min(len(s),len(t)))

    * ממוצע, גרוע O(n)

    קבוצה טובה ל:
    - בדיקת שייכות מהירה
    - הסרת כפילויות
    - פעולות מתמטיות (איחוד, חיתוך)
    """)


if __name__ == "__main__":
    main()
