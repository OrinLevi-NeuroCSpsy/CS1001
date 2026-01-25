# עיבוד תמונות (Image Processing) - סיכום לבחינה

---

## מושגי יסוד

### מהי תמונה דיגיטלית?
**מטריצה** של פיקסלים - כל פיקסל מייצג צבע/בהירות בנקודה מסוימת.

### סוגי תמונות

| סוג | תיאור | ערכים |
|-----|-------|-------|
| **שחור-לבן (Binary)** | כל פיקסל 0 או 1 | 0=שחור, 1=לבן |
| **גווני אפור (Grayscale)** | רמות אפור | 0-255 (8 ביט) |
| **צבעונית (RGB)** | שלושה ערוצים | (R,G,B) כל אחד 0-255 |

### ייצוג בפייתון

```python
# תמונת גווני אפור כרשימת רשימות
image = [
    [0,   50,  100],
    [150, 200, 255],
    [100, 50,  0]
]

# גישה לפיקסל
pixel = image[row][col]  # שורה, עמודה

# ממדים
height = len(image)      # מספר שורות
width = len(image[0])    # מספר עמודות
```

---

## פעולות בסיסיות

### שלילה (Negative)

הופך את הבהירות: כהה → בהיר, בהיר → כהה.

```python
def negative(image):
    """שלילת תמונה"""
    height = len(image)
    width = len(image[0])
    result = []

    for row in range(height):
        new_row = []
        for col in range(width):
            new_row.append(255 - image[row][col])
        result.append(new_row)

    return result

# קיצור עם list comprehension
def negative(image):
    return [[255 - pixel for pixel in row] for row in image]
```

### סף (Threshold)

ממיר לשחור-לבן לפי ערך סף.

```python
def threshold(image, thresh=128):
    """המרה לשחור-לבן לפי סף"""
    return [[255 if pixel >= thresh else 0
             for pixel in row]
            for row in image]

# דוגמה
image = [[100, 150, 200], [50, 130, 80]]
threshold(image, 128)
# [[0, 255, 255], [0, 255, 0]]
```

### בהירות (Brightness)

מוסיף/מחסיר מכל הפיקסלים.

```python
def adjust_brightness(image, delta):
    """שינוי בהירות"""
    result = []
    for row in image:
        new_row = []
        for pixel in row:
            # מוודא שהתוצאה בטווח 0-255
            new_val = max(0, min(255, pixel + delta))
            new_row.append(new_val)
        result.append(new_row)
    return result

# קיצור
def adjust_brightness(image, delta):
    return [[max(0, min(255, p + delta)) for p in row] for row in image]
```

### ניגודיות (Contrast)

מכפיל את המרחק מ-128.

```python
def adjust_contrast(image, factor):
    """שינוי ניגודיות"""
    return [[max(0, min(255, int(128 + (p - 128) * factor)))
             for p in row]
            for row in image]

# factor > 1: ניגודיות גבוהה יותר
# factor < 1: ניגודיות נמוכה יותר
```

---

## סינון (Filtering)

### מהו פילטר/קרנל?
מטריצה קטנה שמחליקים על התמונה ומבצעים חישוב על הסביבה.

### קונבולוציה (Convolution)

```python
def convolve(image, kernel):
    """קונבולוציה - הפעלת פילטר על תמונה"""
    h = len(image)
    w = len(image[0])
    kh = len(kernel)
    kw = len(kernel[0])
    pad_h = kh // 2
    pad_w = kw // 2

    result = [[0] * w for _ in range(h)]

    for i in range(pad_h, h - pad_h):
        for j in range(pad_w, w - pad_w):
            total = 0
            for ki in range(kh):
                for kj in range(kw):
                    row = i + ki - pad_h
                    col = j + kj - pad_w
                    total += image[row][col] * kernel[ki][kj]
            result[i][j] = max(0, min(255, int(total)))

    return result
```

### פילטר ממוצע (Average/Box Filter)

מחליק רעש על ידי ממוצע הסביבה.

```python
# קרנל 3×3
average_kernel = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
]

def average_filter(image, size=3):
    """סינון ממוצע פשוט"""
    h = len(image)
    w = len(image[0])
    pad = size // 2
    result = [[0] * w for _ in range(h)]

    for i in range(pad, h - pad):
        for j in range(pad, w - pad):
            total = 0
            count = 0
            for di in range(-pad, pad + 1):
                for dj in range(-pad, pad + 1):
                    total += image[i + di][j + dj]
                    count += 1
            result[i][j] = total // count

    return result
```

### פילטר גאוס (Gaussian Filter)

ממוצע משוקלל - משקל גבוה יותר למרכז.

