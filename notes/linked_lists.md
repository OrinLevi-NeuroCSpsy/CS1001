# רשימות מקושרות (Linked Lists) - סיכום לבחינה

---

## מוטיבציה

### הבעיה עם רשימות רגילות (Arrays)

| פעולה | רשימה רגילה | בעיה |
|-------|-------------|------|
| הכנסה באמצע | O(n) | צריך להזיז את כל האיברים |
| מחיקה מאמצע | O(n) | צריך להזיז את כל האיברים |
| הכנסה בהתחלה | O(n) | הכי יקר! |

### הפתרון: רשימה מקושרת
במקום לאחסן איברים **ברצף בזיכרון**, כל איבר מצביע לאיבר הבא.

---

## הגדרה פורמלית

**רשימה מקושרת (Linked List)** היא מבנה נתונים המורכב מ**צמתים (Nodes)**, כאשר כל צומת מכיל:
1. **ערך (Data/Value)**
2. **מצביע (Pointer/Reference)** לצומת הבא

```
┌───────────┐    ┌───────────┐    ┌───────────┐
│ value: 5  │    │ value: 10 │    │ value: 15 │
│ next: ────┼───►│ next: ────┼───►│ next: None│
└───────────┘    └───────────┘    └───────────┘
     head                              tail
```

---

## הסבר אינטואיטיבי

דמיינו **שרשרת של קרונות רכבת**:
- כל קרון (צומת) מכיל משא (ערך)
- כל קרון מחובר לקרון הבא (מצביע)
- הקרון האחרון לא מחובר לכלום (None)

**יתרון:** קל להוסיף/להסיר קרון - רק לשנות את החיבורים!

---

## מחלקת Node

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    # מצביע לצומת הבא

    def __repr__(self):
        return f"Node({self.value})"
```

### יצירת שרשרת ידנית

```python
# יצירת צמתים
n1 = Node(5)
n2 = Node(10)
n3 = Node(15)

# חיבור השרשרת
n1.next = n2
n2.next = n3
# n3.next נשאר None

# מעבר על השרשרת
current = n1
while current is not None:
    print(current.value)
    current = current.next
# 5, 10, 15
```

---

## מחלקת LinkedList

```python
class LinkedList:
    def __init__(self):
        self.head = None    # מצביע לצומת הראשון

    def is_empty(self):
        return self.head is None

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " -> None"
```

---

## פעולות בסיסיות

### 1. הוספה בהתחלה - O(1)

```python
def add_first(self, value):
    new_node = Node(value)
    new_node.next = self.head   # החדש מצביע לראש הישן
    self.head = new_node        # החדש הופך לראש

# לפני: head -> [10] -> [20] -> None
# add_first(5)
# אחרי:  head -> [5] -> [10] -> [20] -> None
```

**ויזואליזציה:**
```
לפני:
head ──► [10] ──► [20] ──► None

שלב 1: יוצרים צומת חדש
        [5]

שלב 2: החדש מצביע ל-head הישן
        [5] ──► [10] ──► [20] ──► None

שלב 3: head מצביע לחדש
head ──► [5] ──► [10] ──► [20] ──► None
```

### 2. הוספה בסוף - O(n)

```python
def add_last(self, value):
    new_node = Node(value)

    if self.is_empty():
        self.head = new_node
        return

    # מצא את הצומת האחרון
    current = self.head
    while current.next is not None:
        current = current.next

    current.next = new_node
```

### 3. הוספה במיקום - O(n)

```python
def add_at(self, index, value):
    if index == 0:
        self.add_first(value)
        return

    new_node = Node(value)
    current = self.head

    # הגע לצומת שלפני המיקום
    for _ in range(index - 1):
        if current is None:
            raise IndexError("Index out of range")
        current = current.next

    new_node.next = current.next
    current.next = new_node
```

### 4. מחיקה מההתחלה - O(1)

```python
def remove_first(self):
    if self.is_empty():
        raise IndexError("List is empty")

    value = self.head.value
    self.head = self.head.next  # הראש החדש הוא השני
    return value
