# התאמת מחרוזות (String Matching) - סיכום לבחינה

---

## הבעיה

**נתון:** טקסט T באורך n, תבנית P באורך m (כאשר m ≤ n)

**מטרה:** מצא את כל המופעים של P בתוך T

```
T = "ABABCABABD"
P = "ABAB"

מופעים במיקומים: 0, 5
```

---

## אלגוריתם נאיבי

### הרעיון
בדוק כל מיקום אפשרי בטקסט.

### מימוש

```python
def naive_search(text, pattern):
    """חיפוש נאיבי - O(n × m)"""
    n, m = len(text), len(pattern)
    matches = []

    for i in range(n - m + 1):
        # בדוק האם יש התאמה במיקום i
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            matches.append(i)

    return matches

# או בקיצור:
def naive_search_short(text, pattern):
    n, m = len(text), len(pattern)
    return [i for i in range(n - m + 1)
            if text[i:i+m] == pattern]
```

### דוגמה

```
T = "AAAAB"
P = "AAB"

i=0: AAA vs AAB → לא (תו שלישי שונה)
i=1: AAA vs AAB → לא
i=2: AAB vs AAB → כן! ✓

תוצאה: [2]
```

### סיבוכיות

| מקרה | סיבוכיות |
|------|----------|
| **גרוע** | O(n × m) |
| **ממוצע** | O(n) |

**מקרה גרוע:** T = "AAAA...A", P = "AAA...AB"

---

## אלגוריתם Rabin-Karp

### הרעיון המרכזי
**השתמש ב-hash במקום השוואת תווים!**

במקום להשוות m תווים בכל מיקום:
1. חשב hash של התבנית
2. חשב hash של חלון בטקסט
3. אם ה-hash זהה → בדוק התאמה מלאה

### Rolling Hash (גלגול ה-hash)

**הקסם:** אפשר לעדכן את ה-hash ב-O(1) כשמזיזים את החלון!

```
hash("BCD") = hash("ABCD" - 'A') + 'D'
```

### נוסחת ה-Hash

נתייחס לכל תו כספרה בבסיס d (בדרך כלל d=256 לכל תווי ASCII).

```
hash(s) = (s[0]×d^(m-1) + s[1]×d^(m-2) + ... + s[m-1]) mod q
```

כאשר q הוא מספר ראשוני גדול (למניעת התנגשויות).

### עדכון Rolling Hash

```python
# מעבר מ-text[i:i+m] ל-text[i+1:i+m+1]
new_hash = (d × (old_hash - text[i] × d^(m-1)) + text[i+m]) mod q
```

**ויזואלית:**
```
חלון ישן: [A B C D] E F
           ↓
חלון חדש: A [B C D E] F

new_hash = (hash - A×d³)×d + E
```

### מימוש מלא

```python
def rabin_karp(text, pattern, d=256, q=101):
    """
    אלגוריתם Rabin-Karp
    d = גודל האלפבית (256 ל-ASCII)
    q = מספר ראשוני לחישוב mod
    """
    n, m = len(text), len(pattern)
    if m > n:
        return []

    matches = []

    # חישוב d^(m-1) mod q
    h = pow(d, m - 1, q)

    # חישוב hash התחלתי לתבנית ולחלון הראשון
    p_hash = 0  # hash של התבנית
    t_hash = 0  # hash של החלון בטקסט

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # סריקת הטקסט
    for i in range(n - m + 1):
        # בדיקה אם ה-hash זהה
        if p_hash == t_hash:
            # וידוא התאמה מלאה (בגלל התנגשויות אפשריות)
            if text[i:i+m] == pattern:
                matches.append(i)

        # עדכון rolling hash (אם יש עוד מיקומים)
        if i < n - m:
            # הסר את התו הראשון, הוסף את הבא
            t_hash = (d * (t_hash - ord(text[i]) * h) +
                      ord(text[i + m])) % q

            # טיפול במספרים שליליים
            if t_hash < 0:
                t_hash += q

    return matches
```

### דוגמת מעקב

