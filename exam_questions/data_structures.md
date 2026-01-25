# שאלות מבחן - מבני נתונים

---

## שאלה 1: עץ חיפוש בינארי - הגדרה שגויה (2022b מועד א', שאלה 1א')

**טענה:** אם לכל צומת v עם בן שמאלי מתקיים v.left.key < v.key, ולכל צומת v עם בן ימני מתקיים v.key < v.right.key, אז העץ הוא עץ חיפוש בינארי.

**תשובה:** הטענה **לא נכונה**!

**דוגמה נגדית:**
```
      5
     / \
    3   7
     \
      6   ← 6 > 5 אבל נמצא בתת-עץ שמאלי!
```

**טריק חשוב:** BST דורש שכל הצמתים בתת-עץ שמאלי יהיו קטנים מהשורש!

---

## שאלה 2: סכום עומקים בעץ (2023a מועד א', שאלה 2)

```python
def sum_depths(T):
    def helper(node, depth):
        if node is None:
            return 0
        return depth + helper(node.left, depth+1) + helper(node.right, depth+1)
    return helper(T.root, 0)
```

**סיבוכיות:** Θ(n) - עוברים על כל צומת פעם אחת

---

## שאלה 3: MergingLists (2022b מועד א', שאלה 4)

**מבנה הנתונים:** רשימות ממוינות באורכים m, 2m, 4m, ...

**Insert complexity עם m=1:** O(log n)
- במקרה הגרוע, מיזוג כל הרשימות

**Find complexity:** O(log² n)
- log n רשימות, חיפוש בינארי בכל אחת

---

## שאלה 4: עץ עם הורים - successor (2023b מועד א', שאלה 4ב')

```python
def successor(v):
    if v.right != None:
        return get_min(v.right)

    parent = v.parent
    while parent != None and v == parent.right:
        v = parent
        parent = v.parent
    return parent
```

**טריק חשוב:** אם אין תת-עץ ימני, הסוקסור הוא האב הראשון שאנחנו בן שמאלי שלו!

---

## שאלה 5: In-order ללא רקורסיה (2023b מועד א', שאלה 4ג')

```python
def inorder_loop(T):
    v = get_min(T.root)
    while v != None:
        print(v.key)
        v = successor(v)
    return None
```

**סיבוכיות:** Θ(n) - כל קשת נעברת לכל היותר פעמיים

---

## שאלה 6: טבלת האש - בחירת פונקציית hash (2023b מועד א', שאלה 1ה')

**השוואה (מהיר למאט):**
1. `Hashtable(100, lambda x: x%20)` - פיזור טוב
2. `Hashtable(10, lambda x: x)` - פיזור סביר
3. `Hashtable(10, lambda x: int(math.log(x,10)))` - רק 10 ערכים
4. `Hashtable(10, lambda x: 1 if x%2==0 else 0)` - רק 2 ערכים!

---

## קישורים לסיכומים

- [עצי חיפוש בינאריים](../notes/oop.md)
- [טבלאות האש](../notes/hash_tables.md)
- [רשימות מקושרות](../notes/linked_lists.md)
