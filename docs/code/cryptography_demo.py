"""
קריפטוגרפיה - ראשוניות, פרמה, RSA
מבוא למדעי המחשב
"""

import random


# ========================================
# בדיקת ראשוניות
# ========================================

def is_prime_naive(n):
    """בדיקת ראשוניות נאיבית - O(n)"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_sqrt(n):
    """בדיקת ראשוניות יעילה - O(√n)"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# ========================================
# modpower - חזקה מודולרית
# ========================================

def modpower(a, b, c):
    """
    חישוב a^b mod c ביעילות - O(log b)
    שיטת ריבוע חוזר (repeated squaring)
    """
    result = 1
    a = a % c

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        b = b // 2
        a = (a * a) % c

    return result


# ========================================
# משפט פרמה הקטן
# ========================================

def is_fermat_witness(a, m):
    """בודק אם a הוא עד פרמה ל-m"""
    return modpower(a, m - 1, m) != 1


def is_prime_fermat(m, k=100):
    """
    בדיקת ראשוניות הסתברותית - מבחן פרמה
    k = מספר איטרציות
    """
    if m < 2:
        return False
    if m == 2:
        return True
    if m % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, m - 2)
        if is_fermat_witness(a, m):
            return False  # בוודאות פריק

    return True  # כנראה ראשוני


# ========================================
# GCD ו-Extended GCD
# ========================================

def gcd(a, b):
    """אלגוריתם אוקלידס - O(log min(a,b))"""
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    """
    אלגוריתם אוקלידס המורחב
    מחזיר (gcd, x, y) כך ש-ax + by = gcd(a,b)
    """
    if a == 0:
        return b, 0, 1

    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd_val, x, y


def mod_inverse(a, m):
    """הופכי מודולרי: a^(-1) mod m"""
    gcd_val, x, _ = extended_gcd(a, m)
    if gcd_val != 1:
        return None  # אין הופכי
    return x % m


# ========================================
# Diffie-Hellman Key Exchange
# ========================================

def diffie_hellman_demo():
    """הדגמת פרוטוקול Diffie-Hellman"""
    print("\n--- Diffie-Hellman Key Exchange ---")

    # פרמטרים ציבוריים
    p = 23  # מספר ראשוני
    g = 5   # בסיס (generator)

    print(f"פרמטרים ציבוריים: p={p}, g={g}")

    # Alice בוחרת מפתח סודי
    a = 6  # סודי!
    A = modpower(g, a, p)  # ציבורי
    print(f"\nAlice: סודי a={a}, שולחת A = g^a mod p = {A}")

    # Bob בוחר מפתח סודי
    b = 15  # סודי!
    B = modpower(g, b, p)  # ציבורי
    print(f"Bob:   סודי b={b}, שולח B = g^b mod p = {B}")

    # חישוב המפתח המשותף
    K_alice = modpower(B, a, p)  # B^a = g^(ab)
    K_bob = modpower(A, b, p)    # A^b = g^(ab)

    print(f"\nמפתח משותף:")
    print(f"  Alice מחשבת: B^a mod p = {K_alice}")
    print(f"  Bob מחשב:    A^b mod p = {K_bob}")
    print(f"  שווים: {K_alice == K_bob}")


# ========================================
# RSA (פשוט)
# ========================================

def rsa_demo():
    """הדגמת RSA פשוט"""
    print("\n--- RSA ---")

    # יצירת מפתחות
    p, q = 61, 53  # ראשוניים
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17  # מפתח ציבורי (זר ל-phi)
    d = mod_inverse(e, phi)  # מפתח פרטי

    print(f"p={p}, q={q}")
    print(f"n = p×q = {n}")
    print(f"φ(n) = (p-1)(q-1) = {phi}")
    print(f"מפתח ציבורי: (e, n) = ({e}, {n})")
    print(f"מפתח פרטי: d = {d}")

    # הצפנה ופענוח
    message = 42
    encrypted = modpower(message, e, n)
    decrypted = modpower(encrypted, d, n)

    print(f"\nהודעה: {message}")
    print(f"מוצפנת: m^e mod n = {encrypted}")
    print(f"מפוענחת: c^d mod n = {decrypted}")
    print(f"נכון: {decrypted == message}")


def main():
    print("=" * 60)
    print("קריפטוגרפיה וראשוניות")
    print("=" * 60)

    # בדיקת ראשוניות
    print("\n--- בדיקת ראשוניות ---")
    for n in [2, 17, 561, 1009]:
        naive = is_prime_sqrt(n)
        fermat = is_prime_fermat(n)
        print(f"{n}: sqrt={naive}, fermat={fermat}")

    # מספרי קרמייכל (כושלים במבחן פרמה!)
    print("\n--- מספרי קרמייכל ---")
    print("561 = 3 × 11 × 17 (פריק, אבל עובר פרמה לרוב הבסיסים)")

    # modpower
    print("\n--- modpower ---")
    print(f"3^100 mod 7 = {modpower(3, 100, 7)}")
    print(f"2^1000 mod 13 = {modpower(2, 1000, 13)}")

    # Diffie-Hellman
    diffie_hellman_demo()

    # RSA
    rsa_demo()

    # סיכום
    print("\n" + "=" * 60)
    print("נקודות חשובות")
    print("=" * 60)
    print("""
    משפט פרמה הקטן:
    - אם p ראשוני ו-gcd(a,p)=1, אז a^(p-1) ≡ 1 (mod p)

    מספרי קרמייכל:
    - פריקים שעוברים את מבחן פרמה לכל הבסיסים
    - דוגמה: 561 = 3 × 11 × 17

    modpower:
    - O(log b) במקום O(b)
    - ריבוע חוזר

    Diffie-Hellman:
    - ציבורי: p, g, A=g^a, B=g^b
    - סודי: a, b, K=g^(ab)
    """)


if __name__ == "__main__":
    main()
