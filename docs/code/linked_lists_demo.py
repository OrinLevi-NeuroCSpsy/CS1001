"""
רשימות מקושרות - מימוש והדגמות
מבוא למדעי המחשב
"""


# ========================================
# רשימה מקושרת חד-כיוונית
# ========================================

class Node:
    """צומת ברשימה מקושרת"""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:
    """רשימה מקושרת חד-כיוונית"""

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if not self.head:
            return "[]"
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)

    def prepend(self, value):
        """הוספה בהתחלה - O(1)"""
        self.head = Node(value, self.head)
        self.size += 1

    def append(self, value):
        """הוספה בסוף - O(n)"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def find(self, value):
        """חיפוש - O(n)"""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        """מחיקה - O(n)"""
        if not self.head:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False

    def reverse(self):
        """היפוך - O(n)"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_list(self):
        """המרה לרשימה רגילה"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


# ========================================
# רשימה מקושרת דו-כיוונית
# ========================================

class DNode:
    """צומת ברשימה דו-כיוונית"""

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """רשימה מקושרת דו-כיוונית"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if not self.head:
            return "[]"
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " <-> ".join(values)

    def append(self, value):
        """הוספה בסוף - O(1)"""
        new_node = DNode(value, prev=self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def prepend(self, value):
        """הוספה בהתחלה - O(1)"""
        new_node = DNode(value, next=self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1


# ========================================
# פונקציות עזר רקורסיביות
# ========================================

def length_rec(node):
    """אורך רשימה - רקורסיבי"""
    if node is None:
        return 0
    return 1 + length_rec(node.next)


def sum_rec(node):
    """סכום ערכים - רקורסיבי"""
    if node is None:
        return 0
    return node.value + sum_rec(node.next)


def print_reverse(node):
    """הדפסה הפוכה - רקורסיבי"""
    if node is None:
        return
    print_reverse(node.next)
    print(node.value, end=" ")


def main():
    print("=" * 60)
    print("רשימות מקושרות")
    print("=" * 60)

    # רשימה חד-כיוונית
    print("\n--- רשימה חד-כיוונית ---")
    lst = LinkedList()

    for val in [1, 2, 3, 4, 5]:
        lst.append(val)

    print(f"רשימה: {lst}")
    print(f"אורך: {len(lst)}")

    # חיפוש
    print(f"\nfind(3): {lst.find(3)}")
    print(f"find(10): {lst.find(10)}")

    # מחיקה
    lst.delete(3)
    print(f"\nאחרי delete(3): {lst}")

    # היפוך
    lst.reverse()
    print(f"אחרי reverse(): {lst}")

    # הוספה בהתחלה
    lst.prepend(0)
    print(f"אחרי prepend(0): {lst}")

    # רשימה דו-כיוונית
    print("\n--- רשימה דו-כיוונית ---")
    dlst = DoublyLinkedList()

    for val in [1, 2, 3]:
        dlst.append(val)

    print(f"רשימה: {dlst}")
    dlst.prepend(0)
    print(f"אחרי prepend(0): {dlst}")

    # פונקציות רקורסיביות
    print("\n--- פונקציות רקורסיביות ---")
    lst2 = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        lst2.append(val)

    print(f"רשימה: {lst2}")
    print(f"length_rec: {length_rec(lst2.head)}")
    print(f"sum_rec: {sum_rec(lst2.head)}")
    print("print_reverse: ", end="")
    print_reverse(lst2.head)
    print()

    # השוואת סיבוכיויות
    print("\n" + "=" * 60)
    print("השוואת סיבוכיויות")
    print("=" * 60)
    print("""
    | פעולה           | רשימה מקושרת | מערך/רשימה |
    |-----------------|--------------|------------|
    | גישה לאינדקס i | O(n)         | O(1)       |
    | הוספה בהתחלה   | O(1)         | O(n)       |
    | הוספה בסוף     | O(n)/O(1)*   | O(1)**     |
    | הוספה באמצע    | O(n)         | O(n)       |
    | מחיקה בהתחלה   | O(1)         | O(n)       |
    | חיפוש          | O(n)         | O(n)       |

    * O(1) אם שומרים מצביע ל-tail
    ** Amortized O(1) בפייתון
    """)


if __name__ == "__main__":
    main()