```

### 5. מחיקה מהסוף - O(n)

```python
def remove_last(self):
    if self.is_empty():
        raise IndexError("List is empty")

    if self.head.next is None:  # רק איבר אחד
        value = self.head.value
        self.head = None
        return value

    # מצא את הצומת לפני האחרון
    current = self.head
    while current.next.next is not None:
        current = current.next

    value = current.next.value
    current.next = None
    return value
```

### 6. מחיקה לפי ערך - O(n)

```python
def remove_value(self, value):
    if self.is_empty():
        return False

    # מקרה מיוחד: הערך בראש
    if self.head.value == value:
        self.head = self.head.next
        return True

    current = self.head
    while current.next is not None:
        if current.next.value == value:
            current.next = current.next.next  # דילוג
            return True
        current = current.next

    return False  # לא נמצא
```

**ויזואליזציה של מחיקה:**
```
לפני: head -> [5] -> [10] -> [15] -> None
מחיקת 10:

שלב 1: מצא את הצומת לפני 10
        head -> [5] -> [10] -> [15] -> None
                 ↑
              current

שלב 2: current.next = current.next.next
        head -> [5] ──────────► [15] -> None
                      (דילוג על 10)
```

### 7. חיפוש - O(n)

```python
def find(self, value):
    """מחזיר את האינדקס, או -1 אם לא נמצא"""
    current = self.head
    index = 0

    while current is not None:
        if current.value == value:
            return index
        current = current.next
        index += 1

    return -1

def __contains__(self, value):
    """תמיכה ב-in"""
    return self.find(value) != -1
```

### 8. אורך - O(n)

```python
def __len__(self):
    count = 0
    current = self.head
    while current is not None:
        count += 1
        current = current.next
    return count
```

---

## מימוש מלא

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_first(self):
        if self.is_empty():
            raise IndexError("List is empty")
        value = self.head.value
        self.head = self.head.next
        return value

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " -> None"

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
```

### שימוש

```python
lst = LinkedList()
lst.add_first(3)
lst.add_first(2)
lst.add_first(1)
print(lst)  # 1 -> 2 -> 3 -> None

lst.add_last(4)
print(lst)  # 1 -> 2 -> 3 -> 4 -> None

lst.remove_first()
print(lst)  # 2 -> 3 -> 4 -> None

for val in lst:
    print(val)  # 2, 3, 4
```

---

## השוואת סיבוכיות

| פעולה | רשימה רגילה | רשימה מקושרת |
|-------|-------------|--------------|
| גישה לאינדקס `[i]` | **O(1)** | O(n) |
| הוספה בהתחלה | O(n) | **O(1)** |
| הוספה בסוף | O(1)* | O(n)** |
| הוספה באמצע | O(n) | O(n)*** |
| מחיקה מהתחלה | O(n) | **O(1)** |
| מחיקה מסוף | O(1) | O(n) |
| חיפוש | O(n) | O(n) |

\* Amortized
\** O(1) אם שומרים מצביע ל-tail
\*** O(1) אם כבר יש מצביע למיקום

---

## וריאציות

### רשימה מקושרת עם tail

```python
class LinkedListWithTail:
    def __init__(self):
        self.head = None
        self.tail = None    # מצביע לאחרון

    def add_last(self, value):  # עכשיו O(1)!
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
```

### רשימה מקושרת דו-כיוונית (Doubly Linked List)

כל צומת מצביע גם **קדימה** וגם **אחורה**.

```python
class DNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None    # מצביע לקודם
```

```
       ┌──────────────┐    ┌──────────────┐
None ◄─┤ prev    next ├───►│ prev    next ├───► None
       │   value: 5   │◄───┤   value: 10  │
       └──────────────┘    └──────────────┘
```

**יתרון:** מחיקה מהסוף ב-O(1) עם tail

### רשימה מעגלית (Circular Linked List)

האחרון מצביע לראשון.

```
    ┌──► [5] ──► [10] ──► [15] ──┐
    │                            │
    └────────────────────────────┘
```

---

## פעולות מתקדמות

