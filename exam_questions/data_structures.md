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

## שאלה 7: Hash Table עם שרשראות (2024a מועד א', שאלה 1ד')

```python
>>> t1 = Hashtable(10)
>>> t2 = Hashtable(20)
>>> t1.insert(x)
>>> t1.insert(y)
>>> t2.insert(x)
>>> t2.insert(y)
```

**שאלה:** אם t1.table[i] עבור i כלשהו היא שרשרת באורך 2, מה נכון בהכרח?

**אפשרויות:**
1. hash(x) == hash(y)
2. ב-t2 גם יש שרשרת באורך 2
3. t2.table[i] היא לא שרשרת ריקה
4. אף תשובה מהנ"ל לא נכונה

**תשובה:** 3 - t2.table[i] היא לא שרשרת ריקה

**הסבר:** אם x ו-y נפלו לאותו תא ב-t1, אז לפחות אחד מהם יפול לתא i גם ב-t2 (כי hash(x) % 20 יכול להיות i או i+10)

---

## שאלה 8: BST - בדיקת תכונה (2024a מועד ב', שאלה 1ב')

```python
def what(self):
    def what_rec(node):
        if node == None:
            return True
        elif [node.left, node.right].count(None) == 1:
            return False
        else:
            return what_rec(node.left) and what_rec(node.right)
    return what_rec(self.root)
```

**שאלה:** עבור אילו עצים המתודה תחזיר True?

**תשובה:** עצים שבהם לכל צומת יש 0 או 2 ילדים (לא בדיוק ילד אחד)

---

## שאלה 9: BST - בדיקת אב קדמון (2024a מועד ב', שאלה 3א')

**הגדרה:** p הוא אב קדמון של צומת a אם p ≠ a וגם p נמצא על המסלול מהשורש ל-a.

```python
def is_ancestor(self, key1, key2):
    node = self.root
    while node != None:
        if node.key == key1:
            # key1 נמצא, בדוק אם key2 בתת-עץ שלו
            return self._find_in_subtree(node, key2)
        elif node.key == key2:
            # key2 נמצא, בדוק אם key1 בתת-עץ שלו
            return self._find_in_subtree(node, key1)
        elif key1 < node.key and key2 < node.key:
            node = node.left
        elif key1 > node.key and key2 > node.key:
            node = node.right
        else:
            # key1 ו-key2 בצדדים שונים - לא אב קדמון
            return False
    return False
```

---

## שאלה 10: Hash Functions (2025a מועד א', שאלה 1ג')

**נתון:** n = 1024·m, מכניסים מספרים 1 עד n לטבלת האש

| hash_func | תוצאה |
|-----------|-------|
| lambda x: x%10 | הכנסה וחיפוש תקינים, אבל סיבוכיות > O(1) |
| lambda x: random.randint(x) | לא מאפשר חיפוש תקין |
| lambda x: 1 | הכנסה וחיפוש תקינים, אבל סיבוכיות > O(1) |
| lambda x: -1*x | הכנסה וחיפוש תקינים, O(1) |
| lambda x: int(math.log(x,2)) | הכנסה וחיפוש תקינים, אבל סיבוכיות > O(1) |

**הסבר:**
- `random.randint(x)` - מחזיר ערך אקראי שונה בכל קריאה, אז לא ניתן למצוא את האיבר
- `-1*x` - פונקציה דטרמיניסטית, פיזור טוב כי n = 1024m
- `x%10` - רק 10 ערכים אפשריים, שרשראות ארוכות

---

## שאלה 11: BST עם טווח מפתחות (2025a מועד א', שאלה 4)

**רעיון:** לכל צומת נוסיף שדה key_range = [min, max] של כל המפתחות בתת-העץ שלו

```python
class TreeNode:
    def update_key_range(self):
        min_key = self.key
        max_key = self.key

        if self.left is not None:
            min_key = min(min_key, self.left.key_range[0])
        if self.right is not None:
            max_key = max(max_key, self.right.key_range[1])

        self.key_range[0] = min_key
        self.key_range[1] = max_key
```

**הנחה:** הילדים כבר מעודכנים → סיבוכיות O(1) לצומת

**עדכון כל העץ:** סיבוכיות O(n) עם post-order traversal

---

## שאלה 12: עץ ביטויים אלגבריים (2024a מועד א', שאלה 2)

```python
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_to_exp(tree_node):
    if tree_node.left is None:
        return tree_node.val

    expression = "(" + tree_to_exp(tree_node.left) + ")"
    expression += tree_node.val
    expression += "(" + tree_to_exp(tree_node.right) + ")"

    return expression
```

**דוגמה:** עץ עם שורש "-", בן שמאל "+" (עם a ו-"*" שיש לו b,c), בן ימין "/" (עם d,e)

**תוצאה:** ((a)+(b)*(c))-((d)/(e))

---

## קישורים לסיכומים

- [עצי חיפוש בינאריים](../notes/oop.md)
- [טבלאות האש](../notes/hash_tables.md)
- [רשימות מקושרות](../notes/linked_lists.md)
