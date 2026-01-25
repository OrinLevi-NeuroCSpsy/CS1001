# שאלות מבחן - סיבוכיות

---

## שאלה 1: רקורסיה עם חיתוך רשימות (2023b מועד א', שאלה 1ב')

```python
def rec_func1(lst):
    n = len(lst)
    if n <= 1:
        return None
    rec_func1(lst[:n//2])
    rec_func1(lst[n//2:3*n//4])
```

**שאלה:** מהו זמן הריצה כתלות ב-n?

**תשובה:** O(n log n)

**הסבר:**
- חיתוך רשימה `lst[:n//2]` לוקח O(n/2) = O(n)
- יש log(n) רמות ברקורסיה
- בכל רמה עבודה O(n) סה"כ

**טריק חשוב:** חיתוך רשימות בפייתון לוקח O(k) כאשר k הוא אורך החיתוך!

---

## שאלה 2: לולאה עם חזקות של 2 (2023a מועד א', שאלה 1ד')

```python
def f(n):
    val = 1
    p = 1
    for i in range(n):
        if i == p:
            for j in range(i):
                val += 1
            p = p*2
```

**שאלה:** מהו זמן הריצה?

**תשובה:** Θ(n)

**הסבר:** הלולאה הפנימית רצה רק כאשר i הוא חזקה של 2.
סכום: 1 + 2 + 4 + 8 + ... + n/2 < 2n = O(n)

**טריק חשוב:** לולאה פנימית שרצה רק לעתים רחוקות!

---

## שאלה 3: Quicksort - עומק עץ רקורסיה (2022b מועד א', שאלה 1ג')

**נתון:** רשימה L באורך n עם איברים מ-[1, k].

**שאלה:** מהו העומק המקסימלי של עץ הרקורסיה?

**תשובה:** k (או min(n, k))

**הסבר:**
- יש רק k ערכים שונים אפשריים
- בכל רמה לפחות ערך אחד "נגמר"
- לכן לכל היותר k רמות

---

## שאלה 4: סכום עומקים בעץ (2023a מועד א', שאלה 2)

**שאלה:** מהו סכום העומקים המקסימלי/מינימלי בעץ בינארי בן n צמתים?

**מקסימלי (עץ שרשרת):** Θ(n²)
- סכום: 0 + 1 + 2 + ... + (n-1) = n(n-1)/2

**מינימלי (עץ מאוזן):** Θ(n log n)
- כ-n/2 צמתים בעומק log n

---

## שאלה 5: Binary Search משופר (2025a מועד א', שאלה 1א')

```python
def binary_search_new(lst, key):
    n = len(lst)
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right)//2
        if key == lst[mid]:
            while mid+1 < len(lst) and lst[mid+1] == key:
                mid += 1
            return mid
        elif key < lst[mid]:
            right = mid-1
        else:
            left = mid+1
    return None
```

**שאלה א:** עבור lst = [1,3,5,5,5,5,6,7], key = 5, מה יוחזר?

**תשובה:** 5 (האינדקס של ה-5 האחרון ברצף)

**שאלה ב:** מהי סיבוכיות הזמן במקרה הגרוע?

**תשובה:** O(n)

**הסבר:** במקרה הגרוע כל האיברים זהים ל-key, אז לולאת ה-while הפנימית עוברת על כל הרשימה.

---

## שאלה 6: ניתוח לולאות (2024a מועד ב', שאלה 1א')

```python
def f(L):
    n = len(L)
    res = []
    for i in range(n-500, n):
        m = math.floor(math.log2(i))
        for j in range(m):
            k = 1
            while k<n:
                k*=2
                res.append(k)
    return res
```

**שאלה:** מהו זמן הריצה כתלות ב-n?

**תשובה:** O(log²n)

**הסבר:**
- לולאה חיצונית: 500 איטרציות (קבוע)
- לולאה אמצעית: O(log n) איטרציות
- לולאה פנימית: O(log n) איטרציות
- סה"כ: O(500 · log n · log n) = O(log²n)

---

## שאלה 7: Quicksort עם שינוי (2024a מועד א', שאלה 1א')

```python
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        smaller = [elem for elem in lst[1:] if elem < pivot]
        equal = [elem for elem in lst[1:] if elem == pivot]
        greater = [elem for elem in lst[1:] if elem > pivot]
        return quicksort(smaller) + equal + quicksort(greater)
```

**שאלה:** מה הפלט של quicksort([1,2,3,4])? מה הסיבוכיות במקרה הגרוע?

**תשובה:**
- פלט: [1,2,3,4] (ממוין נכון)
- סיבוכיות: O(n²) - כי השתמשו ב-lst[1:] שמבטיח pivot לא נכלל פעמיים

**הערה:** ההבדל מהגרסה המקורית - lst[1:] במקום lst

