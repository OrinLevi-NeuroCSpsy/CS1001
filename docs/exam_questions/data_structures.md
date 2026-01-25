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

## שאלה 13: BST - סדר הכנסה (2024b מועד ב', שאלה 1א')

**נתון עץ BST:**
```
        18
       /  \
     13    29
    /     /  \
   11   24    38
  /    /  \
 6   19   25
  \
   8
```

**טענות על סדר ההכנסה:**

| טענה | תשובה |
|------|-------|
| "8" הוכנס אחרון | לא ניתן לדעת |
| "18" הוכנס ראשון | **נכון בהכרח** (שורש) |
| "25" הוכנס מאוחר יותר מ-"29" | **נכון בהכרח** (25 צאצא של 29) |
| "25" היה השלישי שהוכנס | לא ניתן לדעת |
| "11" הוכנס מיד אחרי "13" | לא ניתן לדעת |

**טריק חשוב:** השורש תמיד הוכנס ראשון! צאצא תמיד הוכנס אחרי אבותיו!

---

## שאלה 14: Hash Table - התנגשויות (2024b מועד א', שאלה 1ב')

**טענות על Hash Tables:**

| טענה | נכון? |
|------|-------|
| אם n=m ו-n>1, קיימת h שמבטיחה 0 התנגשויות לכל אוסף | **לא נכון** - תלוי באוסף |
| אם n>m ונתון אוסף מסוים, תמיד ניתן למצוא h ללא התנגשויות | **לא נכון** - יונים בתאים |
| אם m=n/2, אורך השרשרת הארוכה ביותר יהיה 2 | **לא נכון** - יכול להיות יותר |
| במקרה הגרוע, סיבוכיות חיפוש זהה לרשימה לא ממוינת | **נכון** - O(n) |

---

## שאלה 15: עץ משימות בינארי (2024b מועד ב', שאלה 4)

**הגדרה:** עץ משימות בינארי משרה סדר - כל משימה יכולה להתבצע רק אחרי ההורה שלה.

```python
def print_ordered_tasks(t_tree):
    def recA(node):
        if node is None:
            return
        recA(node.left)
        recA(node.right)
        print(node.key)  # post-order!
    recA(t_tree.root)
```

**סדר מדורג (BFS):**
```python
def get_level_ordered_tasks(t_tree):
    ordered_lst = []
    queue = [t_tree.root]
    while len(queue) > 0:
        node = queue.pop(0)
        ordered_lst.append(node.key)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ordered_lst
```

---

## שאלה 16: BST - סכום צמתים בעומק זוגי (2025a מועד ב', שאלה 1א')

```python
def what(self):
    def why(n, w):
        if n is None:
            return 0
        if w % 2 == 0:  # עומק זוגי
            a = why(n.left, w + 1)
            b = why(n.right, w + 1)
            return n.key + a + b
        return why(n.left, w + 1) + why(n.right, w + 1)
    return why(self.root, 0)
```

**עץ לדוגמה:**
```
      1        (עומק 0 - זוגי)
     / \
    2   3      (עומק 1 - אי-זוגי)
   / \ / \
  4  5 6  7    (עומק 2 - זוגי)
```

**תשובה:** what() מחזיר סכום המפתחות בעומק זוגי = 1 + 4 + 5 + 6 + 7 = **23**

---

## שאלה 17: BST עם key_range - שיפור lookup (2025a מועד ב', שאלה 4א')

**רעיון:** לכל צומת יש שדה key_range = [min, max] של כל המפתחות בתת-העץ שלו.

**שיפור ל-lookup:**
```python
def lookup(self, key):
    node = self.root
    while node != None:
        # שיפור: בדוק אם key בטווח לפני המשך
        if key < node.key_range[0] or key > node.key_range[1]:
            return None  # לא יכול להיות בתת-עץ הזה
        if key == node.key:
            return node.val
        elif key < node.key:
            node = node.left
        else:
            node = node.right
    return None
```

**דוגמה לשיפור:** עבור key=5 בעץ שבו key_range של השורש הוא [6,38], נדע מיד ש-5 לא בעץ!

---

## שאלה 18: BST עם key_range - insert (2025a מועד ב', שאלה 4ב')

```python
def insert(self, key, val):
    parent = None
    node = self.root
    ancestors = []  # שמור את כל האבות
    inserted_node = Tree_node(key, val)

    while node != None:
        ancestors.append(node)  # הוסף לרשימת האבות
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if key < parent.key:
        parent.left = inserted_node
    else:
        parent.right = inserted_node

    inserted_node.key_range = [key, key]
    # עדכן key_range לכל האבות
    for ancestor in ancestors:
        ancestor.key_range[0] = min(ancestor.key_range[0], key)
        ancestor.key_range[1] = max(ancestor.key_range[1], key)
```

