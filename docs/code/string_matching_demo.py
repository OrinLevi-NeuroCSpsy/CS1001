"""
התאמת מחרוזות - אלגוריתמים
מבוא למדעי המחשב
"""


# ========================================
# חיפוש נאיבי
# ========================================

def naive_search(text, pattern):
    """
    חיפוש נאיבי - O(n*m)
    מחזיר רשימת אינדקסים של התאמות
    """
    n, m = len(text), len(pattern)
    matches = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)

    return matches


def naive_search_verbose(text, pattern):
    """חיפוש נאיבי עם הדפסות"""
    n, m = len(text), len(pattern)
    comparisons = 0

    print(f"טקסט: {text}")
    print(f"תבנית: {pattern}")
    print("-" * 40)

    for i in range(n - m + 1):
        print(f"\nמיקום {i}:")
        print(f"  {'  ' * i}{pattern}")
        print(f"  {text}")

        match = True
        for j in range(m):
            comparisons += 1
            if text[i + j] != pattern[j]:
                print(f"  אי-התאמה במיקום {j}: '{text[i+j]}' != '{pattern[j]}'")
                match = False
                break

        if match:
            print(f"  התאמה!")

    print(f"\nסה\"כ השוואות: {comparisons}")


# ========================================
# אלגוריתם Rabin-Karp
# ========================================

def rabin_karp(text, pattern, base=256, prime=101):
    """
    אלגוריתם Rabin-Karp עם rolling hash
    O(n+m) בממוצע, O(n*m) במקרה גרוע
    """
    n, m = len(text), len(pattern)
    matches = []

    if m > n:
        return matches

    # חישוב hash של התבנית
    pattern_hash = 0
    text_hash = 0
    h = pow(base, m - 1, prime)  # base^(m-1) mod prime

    # חישוב hash התחלתי
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    # חיפוש
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # אימות (כי יתכנו התנגשויות)
            if text[i:i+m] == pattern:
                matches.append(i)

        # עדכון rolling hash
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) +
                        ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return matches


def rabin_karp_verbose(text, pattern, base=256, prime=101):
    """Rabin-Karp עם הדפסות"""
    n, m = len(text), len(pattern)

    print(f"טקסט: {text}")
    print(f"תבנית: {pattern}")
    print(f"base={base}, prime={prime}")
    print("-" * 40)

    # חישוב hash של התבנית
    pattern_hash = 0
    for c in pattern:
        pattern_hash = (base * pattern_hash + ord(c)) % prime
    print(f"hash(pattern) = {pattern_hash}")

    # חישוב hash התחלתי
    text_hash = 0
    h = pow(base, m - 1, prime)

    for i in range(m):
        text_hash = (base * text_hash + ord(text[i])) % prime

    print(f"hash(text[0:{m}]) = {text_hash}")

    # חיפוש
    for i in range(n - m + 1):
        print(f"\ni={i}: hash={text_hash}", end="")

        if pattern_hash == text_hash:
            if text[i:i+m] == pattern:
                print(f" ✓ התאמה!")
            else:
                print(f" (התנגשות hash)")
        else:
            print()

        # עדכון rolling hash
        if i < n - m:
            old_hash = text_hash
            text_hash = (base * (text_hash - ord(text[i]) * h) +
                        ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime


# ========================================
# השוואת אלגוריתמים
# ========================================

def compare_algorithms(text, pattern):
    """השוואת האלגוריתמים"""
    print(f"\nטקסט: '{text}'")
    print(f"תבנית: '{pattern}'")
    print("-" * 40)

    # נאיבי
    matches1 = naive_search(text, pattern)
    print(f"נאיבי: {matches1}")

    # Rabin-Karp
    matches2 = rabin_karp(text, pattern)
    print(f"Rabin-Karp: {matches2}")


def main():
    print("=" * 60)
    print("התאמת מחרוזות")
    print("=" * 60)

    # חיפוש נאיבי
    print("\n--- חיפוש נאיבי ---")
    text = "AABAACAADAABAAABAA"
    pattern = "AABA"
    naive_search_verbose(text, pattern)

    # Rabin-Karp
    print("\n" + "=" * 60)
    print("--- Rabin-Karp ---")
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    rabin_karp_verbose(text, pattern)

    # השוואה
    print("\n" + "=" * 60)
    print("--- השוואות ---")
    compare_algorithms("ABABDABACDABABCABAB", "ABABCABAB")

    # סיבוכיות
    print("\n" + "=" * 60)
    print("סיבוכיות")
    print("=" * 60)
    print("""
    | אלגוריתם    | ממוצע      | גרוע       | הערות            |
    |-------------|------------|------------|------------------|
    | נאיבי       | O(n*m)     | O(n*m)     | פשוט             |
    | Rabin-Karp  | O(n+m)     | O(n*m)     | rolling hash     |
    | KMP         | O(n+m)     | O(n+m)     | preprocessing    |

    n = אורך הטקסט
    m = אורך התבנית

    Rabin-Karp יתרונות:
    - חיפוש מרובה תבניות
    - rolling hash מהיר
    """)


if __name__ == "__main__":
    main()
