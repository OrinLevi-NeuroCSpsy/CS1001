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

## שאלה 12: גנרטורים עם השהייה סופית (2024b מועד א', שאלה 1ה')

**הגדרות:**
- גנרטור בעל **השהייה סופית** - כל next מחזיר ערך תוך זמן סופי
- גנרטור **מייצר קבוצה S** - מחזיר כל איבר מ-S פעם אחת בדיוק

**שאלות:**

| גנרטור | ניתן לבנות? |
|--------|-------------|
| gen1(g1, g2) - חיתוך שני גנרטורים אינסופיים | **לא ניתן** |
| gen2(g1, g2) - איחוד שני גנרטורים אינסופיים | **ניתן** (round-robin) |
| gen3(lst) - איחוד רשימה של גנרטורים | **ניתן** |
| gen4(gen_of_gens) - איחוד גנרטור של גנרטורים | **ניתן** |

**הסבר:** חיתוך לא ניתן כי אולי אף פעם לא נמצא איבר משותף!

---

## שאלה 13: חלוקות של מספר שלם (2024b מועד ב', שאלה 2)

**הגדרה:** חלוקה (partition) של n היא הצגתו כסכום של שלמים חיוביים.

**דוגמאות:**
- partitions(3) = [[3], [2,1], [1,1,1]]
- partitions(5) = [[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]]

```python
def partitions(x):
    return rec(x, 1)

def rec(x, min_val):
    if x < min_val:
        return []
    if x == min_val:
        return [[x]]

    result = [[x]]  # x עצמו כחלוקה
    for i in range(min_val, x):
        for rest in rec(x - i, i):
            result.append([i] + rest)
    return result
```

**סיבוכיות:** לא פולינומית! מספר החלוקות גדל כ-2^√x

**שאלה:** האם ניתן לממש num_partitions בזמן פולינומי?
**תשובה:** כן! עם תכנות דינמי, O(x²)

---

## שאלה 14: Memoization - מתי משפר? (2024b מועד ב', שאלה 1ו')

| אלגוריתם | Memoization משפר? |
|----------|-------------------|
| חיפוש בינארי רקורסיבי | **לא** - אין חישובים חוזרים |
| Quicksort | **לא** - הרשימות שונות בכל קריאה |
| מגדלי האנוי | **לא** - אותה בעיה לא נפתרת פעמיים |
| Binom(n,k) | **כן** - אותם (n,k) מחושבים הרבה פעמים |

---

## שאלה 15: LIS - Longest Increasing Subsequence (2025a מועד ב', שאלה 2)

**הגדרה:** תת-סדרה עולה של sr היא תת-סדרה שכל מספר בה גדול ממש מהמספר שלפניו.

```python
def LIS(lst):
    initial_prev = min(lst) - 1
    return LIS_rec(lst, 0, initial_prev)

def LIS_rec(lst, i, prev):
    if i == len(lst):
        return 0
    # אפשרות 1: לא לכלול את lst[i]
    skip = LIS_rec(lst, i + 1, prev)
    # אפשרות 2: לכלול את lst[i] (רק אם גדול מ-prev)
    take = 0
    if lst[i] > prev:
        take = 1 + LIS_rec(lst, i + 1, lst[i])
    return max(skip, take)
```

**דוגמאות:**
- LIS([1, 2, 6, 2, 4.5, 7]) = 4 ([1,2,4.5,7])
- LIS([10, 5, 1]) = 1
- LIS([10]) = 1

**עומק עץ רקורסיה:** k = log(n) → עומק n במקרה הגרוע

---

## שאלה 16: LIS_include - LIS עם אילוץ (2025a מועד ב', שאלה 2ב')

**בעיה:** מצא אורך LIS שחייב לכלול איברים באינדקסים מסוימים.

```python
def LIS_include(lst, idxs):
    # בדוק שהאינדקסים הנדרשים יוצרים סדרה עולה
    for i in range(len(idxs) - 1):
        if lst[idxs[i]] >= lst[idxs[i+1]]:
            return -1

    res = len(idxs)
    for i in range(len(idxs) - 1):
        # מצא LIS בין שני אינדקסים עוקבים
        sub_lst = lst[idxs[i]+1 : idxs[i+1]]
        if len(sub_lst) > 0:
            # סנן רק ערכים בטווח המתאים
            filtered = [x for x in sub_lst
                       if lst[idxs[i]] < x < lst[idxs[i+1]]]
            if filtered:
                res += LIS(filtered)
    return res
```

**דוגמאות:**
- LIS_include([1,100,5,200,300,10,400], [0,5,6]) = 4 → [1,5,10,400]
- LIS_include([50,100,200,300,10,400], [0,3,4,5]) = -1 (300 > 10)

---

## שאלה 17: גנרטור לפלטי פונקציה (2025a מועד ב', שאלה 1ד')

**בעיה:** נתונה פונקציה f שמקבלת מספר שלם חיובי ומחזירה מספר כלשהו. רוצים גנרטור שמייצר את כל הפלטים האפשריים של f.

**שאלה:** האם ניתן לממש גנרטור כזה בעל השהייה סופית?

**תשובה:** **ניתן!**

