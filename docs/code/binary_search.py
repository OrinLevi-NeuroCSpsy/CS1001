"""
חיפוש בינארי - מימוש איטרטיבי עם הדפסות
מבוא למדעי המחשב
"""


def binary_search(lst, target):
    """
    חיפוש בינארי איטרטיבי עם הדפסות שמראות את צמצום הטווח.

    Args:
        lst: רשימה ממוינת
        target: הערך המבוקש

    Returns:
        אינדקס הערך אם נמצא, אחרת -1
    """
    low = 0
    high = len(lst) - 1
    iteration = 1

    print(f"מחפש את {target} ברשימה: {lst}")
    print("-" * 50)

    while low <= high:
        mid = (low + high) // 2

        # הצגת מצב נוכחי
        print(f"איטרציה {iteration}:")
        print(f"  טווח: [{low}, {high}]")
        print(f"  אמצע: {mid}, ערך: {lst[mid]}")

        if lst[mid] == target:
            print(f"  >>> נמצא! {target} נמצא באינדקס {mid}")
            return mid

        elif lst[mid] < target:
            print(f"  {lst[mid]} < {target}, מחפשים בחצי הימני")
            low = mid + 1

        else:
            print(f"  {lst[mid]} > {target}, מחפשים בחצי השמאלי")
            high = mid - 1

        print()
        iteration += 1

    print(f">>> הערך {target} לא נמצא ברשימה")
    return -1


def main():
    # דוגמה 1: חיפוש מוצלח
    print("=" * 50)
    print("דוגמה 1: חיפוש ערך שקיים")
    print("=" * 50)
    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    result = binary_search(numbers, 23)
    print()

    # דוגמה 2: חיפוש ערך שלא קיים
    print("=" * 50)
    print("דוגמה 2: חיפוש ערך שלא קיים")
    print("=" * 50)
    result = binary_search(numbers, 50)
    print()

    # דוגמה 3: חיפוש ערך בקצה
    print("=" * 50)
    print("דוגמה 3: חיפוש ערך בקצה הרשימה")
    print("=" * 50)
    result = binary_search(numbers, 91)


if __name__ == "__main__":
    main()
