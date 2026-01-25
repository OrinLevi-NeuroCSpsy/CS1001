# קריפטוגרפיה ותורת המספרים - סיכום לבחינה

---

## מושגי יסוד בתורת המספרים

### מספרים ראשוניים (Prime Numbers)

**הגדרה:** מספר טבעי גדול מ-1 שמתחלק רק ב-1 ובעצמו.

```
ראשוניים: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
לא ראשוניים: 4=2×2, 6=2×3, 9=3×3, 12=2×2×3, ...
```

**שים לב:**
- 1 **אינו** ראשוני
- 2 הוא הראשוני הזוגי **היחיד**

### מחלק (Divisor)

a מחלק את b (מסומן a|b) אם קיים מספר שלם k כך ש: b = a × k

```python
12 % 3 == 0  # True, כי 3 מחלק 12
12 % 5 == 0  # False, כי 5 לא מחלק 12
```

### מחלק משותף מקסימלי (GCD)

המספר הגדול ביותר שמחלק את שני המספרים.

```python
import math
math.gcd(12, 18)  # 6
math.gcd(17, 13)  # 1 (זרים)
```

---

## בדיקת ראשוניות

### אלגוריתם נאיבי - O(n)

```python
def is_prime_naive(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

### אלגוריתם משופר - O(√n)

**תובנה:** אם n = a × b ו-a ≤ b, אז a ≤ √n

```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # בודקים רק עד שורש n, ורק אי-זוגיים
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
```

**למה עד √n מספיק?**
```
אם n = a × b ושניהם > √n, אז a × b > √n × √n = n
סתירה! לכן לפחות אחד מהם ≤ √n
```

### דוגמה

```
בדיקת 101:
√101 ≈ 10.05
נבדוק: 2, 3, 5, 7 (ראשוניים עד 10)
101 % 2 ≠ 0
101 % 3 ≠ 0
101 % 5 ≠ 0
101 % 7 ≠ 0
→ 101 ראשוני!
```

---

## חשבון מודולרי (Modular Arithmetic)

### מהו?
חשבון "מעגלי" - כשמגיעים למספר מסוים, חוזרים ל-0.

```
שעון: 10 + 5 = 15 → 3 (mod 12)
```

### תכונות

```
(a + b) mod n = ((a mod n) + (b mod n)) mod n
(a × b) mod n = ((a mod n) × (b mod n)) mod n
```

**דוגמה:**
```python
(7 + 8) % 5       # 15 % 5 = 0
(7 % 5 + 8 % 5) % 5  # (2 + 3) % 5 = 0 ✓

(7 * 8) % 5       # 56 % 5 = 1
(7 % 5 * 8 % 5) % 5  # (2 * 3) % 5 = 1 ✓
```

---

## העלאה בחזקה מודולרית

### הבעיה
לחשב a^b mod n כאשר b גדול מאוד.

```python
# נאיבי - לא יעיל!
(2 ** 1000) % 17  # מחשב 2^1000 ואז mod
```

### פתרון: Repeated Squaring - O(log b)

**רעיון:** במקום לכפול b פעמים, משתמשים בייצוג הבינארי של b.

```
a^13 = a^(1101₂) = a^8 × a^4 × a^1
```

### מימוש

```python
def power_mod(base, exp, mod):
    """מחשב (base^exp) % mod ביעילות"""
    result = 1
    base = base % mod

    while exp > 0:
        # אם הביט הנוכחי הוא 1
        if exp % 2 == 1:
            result = (result * base) % mod

        # עוברים לביט הבא
        exp = exp // 2
        base = (base * base) % mod

    return result
```

**או בפייתון מובנה:**
```python
pow(base, exp, mod)  # יעיל!
```

### דוגמת מעקב

```
חשב 3^13 mod 7:

exp=13 (1101₂), base=3, result=1

exp=13 (אי-זוגי): result = 1×3 % 7 = 3
exp=6, base = 3×3 % 7 = 2

exp=6 (זוגי): result נשאר 3
exp=3, base = 2×2 % 7 = 4

exp=3 (אי-זוגי): result = 3×4 % 7 = 5
exp=1, base = 4×4 % 7 = 2

exp=1 (אי-זוגי): result = 5×2 % 7 = 3
exp=0 → סיום

תשובה: 3^13 mod 7 = 3
```

---

## פרוטוקול Diffie-Hellman

### מטרה
שני צדדים (Alice ו-Bob) רוצים ליצור **מפתח סודי משותף** דרך ערוץ **לא מאובטח**.

### הפרמטרים הציבוריים
- **p** = מספר ראשוני גדול
- **g** = generator (בסיס)

### השלבים

```
פרמטרים ציבוריים: p, g

1. Alice בוחרת מספר סודי a
   מחשבת: A = g^a mod p
   שולחת A ל-Bob (ציבורי)

2. Bob בוחר מספר סודי b
   מחשב: B = g^b mod p
   שולח B ל-Alice (ציבורי)

3. Alice מחשבת: K = B^a mod p = (g^b)^a mod p = g^(ab) mod p
   Bob מחשב:   K = A^b mod p = (g^a)^b mod p = g^(ab) mod p

   שניהם קיבלו את אותו K!
```

### דוגמה מספרית

```
p = 23, g = 5

Alice: a = 6 (סודי)
       A = 5^6 mod 23 = 8 (ציבורי)

Bob:   b = 15 (סודי)
       B = 5^15 mod 23 = 19 (ציבורי)

