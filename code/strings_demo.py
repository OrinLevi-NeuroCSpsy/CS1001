"""
מחרוזות (Strings) בפייתון - הדגמות
מבוא למדעי המחשב
"""


def demo_creation():
    """יצירת מחרוזות"""
    print("=" * 60)
    print("יצירת מחרוזות")
    print("=" * 60)

    s1 = "Hello"
    s2 = 'World'
    s3 = """מחרוזת
רב-שורתית"""
    s4 = str(42)
    empty = ""

    print(f"גרשיים כפולים: {repr(s1)}")
    print(f"גרשיים בודדים: {repr(s2)}")
    print(f"רב-שורתית: {repr(s3)}")
    print(f"המרה ממספר: {repr(s4)}")
    print(f"ריקה: {repr(empty)}")


def demo_immutability():
    """מחרוזות הן Immutable"""
    print("\n" + "=" * 60)
    print("מחרוזות הן Immutable (בלתי משתנות)")
    print("=" * 60)

    s = "Hello"
    print(f"מחרוזת: {repr(s)}")
    print("-" * 40)

    print("\nניסיון לשנות תו:")
    print("s[0] = 'J'  # TypeError!")
    print()
    print("הדרך הנכונה - יצירת מחרוזת חדשה:")
    new_s = 'J' + s[1:]
    print(f"new_s = 'J' + s[1:] = {repr(new_s)}")


def demo_indexing_slicing():
    """אינדקס וחיתוך"""
    print("\n" + "=" * 60)
    print("אינדקס וחיתוך (Indexing & Slicing)")
    print("=" * 60)

    s = "Python"
    print(f"מחרוזת: {repr(s)}")
    print("-" * 40)

    # אינדקס
    print("\nאינדקס:")
    for i in range(len(s)):
        print(f"  s[{i}] = '{s[i]}'   s[{-len(s)+i}] = '{s[-len(s)+i]}'")

    # חיתוך
    print("\nחיתוך:")
    examples = [
        ("s[0:3]", s[0:3]),
        ("s[2:]", s[2:]),
        ("s[:4]", s[:4]),
        ("s[::2]", s[::2]),
        ("s[::-1]", s[::-1]),
    ]

    for expr, result in examples:
        print(f"  {expr:<10} = {repr(result)}")


def demo_operators():
    """אופרטורים"""
    print("\n" + "=" * 60)
    print("אופרטורים על מחרוזות")
    print("=" * 60)

    print("\nשרשור (+):")
    print(f"  'Hello' + ' ' + 'World' = {'Hello' + ' ' + 'World'!r}")

    print("\nכפל (*):")
    print(f"  'ab' * 3 = {'ab' * 3!r}")
    print(f"  '-' * 10 = {'-' * 10!r}")

    print("\nשייכות (in):")
    print(f"  'ell' in 'Hello' = {'ell' in 'Hello'}")
    print(f"  'xyz' in 'Hello' = {'xyz' in 'Hello'}")

    print("\nהשוואה:")
    print(f"  'apple' < 'banana' = {'apple' < 'banana'}")
    print(f"  'abc' == 'abc' = {'abc' == 'abc'}")


def demo_methods_check():
    """מתודות בדיקה"""
    print("\n" + "=" * 60)
    print("מתודות בדיקה (מחזירות True/False)")
    print("=" * 60)

    test_strings = ["Hello", "hello", "HELLO", "Hello123", "123", "   ", ""]

    print(f"{'מחרוזת':<12} {'isalpha':<8} {'isdigit':<8} {'isalnum':<8} {'isupper':<8} {'islower':<8}")
    print("-" * 60)

    for s in test_strings:
        display = repr(s) if s else "''"
        print(f"{display:<12} {str(s.isalpha()):<8} {str(s.isdigit()):<8} {str(s.isalnum()):<8} {str(s.isupper()):<8} {str(s.islower()):<8}")


def demo_methods_transform():
    """מתודות המרה"""
    print("\n" + "=" * 60)
    print("מתודות המרה (מחזירות מחרוזת חדשה)")
    print("=" * 60)

    s = "hello World"
    print(f"מחרוזת: {repr(s)}")
    print("-" * 40)

    methods = [
        ("upper()", s.upper()),
        ("lower()", s.lower()),
        ("capitalize()", s.capitalize()),
        ("title()", s.title()),
        ("swapcase()", s.swapcase()),
    ]

    for method, result in methods:
        print(f"s.{method:<15} = {repr(result)}")


def demo_find_replace():
    """חיפוש והחלפה"""
    print("\n" + "=" * 60)
    print("חיפוש והחלפה")
    print("=" * 60)

    s = "Hello World, Hello Python"
    print(f"מחרוזת: {repr(s)}")
    print("-" * 40)

    print("\nחיפוש:")
    print(f"  s.find('o')        = {s.find('o')}")
    print(f"  s.find('o', 5)     = {s.find('o', 5)}")
    print(f"  s.rfind('o')       = {s.rfind('o')}")
    print(f"  s.find('xyz')      = {s.find('xyz')}  # לא נמצא")
    print(f"  s.count('o')       = {s.count('o')}")
    print(f"  s.count('Hello')   = {s.count('Hello')}")

    print("\nהתחלה וסיום:")
    print(f"  s.startswith('Hello') = {s.startswith('Hello')}")
    print(f"  s.endswith('Python')  = {s.endswith('Python')}")

    print("\nהחלפה:")
    print(f"  s.replace('Hello', 'Hi') = {repr(s.replace('Hello', 'Hi'))}")
    print(f"  s.replace('o', '0')      = {repr(s.replace('o', '0'))}")


