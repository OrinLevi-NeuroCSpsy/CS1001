"""
זיכרון בפייתון - דוגמאות קוד
Memory Management in Python - Code Examples
"""

# ========================================
# 1. משתנים כמצביעים (References)
# ========================================

print("=" * 50)
print("1. Variables as References")
print("=" * 50)

x = [1, 2, 3]
print(f"x = {x}")
print(f"id(x) = {id(x)}")

y = x  # y מצביע לאותו אובייקט!
print(f"\ny = x")
print(f"id(y) = {id(y)}")
print(f"x is y: {x is y}")  # True - אותו אובייקט

z = [1, 2, 3]  # אובייקט חדש עם אותו ערך
print(f"\nz = [1, 2, 3]  # new object")
print(f"id(z) = {id(z)}")
print(f"x is z: {x is z}")  # False - אובייקטים שונים
print(f"x == z: {x == z}")  # True - ערכים שווים


# ========================================
# 2. == מול is
# ========================================

print("\n" + "=" * 50)
print("2. == vs is")
print("=" * 50)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"a = {a}")
print(f"b = a")
print(f"c = [1, 2, 3]")
print()
print(f"a == b: {a == b}  (same values)")
print(f"a == c: {a == c}  (same values)")
print(f"a is b: {a is b}  (same object)")
print(f"a is c: {a is c}  (different objects)")


# ========================================
# 3. Mutable vs Immutable
# ========================================

print("\n" + "=" * 50)
print("3. Mutable vs Immutable")
print("=" * 50)

# Immutable - int
print("\nImmutable (int):")
x = 5
print(f"x = {x}, id(x) = {id(x)}")
x = x + 1
print(f"x = x + 1 -> x = {x}, id(x) = {id(x)}  # new object!")

# Mutable - list
print("\nMutable (list):")
lst = [1, 2, 3]
print(f"lst = {lst}, id(lst) = {id(lst)}")
lst.append(4)
print(f"lst.append(4) -> lst = {lst}, id(lst) = {id(lst)}  # same object!")


# ========================================
# 4. Aliasing
# ========================================

print("\n" + "=" * 50)
print("4. Aliasing")
print("=" * 50)

# Basic aliasing
a = [1, 2, 3]
b = a  # b is an alias for a
print(f"a = {a}")
print(f"b = a")

b.append(4)
print(f"\nb.append(4)")
print(f"a = {a}  # a changed too!")
print(f"b = {b}")

# Aliasing in nested lists (common mistake!)
print("\nNested list aliasing (MISTAKE):")
row = [0, 0, 0]
matrix_bad = [row, row, row]  # all rows are the same object!
print(f"matrix_bad = {matrix_bad}")
matrix_bad[0][0] = 1
print(f"matrix_bad[0][0] = 1")
print(f"matrix_bad = {matrix_bad}  # all rows changed!")

print("\nCorrect way:")
matrix_good = [[0, 0, 0] for _ in range(3)]  # separate objects
print(f"matrix_good = {matrix_good}")
matrix_good[0][0] = 1
print(f"matrix_good[0][0] = 1")
print(f"matrix_good = {matrix_good}  # only first row changed")


# ========================================
# 5. Shallow Copy vs Deep Copy
# ========================================

print("\n" + "=" * 50)
print("5. Shallow Copy vs Deep Copy")
print("=" * 50)

import copy

original = [[1, 2], [3, 4]]
print(f"original = {original}")

# Shallow copy
shallow = copy.copy(original)  # or original[:] or list(original)
print(f"\nshallow = copy.copy(original)")
print(f"original is shallow: {original is shallow}  # different outer lists")
print(f"original[0] is shallow[0]: {original[0] is shallow[0]}  # same inner lists!")

shallow[0][0] = 999
print(f"\nshallow[0][0] = 999")
print(f"original = {original}  # original changed!")
print(f"shallow = {shallow}")

# Reset
original = [[1, 2], [3, 4]]

# Deep copy
deep = copy.deepcopy(original)
print(f"\noriginal = {original}")
print(f"deep = copy.deepcopy(original)")
print(f"original[0] is deep[0]: {original[0] is deep[0]}  # different inner lists!")

deep[0][0] = 999
print(f"\ndeep[0][0] = 999")
print(f"original = {original}  # original unchanged!")
print(f"deep = {deep}")


# ========================================
# 6. Functions and Mutability
# ========================================

print("\n" + "=" * 50)
print("6. Functions and Mutability")
print("=" * 50)

def add_one_int(n):
    """Immutable - doesn't change original"""
    n = n + 1
    return n

def add_element(lst):
    """Mutable - changes original!"""
    lst.append(4)

# Immutable
x = 5
result = add_one_int(x)
print(f"x = {x}")
print(f"add_one_int(x) returned {result}")
print(f"x after function: {x}  # unchanged")

# Mutable
print()
my_list = [1, 2, 3]
print(f"my_list = {my_list}")
add_element(my_list)
print(f"add_element(my_list)")
print(f"my_list after function: {my_list}  # changed!")


# ========================================
# 7. Default Mutable Arguments (MISTAKE!)
# ========================================

print("\n" + "=" * 50)
print("7. Default Mutable Arguments (MISTAKE!)")
print("=" * 50)

# BAD - default mutable argument
def bad_append(item, lst=[]):
    lst.append(item)
    return lst

print("bad_append with default []:")
print(f"bad_append(1) = {bad_append(1)}")
print(f"bad_append(2) = {bad_append(2)}  # Oops!")
print(f"bad_append(3) = {bad_append(3)}  # Getting worse!")

# GOOD - use None
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print("\ngood_append with None:")
print(f"good_append(1) = {good_append(1)}")
print(f"good_append(2) = {good_append(2)}")
print(f"good_append(3) = {good_append(3)}")


# ========================================
# 8. Call Stack Demonstration
# ========================================

print("\n" + "=" * 50)
print("8. Call Stack Demonstration")
print("=" * 50)

def factorial(n, depth=0):
    """Factorial with call stack visualization"""
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")

    if n <= 1:
        print(f"{indent}factorial({n}) returns 1 (base case)")
        return 1

    result = n * factorial(n - 1, depth + 1)
    print(f"{indent}factorial({n}) returns {result}")
    return result

print("Calculating factorial(4):")
print(f"Result: {factorial(4)}")


# ========================================
# 9. Recursion Trace
# ========================================

print("\n" + "=" * 50)
print("9. Recursion Trace (Fibonacci)")
print("=" * 50)

call_count = 0

def fib_traced(n, depth=0):
    """Fibonacci with trace"""
    global call_count
    call_count += 1

    indent = "  " * depth
    print(f"{indent}fib({n})")

    if n <= 1:
        return n

    return fib_traced(n - 1, depth + 1) + fib_traced(n - 2, depth + 1)

call_count = 0
result = fib_traced(4)
print(f"\nfib(4) = {result}")
print(f"Total calls: {call_count}")


# ========================================
# 10. Summary Table
# ========================================

print("\n" + "=" * 50)
print("10. Summary")
print("=" * 50)

print("""
| Operation          | Creates new object? | Copies nested? |
|--------------------|---------------------|----------------|
| b = a              | No (alias)          | N/A            |
| b = a[:]           | Yes (shallow)       | No             |
| b = list(a)        | Yes (shallow)       | No             |
| b = a.copy()       | Yes (shallow)       | No             |
| b = copy.deepcopy(a)| Yes (deep)         | Yes            |

Immutable types: int, float, str, tuple, bool, frozenset
Mutable types: list, dict, set, custom objects
""")