### היפוך רשימה - O(n)

```python
def reverse(self):
    prev = None
    current = self.head

    while current is not None:
        next_node = current.next  # שמור את הבא
        current.next = prev       # הפוך את הכיוון
        prev = current            # התקדם
        current = next_node

    self.head = prev
```

**ויזואליזציה:**
```
לפני: [1] -> [2] -> [3] -> None

שלב 1: prev=None, curr=[1]
        None <- [1]    [2] -> [3] -> None

שלב 2: prev=[1], curr=[2]
        None <- [1] <- [2]    [3] -> None

שלב 3: prev=[2], curr=[3]
        None <- [1] <- [2] <- [3]

אחרי:  [3] -> [2] -> [1] -> None
```

### זיהוי מעגל (Floyd's Algorithm)

```python
def has_cycle(self):
    """בודק אם יש מעגל ברשימה"""
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next          # צעד אחד
        fast = fast.next.next     # שני צעדים
        if slow == fast:
            return True

    return False
```

### מציאת האמצע - O(n)

```python
def find_middle(self):
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.value if slow else None
```

---

## טעויות נפוצות

### טעות 1: שכחה לטפל ברשימה ריקה

```python
# שגוי
def add_last(self, value):
    current = self.head
    while current.next:  # קריסה אם head הוא None!
        current = current.next

# נכון
def add_last(self, value):
    if self.is_empty():
        self.head = Node(value)
        return
    # ...
```

### טעות 2: איבוד ההפניה

```python
# שגוי - איבדנו את השרשרת!
def add_first(self, value):
    self.head = Node(value)      # הראש הישן אבד
    self.head.next = old_head    # old_head לא מוגדר

# נכון
def add_first(self, value):
    new_node = Node(value)
    new_node.next = self.head    # קודם מחברים
    self.head = new_node         # אז מעדכנים head
```

### טעות 3: לולאה אינסופית

```python
# שגוי
while current:
    # שכחנו להתקדם!
    print(current.value)

# נכון
while current:
    print(current.value)
    current = current.next
```

### טעות 4: השוואה עם == במקום is

```python
# לבדיקת None, עדיף is:
while current is not None:  # נכון
while current != None:      # עובד אבל פחות פייתוני
while current:              # הכי קצר ונכון
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: מה יודפס?

```python
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

current = n1
while current:
    print(current.value, end=" ")
    current = current.next
```

**תשובה:** `1 2 3`

---

### שאלה 2: השלם את הפונקציה

```python
def count_nodes(head):
    """מחזירה את מספר הצמתים ברשימה"""
    # השלם
```

**פתרון:**
```python
def count_nodes(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
```

---

### שאלה 3: מה הסיבוכיות?

```python
def mystery(lst):  # lst הוא LinkedList
    current = lst.head
    while current and current.next:
        current = current.next.next
    return current
```

**תשובה:** O(n/2) = **O(n)** - עוברים על חצי מהרשימה

---

### שאלה 4: מצא באג

```python
def remove_last(self):
    current = self.head
    while current.next:
        current = current.next
    current = None
```

**באג:** `current = None` משנה רק משתנה לוקאלי, לא את הרשימה.

**תיקון:**
```python
def remove_last(self):
    if self.head.next is None:
        self.head = None
        return
    current = self.head
    while current.next.next:
        current = current.next
    current.next = None  # מנתק את האחרון
```

---

## סיכום נקודות חשובות

- [ ] **Node** = value + next (מצביע)
- [ ] **הוספה/מחיקה בהתחלה** = O(1)
- [ ] **גישה לאינדקס** = O(n) (חיסרון מרכזי)
- [ ] **עם tail** = הוספה בסוף O(1)
- [ ] תמיד לטפל במקרה של רשימה ריקה
- [ ] שמירת הפניות לפני שינוי מצביעים
- [ ] `while current:` לא `while current.next:`
- [ ] היפוך רשימה: שלושה מצביעים (prev, current, next)

---

## קישורים נוספים

- **קוד:** [linked_lists_demo.py](../code/linked_lists_demo.py)
