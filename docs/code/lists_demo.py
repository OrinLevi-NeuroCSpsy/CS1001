"""
רשימות (Lists) בפייתון - הדגמות
מבוא למדעי המחשב
"""


def demo_creation():
    """יצירת רשימות"""
    print("=" * 60)
    print("יצירת רשימות")
    print("=" * 60)

    # דרכים שונות ליצירה
    empty = []
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    from_range = list(range(5))
    nested = [[1, 2], [3, 4]]

    print(f"רשימה ריקה: {empty}")
    print(f"מספרים: {numbers}")
    print(f"טיפוסים מעורבים: {mixed}")
    print(f"מ-range: {from_range}")
    print(f"מקוננת: {nested}")


def demo_indexing():
    """גישה לאיברים"""
    print("\n" + "=" * 60)
    print("גישה לאיברים (Indexing)")
    print("=" * 60)

    lst = ['a', 'b', 'c', 'd', 'e']
    print(f"רשימה: {lst}")
    print("-" * 40)

    # אינדקס חיובי
    print("\nאינדקס חיובי:")
    for i in range(len(lst)):
        print(f"  lst[{i}] = '{lst[i]}'")

    # אינדקס שלילי
    print("\nאינדקס שלילי:")
    for i in range(-1, -len(lst)-1, -1):
        print(f"  lst[{i}] = '{lst[i]}'")


def demo_slicing():
    """חיתוך (Slicing)"""
    print("\n" + "=" * 60)
    print("חיתוך (Slicing)")
    print("=" * 60)

    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"רשימה: {lst}")
    print("-" * 40)

    examples = [
        ("lst[2:5]", lst[2:5], "מ-2 עד 5 (לא כולל)"),
        ("lst[:4]", lst[:4], "מההתחלה עד 4"),
        ("lst[6:]", lst[6:], "מ-6 עד הסוף"),
        ("lst[:]", lst[:], "העתק של הכל"),
        ("lst[::2]", lst[::2], "כל איבר שני"),
        ("lst[1::2]", lst[1::2], "איברים במקום אי-זוגי"),
        ("lst[::-1]", lst[::-1], "הפוך"),
        ("lst[-3:]", lst[-3:], "3 אחרונים"),
    ]

    for expr, result, desc in examples:
        print(f"{expr:<15} = {str(result):<25} # {desc}")


def demo_methods():
    """מתודות של רשימות"""
    print("\n" + "=" * 60)
    print("מתודות של רשימות")
    print("=" * 60)

    # הוספת איברים
    print("\nהוספת איברים:")
    print("-" * 40)

    lst = [1, 2, 3]
    print(f"התחלה: {lst}")

    lst.append(4)
    print(f"append(4): {lst}")

    lst.insert(1, 10)
    print(f"insert(1, 10): {lst}")

    lst.extend([5, 6])
    print(f"extend([5, 6]): {lst}")

    # הסרת איברים
    print("\nהסרת איברים:")
    print("-" * 40)

    lst = [1, 2, 3, 2, 4, 5]
    print(f"התחלה: {lst}")

    lst.remove(2)
    print(f"remove(2): {lst}  # מסיר את ה-2 הראשון")

    x = lst.pop()
    print(f"pop(): החזיר {x}, רשימה: {lst}")

    x = lst.pop(0)
    print(f"pop(0): החזיר {x}, רשימה: {lst}")

    # חיפוש
    print("\nחיפוש:")
    print("-" * 40)

    lst = ['a', 'b', 'c', 'b', 'd']
    print(f"רשימה: {lst}")
    print(f"index('b'): {lst.index('b')}  # אינדקס ראשון")
    print(f"count('b'): {lst.count('b')}  # כמה פעמים")

    # מיון והיפוך
    print("\nמיון והיפוך:")
    print("-" * 40)

    lst = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"התחלה: {lst}")

    lst.sort()
    print(f"sort(): {lst}")

    lst.sort(reverse=True)
    print(f"sort(reverse=True): {lst}")

    lst.reverse()
    print(f"reverse(): {lst}")


def demo_common_mistakes():
    """טעויות נפוצות"""
    print("\n" + "=" * 60)
    print("טעויות נפוצות")
    print("=" * 60)

    # append vs extend
    print("\nappend vs extend:")
    print("-" * 40)

    lst1 = [1, 2]
    lst1.append([3, 4])
    print(f"append([3, 4]): {lst1}  # רשימה בתוך רשימה!")

    lst2 = [1, 2]
    lst2.extend([3, 4])
    print(f"extend([3, 4]): {lst2}  # איברים נפרדים")

    # sort מחזירה None
    print("\nsort() מחזירה None:")
    print("-" * 40)

    lst = [3, 1, 2]
    result = lst.sort()
    print(f"result = lst.sort()")
    print(f"result = {result}  # None!")
    print(f"lst = {lst}  # הרשימה השתנתה במקום")

    # Aliasing
    print("\nAliasing (שני שמות לאותה רשימה):")
    print("-" * 40)

    a = [1, 2, 3]
    b = a
    print(f"a = {a}")
    print(f"b = a  # b מצביע לאותה רשימה")

    b.append(4)
    print(f"b.append(4)")
    print(f"a = {a}  # גם a השתנתה!")
    print(f"b = {b}")

    print("\nהעתקה נכונה:")
    a = [1, 2, 3]
    b = a.copy()
    b.append(4)
    print(f"b = a.copy()")
    print(f"a = {a}  # a לא השתנתה")
    print(f"b = {b}")


def demo_list_comprehension():
    """List Comprehension"""
    print("\n" + "=" * 60)
    print("List Comprehension")
    print("=" * 60)

    # ריבועים
    squares = [x**2 for x in range(6)]
    print(f"[x**2 for x in range(6)] = {squares}")

    # עם תנאי
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"[x for x in range(10) if x % 2 == 0] = {evens}")

    # המרה
    words = ['hello', 'world']
    upper = [s.upper() for s in words]
    print(f"[s.upper() for s in {words}] = {upper}")

    # השוואה ללולאה רגילה
    print("\nהשוואה ללולאה רגילה:")
    print("-" * 40)
    print("# List Comprehension:")
    print("squares = [x**2 for x in range(6)]")
    print("\n# לולאה רגילה (שווה ערך):")
    print("squares = []")
    print("for x in range(6):")
    print("    squares.append(x**2)")


def demo_loops():
    """לולאות על רשימות"""
    print("\n" + "=" * 60)
    print("לולאות על רשימות")
    print("=" * 60)

    lst = ['a', 'b', 'c']
    print(f"רשימה: {lst}")

    print("\nfor item in lst:")
    for item in lst:
        print(f"  {item}")

    print("\nfor i in range(len(lst)):")
    for i in range(len(lst)):
        print(f"  i={i}, lst[i]='{lst[i]}'")

    print("\nfor i, item in enumerate(lst):")
    for i, item in enumerate(lst):
        print(f"  i={i}, item='{item}'")


def main():
    demo_creation()
    demo_indexing()
    demo_slicing()
    demo_methods()
    demo_common_mistakes()
    demo_list_comprehension()
    demo_loops()


if __name__ == "__main__":
    main()