```
T = "ABCAB"
P = "AB"
d = 256, q = 101

שלב 1: חישוב hash התחלתי
p_hash = (256×65 + 66) % 101 = (16640 + 66) % 101 = 16706 % 101 = 43
t_hash = (256×65 + 66) % 101 = 43

שלב 2: סריקה
i=0: t_hash(43) == p_hash(43) → בדיקה → "AB"=="AB" ✓ מצאנו!
     עדכון: t_hash = (256×(43 - 65×1) + 67) % 101 = ...

i=1: t_hash ≠ p_hash → דילוג

i=2: t_hash ≠ p_hash → דילוג

i=3: t_hash == p_hash → בדיקה → "AB"=="AB" ✓ מצאנו!

תוצאה: [0, 3]
```

### סיבוכיות

| מקרה | סיבוכיות | הסבר |
|------|----------|------|
| **ממוצע** | O(n + m) | מעט התנגשויות |
| **גרוע** | O(n × m) | הרבה התנגשויות |

**מקרה גרוע:** כל ה-hash-ים זהים (נדיר עם q גדול)

---

## התנגשויות (Collisions)

### מה זה?
שתי מחרוזות שונות עם אותו hash.

```python
# דוגמה (לא אמיתית, להמחשה):
hash("AB") = 43
hash("XY") = 43  # התנגשות!
```

### למה בודקים התאמה מלאה?

```python
if p_hash == t_hash:
    if text[i:i+m] == pattern:  # חובה! בגלל התנגשויות
        matches.append(i)
```

בלי הבדיקה הנוספת, נחזיר false positives.

### הקטנת התנגשויות
- בחר q ראשוני וגדול
- אפשר להשתמש בכמה hash-ים במקביל

---

## השוואת אלגוריתמים

| אלגוריתם | זמן ממוצע | זמן גרוע | יתרונות |
|----------|-----------|----------|---------|
| **נאיבי** | O(n) | O(n×m) | פשוט |
| **Rabin-Karp** | O(n+m) | O(n×m) | טוב למספר תבניות |
| **KMP** | O(n+m) | O(n+m) | גרוע קבוע |
| **Boyer-Moore** | O(n/m) | O(n×m) | מהיר בפרקטיקה |

---

## חיפוש מספר תבניות

### הבעיה
מצא את כל מופעי k תבניות שונות בטקסט.

### פתרון נאיבי
הרץ Rabin-Karp k פעמים → O(k × n)

### פתרון משופר
חשב hash לכל התבניות והשווה במעבר אחד.

```python
def multi_pattern_search(text, patterns):
    """חיפוש מספר תבניות עם Rabin-Karp"""
    d, q = 256, 101
    n = len(text)

    # מיון לפי אורך (אותו אורך = אותו rolling hash)
    by_length = {}
    for p in patterns:
        m = len(p)
        if m not in by_length:
            by_length[m] = []
        by_length[m].append(p)

    results = {p: [] for p in patterns}

    for m, group in by_length.items():
        if m > n:
            continue

        # חישוב hash לכל תבנית באורך m
        pattern_hashes = {}
        for p in group:
            h = 0
            for c in p:
                h = (d * h + ord(c)) % q
            pattern_hashes[h] = pattern_hashes.get(h, []) + [p]

        # סריקת הטקסט
        h = pow(d, m - 1, q)
        t_hash = 0
        for i in range(m):
            t_hash = (d * t_hash + ord(text[i])) % q

        for i in range(n - m + 1):
            if t_hash in pattern_hashes:
                for p in pattern_hashes[t_hash]:
                    if text[i:i+m] == p:
                        results[p].append(i)

            if i < n - m:
                t_hash = (d * (t_hash - ord(text[i]) * h) +
                          ord(text[i + m])) % q
                if t_hash < 0:
                    t_hash += q

    return results
```

---

## שימוש ב-Python מובנה

```python
text = "ABABCABABD"
pattern = "ABAB"

# מציאת מופע ראשון
text.find(pattern)      # 0
text.index(pattern)     # 0 (זורק שגיאה אם לא נמצא)

# מציאת כל המופעים
def find_all(text, pattern):
    start = 0
    while True:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        yield pos
        start = pos + 1

list(find_all(text, pattern))  # [0, 5]

# ספירת מופעים (לא חופפים)
text.count(pattern)     # 2
```