```python
gaussian_kernel = [
    [1/16, 2/16, 1/16],
    [2/16, 4/16, 2/16],
    [1/16, 2/16, 1/16]
]
```

### פילטר מדיאנה (Median Filter)

ממיין את הסביבה ולוקח את האמצעי. **טוב לרעש "מלח ופלפל"**.

```python
def median_filter(image, size=3):
    """סינון מדיאנה"""
    h = len(image)
    w = len(image[0])
    pad = size // 2
    result = [[0] * w for _ in range(h)]

    for i in range(pad, h - pad):
        for j in range(pad, w - pad):
            neighborhood = []
            for di in range(-pad, pad + 1):
                for dj in range(-pad, pad + 1):
                    neighborhood.append(image[i + di][j + dj])
            neighborhood.sort()
            result[i][j] = neighborhood[len(neighborhood) // 2]

    return result
```

---

## גילוי קצוות (Edge Detection)

### מהם קצוות?
מקומות בתמונה עם **שינוי חד** בבהירות.

### פילטר Sobel

מחשב גרדיאנט (נגזרת) בכיוון X ו-Y.

```python
# גרדיאנט אופקי (קצוות אנכיים)
sobel_x = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

# גרדיאנט אנכי (קצוות אופקיים)
sobel_y = [
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
]

def sobel_edge(image):
    """גילוי קצוות Sobel"""
    gx = convolve(image, sobel_x)
    gy = convolve(image, sobel_y)

    h = len(image)
    w = len(image[0])
    result = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            # גודל הגרדיאנט
            magnitude = int((gx[i][j]**2 + gy[i][j]**2)**0.5)
            result[i][j] = min(255, magnitude)

    return result
```

### פילטר Laplacian

מחשב נגזרת שנייה - קצוות בכל הכיוונים.

```python
laplacian = [
    [0,  1, 0],
    [1, -4, 1],
    [0,  1, 0]
]

# או גרסה עם אלכסונים
laplacian_8 = [
    [1,  1, 1],
    [1, -8, 1],
    [1,  1, 1]
]
```

---

## טרנספורמציות גיאומטריות

### סיבוב 90° ימינה

```python
def rotate_90_right(image):
    """סיבוב 90 מעלות ימינה"""
    h = len(image)
    w = len(image[0])
    result = [[0] * h for _ in range(w)]

    for i in range(h):
        for j in range(w):
            result[j][h - 1 - i] = image[i][j]

    return result
```

### סיבוב 90° שמאלה

```python
def rotate_90_left(image):
    """סיבוב 90 מעלות שמאלה"""
    h = len(image)
    w = len(image[0])
    result = [[0] * h for _ in range(w)]

    for i in range(h):
        for j in range(w):
            result[w - 1 - j][i] = image[i][j]

    return result
```

### היפוך אופקי (Flip Horizontal)

```python
def flip_horizontal(image):
    """היפוך אופקי (מראה)"""
    return [row[::-1] for row in image]
```

### היפוך אנכי (Flip Vertical)

```python
def flip_vertical(image):
    """היפוך אנכי"""
    return image[::-1]
```

### שינוי גודל (Resize) - Nearest Neighbor

```python
def resize(image, new_h, new_w):
    """שינוי גודל בשיטת השכן הקרוב"""
    h = len(image)
    w = len(image[0])
    result = [[0] * new_w for _ in range(new_h)]

    for i in range(new_h):
        for j in range(new_w):
            # מיפוי למיקום המקורי
            src_i = int(i * h / new_h)
            src_j = int(j * w / new_w)
            result[i][j] = image[src_i][src_j]

    return result
```

---

## היסטוגרמה

### מהי?
התפלגות ערכי הפיקסלים בתמונה.

```python
def histogram(image):
    """חישוב היסטוגרמה"""
    hist = [0] * 256

    for row in image:
        for pixel in row:
            hist[pixel] += 1

    return hist
```

### איזון היסטוגרמה (Histogram Equalization)

משפר ניגודיות על ידי "מריחה" אחידה של הערכים.

```python
def histogram_equalization(image):
    """איזון היסטוגרמה"""
    h = len(image)
    w = len(image[0])
    total_pixels = h * w

    # חישוב היסטוגרמה
    hist = histogram(image)

    # חישוב CDF (Cumulative Distribution Function)
    cdf = [0] * 256
    cdf[0] = hist[0]
    for i in range(1, 256):
        cdf[i] = cdf[i-1] + hist[i]

    # מיפוי ערכים חדשים
    mapping = [int(255 * cdf[i] / total_pixels) for i in range(256)]

    # יצירת תמונה חדשה
    return [[mapping[pixel] for pixel in row] for row in image]
```

---

## עבודה עם תמונות צבעוניות

