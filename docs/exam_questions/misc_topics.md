# שאלות מבחן - נושאים נוספים

---

## PageRank (2023a, 2023b)

### שאלה 1: ניתוח PageRank (2023a מועד א', שאלה 1ג')

```python
def PageRank(G, t, p):
    curr = 0
    n = len(G)
    counters = [0 for i in range(n)]
    for step in range(t):
        if random.random() < p and len(G[curr]) > 0:
            curr = random.choice(G[curr])
        else:
            curr = random.randrange(n)
        counters[curr] += 1
    return counters  # שינוי מהמקור
```

**טריקים:**
- `random.random() < p` - הסתברות p ללכת לפי קשתות
- `random.randrange(n)` - קפיצה אקראית
- צמתים ללא קשתות יוצאות תמיד גורמים לקפיצה

---

## עיבוד תמונות

### שאלה 2: חציון מקומי (2023a מועד א', שאלה 1ו')

```python
def local_medians(img, kx=1, ky=1):
    median = lambda lst: sorted(lst)[len(lst)//2]
    return local_op(img, median, kx, ky)
```

**טריק חשוב:**
- החציון נבחר מהרשימה הממוינת במיקום `len//2`
- עבור סביבה 3×3: 9 פיקסלים, מיקום 4 (האמצעי)
- בקצוות - סביבה קטנה יותר!

---

## דקדוקים חסרי הקשר

### שאלה 3: זיהוי שפת דקדוק (2022b מועד א', שאלה 1ב')

**נתון:**
```
S → 1S | 0A | ε
A → 1A | 0S
```

**שאלה:** מהי שפת הדקדוק?

**תשובה:** כל המחרוזות מעל {0,1} עם מספר זוגי של אפסים.

**איך לפתור:**
1. עקוב אחר המשתנים
2. S = מספר זוגי של 0
3. A = מספר אי-זוגי של 0

---

## מיון עם פונקציית סידור מקורבת (2023a שאלה 3)

### שאלה 4: מיון עם q(L,i) שטועה לכל היותר ב-1

```python
def sort_with_q(L, q):
    n = len(L)
    result = [None] * n
    for i in range(n):
        result[q(L, i)] = L[i]

    for i in range(n - 3):
        result[i:i+4] = sorted(result[i:i+4])

    return result
```

**סיבוכיות:** Θ(n) - כי מיון 4 איברים הוא O(1)

---

## נקודות קולינאריות (2022b שאלה 3)

### שאלה 5: מציאת מספר מקסימלי של נקודות על קו ישר

```python
def collinear_point(L, p):
    slopes = {}
    for q in L:
        if q != p and q[0] != p[0]:
            s = slope(p, q)
            slopes[s] = slopes.get(s, 0) + 1
    return max(slopes.values()) + 1 if slopes else 1

collinear = lambda L: max(collinear_point(L, p) for p in L)
```

**סיבוכיות:**
- `collinear_point`: O(n) ממוצע (hash)
- `collinear`: O(n²) ממוצע

**שיפור למקרה גרוע:** מיון לפי שיפוע → O(n² log n)

---

## שאלה 6: ייצוג נקודה צפה (2024a מועד א', שאלה 1ג')

**נתון:** ייצוג floating-point עם:
- 1 ביט סימן
- 4 ביטים מנטיסה
- 3 ביטים מעריך (excess-3)

**שאלה:** מהו הייצוג של המספר 5.5?

**פתרון:**
1. 5.5 בבינארי = 101.1
2. נרמול: 1.011 × 2²
3. מנטיסה (אחרי הנקודה): 0110
4. מעריך: 2 + 3 = 5 → 101
5. סימן: 0 (חיובי)

**תשובה:** 0 101 0110

---

## שאלה 7: Aliasing ורשימות (2024a מועד ב', שאלה 1ה')

```python
>>> a = [1, 2, 3]
>>> b = a
>>> c = a[:]
>>> a[0] = 10
>>> a.append(4)
>>> print(a, b, c)
```

**תשובה:** `[10, 2, 3, 4] [10, 2, 3, 4] [1, 2, 3]`

**הסבר:**
- `b = a` - aliasing, b ו-a מצביעים לאותו אובייקט
- `c = a[:]` - shallow copy, c הוא אובייקט חדש
- שינויים ב-a משפיעים על b אבל לא על c

---

## שאלה 8: PageRank משופר (2025a מועד א', שאלה 1ד')

```python
def PageRank_new(G, t, p):
    n = len(G)
    curr = 0
    counters = [0] * n
    for step in range(t):
        counters[curr] += 1  # שינוי: סופרים לפני המעבר
        if random.random() < p and len(G[curr]) > 0:
            curr = random.choice(G[curr])
        else:
            curr = random.randrange(n)
    return counters
```