---

## טעויות נפוצות

### טעות 1: שכחת בדיקת התאמה מלאה

```python
# שגוי!
if p_hash == t_hash:
    matches.append(i)  # יכול להיות false positive

# נכון
if p_hash == t_hash:
    if text[i:i+m] == pattern:
        matches.append(i)
```

### טעות 2: hash שלילי

```python
# מספרים שליליים אחרי mod יכולים לקרות בפייתון
t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q

# צריך לטפל:
if t_hash < 0:
    t_hash += q
```

### טעות 3: חריגה מגבולות

```python
# שגוי - נגמר לפני הסוף
for i in range(n - m):  # חסר +1!

# נכון
for i in range(n - m + 1):
```

### טעות 4: בלבול בין מיקום למופע

```python
# מיקום = אינדקס (0-based)
# מופע = המחרוזת עצמה

matches = find_all("ABAB", "AB")  # [0, 2] - מיקומים!
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: סיבוכיות נאיבי

מה סיבוכיות הזמן של האלגוריתם הנאיבי במקרה הגרוע?

**תשובה:** O(n × m)

**הסבר:** בכל מיקום (n-m+1 מיקומים) משווים עד m תווים.

---

### שאלה 2: Rolling Hash

הסבר איך עובד rolling hash.

**תשובה:**
Rolling hash מאפשר לעדכן את ה-hash ב-O(1) כשמזיזים את החלון:

```
hash חדש = (hash ישן - תו_שיצא × d^(m-1)) × d + תו_שנכנס

דוגמה: מעבר מ-"ABC" ל-"BCD":
new_hash = (hash(ABC) - 'A'×256²) × 256 + 'D'
```

---

### שאלה 3: התנגשויות

מדוע צריך לבדוק התאמה מלאה אחרי התאמת hash?

**תשובה:**
כי עלולות להיות **התנגשויות** - מחרוזות שונות עם אותו hash. בדיקת ה-hash בלבד יכולה לתת false positives.

---

### שאלה 4: חישוב hash

חשב את ה-hash של "AB" עם d=10, q=13.

**תשובה:**
```
hash("AB") = (A×d + B) mod q
           = (65×10 + 66) mod 13
           = 716 mod 13
           = 1
```

---

### שאלה 5: מציאת מופעים

נתון: T="AABAACAADAABAABA", P="AABA"

מצא את כל מיקומי המופעים.

**פתרון:**
```
בדיקה ידנית:
i=0:  AABA = AABA ✓
i=1:  ABAA ≠ AABA
i=2:  BAAC ≠ AABA
...
i=9:  AABA = AABA ✓
i=12: AABA = AABA ✓

תשובה: [0, 9, 12]
```

---

### שאלה 6: יתרון Rabin-Karp

מה היתרון של Rabin-Karp על האלגוריתם הנאיבי?

**תשובה:**
1. **בממוצע O(n+m)** במקום O(n×m)
2. **יעיל לחיפוש מספר תבניות** - אפשר לחשב hash לכולן ולחפש במעבר אחד
3. **פשוט למימוש** יחסית לאלגוריתמים מתוחכמים כמו KMP

---

## סיכום נקודות חשובות

- [ ] **בעיית התאמת מחרוזות**: מציאת תבנית P בתוך טקסט T
- [ ] **נאיבי**: O(n×m) גרוע, פשוט למימוש
- [ ] **Rabin-Karp**: משתמש ב-hash לזיהוי מהיר
- [ ] **Rolling Hash**: עדכון hash ב-O(1) בהזזת חלון
- [ ] **התנגשויות**: hash זהה למחרוזות שונות → חובה לבדוק התאמה מלאה
- [ ] **סיבוכיות RK**: ממוצע O(n+m), גרוע O(n×m)
- [ ] **יתרון RK**: יעיל לחיפוש מספר תבניות
- [ ] נוסחת hash: `hash(s) = Σ s[i]×d^(m-1-i) mod q`
