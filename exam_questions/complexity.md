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

## קישורים לסיכומים

- [סיבוכיות](../notes/complexity.md)
- [רקורסיה](../notes/functions_and_recursion.md)
- [טריקים לבחינה](../notes/exam_tricks.md)