**שאלה:** מה ההבדל בין הגרסה החדשה לישנה?

**תשובה:** בגרסה החדשה סופרים את הצומת לפני המעבר, בישנה אחרי.

**השלכה:** הצומת ההתחלתי (0) תמיד ייספר בגרסה החדשה.

---

## שאלה 9: מחלקת Word Similarity (2024a מועד א', שאלה 4)

```python
class WordSimilarity:
    def __init__(self, filename):
        self.words = {}
        with open(filename) as f:
            for line in f:
                parts = line.strip().split()
                word = parts[0]
                vector = [float(x) for x in parts[1:]]
                self.words[word] = vector

    def similarity(self, word1, word2):
        if word1 not in self.words or word2 not in self.words:
            return None
        v1 = self.words[word1]
        v2 = self.words[word2]
        return sum(a*b for a, b in zip(v1, v2))

    def most_similar(self, word, k):
        if word not in self.words:
            return []
        scores = []
        for other in self.words:
            if other != word:
                sim = self.similarity(word, other)
                scores.append((sim, other))
        scores.sort(reverse=True)
        return [w for _, w in scores[:k]]
```

**הסבר:**
- דמיון בין מילים מחושב לפי מכפלה סקלרית של וקטורים
- `most_similar` מחזיר k מילים הכי דומות

---

## שאלה 10: ייצוג שברים מדויק (2025a מועד א', שאלה 1ה')

**שאלה:** אילו מהמספרים הבאים ניתן לייצג **בדיוק** ב-floating point (בסיס 2)?

| מספר | ניתן לייצג? |
|------|-------------|
| 0.5 | כן (= 2⁻¹) |
| 0.25 | כן (= 2⁻²) |
| 0.1 | לא (שבר אינסופי בבינארי) |
| 0.75 | כן (= 2⁻¹ + 2⁻²) |
| 0.3 | לא (שבר אינסופי בבינארי) |

**כלל:** מספר ניתן לייצג בדיוק אם ורק אם הוא סכום של חזקות שליליות של 2.

---

## שאלה 11: ContextPageRank (2024b מועד ב', שאלה 3)

**שינוי מ-PageRank רגיל:** בסיכוי p קופצים לדף c (ה-context), בסיכוי 1-p ממשיכים רגיל.

```python
def ContextPageRank(G, t, c, p):
    curr = c
    n = len(G)
    counters = [0 for i in range(n)]
    for step in range(t):
        if random.random() < p:
            curr = c
        else:
            if len(G[curr]) > 0:
                curr = random.choice(G[curr])
            else:
                curr = random.randrange(n)
        counters[curr] += 1
    return [cnt/t for cnt in counters]
```

**השפעת p:**
- p=0: PageRank רגיל
- p=1: תמיד נשאר ב-c, counters[c] = 1.0

---

## שאלה 12: ייצוג מספרים ותווים (2024b מועד ב', שאלה 1ב')

**טענות:**

| טענה | נכון? |
|------|-------|
| ניתן לייצג כל ממשי בין 0-1 ב-128 ביטים | **לא** - אין-סוף ממשיים |
| f(n) = כמות מספרים ב-n ספרות בסיס 4, g(n) = כמות ב-n ביטים. f(n)=2·g(n) | **לא** - f(n)=4ⁿ, g(n)=2ⁿ, f(n)=g(n)² |
| Fixed-length הוא תמיד prefix-free | **נכון** |
| בייצוג בינארי, זוגיות סכום הביטים = זוגיות המספר | **לא נכון** |
| ב-floating point יש מספר ייצוגים לכל ממשי | **לא נכון** - ייצוג יחיד |

---

## שאלה 13: המרת בסיסים (2024b מועד א', שאלה 1א')

**פונקציה:** convert_base(n, b) - ממירה n לבסיס b

**טענות:**

