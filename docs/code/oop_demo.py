"""
תכנות מונחה עצמים (OOP) - דוגמאות
מבוא למדעי המחשב
"""


# ========================================
# מחלקה בסיסית
# ========================================

class Point:
    """נקודה במישור"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5


# ========================================
# עץ חיפוש בינארי
# ========================================

class BSTNode:
    """צומת בעץ חיפוש בינארי"""

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BST:
    """עץ חיפוש בינארי"""

    def __init__(self):
        self.root = None

    def insert(self, key):
        """הכנסת מפתח"""
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key)
        return node

    def find(self, key):
        """חיפוש מפתח"""
        return self._find_rec(self.root, key)

    def _find_rec(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._find_rec(node.left, key)
        else:
            return self._find_rec(node.right, key)

    def inorder(self):
        """סריקה inorder (ממוין)"""
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, node, result):
        if node:
            self._inorder_rec(node.left, result)
            result.append(node.key)
            self._inorder_rec(node.right, result)

    def height(self):
        """גובה העץ"""
        return self._height_rec(self.root)

    def _height_rec(self, node):
        if node is None:
            return -1
        return 1 + max(self._height_rec(node.left),
                       self._height_rec(node.right))

    def min_key(self):
        """מפתח מינימלי"""
        if not self.root:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.key

    def max_key(self):
        """מפתח מקסימלי"""
        if not self.root:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.key


# ========================================
# ירושה
# ========================================

class Shape:
    """צורה גאומטרית - מחלקת בסיס"""

    def __init__(self, color="black"):
        self.color = color

    def area(self):
        raise NotImplementedError("מחלקות יורשות חייבות לממש")

    def perimeter(self):
        raise NotImplementedError("מחלקות יורשות חייבות לממש")


class Rectangle(Shape):
    """מלבן"""

    def __init__(self, width, height, color="black"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


class Circle(Shape):
    """מעגל"""

    def __init__(self, radius, color="black"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def __repr__(self):
        return f"Circle({self.radius})"


def main():
    print("=" * 60)
    print("תכנות מונחה עצמים")
    print("=" * 60)

    # נקודות
    print("\n--- מחלקת Point ---")
    p1 = Point(3, 4)
    p2 = Point(6, 8)

    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p1 + p2 = {p1 + p2}")
    print(f"מרחק: {p1.distance(p2):.2f}")

    # עץ חיפוש בינארי
    print("\n--- עץ חיפוש בינארי ---")
    bst = BST()
    values = [5, 3, 7, 1, 4, 6, 8]

    for v in values:
        bst.insert(v)

    print(f"הכנסנו: {values}")
    print(f"inorder: {bst.inorder()}")
    print(f"גובה: {bst.height()}")
    print(f"מינימום: {bst.min_key()}")
    print(f"מקסימום: {bst.max_key()}")
    print(f"find(4): {bst.find(4)}")
    print(f"find(10): {bst.find(10)}")

    # ירושה
    print("\n--- ירושה ---")
    rect = Rectangle(5, 3)
    circ = Circle(2)

    print(f"מלבן: {rect}")
    print(f"  שטח: {rect.area()}")
    print(f"  היקף: {rect.perimeter()}")

    print(f"מעגל: {circ}")
    print(f"  שטח: {circ.area():.2f}")
    print(f"  היקף: {circ.perimeter():.2f}")

    # פולימורפיזם
    print("\n--- פולימורפיזם ---")
    shapes = [Rectangle(4, 3), Circle(2), Rectangle(2, 2)]
    total_area = sum(s.area() for s in shapes)
    print(f"צורות: {shapes}")
    print(f"שטח כולל: {total_area:.2f}")

    # מתודות מיוחדות
    print("\n" + "=" * 60)
    print("מתודות מיוחדות (dunder methods)")
    print("=" * 60)
    print("""
    __init__    - בנאי (constructor)
    __repr__    - ייצוג מפורט (למתכנתים)
    __str__     - ייצוג קריא (למשתמשים)
    __eq__      - השוואה (==)
    __lt__      - קטן מ (<)
    __add__     - חיבור (+)
    __len__     - אורך (len())
    __getitem__ - גישה באינדקס ([])
    __iter__    - איטרציה (for)
    """)


if __name__ == "__main__":
    main()