```python
def outputs_generator(f):
    seen = set()
    n = 1
    while True:
        result = f(n)
        if result not in seen:
            seen.add(result)
            yield result
        n += 1
```

**הסבר:** לכל פלט של f קיים קלט שמייצר אותו, אז בסופו של דבר נמצא כל פלט.

---

## שאלה 18: חלוקת סטודנטים לקבוצות (2025b מועד א', שאלה 2)

**בעיה:** חלק n סטודנטים (לפי גבהים ממוינים) ל-k קבוצות כך שסכום הפרשי הגבהים מינימלי.

```python
def min_sum_heights_diff(hgts, k):
    return rec(hgts, 0, k)

def rec(hgts, start, k):
    n = len(hgts)
    if start >= n:
        return 0
    if k == 1:
        return hgts[n-1] - hgts[start]  # הפרש בין ראשון לאחרון

    scores = []
    for end in range(start, n - k + 1):
        # קבוצה מ-start עד end
        group_diff = hgts[end] - hgts[start] if end > start else 0
        rest = rec(hgts, end + 1, k - 1)
        scores.append(group_diff + rest)
    return min(scores)
```

**עומק עץ רקורסיה:** k (מספר הקבוצות)

**פתרון איטרטיבי O(n log n):**
```python
def min_sum_heights_diff(heights, k):
    diff = [heights[i+1] - heights[i] for i in range(len(heights)-1)]
    diff.sort(reverse=True)
    return sum(diff) - sum(diff[:k-1])
```

**הסבר:** מחלקים במקומות עם ההפרשים הגדולים ביותר!

---

## שאלה 19: שאלות על גנרטורים (2025b מועד ב', שאלה 1ב')

**(i) מה יודפס?**
```python
def g():
    yield 10
    yield 20

x = g()
print(next(x))
```
**תשובה:** 10 - next מחזיר את הערך הראשון

**(ii) מה הטיפוס של x?**
```python
def create_generator():
    i = 1
    while True:
        i += 1
        return i

x = create_generator()
```
**תשובה:** int - הפונקציה משתמשת ב-return ולא yield, אז היא פונקציה רגילה!

**(iii) זמן וזיכרון:**
```python
l_1 = [x for x in range(10**6)]  # שורה 1
l_2 = (x for x in range(10**6))  # שורה 2
```
**תשובה:** שורה 1 תיקח זמן רב יותר, ו-l_1 יתפוס מקום רב יותר.

**הסבר:** l_1 הוא list comprehension - יוצר את כל הרשימה מיד. l_2 הוא generator expression - מייצר ערכים רק כשמבקשים.

---

## שאלה 20: עץ רקורסיה של subset_sum (2025b מועד ב', שאלה 1ג')

```python
def subset_sum(L, s):
    if s == 0:
        return True
    if L == []:
        return False
    with_first = subset_sum(L[1:], s - L[0])
    without_first = subset_sum(L[1:], s)
    return with_first or without_first

subset_sum([2, 4, 7, -1], 6)
```

**כמות קודקודים בכל רמה:**

| רמה | כמות |
|-----|------|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 7 (לא 8 כי יש עצירה מוקדמת עם s=0) |
| 4 | 8 |

**הסבר:** בדרך כלל כל צומת מתפצל ל-2, אבל כאשר s=0 יש עצירה מוקדמת.

---

## שאלה 21: ספירת מסלולים בסריג עם Memoization (2025b מועד ב', שאלה 3)

```python
def cnt_paths_2d_mem(gp):
    part_paths_dict = {}
    return cnt_paths_2d_mem_rec(gp, part_paths_dict)

def cnt_paths_2d_mem_rec(gp, part_paths_dict):
    if gp[0] == gp[1] == 0:
        return 1
    result = 0

    if gp[0] > 0:
        p0 = (gp[0]-1, gp[1])
        if p0 not in part_paths_dict:
            part_paths_dict[p0] = cnt_paths_2d_mem_rec(p0, part_paths_dict)
        result += part_paths_dict[p0]

    if gp[1] > 0:
        p1 = (gp[0], gp[1]-1)
        if p1 not in part_paths_dict:
            part_paths_dict[p1] = cnt_paths_2d_mem_rec(p1, part_paths_dict)
        result += part_paths_dict[p1]

    return result
```

**סיבוכיות:** O(x·y) - יש (x+1)·(y+1) תתי-בעיות שונות.

**הוספת מכשולים (שורה 11):**
```python
if gp in obstacles_list:
    return 0
```

**סיבוכיות עם מכשולים:** O(x·y·n) - אם obstacles_list היא רשימה, בדיקת `in` היא O(n).

**הוספת מסלולים אלכסוניים:**
```python
if gp[0] > 0 and gp[1] > 0:
    p2 = (gp[0]-1, gp[1]-1)
    if p2 not in part_paths_dict:
        part_paths_dict[p2] = cnt_paths_2d_mem_rec(p2, part_paths_dict)
    result += part_paths_dict[p2]
```

**סיבוכיות עם אלכסוניים:** עדיין O(x·y)

---

## קישורים לסיכומים

- [פונקציות ורקורסיה](../notes/functions_and_recursion.md)
- [Memoization](../notes/memoization.md)
- [איטרטורים וגנרטורים](../notes/iterators_generators.md)