---

## שאלה 8: Quicksort עם ערכים מוגבלים (2024b מועד א', שאלה 1ג')

```python
def det_qs(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        smaller = [elem for elem in lst if elem < pivot]
        equal = [elem for elem in lst if elem == pivot]
        greater = [elem for elem in lst if elem > pivot]
        return det_qs(smaller) + equal + det_qs(greater)
```

**שאלה:** מהי סיבוכיות הזמן במקרה הגרוע עבור רשימה באורך n עם איברים בין 0 ל-1000?

**תשובה:** O(n)

**הסבר:** יש רק 1001 ערכים שונים אפשריים. בכל רמה של הרקורסיה, לפחות ערך אחד "נגמר" (עובר ל-equal). לכן יש לכל היותר 1001 רמות, ובכל רמה העבודה היא O(n).

---

## שאלה 9: ניתוח לולאות מורכבות (2024b מועד ב', שאלה 1ה')

```python
def f(L):
    n = len(L)
    res = []
    for i in range(50, n):
        m = math.floor(math.log(i, 3))  # log base 3
        for j in range(m):
            k = 1
            while k < n:
                k *= 3
                res.append(k)
    return res
```

**שאלה:** מהי סיבוכיות הזמן כתלות ב-n?

**תשובה:** Θ(n·log²n)

**הסבר:**
- לולאה חיצונית: O(n) איטרציות
- לולאה אמצעית: O(log₃n) = O(log n) איטרציות
- לולאה פנימית: O(log₃n) = O(log n) איטרציות
- סה"כ: O(n · log n · log n) = O(n·log²n)

---

## שאלה 10: my_quicksort עם min כציר (2024b מועד ב', שאלה 1ד')

```python
def my_quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = min(lst)
        smaller = [elem for elem in lst if elem <= pivot]
        greater = [elem for elem in lst if elem > pivot]
        return my_quicksort(smaller) + my_quicksort(greater)
```

**טענות:**

| טענה | נכונה? |
|------|--------|
| קיימות רשימות לא-ריקות שהקוד לא יסיים לרוץ | **נכון** - רשימה עם כפילויות כמו [1,1] תגרום ללולאה אינסופית |
| קיימות רשימות שהקוד יסיים אבל יחזיר רשימה לא ממוינת | **לא נכון** |
| עבור רשימה עם כל המספרים 1 עד k, הפונקציה תחזיר רשימה ממוינת | **נכון** |
| עבור רשימה באורך k+1 עם ערכים 1 עד k, הפונקציה תחזיר רשימה ממוינת | **לא נכון** - יש כפילות |

---

## שאלה 11: Quicksort על רשימות שונות (2025a מועד ב', שאלה 1ב')

**נתונות שלוש רשימות:**
```python
lst1 = [(100*i) + random.randint(0, 10) for i in range(n)]
lst2 = [(i + random.randint(0, n)) % n for i in range(n)]
lst3 = generate_sequence(0, n)

def generate_sequence(min_val, max_val):
    if max_val - min_val <= 1:
        return []
    val = (min_val + max_val)//2
    left = generate_sequence(val, max_val)
    right = generate_sequence(min_val, val)
    return [val] + left + right
```

**סיבוכיות עבור כל רשימה:**

| רשימה | rnd_qs (אקראי) | det_qs (דטרמיניסטי) |
|-------|----------------|---------------------|
| lst1 | O(n log n) | O(n log n) - כמעט ממוין |
| lst2 | O(n log n) | O(n²) - סדר אקראי |
| lst3 | O(n log n) | O(n log n) - האמצעי תמיד ראשון |

**הסבר:**
- lst1: ערכים עולים עם רעש קטן → כמעט ממוין
- lst2: ערכים אקראיים בטווח [0,n)
- lst3: יוצרת סדר שהציר תמיד מחלק באופן מאוזן (האמצע ראשון)

---

## שאלה 12: Selection Sort משופר (2025b מועד א', שאלה 1ה')

```python
def selection_sort_2(lst):
    n = len(lst)
    i = 0
    while i < n:
        m_index = i
        for j in range(i+1, n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
        i += 1
        # שיפור: מדלג על כפילויות
        for j in range(i, n):
            if lst[j] == lst[i-1]:
                swap(lst, i, j)
                i += 1
    return None
```

**השוואת סיבוכיות:**

| רשימה | selection_sort_1 | selection_sort_2 |
|-------|------------------|------------------|
| `[i for i in range(n)]` | O(n²) | O(n²) |
| `[(i % 100) for i in range(n)]` | O(n²) | O(n) - רק 100 ערכים שונים |
| `[(i % int(n**0.5)) for i in range(n)]` | O(n²) | O(n^1.5) |

**הסבר:** הגרסה המשופרת מדלגת על כל הכפילויות של הערך הנבחר, מה שחוסך איטרציות כשיש הרבה ערכים זהים.

