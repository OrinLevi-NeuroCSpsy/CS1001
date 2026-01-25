# קריאה וכתיבה לקבצים (File I/O) - סיכום לבחינה

---

## מושגי יסוד

### מהו קובץ?
אוסף נתונים המאוחסן בזיכרון הקבוע (דיסק).

### סוגי קבצים
| סוג | תיאור | דוגמאות |
|-----|-------|---------|
| **טקסט** | תווים קריאים | `.txt`, `.py`, `.csv` |
| **בינארי** | בתים גולמיים | `.jpg`, `.exe`, `.bin` |

---

## פתיחת קובץ: open()

### תחביר
```python
file = open(filename, mode, encoding='utf-8')
```

### מצבי פתיחה (Modes)

| Mode | משמעות | הסבר |
|------|--------|------|
| `'r'` | Read | קריאה (ברירת מחדל). שגיאה אם הקובץ לא קיים |
| `'w'` | Write | כתיבה. **מוחק תוכן קיים!** יוצר אם לא קיים |
| `'a'` | Append | הוספה לסוף. יוצר אם לא קיים |
| `'r+'` | Read+Write | קריאה וכתיבה. הקובץ חייב להיות קיים |
| `'w+'` | Write+Read | כתיבה וקריאה. מוחק תוכן קיים |
| `'rb'` | Read Binary | קריאה בינארית |
| `'wb'` | Write Binary | כתיבה בינארית |

### דוגמה בסיסית

```python
# פתיחה
f = open('example.txt', 'r', encoding='utf-8')

# עבודה עם הקובץ
content = f.read()

# סגירה (חובה!)
f.close()
```

---

## הדרך הנכונה: with (Context Manager)

### למה with?
- **סוגר אוטומטית** את הקובץ
- גם אם יש שגיאה באמצע
- קוד בטוח ונקי יותר

### תחביר

```python
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# הקובץ נסגר אוטומטית כאן
```

### השוואה

```python
# בלי with - צריך לזכור לסגור
f = open('file.txt', 'r')
try:
    content = f.read()
finally:
    f.close()

# עם with - פשוט ובטוח
with open('file.txt', 'r') as f:
    content = f.read()
```

---

## קריאה מקובץ

### read() - כל התוכן

```python
with open('example.txt', 'r') as f:
    content = f.read()      # מחרוזת אחת עם כל התוכן
    print(content)
```

### read(n) - n תווים

```python
with open('example.txt', 'r') as f:
    chunk = f.read(10)      # 10 תווים ראשונים
    rest = f.read()         # השאר
```

### readline() - שורה אחת

```python
with open('example.txt', 'r') as f:
    line1 = f.readline()    # שורה ראשונה (כולל \n)
    line2 = f.readline()    # שורה שנייה
```

### readlines() - רשימת שורות

```python
with open('example.txt', 'r') as f:
    lines = f.readlines()   # ['line1\n', 'line2\n', 'line3\n']
```

### לולאה על שורות (מומלץ!)

```python
with open('example.txt', 'r') as f:
    for line in f:          # יעיל בזיכרון!
        print(line.strip()) # strip מסיר \n
```

### השוואת שיטות קריאה

| שיטה | מתי להשתמש | זיכרון |
|------|------------|--------|
| `read()` | קבצים קטנים, צריך הכל | טוען הכל |
| `readline()` | שורה אחת בכל פעם | חסכוני |
| `readlines()` | רשימת שורות, עיבוד לא סדרתי | טוען הכל |
| `for line in f` | קבצים גדולים | הכי חסכוני |

---

## כתיבה לקובץ

### write() - כתיבת מחרוזת

```python
with open('output.txt', 'w') as f:
    f.write('Hello World\n')
    f.write('Second line\n')
```

**שים לב:** `write()` לא מוסיף `\n` אוטומטית!

### writelines() - כתיבת רשימה

```python
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as f:
    f.writelines(lines)
```

### print() לקובץ

```python
with open('output.txt', 'w') as f:
    print('Hello', file=f)      # מוסיף \n אוטומטית
    print('World', file=f)
```

---

## הוספה לקובץ (Append)

```python
with open('log.txt', 'a') as f:
    f.write('New log entry\n')
# לא מוחק תוכן קיים!
```

---

## דוגמאות שימושיות

### העתקת קובץ

```python
with open('source.txt', 'r') as src:
    with open('dest.txt', 'w') as dst:
        for line in src:
            dst.write(line)

# או בקיצור:
with open('source.txt', 'r') as src, open('dest.txt', 'w') as dst:
    dst.write(src.read())
```

### ספירת שורות/מילים/תווים

```python
with open('text.txt', 'r') as f:
    content = f.read()

lines = content.count('\n') + 1
words = len(content.split())
chars = len(content)
```

### חיפוש בקובץ

```python
def find_in_file(filename, search_term):
    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            if search_term in line:
                print(f"Line {line_num}: {line.strip()}")
```

### קריאת קובץ CSV פשוט

```python
with open('data.csv', 'r') as f:
    for line in f:
        values = line.strip().split(',')
        print(values)

# או עם header:
with open('data.csv', 'r') as f:
    header = f.readline().strip().split(',')
    for line in f:
        values = line.strip().split(',')
        row = dict(zip(header, values))
        print(row)
```

### כתיבת CSV פשוט

```python
data = [
    ['Name', 'Age', 'City'],
    ['דני', '25', 'תל אביב'],
    ['רוני', '30', 'חיפה']
]

with open('output.csv', 'w') as f:
    for row in data:
        f.write(','.join(row) + '\n')
```

