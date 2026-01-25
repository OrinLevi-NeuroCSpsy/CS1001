# דחיסת נתונים (Data Compression) - סיכום לבחינה

---

## מושגי יסוד

### מהי דחיסה?
הקטנת גודל הייצוג של מידע תוך שמירה על היכולת לשחזר אותו.

### סוגי דחיסה

| סוג | הסבר | דוגמאות |
|-----|------|---------|
| **Lossless** (ללא אובדן) | שחזור מושלם | ZIP, PNG, Huffman |
| **Lossy** (עם אובדן) | שחזור חלקי | JPEG, MP3 |

### יחס דחיסה

```
יחס דחיסה = גודל מקורי / גודל דחוס
```

דוגמה: קובץ 100KB שנדחס ל-25KB → יחס 4:1

---

## קידוד Huffman

### הרעיון המרכזי
**תווים נפוצים יקבלו קוד קצר יותר.**

במקום 8 ביטים לכל תו (ASCII), נשתמש בקוד באורך משתנה.

### תכונות קוד Huffman
- **Prefix-free**: אף קוד אינו רישא (prefix) של קוד אחר
- **אופטימלי**: הקידוד הכי קצר שאפשר לקוד prefix-free
- **מבוסס תדירויות**: צריך לדעת מראש את התדירויות

### בניית עץ Huffman

**אלגוריתם:**
1. צור צומת לכל תו עם התדירות שלו
2. **בכל שלב**: מזג את שני הצמתים עם התדירות הנמוכה ביותר
3. חזור עד שנשאר עץ אחד
4. קרא את הקוד: שמאל = 0, ימין = 1

### דוגמה מלאה

```
מחרוזת: "ABRACADABRA"

שלב 1: ספירת תדירויות
A: 5
B: 2
R: 2
C: 1
D: 1

שלב 2: בניית העץ (מזגים את הנמוכים ביותר)

איטרציה 1: מזג C(1) + D(1) = CD(2)
איטרציה 2: מזג B(2) + R(2) = BR(4)
איטרציה 3: מזג CD(2) + BR(4) = CDBR(6)
איטרציה 4: מזג A(5) + CDBR(6) = שורש(11)

העץ הסופי:
          (11)
         /    \
       A(5)   (6)
             /    \
           (2)    (4)
          / \    /   \
        C(1) D(1) B(2) R(2)

שלב 3: קריאת הקודים
A: 0
C: 100
D: 101
B: 110
R: 111
```

### מימוש

```python
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    """בונה עץ Huffman מטקסט"""
    # ספירת תדירויות
    freq = Counter(text)

    # יצירת heap של צמתים
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    # בניית העץ
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def build_codes(root, current_code="", codes=None):
    """בונה מילון קודים מהעץ"""
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:  # עלה
        codes[root.char] = current_code if current_code else "0"

    build_codes(root.left, current_code + "0", codes)
    build_codes(root.right, current_code + "1", codes)

    return codes

def huffman_encode(text):
    """מקודד טקסט ב-Huffman"""
    tree = build_huffman_tree(text)
    codes = build_codes(tree)
    encoded = ''.join(codes[char] for char in text)
    return encoded, codes, tree

def huffman_decode(encoded, tree):
    """מפענח טקסט מקודד Huffman"""
    result = []
    node = tree

    for bit in encoded:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char is not None:  # הגענו לעלה
            result.append(node.char)
            node = tree  # חזרה לשורש

    return ''.join(result)
```

### דוגמת שימוש

```python
text = "ABRACADABRA"
encoded, codes, tree = huffman_encode(text)

print("קודים:", codes)
# {'A': '0', 'B': '110', 'R': '111', 'C': '100', 'D': '101'}

print("מקודד:", encoded)
# '0110111010010101110111'

print("אורך מקורי:", len(text) * 8, "bits")
# 88 bits (11 תווים × 8 ביט)

print("אורך דחוס:", len(encoded), "bits")
# 23 bits

print("פענוח:", huffman_decode(encoded, tree))
# 'ABRACADABRA'
```

### חישוב אורך ממוצע

```
אורך ממוצע = Σ (תדירות_יחסית × אורך_קוד)
```

**דוגמה:**
```
A: תדירות 5/11, קוד אורך 1 → 5/11 × 1 = 0.45
B: תדירות 2/11, קוד אורך 3 → 2/11 × 3 = 0.55
R: תדירות 2/11, קוד אורך 3 → 2/11 × 3 = 0.55
C: תדירות 1/11, קוד אורך 3 → 1/11 × 3 = 0.27
D: תדירות 1/11, קוד אורך 3 → 1/11 × 3 = 0.27

אורך ממוצע = 0.45 + 0.55 + 0.55 + 0.27 + 0.27 = 2.09 bits/char
(במקום 8 bits/char ב-ASCII!)
```

