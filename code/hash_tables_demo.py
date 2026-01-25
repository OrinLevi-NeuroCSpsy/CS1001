"""
טבלאות האש - מימוש והדגמות
מבוא למדעי המחשב
"""


# ========================================
# טבלת האש עם שרשור (Chaining)
# ========================================

class HashTableChaining:
    """טבלת האש עם שרשור"""

    def __init__(self, size=10, hash_func=None):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.hash_func = hash_func or (lambda x: hash(x) % self.size)
        self.num_items = 0

    def insert(self, key, value=None):
        """הכנסת מפתח (עם ערך אופציונלי)"""
        idx = self.hash_func(key)
        # בדוק אם המפתח כבר קיים
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))
        self.num_items += 1

    def find(self, key):
        """חיפוש מפתח"""
        idx = self.hash_func(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """מחיקת מפתח"""
        idx = self.hash_func(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                self.num_items -= 1
                return True
        return False

    def load_factor(self):
        """עומס הטבלה"""
        return self.num_items / self.size

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                items = ', '.join(f"{k}:{v}" for k, v in bucket)
                result.append(f"[{i}]: {items}")
        return '\n'.join(result)


# ========================================
# פונקציות האש
# ========================================

def hash_mod(key, size):
    """פונקציית האש פשוטה: key mod size"""
    return key % size


def hash_mult(key, size, A=0.6180339887):
    """פונקציית האש כפלית"""
    return int(size * ((key * A) % 1))


def hash_string(s, size):
    """פונקציית האש למחרוזות"""
    h = 0
    for i, char in enumerate(s):
        h += ord(char) * (31 ** i)
    return h % size


# ========================================
# ניתוח התנגשויות
# ========================================

def analyze_collisions(keys, size, hash_func):
    """ניתוח התנגשויות לפונקציית האש"""
    buckets = [0] * size
    for key in keys:
        idx = hash_func(key, size)
        buckets[idx] += 1

    collisions = sum(max(0, count - 1) for count in buckets)
    max_chain = max(buckets)
    empty = buckets.count(0)

    return {
        'collisions': collisions,
        'max_chain': max_chain,
        'empty_buckets': empty,
        'distribution': buckets
    }


def main():
    print("=" * 60)
    print("טבלאות האש")
    print("=" * 60)

    # יצירת טבלה
    print("\n--- טבלת האש עם שרשור ---")
    ht = HashTableChaining(size=7)

    # הכנסת ערכים
    data = [("apple", 5), ("banana", 3), ("cherry", 8),
            ("date", 2), ("elderberry", 7)]

    for key, value in data:
        ht.insert(key, value)
        print(f"insert('{key}', {value})")

    print(f"\nמצב הטבלה:")
    print(ht)
    print(f"\nעומס: {ht.load_factor():.2f}")

    # חיפוש
    print("\n--- חיפוש ---")
    print(f"find('banana') = {ht.find('banana')}")
    print(f"find('grape') = {ht.find('grape')}")

    # ניתוח התנגשויות
    print("\n--- ניתוח התנגשויות ---")
    keys = list(range(0, 100, 7))  # מספרים שמתחלקים ב-7
    print(f"מפתחות: {keys[:10]}...")

    analysis = analyze_collisions(keys, 10, hash_mod)
    print(f"\nעם hash_mod (size=10):")
    print(f"  התנגשויות: {analysis['collisions']}")
    print(f"  שרשרת מקסימלית: {analysis['max_chain']}")
    print(f"  תאים ריקים: {analysis['empty_buckets']}")
    print(f"  פיזור: {analysis['distribution']}")

    # פונקציות האש שונות
    print("\n--- השוואת פונקציות האש ---")
    keys = list(range(100))

    for name, func in [("mod", hash_mod), ("mult", hash_mult)]:
        analysis = analyze_collisions(keys, 10, func)
        print(f"{name}: התנגשויות={analysis['collisions']}, "
              f"max_chain={analysis['max_chain']}")

    # סיבוכיות
    print("\n" + "=" * 60)
    print("סיבוכיות")
    print("=" * 60)
    print("""
    | פעולה  | ממוצע  | גרוע  |
    |--------|--------|-------|
    | insert | O(1)   | O(n)  |
    | find   | O(1)   | O(n)  |
    | delete | O(1)   | O(n)  |

    * עומס (load factor) α = n/m
    * כאשר α קבוע, זמן ממוצע O(1)
    * גרוע: כל המפתחות באותו תא

    בחירת פונקציית האש טובה:
    1. פיזור אחיד
    2. חישוב מהיר
    3. דטרמיניסטית
    """)


if __name__ == "__main__":
    main()
