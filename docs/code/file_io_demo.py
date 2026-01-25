"""
קריאה וכתיבה לקבצים - דוגמאות
מבוא למדעי המחשב
"""

import os


# ========================================
# קריאה מקובץ
# ========================================

def demo_read():
    """דוגמאות קריאה"""
    print("--- קריאה מקובץ ---")

    # יצירת קובץ לדוגמה
    sample_content = """שורה ראשונה
שורה שנייה
שורה שלישית"""

    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write(sample_content)

    print("תוכן הקובץ:")
    print("-" * 30)

    # שיטה 1: קריאת כל הקובץ
    with open("sample.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(f"read():\n{repr(content)}\n")

    # שיטה 2: קריאה לרשימת שורות
    with open("sample.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(f"readlines(): {lines}\n")

    # שיטה 3: איטרציה על שורות (מומלץ!)
    print("איטרציה על שורות:")
    with open("sample.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            print(f"  {i}: {line.strip()!r}")

    os.remove("sample.txt")


# ========================================
# כתיבה לקובץ
# ========================================

def demo_write():
    """דוגמאות כתיבה"""
    print("\n--- כתיבה לקובץ ---")

    # כתיבה רגילה (דורס קובץ קיים)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("שורה ראשונה\n")
        f.write("שורה שנייה\n")

    # הוספה לקובץ קיים
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write("שורה נוספת\n")

    # כתיבת רשימה
    lines = ["אלף\n", "בית\n", "גימל\n"]
    with open("output.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)

    print("נכתב לקובץ output.txt")

    # קריאה ובדיקה
    with open("output.txt", "r", encoding="utf-8") as f:
        print(f"תוכן: {f.read()}")

    os.remove("output.txt")


# ========================================
# מצבי פתיחה
# ========================================

def demo_modes():
    """מצבי פתיחת קובץ"""
    print("\n--- מצבי פתיחה ---")
    print("""
    'r'  - קריאה (ברירת מחדל)
    'w'  - כתיבה (דורס קיים)
    'a'  - הוספה (append)
    'x'  - יצירה (שגיאה אם קיים)
    'b'  - בינארי (rb, wb)
    '+'  - קריאה וכתיבה (r+, w+)
    """)


# ========================================
# קבצים בינאריים
# ========================================

def demo_binary():
    """קבצים בינאריים"""
    print("--- קבצים בינאריים ---")

    # כתיבה בינארית
    data = bytes([0, 1, 2, 255, 128])
    with open("binary.bin", "wb") as f:
        f.write(data)

    # קריאה בינארית
    with open("binary.bin", "rb") as f:
        content = f.read()
        print(f"בתים: {list(content)}")

    os.remove("binary.bin")


# ========================================
# טיפול בשגיאות
# ========================================

def demo_errors():
    """טיפול בשגיאות קבצים"""
    print("\n--- טיפול בשגיאות ---")

    # קובץ לא קיים
    try:
        with open("nonexistent.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("FileNotFoundError: הקובץ לא קיים")

    # try-finally (הדרך הישנה)
    print("\ntry-finally vs with:")
    print("""
    # הדרך הישנה (פחות מומלצת):
    f = open('file.txt')
    try:
        content = f.read()
    finally:
        f.close()

    # הדרך המומלצת (with):
    with open('file.txt') as f:
        content = f.read()
    # הקובץ נסגר אוטומטית!
    """)


# ========================================
# דוגמאות מעשיות
# ========================================

def count_words(filename):
    """ספירת מילים בקובץ"""
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return len(words)


def count_lines(filename):
    """ספירת שורות בקובץ"""
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def find_in_file(filename, search_term):
    """חיפוש מחרוזת בקובץ"""
    results = []
    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if search_term in line:
                results.append((i, line.strip()))
    return results


def copy_file(src, dst):
    """העתקת קובץ"""
    with open(src, "r", encoding="utf-8") as f_in:
        with open(dst, "w", encoding="utf-8") as f_out:
            for line in f_in:
                f_out.write(line)


def main():
    print("=" * 60)
    print("קריאה וכתיבה לקבצים")
    print("=" * 60)

    demo_read()
    demo_write()
    demo_modes()
    demo_binary()
    demo_errors()

    print("\n--- פונקציות שימושיות ---")
    print("""
    # ספירת מילים
    def count_words(filename):
        with open(filename, 'r') as f:
            return len(f.read().split())

    # ספירת שורות
    def count_lines(filename):
        with open(filename, 'r') as f:
            return sum(1 for _ in f)

    # חיפוש בקובץ
    def find_in_file(filename, term):
        with open(filename, 'r') as f:
            for i, line in enumerate(f, 1):
                if term in line:
                    print(f"{i}: {line.strip()}")
    """)


if __name__ == "__main__":
    main()