| ביטוי | תשובה |
|-------|--------|
| len(convert_base(n,b)) > len(convert_base(n,b-1)) | לא ניתן לקבוע |
| len(convert_base(n,b)) < len(convert_base(n,b-2)) | לא ניתן לקבוע |
| len(convert_base(n,b)) < len(convert_base(n,b//2)) | **False** - בסיס קטן יותר = ייצוג ארוך יותר |
| 1+len(convert_base(n,b)) == len(convert_base(2*n,b)) | לא ניתן לקבוע |

---

## שאלה 14: My_floating_point (2025a מועד ב', שאלה 1ג')

**ייצוג חדש - 8 ביטים:**
- 1 ביט sign
- 3 ביטים exponent
- 4 ביטים fraction

**נוסחה:** `(-1)^sign × 2^exponent × (1 + fraction)`

**דוגמה:** 01001000
- sign = 0 (חיובי)
- exponent = 100 = 4
- fraction = 1000 → 0.5 (הביט הראשון = 2⁻¹)
- ערך = 1 × 2⁴ × (1 + 0.5) = 16 × 1.5 = **24**

**הכפלה ב-2:** מוסיפים 1 ל-exponent → 01011000

**מרווח בין מספרים עוקבים:** לexponent נתון e, המרווח הוא 2^(e-4) (כי ה-fraction הקטן ביותר הוא 2⁻⁴)

---

## שאלה 15: Closures ו-Aliasing (2025b מועד א', שאלה 1ב')

```python
def f(L):
    def g(x):
        return L[0] == x
    return g

L1 = [1,2,3,4,5,6,7]
my_g = f(L1)
L1[0] = 100
print(my_g(1))  # ?

L2 = [1,2,3,4]
my_g = f(L2)
L2 = []
print(my_g(1))  # ?
```

**תשובות:**
1. **False** - כי L1[0] שונה ל-100, ו-g עדיין מצביעה לאותה רשימה
2. **True** - כי L2 = [] יוצר רשימה חדשה, אבל g מצביעה לרשימה המקורית [1,2,3,4]

**טריק:** Closure שומרת reference לאובייקט, לא עותק!

---

## שאלה 16: דקדוק חסר הקשר (2025b מועד א', שאלה 1ד')

**דקדוק:**
```
S → A B S | c C | c
A → a A | a
B → b B | b
C → c C | c
```

| מחרוזת | ניתן לגזור? |
|--------|-------------|
| ε | **לא** - אין כלל S → ε |
| aaabbbc | **כן** - S → ABS → aABS → aaBS → aabBS → aabbS → aabbcC → aabbbc |
| ab | **לא** - A חייב להסתיים ב-a, וB חייב להתחיל ב-b, אבל צריך S בסוף |
| abaabbcc | **לא** |
| abcaabbcc | **כן** |

---

## שאלה 17: פרוטוקול דיפי-הלמן משונה (2025b מועד א', שאלה 1ו')

**פרוטוקול:**
1. אליס מגרילה p ראשוני, g, h, a ומחשבת x = g^a × h mod(p)
2. אליס שולחת x, g, h, p לבוב
3. בוב מגריל b ומחשב y = g^b × h mod(p)
4. בוב שולח y לאליס
5. אליס מחשבת: k_A = (g^h)^a × (y × h)^h mod(p)
6. בוב מחשב: k_B = (g^h)^b × (x × h)^h mod(p)

**טענות:**

| טענה | נכון? |
|------|-------|
| החישוב בסיבוכיות פולינומית ב-t | **נכון** - ריבוע וכפל מודולרי |
| k_A = k_B תמיד | **לא נכון** - החישובים לא סימטריים |
| מאזין לא יכול לחשב k_A בזמן פולינומי | **לא נכון** - h ציבורי, אז אפשר לחשב |

---

## שאלה 18: טענות סיבוכיות (2025b מועד א', שאלה 1ג')

| טענה | נכון? |
|------|-------|
| 1² + 2² + ... + n² = O(n^3.5) | **מתקיימת** - כי Σi² = n(n+1)(2n+1)/6 = Θ(n³) |
| 9^(n·log₃n) = Θ(n^2n) | **מתקיימת** - כי 9^(n·log₃n) = (3²)^(n·log₃n) = 3^(2n·log₃n) = n^2n |
| n^(log₂n) = O(n^(log₃n)) | **לא מתקיימת** - כי log₂n > log₃n |

---

## שאלה 19: Aliasing עם רשימות מקוננות (2025b מועד א', שאלה 5 - בונוס)

```python
def func(a, b):
    a[0][1] = 99
    b = b[:]
    b[1] = [0]
    a = b
    return a

x = [[1, 2], [3, 4]]
y = x
z = func(x, y)
print(x)  # ?
print(y)  # ?
print(z)  # ?
```

**תשובות:**
- x: **[[1, 99], [3, 4]]** - כי a[0][1] = 99 משנה את הרשימה המקורית
- y: **[[1, 99], [3, 4]]** - y מצביע לאותו אובייקט כמו x
- z: **[[1, 99], [0]]** - כי z = b (לאחר השינויים)

---

## שאלה 20: find_peak עם באגים (2025b מועד ב', שאלה 1א')

**בעיה:** מציאת האיבר המקסימלי ברשימה "עולה-יורדת".

```python
def find_peak(lst):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < lst[mid + 1]:
            low = mid  # באג! צריך low = mid + 1
        else:
            high = mid - 1
    return low
```

**בדיקת קלטים:**

| קריאה | תוצאה |
|-------|-------|
| L = [1,3,2], find_peak(L) | **לולאה אינסופית** - low=0, mid=0, low=mid=0... |
| L = [1], find_peak(L) | **שגיאת זמן ריצה** - lst[mid+1] מחוץ לתחום |
| L = [1,2], find_peak(L) | **שגיאת זמן ריצה** - lst[mid+1] מחוץ לתחום |
| L = [2,1], find_peak(L) | **יוחזר הפלט הנכון** - 0 |

**תיקון הבאג:** `low = mid + 1` במקום `low = mid`

---

## שאלה 21: new_gcd - ניתוח התנהגות (2025b מועד ב', שאלה 1ו')

```python
def modulo(a, b):
    return a - b*(a//b)

def new_gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = modulo(a, b), modulo(b, modulo(a, b))
    return a
```

**ניתוח:**
בשורה `a, b = modulo(a, b), modulo(b, modulo(a, b))`:
- a_new = a % b
- b_new = b % (a % b)

**הבעיה:** b_new יכול להיות 0 כאשר b מתחלק ב-(a % b), מה שיגרום ללולאה להסתיים מוקדם מדי.

**תשובה נכונה:** קיימים זוגות (a,b) עבורם new_gcd **תחזיר מספר שאינו** המחלק המשותף המקסימלי.

**דוגמה:** new_gcd(6, 4):
- a=6, b=4
- a_new = 6 % 4 = 2
- b_new = 4 % 2 = 0
- מחזיר 2 - שזה נכון!

אבל new_gcd(8, 6):
- a=8, b=6
- a_new = 8 % 6 = 2
- b_new = 6 % 2 = 0
- מחזיר 2 - שזה נכון!

צריך לבדוק יותר דוגמאות...

---

## שאלה 22: CFG - פונקציית what (2025b מועד ב', שאלה 4)

**הפונקציה:** מייצרת את כל המילים באורך n הניתנות לגזירה מדקדוק CNF.

```python
def what(n, rules, start_var):
    vrs = list(rules.keys())
    dct = {}
    for V in vrs:
        dct[V] = {}
        dct[V][1] = [ch for ch in rules[V] if len(ch) == 1]

    for lngth in range(2, n + 1):
        for V in vrs:
            dct[V][lngth] = []
            for var_rule in rules[V]:
                if len(var_rule) == 2:
                    X, Y = var_rule[0], var_rule[1]
                    for ln_1 in range(1, lngth):
                        ln_2 = lngth - ln_1
                        for w1 in dct[X][ln_1]:
                            for w2 in dct[Y][ln_2]:
                                w = w1 + w2
                                if w not in dct[V][lngth]:
                                    dct[V][lngth].append(w)
    return sorted(dct[start_var][n])
```

**דוגמה 1:**
```python
rules = {"S":{"AB"}, "A":{"BC", "AA"}, "B":{"1"}, "C":{"0"}}
print(what(5, rules, "S"))
```
**תשובה:** `['11010', '11100']`

**דוגמה 2:**
```python
rules = {"S":{"AB", "BA"}, "A":{"AA", "0"}, "B":{"BB", "1"}}
print(what(3, rules, "S"))
```
**תשובה:** `['001', '010', '011', '100', '101', '110']`

**ניתוח סיבוכיות:**

| דקדוק | סיבוכיות |
|-------|----------|
| rules = {"S":{"AA", "0"}, "A":{"SS", "AA", "0"}} | **אקספוננציאלית** |
| rules = {"S":{"SS", "0", "1"}} | **אקספוננציאלית** |
| rules = {"S":{"0"}} | **פולינומית** - רק מילה אחת לכל אורך |
| rules = {"S":{"AA","BA","AB","BB"}, "A":{"SS","a"}, "B":{"SS","b"}} | **אקספוננציאלית** |

---

## שאלה 23: ספירת מחרוזות sparse (2025b מועד ב', שאלה 4ג')

**הגדרה:** מחרוזת sparse - אחרי כל 1 חייב לבוא 0.

**דוגמאות:**
- sparse: 010010, 00000, 101010
- לא sparse: 01, 0001100 (יש 11)

```python
def cnt_string(m):
    rules = {"S":{"SS", "0", "T"}, "T":{"10"}}
    summ = 0
    for i in range(1, m + 1):
        summ += len(what(i, rules, "S"))
    return summ
```

**הסבר:**
- S → SS (שרשור שני sparse)
- S → 0 (מחרוזת של אפס בודד)
- S → T (הכנסת 10)
- T → 10 (זוג 10)

---

## קישורים לסיכומים

- [עיבוד תמונות](../notes/image_processing.md)
- [פונקציות מסדר גבוה](../notes/higher_order_functions.md)
- [טריקים לבחינה](../notes/exam_tricks.md)
