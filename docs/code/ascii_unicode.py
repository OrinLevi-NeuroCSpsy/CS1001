"""
ASCII ו-Unicode בפייתון
שימוש ב-ord() ו-chr()
מבוא למדעי המחשב
"""


def demo_ord_chr_basics():
    """הדגמת ord() ו-chr() - הבסיס"""

    print("=" * 60)
    print("ord() ו-chr() - המרה בין תווים למספרים")
    print("=" * 60)

    print("\nord(char) - מתו למספר:")
    print("-" * 40)

    examples = ['A', 'Z', 'a', 'z', '0', '9', ' ', '!']
    for char in examples:
        print(f"ord('{char}') = {ord(char)}")

    print("\nchr(num) - ממספר לתו:")
    print("-" * 40)

    numbers = [65, 90, 97, 122, 48, 57, 32, 33]
    for num in numbers:
        print(f"chr({num}) = '{chr(num)}'")


def demo_ascii_patterns():
    """הדגמת דפוסים חשובים ב-ASCII"""

    print("\n" + "=" * 60)
    print("דפוסים חשובים ב-ASCII")
    print("=" * 60)

    # הפרש בין אותיות גדולות לקטנות
    print("\nהפרש בין אות קטנה לגדולה:")
    print("-" * 40)
    print(f"ord('a') - ord('A') = {ord('a')} - {ord('A')} = {ord('a') - ord('A')}")

    # המרת רישיות
    print("\nהמרת רישיות:")
    print("-" * 40)

    upper = 'G'
    lower = chr(ord(upper) + 32)
    print(f"'{upper}' לאות קטנה: chr(ord('{upper}') + 32) = '{lower}'")

    lower = 'g'
    upper = chr(ord(lower) - 32)
    print(f"'{lower}' לאות גדולה: chr(ord('{lower}') - 32) = '{upper}'")

    # המרת ספרה-תו למספר
    print("\nהמרת ספרה-תו לערך מספרי:")
    print("-" * 40)

    for digit_char in '0123456789':
        value = ord(digit_char) - ord('0')
        print(f"ord('{digit_char}') - ord('0') = {ord(digit_char)} - 48 = {value}")


def demo_ascii_table():
    """הדגמת טבלת ASCII"""

    print("\n" + "=" * 60)
    print("טבלת ASCII - תווים מודפסים (32-126)")
    print("=" * 60)

    print("\nאותיות גדולות (65-90):")
    print("-" * 40)
    for i in range(65, 91):
        print(f"{chr(i)}", end=" ")
    print()

    print("\nאותיות קטנות (97-122):")
    print("-" * 40)
    for i in range(97, 123):
        print(f"{chr(i)}", end=" ")
    print()

    print("\nספרות (48-57):")
    print("-" * 40)
    for i in range(48, 58):
        print(f"{chr(i)}", end=" ")
    print()


def demo_hebrew():
    """הדגמת תווים עבריים - Unicode"""

    print("\n" + "=" * 60)
    print("עברית ב-Unicode")
    print("=" * 60)

    print("\nאותיות עבריות וערכי Unicode:")
    print("-" * 40)

    hebrew_letters = "אבגדהוזחטיכלמנסעפצקרשת"

    for letter in hebrew_letters:
        code = ord(letter)
        print(f"'{letter}' = U+{code:04X} = {code}")

    print("\nטווח האותיות העבריות:")
    print("-" * 40)
    print(f"א = {ord('א')} (U+05D0)")
    print(f"ת = {ord('ת')} (U+05EA)")
    print(f"טווח: {ord('א')} - {ord('ת')}")


def demo_unicode_variety():
    """הדגמת מגוון תווי Unicode"""

    print("\n" + "=" * 60)
    print("מגוון תווים ב-Unicode")
    print("=" * 60)

    examples = [
        ("אנגלית", "Hello"),
        ("עברית", "שלום"),
        ("ערבית", "مرحبا"),
        ("יוונית", "Γεια"),
        ("סינית", "你好"),
        ("יפנית", "こんにちは"),
        ("אמוג'י", "😀🎉🐍"),
        ("סמלים", "€₪©®™"),
    ]

    for name, text in examples:
        print(f"\n{name}: {text}")
        print("  ", end="")
        for char in text:
            print(f"'{char}'=U+{ord(char):04X}", end="  ")
        print()


def demo_encoding():
    """הדגמת קידוד UTF-8"""

    print("\n" + "=" * 60)
    print("קידוד UTF-8")
    print("=" * 60)

    examples = [
        ("A", "אנגלית - בית אחד"),
        ("א", "עברית - שני בתים"),
        ("中", "סינית - שלושה בתים"),
        ("😀", "אמוג'י - ארבעה בתים"),
    ]

    print(f"\n{'תו':<4} {'Unicode':<12} {'UTF-8 bytes':<20} {'הערה'}")
    print("-" * 60)

    for char, note in examples:
        code_point = ord(char)
        utf8_bytes = char.encode('utf-8')
        bytes_hex = ' '.join(f'{b:02X}' for b in utf8_bytes)
        print(f"'{char}'   U+{code_point:04X}       {bytes_hex:<20} {note}")


def demo_practical_functions():
    """פונקציות שימושיות"""

    print("\n" + "=" * 60)
    print("פונקציות שימושיות")
    print("=" * 60)

    # פונקציה לבדיקת אות
    def is_letter(char):
        return 'A' <= char <= 'Z' or 'a' <= char <= 'z'

    # פונקציה לבדיקת ספרה
    def is_digit(char):
        return '0' <= char <= '9'

    # פונקציה להמרת רישיות
    def to_upper(char):
        if 'a' <= char <= 'z':
            return chr(ord(char) - 32)
        return char

    def to_lower(char):
        if 'A' <= char <= 'Z':
            return chr(ord(char) + 32)
        return char

    print("\nבדיקות תווים:")
    print("-" * 40)
    test_chars = ['A', 'z', '5', '!', ' ']
    for c in test_chars:
        print(f"'{c}': is_letter={is_letter(c)}, is_digit={is_digit(c)}")

    print("\nהמרת רישיות:")
    print("-" * 40)
    text = "Hello World"
    upper_text = ''.join(to_upper(c) for c in text)
    lower_text = ''.join(to_lower(c) for c in text)
    print(f"מקור:    '{text}'")
    print(f"גדולות:  '{upper_text}'")
    print(f"קטנות:   '{lower_text}'")


def main():
    demo_ord_chr_basics()
    demo_ascii_patterns()
    demo_ascii_table()
    demo_hebrew()
    demo_unicode_variety()
    demo_encoding()
    demo_practical_functions()


if __name__ == "__main__":
    main()
