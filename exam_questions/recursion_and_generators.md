# שאלות מבחן - רקורסיה וגנרטורים

---

## שאלה 1: פיבונאצ'י עם זהות הונסברגר (2022b מועד א', שאלה 2)

**זהות הונסברגר:** F_{m+n} = F_{m-1}·F_n + F_m·F_{n+1}

```python
def fib_hons(k):
    if k <= 1:
        return k
    if k == 2:
        return 1

    m = k // 2
    n = k - m

    fm_1 = fib_hons(m - 1)
    fm = fib_hons(m)
    fn = fib_hons(n)
    fn_1 = fib_hons(n + 1)

    return fm_1 * fn + fm * fn_1
```

**סיבוכיות:** O(log k) - בכל קריאה k מתחלק ב-2

---

## שאלה 2: גנרטור לאינדקסים עולים (2023a מועד א', שאלה 4א')

**בעיה:** ייצר כל הרשימות באורך k מ-i ל-j עם אינדקסים עולים

```python
def asc_ind(i, j, k):
    if k == 2:
        if i < j:
            yield [i, j]
        return

    for m in range(i + 1, j):
        for rest in asc_ind(m, j, k - 1):
            yield [i] + rest
```

**דוגמה:** `asc_ind(3, 8, 4)` →
`[3,4,5,8], [3,4,6,8], [3,4,7,8], [3,5,6,8], [3,5,7,8], [3,6,7,8]`

---

## שאלה 3: פרמוטציות לקסיקוגרפיות (2023b מועד א', שאלה 2)

```python
def local_lex(lst, k):
    if len(lst) == 1:
        return lst

    n = len(lst)
    fact = factorial(n - 1)
    idx = k // fact
    first = lst[idx]
    rest = lst[:idx] + lst[idx+1:]

    return [first] + local_lex(rest, k % fact)
```

**סיבוכיות:** Θ(n²) - בגלל חיתוך הרשימות

---

## שאלה 4: Scope ופונקציות מקוננות (2023b מועד א', שאלה 1ג')

```python
def what():
    lst = [10, [4,5]]
    def who(x):
        def when(y):
            y[1] = 2
        when(x)
        x = 1
    who(lst[1])
    print(lst)  # [10, [4, 2]]
    who(lst)
    print(lst)  # [10, [4, 2]]
```

**טריקים חשובים:**
1. `when(x)` משנה את y[1], לא את x
2. `x = 1` יוצר משתנה מקומי חדש, לא משנה את lst
3. רשימות מועברות by reference

---

## שאלה 5: CYK מורחב (2023a מועד א', שאלה 4ב')

```python
def new_cyk_rec(rule_dict, var, st, i, j):
    if i == j-1:
        return st[i] in rule_dict[var]

    for var_rule in rule_dict[var]:
        rule_len = len(var_rule)
        if rule_len >= 2:
            for indices in asc_ind(i, j, rule_len + 1):
                # indices = [i, k1, k2, ..., j]
                valid = True
                for t in range(rule_len):
                    if not new_cyk_rec(rule_dict, var_rule[t],
                                       st, indices[t], indices[t+1]):
                        valid = False
                        break
                if valid:
                    return True
    return False
```

---

## שאלה 6: פלינדרום רקורסיבי (2024a מועד א', שאלה 1ב')

```python
def is_pal(s):
    if s == "":
        return True
    return s[0] == s[-1] and is_pal(s[1:-1])
```

**הערה:** יש להשלים שורה אחת בלבד!

---

## שאלה 7: רשימה ממוינת רקורסיבית (2024a מועד ב', שאלה 1ג')

```python
def is_sorted(L):
    if len(L) <= 1:
        return True
    return L[0] <= L[1] and is_sorted(L[1:])
```

**הערה:** יש להשלים שורה אחת בלבד!

---

## שאלה 8: גנרטורים - merge ו-filter (2024a מועד ב', שאלה 1ו')

```python
def merge(gen1, gen2):
    left = next(gen1)
    right = next(gen2)
    while True:
        if left <= right:
            yield left
            left = next(gen1)
        else:
            yield right
            right = next(gen2)

def naturals():
    n = 0
    while True:
        yield n
        n += 1

def filter(gen, n):
    val = next(gen)
    while True:
        if val < n:
            yield val
            val = next(gen)
```

**שאלות:**

| קטע קוד | תסתיים? |
|---------|----------|
| `x = merge(naturals(), naturals()); w = next(x)` | כן |
| `x = merge(merge(naturals(),naturals()),naturals()); w = next(x)` | כן |
| `x = filter(naturals(),-10); w = next(x)` | לא (אין val < -10) |
| `x = filter(naturals(),10**10); w = next(x)` | כן |
| `x = naturals` | כן (רק השמה, לא קריאה) |

---

## שאלה 9: LCS - Longest Common Subsequence (2025a מועד א', שאלה 2)

**הגדרה:** תת מחרוזת של st היא מילה שנוצרת מבחירת תווים (לא בהכרח רצופים) בסדר עולה.

```python
def lcs(st1, st2):
    return lcs_rec(st1, st2, len(st1), len(st2))

def lcs_rec(st1, st2, m, n):
    if m == 0 or n == 0:
        return 0
    if st1[m-1] == st2[n-1]:
        return 1 + lcs_rec(st1, st2, m-1, n-1)
    else:
        return max(lcs_rec(st1, st2, m-1, n), lcs_rec(st1, st2, m, n-1))
```

**דוגמאות:**
- LCS("bxcg", "abcdefg") = 3 ("bcg")
- LCS("aaa", "aba") = 2 ("aa")
- LCS("aaaa", "xyz") = 0

**סיבוכיות:**
- מקרה טוב: O(n) - כשכל התווים זהים
- מקרה גרוע: O(2ⁿ) - עץ רקורסיה אקספוננציאלי

---

## שאלה 10: LCS עם Memoization (2025a מועד א', שאלה 2ג')

```python
def lcs_mem(st1, st2):
    m, n = len(st1), len(st2)
    memo = {}

    def lcs_rec(i, j):
        if i == 0 or j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        if st1[i-1] == st2[j-1]:
            result = 1 + lcs_rec(i-1, j-1)
        else:
            result = max(lcs_rec(i-1, j), lcs_rec(i, j-1))

        memo[(i, j)] = result
        return result

    return lcs_rec(m, n)
```

**סיבוכיות עם memoization:** O(m·n)

---

## שאלה 11: Longest Monotone Subsequence (2025a מועד א', שאלה 2ד')

**מחרוזת מונוטונית עולה:** תווים בסדר לקסיקוגרפי עולה (כולל חזרות)

```python
def longest_monotone(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return lcs_mem(st, alphabet)
```

**דוגמאות:**
- longest_monotone("axbyczd") = 4 ("abcd")
- longest_monotone("aabaa") = 4 ("aaaa")

**הסבר:** המחרוזת המונוטונית הארוכה ביותר היא ה-LCS עם האלפבית הממוין!

---

## קישורים לסיכומים

- [פונקציות ורקורסיה](../notes/functions_and_recursion.md)
- [Memoization](../notes/memoization.md)
- [איטרטורים וגנרטורים](../notes/iterators_generators.md)
