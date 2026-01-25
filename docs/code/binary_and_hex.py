"""
המרות בין בסיסים בפייתון
מבוא למדעי המחשב
"""


def demo_builtin_functions():
    """הדגמת פונקציות מובנות להמרה"""

    print("=" * 60)
    print("פונקציות מובנות בפייתון להמרת בסיסים")
    print("=" * 60)

    # המרה מעשרוני לבסיסים אחרים
    num = 42

    print(f"\nהמספר העשרוני: {num}")
    print("-" * 40)
    print(f"bin({num}) = {bin(num):<12} # בינארי")
    print(f"oct({num}) = {oct(num):<12} # אוקטלי (בסיס 8)")
    print(f"hex({num}) = {hex(num):<12} # הקסדצימלי")

    # המרה מבסיסים אחרים לעשרוני
    print("\n" + "-" * 40)
    print("המרה לעשרוני עם int(string, base):")
    print("-" * 40)

    print(f"int('101010', 2)  = {int('101010', 2):<5} # בינארי לעשרוני")
    print(f"int('52', 8)      = {int('52', 8):<5} # אוקטלי לעשרוני")
    print(f"int('2a', 16)     = {int('2a', 16):<5} # הקסדצימלי לעשרוני")

    # שימוש בקידומות
    print("\n" + "-" * 40)
    print("שימוש בקידומות (0b, 0o, 0x):")
    print("-" * 40)

    binary_literal = 0b101010
    octal_literal = 0o52
    hex_literal = 0x2a

    print(f"0b101010 = {binary_literal}")
    print(f"0o52     = {octal_literal}")
    print(f"0x2a     = {hex_literal}")


def demo_decimal_to_binary():
    """הדגמת המרה ידנית מעשרוני לבינארי"""

    print("\n" + "=" * 60)
    print("המרה ידנית: עשרוני → בינארי (שיטת החילוק)")
    print("=" * 60)

    num = 25
    original = num
    remainders = []

    print(f"\nממירים את {num} לבינארי:")
    print("-" * 40)

    while num > 0:
        remainder = num % 2
        quotient = num // 2
        print(f"{num:3} ÷ 2 = {quotient:3}  שארית {remainder}")
        remainders.append(remainder)
        num = quotient

    binary_str = ''.join(str(r) for r in reversed(remainders))
    print("-" * 40)
    print(f"קוראים מלמטה למעלה: {binary_str}")
    print(f"\nתוצאה: {original}₁₀ = {binary_str}₂")
    print(f"בדיקה עם bin(): {bin(original)}")


def demo_binary_to_decimal():
    """הדגמת המרה ידנית מבינארי לעשרוני"""

    print("\n" + "=" * 60)
    print("המרה ידנית: בינארי → עשרוני (סכום חזקות)")
    print("=" * 60)

    binary_str = "110101"

    print(f"\nממירים את {binary_str}₂ לעשרוני:")
    print("-" * 40)

    # הצגת המיקומים והחזקות
    n = len(binary_str)
    print(f"{'מיקום:':<10}", end="")
    for i in range(n - 1, -1, -1):
        print(f"{i:>4}", end="")
    print()

    print(f"{'ספרה:':<10}", end="")
    for digit in binary_str:
        print(f"{digit:>4}", end="")
    print()

    print(f"{'חזקה:':<10}", end="")
    for i in range(n - 1, -1, -1):
        print(f"{2**i:>4}", end="")
    print()

    # חישוב
    print("-" * 40)
    total = 0
    terms = []

    for i, digit in enumerate(binary_str):
        power = n - 1 - i
        value = int(digit) * (2 ** power)
        if digit == '1':
            terms.append(f"{2**power}")
        total += value

    print(f"חישוב: {' + '.join(terms)} = {total}")
    print(f"\nתוצאה: {binary_str}₂ = {total}₁₀")
    print(f"בדיקה עם int(): {int(binary_str, 2)}")


def demo_hex_conversions():
    """הדגמת המרות הקסדצימליות"""

    print("\n" + "=" * 60)
    print("המרות הקסדצימליות")
    print("=" * 60)

    # הקסדצימלי לעשרוני
    hex_str = "2F"
    print(f"\n{hex_str}₁₆ לעשרוני:")
    print("-" * 40)
    print(f"2 × 16¹ + F × 16⁰")
    print(f"= 2 × 16 + 15 × 1")
    print(f"= 32 + 15")
    print(f"= 47₁₀")
    print(f"בדיקה: int('{hex_str}', 16) = {int(hex_str, 16)}")

    # בינארי להקסדצימלי
    print("\n" + "-" * 40)
    print("בינארי → הקסדצימלי (קיבוץ לרביעיות)")
    print("-" * 40)

    binary = "11010110"
    print(f"בינארי: {binary}")

    # קיבוץ לרביעיות
    padded = binary.zfill((len(binary) + 3) // 4 * 4)  # ריפוד לכפולה של 4
    nibbles = [padded[i:i+4] for i in range(0, len(padded), 4)]

    print(f"קיבוץ:  {' '.join(nibbles)}")

    hex_digits = []
    for nibble in nibbles:
        decimal_val = int(nibble, 2)
        hex_digit = hex(decimal_val)[2:].upper()
        hex_digits.append(hex_digit)
        print(f"        {nibble} = {decimal_val:2} = {hex_digit}")

    result = ''.join(hex_digits)
    print(f"\nתוצאה: {binary}₂ = {result}₁₆")


def demo_range():
    """הדגמת טווחי ערכים"""

    print("\n" + "=" * 60)
    print("טווחי ערכים לפי מספר ביטים")
    print("=" * 60)

    print("\nללא סימן (unsigned):")
    print("-" * 40)
    print(f"{'bits':<6} {'מינימום':<12} {'מקסימום':<12} {'כמות ערכים':<12}")
    print("-" * 40)

    for bits in [4, 8, 16, 32]:
        min_val = 0
        max_val = 2**bits - 1
        count = 2**bits
        print(f"{bits:<6} {min_val:<12} {max_val:<12} {count:<12}")


def main():
    demo_builtin_functions()
    demo_decimal_to_binary()
    demo_binary_to_decimal()
    demo_hex_conversions()
    demo_range()


if __name__ == "__main__":
    main()