**סיבוכיות:** O(depth) - ללא שינוי מה-insert הרגיל!

---

## שאלה 19: BST - in_subtree (2025a מועד ב', שאלה 4ג')

```python
def in_subtree(self, node1, node2):
    key2 = node2.key
    if key2 < node1.key_range[0] or key2 > node1.key_range[1]:
        return False
    return True
```

**סיבוכיות:** O(1)! - השימוש ב-key_range מאפשר בדיקה מיידית

---

## שאלה 20: BST - LCA (Lowest Common Ancestor) (2025a מועד ב', שאלה 4ד')

```python
def lca(self, node1, node2):
    node = self.root
    while node is not None:
        if self.in_subtree(node.left, node1) and \
           self.in_subtree(node.left, node2):
            node = node.left
        elif self.in_subtree(node.right, node1) and \
             self.in_subtree(node.right, node2):
            node = node.right
        else:
            # אחד בכל צד, או אחד מהם הוא node
            return node
    return None
```

**סיבוכיות:** O(depth) - יורדים בעץ עד מציאת ה-LCA

---

## שאלה 21: k-מאוזן-מפתחות (2025b מועד א', שאלה 3)

**הגדרה:** עץ הוא k-מאוזן-מפתחות אם לכל i,j < k, ההפרש בין מספר המפתחות עם שארית i למספר המפתחות עם שארית j הוא לכל היותר 1.

```python
def is_key_balanced1(tree, k):
    n = tree.size
    v1 = n + 1  # מינימום
    v2 = -1    # מקסימום
    for i in range(k):
        cnt = count_modk_eq_c(tree.root, k, i)
        if cnt > v2:
            v2 = cnt
        if cnt < v1:
            v1 = cnt
    return v2 - v1 <= 1
```

**סיבוכיות:** O(f(n) · k) - כאשר f(n) הסיבוכיות של count_modk_eq_c

**פתרון יעיל O(n + k):**
```python
def is_key_balanced2(tree, k):
    counts = [0] * k

    def rec(node, k, counts):
        if node is None:
            return
        counts[node.key % k] += 1
        rec(node.left, k, counts)
        rec(node.right, k, counts)

    rec(tree.root, k, counts)
    return max(counts) - min(counts) <= 1
```

---

## שאלה 22: המרת רשימה ממוינת ל-BST מאוזן (2025b מועד ב', שאלה 2ב')

```python
def bst_from_sorted_list(self, lst):
    def bst_from_sorted_list_rec(lst, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = Tree_node(lst[mid], None)
        node.left = bst_from_sorted_list_rec(lst, left, mid - 1)
        node.right = bst_from_sorted_list_rec(lst, mid + 1, right)
        return node

    self.root = bst_from_sorted_list_rec(lst, 0, len(lst) - 1)
    self.size = len(lst)
```

**סיבוכיות:** O(n) - כל צומת נבנה בזמן קבוע.

**יתרונות:**
1. העץ מאוזן לחלוטין
2. סיבוכיות O(n) במקום O(n²)

---

## שאלה 23: BST מרשימה מקושרת ממוינת (2025b מועד ב', שאלה 2ד')

**רעיון:** שמור מצביע curr_head שמתעדכן לאורך הרקורסיה.

```python
def bst_from_sorted_linked_list(self, lst):
    def rec(curr_head, n):
        if n <= 0:
            return (None, curr_head)

        l_tree, curr_head = rec(curr_head, n // 2)
        root = Tree_node(curr_head.value, None)
        root.left = l_tree
        curr_head = curr_head.next
        r_tree, curr_head = rec(curr_head, n - n // 2 - 1)
        root.right = r_tree
        return (root, curr_head)

    self.root = rec(lst.head, lst.size)[0]
```

**סיבוכיות:** O(n)

**טריק חשוב:** בונים את העץ בסדר in-order!
1. בנה תת-עץ שמאלי (מתקדם ב-curr_head)
2. צור את השורש מהאיבר הנוכחי
3. בנה תת-עץ ימני

---

## קישורים לסיכומים

- [עצי חיפוש בינאריים](../notes/oop.md)
- [טבלאות האש](../notes/hash_tables.md)
- [רשימות מקושרות](../notes/linked_lists.md)