### ייצוג RGB

```python
# תמונה צבעונית: כל פיקסל הוא (R, G, B)
color_image = [
    [(255, 0, 0), (0, 255, 0), (0, 0, 255)],  # אדום, ירוק, כחול
    [(255, 255, 0), (255, 0, 255), (0, 255, 255)]  # צהוב, מגנטה, ציאן
]
```

### המרה לגווני אפור

```python
def rgb_to_gray(color_image):
    """המרה לגווני אפור"""
    result = []
    for row in color_image:
        gray_row = []
        for r, g, b in row:
            # נוסחה סטנדרטית (משקולות לפי רגישות העין)
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            gray_row.append(gray)
        result.append(gray_row)
    return result

# או פשוט ממוצע
def rgb_to_gray_simple(color_image):
    return [[(r + g + b) // 3 for r, g, b in row] for row in color_image]
```

### הפרדת ערוצים

```python
def split_channels(color_image):
    """הפרדה לערוצי R, G, B"""
    h = len(color_image)
    w = len(color_image[0])

    r_channel = [[color_image[i][j][0] for j in range(w)] for i in range(h)]
    g_channel = [[color_image[i][j][1] for j in range(w)] for i in range(h)]
    b_channel = [[color_image[i][j][2] for j in range(w)] for i in range(h)]

    return r_channel, g_channel, b_channel
```

---

## טעויות נפוצות

### טעות 1: חריגה מטווח 0-255

```python
# שגוי
new_pixel = pixel + 100  # יכול להיות > 255

# נכון
new_pixel = max(0, min(255, pixel + 100))
```

### טעות 2: בלבול בין שורות ועמודות

```python
# image[row][col] = image[y][x]
# לא image[x][y]!

height = len(image)      # מספר שורות (y)
width = len(image[0])    # מספר עמודות (x)
```

### טעות 3: שכחת padding בקונבולוציה

```python
# פילטר 3×3 דורש padding של 1
# לכן הלולאה מתחילה מ-1 ולא מ-0
for i in range(1, h - 1):
    for j in range(1, w - 1):
```

### טעות 4: שינוי התמונה המקורית

```python
# שגוי - משנה את המקור
def negative(image):
    for row in image:
        for i in range(len(row)):
            row[i] = 255 - row[i]
    return image

# נכון - יוצר עותק חדש
def negative(image):
    return [[255 - p for p in row] for row in image]
```

---

## שאלות בחינה טיפוסיות

### שאלה 1: מה עושה הקוד?

```python
def mystery(image):
    return [[image[i][j]
             for i in range(len(image))]
            for j in range(len(image[0]))]
```

**תשובה:** טרנספוזיציה - מחליף שורות ועמודות (סיבוב + היפוך).

---

### שאלה 2: כתוב פונקציה

כתוב פונקציה שמקבלת תמונה ומחזירה את הפיקסל הבהיר ביותר.

**פתרון:**
```python
def brightest_pixel(image):
    max_val = 0
    max_pos = (0, 0)
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] > max_val:
                max_val = image[i][j]
                max_pos = (i, j)
    return max_val, max_pos
```

---

### שאלה 3: פילטר

מה יהיה הערך במרכז אחרי הפעלת הפילטר?

```
תמונה:          פילטר:
1 2 3           0  1  0
4 5 6           1 -4  1
7 8 9           0  1  0
```

**פתרון:**
```
result = 0×1 + 1×2 + 0×3 +
         1×4 + (-4)×5 + 1×6 +
         0×7 + 1×8 + 0×9
       = 2 + 4 - 20 + 6 + 8
       = 0
```

---

### שאלה 4: סיבוב

אחרי סיבוב 90° ימינה, מה יהיו ממדי התמונה?

תמונה מקורית: 3×5 (3 שורות, 5 עמודות)

**תשובה:** 5×3 (5 שורות, 3 עמודות)

---

## סיכום נקודות חשובות

- [ ] תמונה = **מטריצה** של פיקסלים, `image[row][col]`
- [ ] ערכים בטווח **0-255** (8 ביט)
- [ ] **שלילה**: `255 - pixel`
- [ ] **סף**: המרה לשחור-לבן
- [ ] **קונבולוציה**: הפעלת פילטר על סביבת פיקסל
- [ ] **ממוצע/גאוס**: החלקה ורעש
- [ ] **מדיאנה**: טוב לרעש "מלח ופלפל"
- [ ] **Sobel**: גילוי קצוות (גרדיאנט)
- [ ] **סיבוב 90°**: מחליף בין height ו-width
- [ ] **RGB לאפור**: `0.299R + 0.587G + 0.114B`
- [ ] תמיד לוודא ש: `0 ≤ result ≤ 255`