def demo_split_join():
    """פיצול ואיחוד"""
    print("\n" + "=" * 60)
    print("פיצול (split) ואיחוד (join)")
    print("=" * 60)

    # split
    print("split():")
    print("-" * 40)

    examples = [
        ("'a,b,c'.split(',')", "a,b,c".split(",")),
        ("'Hello World'.split()", "Hello World".split()),
        ("'a::b::c'.split('::')", "a::b::c".split("::")),
        ("'a  b  c'.split(' ')", "a  b  c".split(" ")),
        ("'a  b  c'.split()", "a  b  c".split()),
    ]

    for expr, result in examples:
        print(f"  {expr:<30} = {result}")

    # join
    print("\njoin():")
    print("-" * 40)

    lst = ['a', 'b', 'c']
    print(f"  רשימה: {lst}")
    print(f"  ','.join(lst)  = {repr(','.join(lst))}")
    print(f"  ' '.join(lst)  = {repr(' '.join(lst))}")
    print(f"  ''.join(lst)   = {repr(''.join(lst))}")
    print(f"  '->'.join(lst) = {repr('->'.join(lst))}")


def demo_strip():
    """ניקוי רווחים"""
    print("\n" + "=" * 60)
    print("ניקוי רווחים (strip)")
    print("=" * 60)

    s = "   Hello World   "
    print(f"מחרוזת: {repr(s)}")
    print("-" * 40)

    print(f"s.strip()  = {repr(s.strip())}")
    print(f"s.lstrip() = {repr(s.lstrip())}")
    print(f"s.rstrip() = {repr(s.rstrip())}")

    s2 = "***Hello***"
    print(f"\n{repr(s2)}.strip('*') = {repr(s2.strip('*'))}")


def demo_formatting():
    """עיצוב מחרוזות"""
    print("\n" + "=" * 60)
    print("עיצוב מחרוזות (Formatting)")
    print("=" * 60)

    name = "דני"
    age = 25
    pi = 3.14159

    print("f-strings (מומלץ):")
    print("-" * 40)
    print(f'  f"שמי {{name}}" = f"שמי {name}"')
    print(f'  f"גיל: {{age}}" = f"גיל: {age}"')
    print(f'  f"2+3={{2+3}}" = f"2+3={2+3}"')
    print(f'  f"Pi={{pi:.2f}}" = f"Pi={pi:.2f}"')

    print("\nformat():")
    print("-" * 40)
    print(f'  "שמי {{}}".format("דני") = {"שמי {}".format("דני")!r}')


def demo_common_mistakes():
    """טעויות נפוצות"""
    print("\n" + "=" * 60)
    print("טעויות נפוצות")
    print("=" * 60)

    # מתודות מחזירות ערך חדש
    print("מתודות לא משנות את המקור:")
    print("-" * 40)
    s = "Hello"
    s.upper()
    print(f"s = 'Hello'")
    print(f"s.upper()  # לא שמרנו את התוצאה!")
    print(f"print(s)   # {s!r} - לא השתנה!")
    print()
    s = s.upper()
    print(f"s = s.upper()  # נכון!")
    print(f"print(s)   # {s!r}")

    # find vs index
    print("\nfind() vs index():")
    print("-" * 40)
    s = "Hello"
    print(f"s.find('x')  = {s.find('x')}  # מחזיר -1")
    print(f"s.index('x') = ValueError!  # זורק שגיאה")


def demo_practical():
    """דוגמאות מעשיות"""
    print("\n" + "=" * 60)
    print("דוגמאות מעשיות")
    print("=" * 60)

    # היפוך מחרוזת
    print("היפוך מחרוזת:")
    s = "Hello"
    print(f"  {s!r}[::-1] = {s[::-1]!r}")

    # בדיקת פלינדרום
    print("\nבדיקת פלינדרום:")
    for word in ["אבא", "hello", "עברית"]:
        is_pal = word == word[::-1]
        print(f"  {word!r} == {word[::-1]!r} ? {is_pal}")

    # ספירת מילים
    print("\nספירת מילים:")
    text = "Hello World Hello Python"
    words = text.split()
    print(f"  טקסט: {text!r}")
    print(f"  מילים: {words}")
    print(f"  כמות: {len(words)}")

    # המרה לאותיות ראשונות גדולות
    print("\nהמרת רישיות למילים:")
    text = "hello world python"
    print(f"  {text!r}.title() = {text.title()!r}")


def main():
    demo_creation()
    demo_immutability()
    demo_indexing_slicing()
    demo_operators()
    demo_methods_check()
    demo_methods_transform()
    demo_find_replace()
    demo_split_join()
    demo_strip()
    demo_formatting()
    demo_common_mistakes()
    demo_practical()


if __name__ == "__main__":
    main()
