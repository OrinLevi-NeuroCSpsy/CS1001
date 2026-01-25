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

## קישורים לסיכומים

- [פונקציות ורקורסיה](../notes/functions_and_recursion.md)
- [Memoization](../notes/memoization.md)
- [איטרטורים וגנרטורים](../notes/iterators_generators.md)