---

## מיקום בקובץ (File Position)

### tell() - המיקום הנוכחי

```python
with open('example.txt', 'r') as f:
    print(f.tell())     # 0 (התחלה)
    f.read(5)
    print(f.tell())     # 5 (אחרי 5 תווים)
```

### seek() - קפיצה למיקום

```python
with open('example.txt', 'r') as f:
    f.seek(10)          # קפוץ לתו 10
    content = f.read()  # קרא משם

    f.seek(0)           # חזור להתחלה
```

---

## טיפול בשגיאות

### FileNotFoundError

```python
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("הקובץ לא נמצא!")
```

### IOError / PermissionError

```python
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("קובץ לא נמצא")
except PermissionError:
    print("אין הרשאות")
except IOError as e:
    print(f"שגיאת I/O: {e}")
```

### בדיקה אם קובץ קיים

```python
import os

if os.path.exists('file.txt'):
    with open('file.txt', 'r') as f:
        content = f.read()
else:
    print("הקובץ לא קיים")
```

---

## קידוד (Encoding)

### למה חשוב?
תווים לא-אנגליים (עברית!) דורשים קידוד נכון.

```python
# נכון - תומך בעברית
with open('hebrew.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# עלול להיכשל עם עברית
with open('hebrew.txt', 'r') as f:  # ללא encoding מפורש
    content = f.read()  # UnicodeDecodeError אפשרי
```

### קידודים נפוצים

| קידוד | שימוש |
|-------|-------|
| `utf-8` | ברירת מחדל מומלצת, תומך בכל השפות |
| `ascii` | אנגלית בלבד |
| `cp1255` | עברית (Windows ישן) |
| `iso-8859-8` | עברית (תקן ישן) |

---

## טעויות נפוצות

### טעות 1: שכחה לסגור קובץ

```python
# שגוי - הקובץ נשאר פתוח!
f = open('file.txt', 'r')
content = f.read()
# שכחנו f.close()

# נכון - with סוגר אוטומטית
with open('file.txt', 'r') as f:
    content = f.read()
```

### טעות 2: כתיבה עם 'w' מוחקת הכל!

```python
# זהירות! זה מוחק את כל התוכן:
with open('important.txt', 'w') as f:
    f.write('oops')

# אם רוצים להוסיף - השתמש ב-'a':
with open('log.txt', 'a') as f:
    f.write('new entry\n')
```

### טעות 3: שכחת \n בכתיבה

```python
# שגוי - הכל בשורה אחת
with open('file.txt', 'w') as f:
    f.write('Line 1')
    f.write('Line 2')
# התוצאה: "Line 1Line 2"

# נכון
with open('file.txt', 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')
```

### טעות 4: קריאה אחרי שהקובץ נגמר

```python
with open('file.txt', 'r') as f:
    content1 = f.read()     # קורא הכל
    content2 = f.read()     # מחרוזת ריקה! הגענו לסוף

    f.seek(0)               # חזור להתחלה
    content3 = f.read()     # עכשיו שוב יש תוכן
```

### טעות 5: for על readline

```python
# שגוי - קורא רק שורה אחת כל פעם
with open('file.txt', 'r') as f:
    for char in f.readline():  # לולאה על תווי השורה!
        print(char)

# נכון - לולאה על שורות
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: מה יהיה בקובץ?

```python
with open('test.txt', 'w') as f:
    f.write('A')
    f.write('B')
    f.write('C')
```

**תשובה:** `ABC` (הכל בשורה אחת, בלי רווחים)

---

### שאלה 2: מה יודפס?

```python
# תוכן test.txt: "Hello\nWorld\n"

with open('test.txt', 'r') as f:
    lines = f.readlines()
    print(len(lines))
```

**תשובה:** `2`

---

### שאלה 3: כתוב פונקציה

כתוב פונקציה שסופרת כמה פעמים מילה מופיעה בקובץ.

**פתרון:**
```python
def count_word(filename, word):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += line.lower().split().count(word.lower())
    return count
```

---

### שאלה 4: מה ההבדל?

מה ההבדל בין `'w'` ל-`'a'`?

**תשובה:**
- `'w'` (write) - **מוחק** את כל התוכן הקיים ומתחיל מחדש
- `'a'` (append) - **מוסיף** לסוף הקובץ בלי למחוק

---

### שאלה 5: תקן את הקוד

```python
f = open('data.txt', 'r')
for line in f:
    print(line)
```

**תיקון:**
```python
with open('data.txt', 'r') as f:
    for line in f:
        print(line.strip())  # גם strip כדי להסיר \n כפול
```

---

## סיכום נקודות חשובות

- [ ] **תמיד** להשתמש ב-`with` (סוגר אוטומטית)
- [ ] `'r'` = קריאה, `'w'` = כתיבה (מוחק!), `'a'` = הוספה
- [ ] לולאת `for line in f` - הכי יעיל לקבצים גדולים
- [ ] `write()` לא מוסיף `\n` - צריך להוסיף ידנית
- [ ] תמיד לציין `encoding='utf-8'` לעברית
- [ ] `strip()` מסיר רווחים ו-`\n` מקצוות השורה
- [ ] `readlines()` מחזיר רשימה עם `\n` בכל שורה

---

## קישורים נוספים

- **קוד:** [file_io_demo.py](../code/file_io_demo.py)