---

## אנטרופיה (Entropy)

### הגדרה
**הגבול התיאורטי התחתון** למספר הביטים הממוצע לתו.

```
H = -Σ p(x) × log₂(p(x))
```

כאשר p(x) הוא ההסתברות של כל תו.

### דוגמה

```python
import math

def entropy(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    n = len(text)
    h = 0
    for count in freq.values():
        p = count / n
        h -= p * math.log2(p)

    return h

text = "ABRACADABRA"
print(f"אנטרופיה: {entropy(text):.2f} bits/char")
# ~2.04 bits/char

# Huffman נותן 2.09 - קרוב מאוד לאופטימום!
```

### מה זה אומר?
- אנטרופיה נמוכה = יתירות גבוהה = דחיסה טובה
- Huffman תמיד ≥ אנטרופיה (אבל קרוב מאוד)

---

## דחיסת LZ (Lempel-Ziv)

### הרעיון
**לא צריך לדעת תדירויות מראש!**

במקום לקודד תווים בודדים, מקודדים **תבניות חוזרות** על ידי הפניה למיקום קודם.

### גרסאות נפוצות

| גרסה | שימוש |
|------|-------|
| LZ77 | GZIP, PNG |
| LZ78 | GIF |
| LZW | GIF, TIFF |

### LZ77 - רעיון בסיסי

מחליף רצפים חוזרים ב-**(offset, length, next_char)**

```
טקסט: ABRACADABRA

עיבוד:
A         → (0, 0, 'A')  - תו חדש
B         → (0, 0, 'B')  - תו חדש
R         → (0, 0, 'R')  - תו חדש
A         → (3, 1, 'C')  - A הופיע 3 מיקומים אחורה, אורך 1, אח"כ C
A         → (2, 1, 'D')  - A הופיע 2 מיקומים אחורה, אורך 1, אח"כ D
ABRA      → (7, 4, EOF)  - ABRA הופיע 7 מיקומים אחורה, אורך 4
```

### מימוש LZ77 פשוט

```python
def lz77_encode(text, window_size=100):
    """קידוד LZ77 פשוט"""
    result = []
    i = 0

    while i < len(text):
        best_offset = 0
        best_length = 0

        # חיפוש התאמה בחלון
        start = max(0, i - window_size)
        for j in range(start, i):
            length = 0
            while (i + length < len(text) and
                   text[j + length] == text[i + length] and
                   j + length < i):
                length += 1

            if length > best_length:
                best_length = length
                best_offset = i - j

        # הוספת התו הבא
        if i + best_length < len(text):
            next_char = text[i + best_length]
        else:
            next_char = ''

        result.append((best_offset, best_length, next_char))
        i += best_length + 1

    return result

def lz77_decode(encoded):
    """פענוח LZ77"""
    result = []

    for offset, length, next_char in encoded:
        if length > 0:
            start = len(result) - offset
            for i in range(length):
                result.append(result[start + i])
        if next_char:
            result.append(next_char)

    return ''.join(result)
```

### דוגמה

```python
text = "ABRACADABRA"
encoded = lz77_encode(text)
print(encoded)
# [(0, 0, 'A'), (0, 0, 'B'), (0, 0, 'R'), (3, 1, 'C'),
#  (2, 1, 'D'), (7, 4, '')]

decoded = lz77_decode(encoded)
print(decoded)
# 'ABRACADABRA'
```

---

## LZW (Lempel-Ziv-Welch)

### הרעיון
בונה **מילון** תוך כדי קידוד.

### אלגוריתם קידוד

```python
def lzw_encode(text):
    """קידוד LZW"""
    # מילון התחלתי: כל תו בודד
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    result = []
    w = ""

    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    if w:
        result.append(dictionary[w])

    return result

def lzw_decode(encoded):
    """פענוח LZW"""
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    result = []
    w = chr(encoded[0])
    result.append(w)

    for code in encoded[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == dict_size:
            entry = w + w[0]
        else:
            raise ValueError("Bad encoded code")

        result.append(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry

    return ''.join(result)
```

### דוגמת מעקב

```
טקסט: "ABABABA"

קידוד:
התחלתי: A=65, B=66, ...

קורא A: w="A"
קורא B: AB לא במילון → פלט 65, מוסיף AB=256, w="B"
קורא A: BA לא במילון → פלט 66, מוסיף BA=257, w="A"
קורא B: AB במילון! w="AB"
קורא A: ABA לא במילון → פלט 256, מוסיף ABA=258, w="A"
קורא B: AB במילון! w="AB"
קורא A: ABA במילון! w="ABA"
סוף → פלט 258

תוצאה: [65, 66, 256, 258]
```