---

## שאלה 13: סכום לוגריתמים (2025a מועד ב', שאלה 1ה')

**נתון:**
$$f(n) = \sum_{i=1}^{n \cdot \log(n)} \log(i)$$

**שאלה:** מהי סיבוכיות f(n)?

**תשובה:** Θ(n · log(n) · log(n · log(n))) = **Θ(n · (log n)²)**

**הסבר:**
- יש n·log(n) איטרציות
- כל איטרציה מחשבת log(i) שגדל עד log(n·log(n))
- לפי קירוב סטירלינג: Σlog(i) ≈ k·log(k) כאשר k = n·log(n)

---

## שאלה 14: Hash Table עם עצים מאוזנים (2025b מועד א', שאלה 1א')

**שאלה:** החלפת שרשראות בעצים בינאריים מאוזנים (n=m):

| פעולה | לפני (שרשראות) | אחרי (עצים מאוזנים) |
|-------|----------------|---------------------|
| שליפה - מקרה גרוע | O(n) | **O(log n)** |
| הכנסה - מקרה גרוע | O(n) | **O(log n)** |
| שליפה - ממוצע | O(1) | **O(1)** |
| שליפה - מקרה גרוע (עם עצים) | - | **O(log n)** |

**הסבר:** עץ מאוזן מבטיח גובה O(log k) כאשר k הוא מספר האיברים בתא. במקרה הגרוע כל n האיברים באותו תא, אז O(log n).

---

## שאלה 15: HashTable עם פונקציית האש מיוחדת (2025b מועד ב', שאלה 1ה')

**נתון:** טבלת האש עם n מחרוזות, k גודל האלפבית, m תאים בטבלה (k > m).

```python
def hash_func(my_str):
    c = sorted(set(my_str), key=my_str.count)[-1]
    return ord(c)
```

**לוגיקה:** הפונקציה מוצאת את התו הנפוץ ביותר במחרוזת ומחזירה את ערך ה-ord שלו.

**סיבוכיות הכנסה ממוצעת:** O(n/k)

**הסבר:**
- יש k ערכי hash אפשריים (לפי התו הנפוץ ביותר)
- n מחרוזות מתחלקות בין k תאים
- בממוצע n/k מחרוזות בכל תא

---

## שאלה 16: המרת רשימה ממוינת ל-BST (2025b מועד ב', שאלה 2א')

**הפתרון הטריוויאלי:**
```python
my_tree = Binary_search_tree()
for item in lst:
    my_tree.insert(key=item, val=None)
```

**סיבוכיות:** O(n²)

**מבנה העץ:** שרשרת (chain) - כי הרשימה ממוינת, כל איבר יהיה גדול מהקודם ויתווסף לימין.

**פתרון יעיל O(n):** בחר את האיבר האמצעי כשורש ובנה רקורסיבית.

---

## שאלה 17: BST מרשימה מקושרת (2025b מועד ב', שאלה 2ג')

**בעיה:** אם משתמשים ב-`lst[mid]` על רשימה מקושרת, ה-`__getitem__` הוא O(n).

**סיבוכיות:** O(n² log n)

**הסבר:**
- יש log(n) רמות ברקורסיה
- בכל רמה סה"כ n גישות לאינדקסים
- כל גישה ברשימה מקושרת היא O(n)

**פתרון יעיל O(n):** שמור מצביע curr_head ועדכן אותו לאורך הרקורסיה.

---

## שאלה 18: ספירת מסלולים בסריג (2025b מועד ב', שאלה 3)

**בעיה:** ספירת דרכים מ-(0,0) ל-(x,y) כשבכל צעד מתקדמים ביחידה אחת.

**סיבוכיות עם memoization:** O(x·y)

**עם מכשולים (n מכשולים):** O(x·y·n) - אם בודקים עבור כל נקודה אם היא מכשול ברשימה.

**עם מסלולים אלכסוניים:** עדיין O(x·y) - מספר תתי-הבעיות לא משתנה.

---

## שאלה 19: סכום לוגריתמים של חזקות (2025b מועד ב', שאלה 5 - בונוס)

**נתון:**
$$\sum_{k=1}^{n} \log_2(n^k)$$

**פתרון:**
$$\sum_{k=1}^{n} \log_2(n^k) = \sum_{k=1}^{n} k \cdot \log_2(n) = \log_2(n) \cdot \sum_{k=1}^{n} k = \log_2(n) \cdot \frac{n(n+1)}{2}$$

**תשובה:** Θ(n² · log n)

---

## קישורים לסיכומים

- [סיבוכיות](../notes/complexity.md)
- [רקורסיה](../notes/functions_and_recursion.md)
- [טריקים לבחינה](../notes/exam_tricks.md)
