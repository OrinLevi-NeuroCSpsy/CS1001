"""
רקורסיה - דוגמאות והדגמות
מבוא למדעי המחשב
"""


def factorial(n):
    """עצרת - n!"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci_naive(n):
    """פיבונאצ'י נאיבי - O(2^n)"""
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_efficient(n, memo=None):
    """פיבונאצ'י עם memoization - O(n)"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_efficient(n - 1, memo) + fibonacci_efficient(n - 2, memo)
    return memo[n]


def sum_list(lst):
    """סכום רשימה רקורסיבי"""
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


def reverse_string(s):
    """היפוך מחרוזת רקורסיבי"""
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def binary_search_rec(lst, target, low, high):
    """חיפוש בינארי רקורסיבי"""
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search_rec(lst, target, mid + 1, high)
    else:
        return binary_search_rec(lst, target, low, mid - 1)


def power(base, exp):
    """חזקה רקורסיבית - O(n)"""
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def power_fast(base, exp):
    """חזקה מהירה - O(log n)"""
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power_fast(base, exp // 2)
        return half * half
    else:
        return base * power_fast(base, exp - 1)


def flatten(nested_list):
    """שיטוח רשימה מקוננת"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def main():
    print("=" * 60)
    print("דוגמאות רקורסיה")
    print("=" * 60)

    # עצרת
    print("\nעצרת (factorial):")
    for n in range(6):
        print(f"  {n}! = {factorial(n)}")

    # פיבונאצ'י
    print("\nפיבונאצ'י:")
    print("  נאיבי (איטי):", [fibonacci_naive(i) for i in range(10)])
    print("  עם memo (מהיר):", [fibonacci_efficient(i) for i in range(10)])

    # סכום רשימה
    print("\nסכום רשימה:")
    lst = [1, 2, 3, 4, 5]
    print(f"  sum_list({lst}) = {sum_list(lst)}")

    # היפוך מחרוזת
    print("\nהיפוך מחרוזת:")
    s = "Hello"
    print(f"  reverse_string('{s}') = '{reverse_string(s)}'")

    # חזקה
    print("\nחזקה:")
    print(f"  power(2, 10) = {power(2, 10)}")
    print(f"  power_fast(2, 10) = {power_fast(2, 10)}")

    # שיטוח רשימה
    print("\nשיטוח רשימה מקוננת:")
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(f"  flatten({nested}) = {flatten(nested)}")


if __name__ == "__main__":
    main()
