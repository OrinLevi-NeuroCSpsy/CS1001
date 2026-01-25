# טבלאות גיבוב (Hash Tables) - סיכום לבחינה

---

## מוטיבציה

### הבעיה
רוצים מבנה נתונים שתומך ב:
- הכנסה
- מחיקה
- חיפוש

**בזמן O(1)** (בממוצע)

### פתרונות קיימים וחסרונותיהם

| מבנה | חיפוש | הכנסה | מחיקה |
|------|-------|-------|-------|
| רשימה לא ממוינת | O(n) | O(1) | O(n) |
| רשימה ממוינת | O(log n) | O(n) | O(n) |
| **Hash Table** | **O(1)** | **O(1)** | **O(1)** |

---

## הגדרה פורמלית

**טבלת גיבוב (Hash Table)** היא מבנה נתונים המשתמש ב**פונקציית גיבוב (Hash Function)** כדי למפות מפתחות למיקומים במערך.

```
key → hash(key) → index → value
```

---

## הסבר אינטואיטיבי

דמיינו **ארון עם מגירות ממוספרות**:
- כל פריט מקבל מספר מגירה לפי "נוסחה" (פונקציית hash)
- כשרוצים למצוא פריט, מחשבים את המספר וניגשים ישירות למגירה
- לא צריך לחפש בכל המגירות!

```
מפתח "דני" → hash("דני") = 3 → מגירה 3 → הערך
```

---

## פונקציית Hash

### הגדרה
פונקציה שממירה קלט בגודל שרירותי למספר שלם בטווח קבוע.

```python
def simple_hash(key, table_size):
    return some_calculation(key) % table_size
```

### דרישות מפונקציית hash טובה

1. **דטרמיניסטית** - אותו קלט תמיד נותן אותה תוצאה
2. **פיזור אחיד** - מפזרת את המפתחות באופן שווה
3. **מהירה לחישוב** - O(1) או O(len(key))

### דוגמאות לפונקציות hash

#### Hash למספרים
```python
def hash_int(n, table_size):
    return n % table_size
```

#### Hash למחרוזות
```python
def hash_string(s, table_size):
    total = 0
    for char in s:
        total += ord(char)
    return total % table_size

# דוגמה
hash_string("cat", 10)  # (99+97+116) % 10 = 312 % 10 = 2
```

#### Hash משופר למחרוזות (Polynomial Rolling Hash)
```python
def hash_string_better(s, table_size):
    total = 0
    for i, char in enumerate(s):
        total += ord(char) * (31 ** i)
    return total % table_size
```

### פונקציית hash בפייתון
```python
hash("hello")     # מספר שלם (משתנה בין הרצות)
hash(42)          # 42
hash((1, 2, 3))   # מספר שלם

hash([1, 2, 3])   # TypeError! רשימה לא hashable
```

---

## התנגשויות (Collisions)

### מהי התנגשות?
כאשר שני מפתחות שונים מקבלים אותו אינדקס:
```
hash("cat") = 5
hash("dog") = 5   ← התנגשות!
```

### למה זה בלתי נמנע?
- יש אינסוף מפתחות אפשריים
- יש מספר סופי של תאים בטבלה
- לפי **עקרון שובך היונים** - בהכרח יהיו התנגשויות

---

## שיטות לטיפול בהתנגשויות

### שיטה 1: שרשור (Chaining)

כל תא בטבלה מכיל **רשימה** של כל הזוגות שנופלים לאותו אינדקס.

```
אינדקס 0: []
אינדקס 1: [("cat", 5)]
אינדקס 2: [("dog", 3), ("rat", 7)]  ← שני איברים באותו תא
אינדקס 3: []
אינדקס 4: [("bird", 2)]
```

#### מימוש
```python
class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        # בדוק אם המפתח כבר קיים
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)  # עדכון
                return
        self.table[idx].append((key, value))  # הוספה

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        raise KeyError(key)

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                return
        raise KeyError(key)
```

