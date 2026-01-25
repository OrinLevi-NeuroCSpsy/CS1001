"""
קודים לגילוי ותיקון שגיאות
מבוא למדעי המחשב
"""


# ========================================
# ביט זוגיות (Parity Bit)
# ========================================

def add_parity(data, even=True):
    """הוספת ביט זוגיות"""
    ones = data.count('1')
    if even:
        parity = '0' if ones % 2 == 0 else '1'
    else:
        parity = '1' if ones % 2 == 0 else '0'
    return data + parity


def check_parity(data_with_parity, even=True):
    """בדיקת ביט זוגיות"""
    ones = data_with_parity.count('1')
    if even:
        return ones % 2 == 0
    else:
        return ones % 2 == 1


# ========================================
# קוד המינג (7,4)
# ========================================

def hamming_encode(data):
    """קידוד המינג (7,4) - 4 ביטים ל-7 ביטים"""
    if len(data) != 4:
        raise ValueError("נדרשים בדיוק 4 ביטים")

    d = [int(b) for b in data]

    # ביטי מידע: d[0], d[1], d[2], d[3]
    # מיקומים בקוד: p1, p2, d1, p4, d2, d3, d4
    #                1   2   3   4   5   6   7

    # חישוב ביטי זוגיות
    p1 = d[0] ^ d[1] ^ d[3]  # מיקומים 1,3,5,7
    p2 = d[0] ^ d[2] ^ d[3]  # מיקומים 2,3,6,7
    p4 = d[1] ^ d[2] ^ d[3]  # מיקומים 4,5,6,7

    # בניית הקוד
    code = [p1, p2, d[0], p4, d[1], d[2], d[3]]
    return ''.join(str(b) for b in code)


def hamming_decode(code):
    """פענוח ותיקון המינג (7,4)"""
    if len(code) != 7:
        raise ValueError("נדרשים בדיוק 7 ביטים")

    c = [int(b) for b in code]

    # חישוב סינדרום
    s1 = c[0] ^ c[2] ^ c[4] ^ c[6]  # מיקומים 1,3,5,7
    s2 = c[1] ^ c[2] ^ c[5] ^ c[6]  # מיקומים 2,3,6,7
    s4 = c[3] ^ c[4] ^ c[5] ^ c[6]  # מיקומים 4,5,6,7

    syndrome = s1 + 2 * s2 + 4 * s4

    # תיקון שגיאה
    corrected = c.copy()
    if syndrome != 0:
        error_pos = syndrome - 1
        corrected[error_pos] ^= 1  # הפוך את הביט

    # חילוץ ביטי המידע
    data = [corrected[2], corrected[4], corrected[5], corrected[6]]
    return ''.join(str(b) for b in data), syndrome


# ========================================
# מרחק המינג
# ========================================

def hamming_distance(s1, s2):
    """מרחק המינג בין שתי מחרוזות"""
    if len(s1) != len(s2):
        raise ValueError("המחרוזות חייבות להיות באותו אורך")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def min_distance(code_words):
    """מרחק מינימלי של קוד"""
    min_dist = float('inf')
    for i, w1 in enumerate(code_words):
        for w2 in code_words[i+1:]:
            dist = hamming_distance(w1, w2)
            min_dist = min(min_dist, dist)
    return min_dist


# ========================================
# יכולות גילוי ותיקון
# ========================================

def code_capabilities(d):
    """
    d = מרחק מינימלי של הקוד
    מחזיר: (גילוי, תיקון)
    """
    detect = d - 1
    correct = (d - 1) // 2
    return detect, correct


def main():
    print("=" * 60)
    print("קודים לגילוי ותיקון שגיאות")
    print("=" * 60)

    # ביט זוגיות
    print("\n--- ביט זוגיות ---")
    data = "1011"
    with_parity = add_parity(data)
    print(f"מידע: {data}")
    print(f"עם ביט זוגיות: {with_parity}")
    print(f"בדיקה (תקין): {check_parity(with_parity)}")

    # הכנסת שגיאה
    corrupted = with_parity[0] + ('0' if with_parity[1] == '1' else '1') + with_parity[2:]
    print(f"עם שגיאה: {corrupted}")
    print(f"בדיקה (פגום): {check_parity(corrupted)}")

    # קוד המינג
    print("\n--- קוד המינג (7,4) ---")
    data = "1011"
    encoded = hamming_encode(data)
    print(f"מידע: {data}")
    print(f"מקודד: {encoded}")

    # פענוח ללא שגיאה
    decoded, syndrome = hamming_decode(encoded)
    print(f"\nפענוח ללא שגיאה:")
    print(f"  סינדרום: {syndrome} (0 = תקין)")
    print(f"  מפוענח: {decoded}")

    # הכנסת שגיאה במיקום 3
    corrupted = encoded[:2] + ('0' if encoded[2] == '1' else '1') + encoded[3:]
    print(f"\nהכנסת שגיאה במיקום 3:")
    print(f"  מקורי:  {encoded}")
    print(f"  פגום:   {corrupted}")

    decoded, syndrome = hamming_decode(corrupted)
    print(f"  סינדרום: {syndrome} (מיקום השגיאה)")
    print(f"  מתוקן ומפוענח: {decoded}")
    print(f"  נכון: {decoded == data}")

    # מרחק המינג
    print("\n--- מרחק המינג ---")
    s1 = "10110"
    s2 = "11011"
    print(f"מרחק בין '{s1}' ל-'{s2}': {hamming_distance(s1, s2)}")

    # יכולות קוד
    print("\n--- יכולות קוד לפי מרחק ---")
    for d in range(1, 6):
        detect, correct = code_capabilities(d)
        print(f"d={d}: מגלה עד {detect} שגיאות, מתקן עד {correct} שגיאות")

    # סיכום
    print("\n" + "=" * 60)
    print("נוסחאות חשובות")
    print("=" * 60)
    print("""
    מרחק מינימלי d:
    - גילוי עד d-1 שגיאות
    - תיקון עד ⌊(d-1)/2⌋ שגיאות

    קוד המינג (7,4):
    - 4 ביטי מידע, 3 ביטי זוגיות
    - מרחק d=3
    - מגלה 2, מתקן 1

    חסם סינגלטון:
    - M ≤ q^(n-d+1)
    - M = מספר מילות קוד
    - q = גודל א"ב
    - n = אורך מילה
    - d = מרחק מינימלי
    """)


if __name__ == "__main__":
    main()
