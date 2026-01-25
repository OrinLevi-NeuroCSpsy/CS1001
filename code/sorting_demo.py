"""
אלגוריתמי מיון - דוגמאות והדגמות
מבוא למדעי המחשב
"""


def bubble_sort(lst):
    """מיון בועות - O(n²)"""
    lst = lst.copy()
    n = len(lst)
    for i in range(n):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def selection_sort(lst):
    """מיון בחירה - O(n²)"""
    lst = lst.copy()
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def insertion_sort(lst):
    """מיון הכנסה - O(n²)"""
    lst = lst.copy()
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(lst):
    """מיון מיזוג - O(n log n)"""
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left, right):
    """מיזוג שתי רשימות ממוינות"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quicksort(lst):
    """מיון מהיר - O(n log n) ממוצע"""
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def counting_sort(lst, max_val=None):
    """מיון ספירה - O(n + k)"""
    if not lst:
        return []

    if max_val is None:
        max_val = max(lst)

    count = [0] * (max_val + 1)
    for x in lst:
        count[x] += 1

    result = []
    for i, c in enumerate(count):
        result.extend([i] * c)

    return result


def main():
    print("=" * 60)
    print("אלגוריתמי מיון")
    print("=" * 60)

    lst = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nרשימה מקורית: {lst}")
    print("-" * 40)

    print(f"Bubble Sort:    {bubble_sort(lst)}")
    print(f"Selection Sort: {selection_sort(lst)}")
    print(f"Insertion Sort: {insertion_sort(lst)}")
    print(f"Merge Sort:     {merge_sort(lst)}")
    print(f"Quick Sort:     {quicksort(lst)}")

    print("\n" + "=" * 60)
    print("Counting Sort (למספרים שלמים קטנים)")
    print("=" * 60)
    small_nums = [4, 2, 2, 8, 3, 3, 1]
    print(f"רשימה: {small_nums}")
    print(f"תוצאה: {counting_sort(small_nums)}")

    print("\n" + "=" * 60)
    print("השוואת סיבוכיויות")
    print("=" * 60)
    print("""
    | אלגוריתם       | ממוצע      | גרוע       | מקום  |
    |----------------|------------|------------|-------|
    | Bubble Sort    | O(n²)      | O(n²)      | O(1)  |
    | Selection Sort | O(n²)      | O(n²)      | O(1)  |
    | Insertion Sort | O(n²)      | O(n²)      | O(1)  |
    | Merge Sort     | O(n log n) | O(n log n) | O(n)  |
    | Quick Sort     | O(n log n) | O(n²)      | O(1)  |
    | Counting Sort  | O(n + k)   | O(n + k)   | O(k)  |
    """)


if __name__ == "__main__":
    main()