#### סיבוכיות Chaining

| פעולה | ממוצע | גרוע |
|-------|-------|------|
| חיפוש | O(1 + α) | O(n) |
| הכנסה | O(1) | O(n) |
| מחיקה | O(1 + α) | O(n) |

כאשר **α = n/m** (Load Factor) = מספר איברים / גודל טבלה

---

### שיטה 2: כתובת פתוחה (Open Addressing)

אם התא תפוס, מחפשים תא פנוי אחר **בתוך הטבלה עצמה**.

#### Linear Probing
אם תא i תפוס, ננסה i+1, i+2, i+3, ...

```python
def insert_linear_probing(table, key, value):
    idx = hash(key) % len(table)
    original_idx = idx

    while table[idx] is not None:
        if table[idx][0] == key:  # עדכון
            table[idx] = (key, value)
            return
        idx = (idx + 1) % len(table)
        if idx == original_idx:
            raise Exception("Table is full!")

    table[idx] = (key, value)
```

#### בעיית Clustering
ב-Linear Probing, איברים נוטים להתקבץ ברצפים ארוכים:
```
[None, X, X, X, X, X, None, None, X, X]
       ↑_____________↑
        cluster ארוך → חיפוש איטי
```

#### Quadratic Probing
במקום i+1, i+2, i+3... ננסה i+1², i+2², i+3²...
```
idx, idx+1, idx+4, idx+9, idx+16, ...
```
מפחית clustering אבל לא פותר לגמרי.

#### Double Hashing
משתמשים בפונקציית hash שנייה לקביעת גודל הקפיצה:
```
idx, idx+h2(key), idx+2*h2(key), ...
```

---

## Load Factor (מקדם עומס)

### הגדרה
```
α = n / m
```
- n = מספר איברים בטבלה
- m = גודל הטבלה

### משמעות
- α < 1: יש תאים ריקים
- α = 1: הטבלה מלאה (ב-Open Addressing)
- α > 1: אפשרי רק ב-Chaining

### המלצות
- **Chaining:** לשמור α ≤ 1
- **Open Addressing:** לשמור α ≤ 0.7

