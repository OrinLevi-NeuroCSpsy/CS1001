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

## קישורים לסיכומים

- [עיבוד תמונות](../notes/image_processing.md)
- [פונקציות מסדר גבוה](../notes/higher_order_functions.md)
- [טריקים לבחינה](../notes/exam_tricks.md)
