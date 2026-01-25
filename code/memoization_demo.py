"""
Memoization - שמירת תוצאות ביניים
מבוא למדעי המחשב
"""

import time


# ========================================
# פיבונאצ'י - השוואה
# ========================================

def fib_naive(n):
    """פיבונאצ'י נאיבי - O(2^n)"""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo=None):
    """פיבונאצ'י עם memoization - O(n)"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_memo_decorator(n, cache={}):
    """פיבונאצ'י עם cache כפרמטר ברירת מחדל"""
    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fib_memo_decorator(n - 1) + fib_memo_decorator(n - 2)
    cache[n] = result
    return result


# ========================================
# מטבעות - בעיית אופטימיזציה
# ========================================

def coin_change_naive(coins, amount):
    """מספר מינימלי של מטבעות - נאיבי"""
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        result = coin_change_naive(coins, amount - coin)
        if result != float('inf'):
            min_coins = min(min_coins, result + 1)

    return min_coins


def coin_change_memo(coins, amount, memo=None):
    """מספר מינימלי של מטבעות - עם memoization"""
    if memo is None:
        memo = {}
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        result = coin_change_memo(coins, amount - coin, memo)
        if result != float('inf'):
            min_coins = min(min_coins, result + 1)

    memo[amount] = min_coins
    return min_coins


# ========================================
# בעיית הילוך על מדרגות
# ========================================

def climb_stairs_naive(n):
    """כמה דרכים לעלות n מדרגות (צעד 1 או 2)"""
    if n <= 1:
        return 1
    return climb_stairs_naive(n - 1) + climb_stairs_naive(n - 2)


def climb_stairs_memo(n, memo=None):
    """עם memoization"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]


# ========================================
# LCS - תת-רצף משותף ארוך ביותר
# ========================================

def lcs_naive(s1, s2):
    """אורך LCS - נאיבי"""
    if not s1 or not s2:
        return 0
    if s1[-1] == s2[-1]:
        return 1 + lcs_naive(s1[:-1], s2[:-1])
    return max(lcs_naive(s1[:-1], s2), lcs_naive(s1, s2[:-1]))


def lcs_memo(s1, s2, memo=None):
    """אורך LCS - עם memoization"""
    if memo is None:
        memo = {}
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    if not s1 or not s2:
        return 0
    if s1[-1] == s2[-1]:
        result = 1 + lcs_memo(s1[:-1], s2[:-1], memo)
    else:
        result = max(lcs_memo(s1[:-1], s2, memo), lcs_memo(s1, s2[:-1], memo))
    memo[(s1, s2)] = result
    return result


def main():
    print("=" * 60)
    print("Memoization - השוואת ביצועים")
    print("=" * 60)

    # פיבונאצ'י
    print("\n--- פיבונאצ'י ---")
    n = 30

    start = time.time()
    result_naive = fib_naive(n)
    time_naive = time.time() - start

    start = time.time()
    result_memo = fib_memo(n)
    time_memo = time.time() - start

    print(f"fib({n}) = {result_naive}")
    print(f"נאיבי: {time_naive:.4f} שניות")
    print(f"memo:  {time_memo:.6f} שניות")
    print(f"שיפור: {time_naive / max(time_memo, 0.000001):.0f}x")

    # מטבעות
    print("\n--- מטבעות ---")
    coins = [1, 5, 10, 25]
    amount = 30

    start = time.time()
    result = coin_change_memo(coins, amount)
    elapsed = time.time() - start

    print(f"מטבעות: {coins}")
    print(f"סכום: {amount}")
    print(f"מספר מטבעות מינימלי: {result}")
    print(f"זמן: {elapsed:.6f} שניות")

    # מדרגות
    print("\n--- מדרגות ---")
    n = 30
    result = climb_stairs_memo(n)
    print(f"דרכים לעלות {n} מדרגות: {result}")

    # LCS
    print("\n--- LCS ---")
    s1, s2 = "ABCDGH", "AEDFHR"
    result = lcs_memo(s1, s2)
    print(f"LCS('{s1}', '{s2}') = {result}")

    print("\n" + "=" * 60)
    print("מתי להשתמש ב-Memoization?")
    print("=" * 60)
    print("""
    1. חפיפה בתתי-בעיות (overlapping subproblems)
    2. מבנה אופטימלי (optimal substructure)
    3. כשאותן קריאות חוזרות הרבה פעמים

    דוגמאות קלאסיות:
    - פיבונאצ'י
    - מטבעות
    - LCS
    - Edit Distance
    - בעיות תכנון דינמי
    """)


if __name__ == "__main__":
    main()