Alice: K = 19^6 mod 23 = 2
Bob:   K = 8^15 mod 23 = 2

מפתח משותף: K = 2
```

### מימוש

```python
def diffie_hellman_demo():
    # פרמטרים ציבוריים
    p = 23  # ראשוני
    g = 5   # generator

    # סודות
    a = 6   # של Alice
    b = 15  # של Bob

    # חישובים ציבוריים
    A = pow(g, a, p)  # Alice שולחת
    B = pow(g, b, p)  # Bob שולח

    # מפתח משותף
    K_alice = pow(B, a, p)
    K_bob = pow(A, b, p)

    print(f"A = {A}, B = {B}")
    print(f"K (Alice) = {K_alice}")
    print(f"K (Bob) = {K_bob}")
    assert K_alice == K_bob
```

### למה זה בטוח?
**בעיית הלוג הבדיד (Discrete Log Problem):**
- קל לחשב: g^a mod p
- קשה מאוד לחשב: למצוא a כאשר נתון g^a mod p

האקר רואה: p, g, A, B
אבל לא יכול לחשב a או b (עם p גדול מספיק).

---

## משפט פרמה הקטן

### הניסוח
אם p ראשוני ו-a לא מתחלק ב-p, אז:
```
a^(p-1) ≡ 1 (mod p)
```

### שימוש לבדיקת ראשוניות (Fermat Test)

```python
import random

def fermat_test(n, k=10):
    """בדיקת ראשוניות הסתברותית"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False  # בטוח לא ראשוני

    return True  # כנראה ראשוני
```

**שים לב:** זו בדיקה **הסתברותית** - יכולה לטעות (מספרי Carmichael).

---

## מציאת מחלקים

### כל המחלקים - O(√n)

```python
def find_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)

find_divisors(12)  # [1, 2, 3, 4, 6, 12]
```

### פירוק לגורמים ראשוניים

```python
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

prime_factors(60)  # [2, 2, 3, 5] = 2² × 3 × 5
```

---

## אלגוריתם אוקלידס ל-GCD

### הרעיון
```
gcd(a, b) = gcd(b, a mod b)
gcd(a, 0) = a
```

### מימוש

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

gcd(48, 18)  # 6
```

### מעקב
```
gcd(48, 18):
  gcd(18, 48 % 18) = gcd(18, 12)
  gcd(12, 18 % 12) = gcd(12, 6)
  gcd(6, 12 % 6) = gcd(6, 0)
  = 6
```

---

## טעויות נפוצות

### טעות 1: 1 הוא ראשוני
```python
# שגוי
def is_prime(n):
    if n == 1:
        return True  # 1 אינו ראשוני!
```

### טעות 2: שכחה ש-2 ראשוני וזוגי
```python
# שגוי - פוסל את 2
def is_prime(n):
    if n % 2 == 0:
        return False  # גם 2 נפסל!

# נכון
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
```

### טעות 3: בדיקה עד n במקום √n
```python
# לא יעיל - O(n)
for i in range(2, n):
    ...

# יעיל - O(√n)
while i * i <= n:
    ...
```

### טעות 4: חישוב חזקה גדולה ואז mod
```python
# לא יעיל ויכול לגרום ל-overflow
result = (base ** exp) % mod

# נכון
result = pow(base, exp, mod)
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: האם 97 ראשוני?

**פתרון:**
```
√97 ≈ 9.85
בדיקת מחלקים עד 9: 2, 3, 5, 7
97 % 2 = 1 (אי-זוגי)
97 % 3 = 1 (9+7=16, לא מתחלק ב-3)
97 % 5 = 2
97 % 7 = 6
→ 97 ראשוני ✓
```

---

### שאלה 2: חשב 5^100 mod 7

**פתרון:**
```
לפי משפט פרמה: 5^6 ≡ 1 (mod 7)
100 = 6 × 16 + 4
5^100 = 5^(6×16) × 5^4 = (5^6)^16 × 5^4 ≡ 1^16 × 5^4 (mod 7)
5^4 = 625 = 89×7 + 2 = 2 (mod 7)
תשובה: 2
```

---

### שאלה 3: Diffie-Hellman

p=11, g=2. Alice בוחרת a=3, Bob בוחר b=5. מהו המפתח המשותף?

**פתרון:**
```
A = 2^3 mod 11 = 8
B = 2^5 mod 11 = 32 mod 11 = 10

K = B^a mod 11 = 10^3 mod 11 = 1000 mod 11 = 10
(או K = A^b mod 11 = 8^5 mod 11 = 32768 mod 11 = 10)

מפתח: K = 10
```

---

## סיכום נקודות חשובות

- [ ] **ראשוני** = מתחלק רק ב-1 ובעצמו (1 לא ראשוני!)
- [ ] בדיקת ראשוניות: מספיק לבדוק עד **√n**
- [ ] **חשבון מודולרי**: (a×b) mod n = ((a mod n)×(b mod n)) mod n
- [ ] **Repeated Squaring**: חזקה מודולרית ב-O(log n)
- [ ] **Diffie-Hellman**: g^a mod p, g^b mod p → מפתח משותף g^(ab) mod p
- [ ] **משפט פרמה**: a^(p-1) ≡ 1 (mod p) כש-p ראשוני
- [ ] `pow(base, exp, mod)` - מובנה ויעיל בפייתון

---

## קישורים נוספים

- **קוד:** [cryptography_demo.py](../code/cryptography_demo.py)
- **שאלות בחינה:** [cryptography_and_primes.md](../exam_questions/cryptography_and_primes.md)