---

## השוואת שיטות

| שיטה | יתרונות | חסרונות |
|------|---------|---------|
| **Huffman** | אופטימלי לתדירויות ידועות | צריך שני מעברים, צריך לשמור עץ |
| **LZ77** | מעבר אחד, טוב לטקסט | איטי (חיפוש בחלון) |
| **LZW** | מעבר אחד, מהיר | מילון יכול לגדול |

---

## טעויות נפוצות

### טעות 1: בלבול בסדר מיזוג Huffman

```
# שגוי - לא תמיד מזגים לפי סדר ה-א"ב
# נכון - תמיד מזגים את שני הצמתים עם התדירות הנמוכה ביותר
```

### טעות 2: שכחה ש-Huffman הוא prefix-free

```
# קוד תקין:
A = 0, B = 10, C = 11

# קוד לא תקין:
A = 0, B = 01, C = 011  # 0 הוא prefix של 01!
```

### טעות 3: אנטרופיה לעומת אורך ממוצע

```
אנטרופיה = גבול תיאורטי תחתון
אורך ממוצע של Huffman ≥ אנטרופיה

הם קרובים אבל לא זהים!
```

### טעות 4: LZ לעומת Huffman

```
Huffman = סטטיסטי (צריך תדירויות)
LZ = מילוני (לא צריך מידע מראש)

לפעמים LZ טוב יותר, לפעמים Huffman!
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: בניית עץ Huffman

נתון: A:4, B:2, C:1, D:1

בנה את עץ Huffman ורשום את הקודים.

**פתרון:**
```
שלב 1: מזג C(1) + D(1) = CD(2)
שלב 2: מזג B(2) + CD(2) = BCD(4)
שלב 3: מזג A(4) + BCD(4) = שורש(8)

עץ:
       (8)
      /   \
    A(4)  (4)
         /   \
       B(2)  (2)
            /   \
          C(1)  D(1)

קודים:
A = 0
B = 10
C = 110
D = 111
```

---

### שאלה 2: חישוב אורך ממוצע

בהינתן הקודים מהשאלה הקודמת, מהו האורך הממוצע?

**פתרון:**
```
סה"כ תווים: 4+2+1+1 = 8

אורך ממוצע = (4/8×1) + (2/8×2) + (1/8×3) + (1/8×3)
           = 0.5 + 0.5 + 0.375 + 0.375
           = 1.75 bits/char
```

---

### שאלה 3: פענוח Huffman

בהינתן: A=0, B=10, C=11

פענח: 0101100

**פתרון:**
```
0  → A
10 → B
11 → C
0  → A
0  → A

תשובה: ABCAA
```

---

### שאלה 4: מדוע קוד Huffman הוא prefix-free?

**תשובה:**
כי כל תו נמצא **בעלה** של העץ. אם תו היה בצומת פנימי, הקוד שלו היה prefix של קוד אחר (בצאצאיו). בעץ Huffman כל התווים בעלים, לכן אף קוד לא יכול להיות prefix של אחר.

---

### שאלה 5: LZ77

קודד את המחרוזת "AABABAB" ב-LZ77.

**פתרון:**
```
A       → (0, 0, 'A')  - תו חדש
A       → (1, 1, 'B')  - A הופיע 1 אחורה, אורך 1, אח"כ B
ABAB    → (2, 4, '')   - AB הופיע 2 אחורה, אורך 4

תוצאה: [(0,0,'A'), (1,1,'B'), (2,4,'')]
```

---

## סיכום נקודות חשובות

- [ ] **Huffman** = קידוד אופטימלי לפי תדירויות, תווים נפוצים ← קוד קצר
- [ ] **Prefix-free** = אף קוד לא רישא של אחר (מאפשר פענוח חד-ערכי)
- [ ] **בניית עץ**: מזג תמיד את שני הצמתים עם התדירות הנמוכה ביותר
- [ ] **קריאת קודים**: שמאל=0, ימין=1
- [ ] **אנטרופיה** = גבול תיאורטי תחתון (Huffman קרוב אליו)
- [ ] **LZ** = דחיסה מילונית, לא צריך תדירויות מראש
- [ ] **LZ77** = (offset, length, next) - הפניה למיקום קודם
- [ ] **LZW** = בונה מילון תוך כדי קידוד

---

## קישורים נוספים

- **קוד:** [compression_demo.py](../code/compression_demo.py)
- **שאלות בחינה:** [compression.md](../exam_questions/compression.md)
