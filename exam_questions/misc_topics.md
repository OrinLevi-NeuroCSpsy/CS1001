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

## קישורים לסיכומים

- [עיבוד תמונות](../notes/image_processing.md)
- [פונקציות מסדר גבוה](../notes/higher_order_functions.md)
- [טריקים לבחינה](../notes/exam_tricks.md)