### Rehashing
כשה-Load Factor גבוה מדי:
1. יוצרים טבלה חדשה גדולה יותר (בד"כ פי 2)
2. מכניסים מחדש את כל האיברים
3. סיבוכיות: O(n), אבל קורה לעיתים רחוקות

---

## Hash Tables בפייתון

### dict
```python
d = {"a": 1, "b": 2}  # Hash table מאחורי הקלעים
d["c"] = 3            # O(1) בממוצע
```

### set
```python
s = {1, 2, 3}         # גם מבוסס Hash table
2 in s                # O(1) בממוצע
```

### מה Hashable בפייתון?

| טיפוס | Hashable? | סיבה |
|-------|-----------|------|
| int | ✅ | Immutable |
| float | ✅ | Immutable |
| str | ✅ | Immutable |
| tuple | ✅* | Immutable (*אם כל האיברים hashable) |
| frozenset | ✅ | Immutable |
| list | ❌ | Mutable |
| dict | ❌ | Mutable |
| set | ❌ | Mutable |

---

## השוואה: Chaining vs Open Addressing

| קריטריון | Chaining | Open Addressing |
|----------|----------|-----------------|
| מימוש | פשוט יותר | מורכב יותר |
| זיכרון נוסף | כן (לרשימות) | לא |
| Load Factor | יכול להיות > 1 | חייב להיות < 1 |
| מחיקה | פשוטה | מסובכת (tombstones) |
| Cache | פחות יעיל | יותר יעיל |
| Clustering | אין | יש (בעיקר ב-Linear) |

---

## Cuckoo Hashing (מתקדם)

### רעיון
- שתי פונקציות hash, שתי טבלאות
- לכל מפתח יש בדיוק **שני מיקומים אפשריים**
- חיפוש: O(1) **במקרה הגרוע** (לא רק ממוצע!)

### איך זה עובד?
1. חשב h1(key) ו-h2(key)
2. אם אחד מהם פנוי - שים שם
3. אם שניהם תפוסים - "בעט" את אחד המפתחות למיקום השני שלו
4. חזור על התהליך (כמו ציפור קוקייה שמבעיטה ביצים)

```
הכנסת X:
T1[h1(X)] תפוס על ידי Y → בעט את Y
T2[h2(Y)] תפוס על ידי Z → בעט את Z
T1[h1(Z)] פנוי → שים את Z שם
```

---

## טעויות נפוצות

### טעות 1: חשיבה ש-O(1) תמיד מובטח
```python
# במקרה הגרוע (כל המפתחות באותו תא) → O(n)
```

### טעות 2: שימוש ב-Mutable כמפתח
```python
d = {}
d[[1, 2]] = "value"  # TypeError!
```

### טעות 3: הנחה שסדר ה-hash קבוע
```python
# hash("hello") יכול להחזיר ערכים שונים בהרצות שונות
# (מ-Python 3.3+ יש רנדומיזציה)
```

### טעות 4: שכחה לטפל ב-Rehashing
```python
# אם הטבלה מתמלאת ולא עושים rehash → ביצועים מתדרדרים
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: חישוב אינדקס
טבלת hash בגודל 7. פונקציית hash: `h(k) = k % 7`

הכנס את המפתחות: 14, 21, 8, 15, 4

**פתרון:**
```
14 % 7 = 0 → table[0] = 14
21 % 7 = 0 → התנגשות! (עם 14)
8 % 7 = 1  → table[1] = 8
15 % 7 = 1 → התנגשות! (עם 8)
4 % 7 = 4  → table[4] = 4
```

עם Chaining:
```
[0]: [14, 21]
[1]: [8, 15]
[2]: []
[3]: []
[4]: [4]
[5]: []
[6]: []
```

---

### שאלה 2: Linear Probing
טבלה בגודל 5, h(k) = k % 5

הכנס: 3, 8, 13, 18

**פתרון:**
```
3 % 5 = 3  → table[3] = 3
8 % 5 = 3  → תפוס, נסה 4 → table[4] = 8
13 % 5 = 3 → תפוס, נסה 4 → תפוס, נסה 0 → table[0] = 13
18 % 5 = 3 → תפוס, 4 תפוס, 0 תפוס, נסה 1 → table[1] = 18

מצב סופי: [13, 18, _, 3, 8]
```

---

### שאלה 3: מהו Load Factor?
טבלה בגודל 20 עם 15 איברים.

**תשובה:** α = 15/20 = 0.75

---

### שאלה 4: למה רשימה לא יכולה להיות מפתח במילון?

**תשובה:** רשימה היא Mutable. אם היא תשתנה אחרי ההכנסה, ה-hash שלה ישתנה והמפתח "יאבד" בטבלה.

---

## סיכום נקודות חשובות

- [ ] Hash table = מערך + פונקציית hash
- [ ] פונקציית hash: ממירה מפתח לאינדקס
- [ ] התנגשות: שני מפתחות → אותו אינדקס
- [ ] פתרונות: **Chaining** (רשימות) או **Open Addressing** (חיפוש תא פנוי)
- [ ] Load Factor α = n/m, לשמור נמוך
- [ ] סיבוכיות ממוצעת: **O(1)**, גרועה: O(n)
- [ ] בפייתון: `dict` ו-`set` מבוססים על hash tables
- [ ] רק **Immutable** יכול להיות מפתח/איבר

---

## קישורים נוספים

- **קוד:** [hash_tables_demo.py](../code/hash_tables_demo.py)
- **שאלות בחינה:** [data_structures.md](../exam_questions/data_structures.md)
