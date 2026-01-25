"""
עיבוד תמונות - פעולות בסיסיות
מבוא למדעי המחשב
"""


# ========================================
# ייצוג תמונה כמטריצה
# ========================================

def create_sample_image(rows, cols, pattern="gradient"):
    """יצירת תמונה לדוגמה"""
    if pattern == "gradient":
        return [[int(255 * j / cols) for j in range(cols)] for i in range(rows)]
    elif pattern == "checkerboard":
        return [[(i + j) % 2 * 255 for j in range(cols)] for i in range(rows)]
    elif pattern == "random":
        import random
        return [[random.randint(0, 255) for j in range(cols)] for i in range(rows)]
    else:
        return [[128 for j in range(cols)] for i in range(rows)]


def print_image(img, title="Image"):
    """הדפסת תמונה (ASCII art)"""
    print(f"\n{title}:")
    chars = " .:-=+*#%@"
    for row in img:
        line = ""
        for pixel in row:
            idx = min(int(pixel / 256 * len(chars)), len(chars) - 1)
            line += chars[idx] * 2
        print(line)


# ========================================
# פעולות בסיסיות
# ========================================

def negative(img):
    """נגטיב - היפוך צבעים"""
    rows, cols = len(img), len(img[0])
    return [[255 - img[i][j] for j in range(cols)] for i in range(rows)]


def threshold(img, thresh=128):
    """סף - המרה לשחור-לבן"""
    rows, cols = len(img), len(img[0])
    return [[255 if img[i][j] > thresh else 0 for j in range(cols)]
            for i in range(rows)]


def flip_horizontal(img):
    """היפוך אופקי"""
    return [row[::-1] for row in img]


def flip_vertical(img):
    """היפוך אנכי"""
    return img[::-1]


def rotate_90(img):
    """סיבוב 90 מעלות עם כיוון השעון"""
    rows, cols = len(img), len(img[0])
    return [[img[rows - 1 - i][j] for i in range(rows)] for j in range(cols)]


def scale_down(img, factor=2):
    """הקטנה בפקטור"""
    rows, cols = len(img), len(img[0])
    new_rows, new_cols = rows // factor, cols // factor
    return [[img[i * factor][j * factor] for j in range(new_cols)]
            for i in range(new_rows)]


# ========================================
# פילטרים (Convolution)
# ========================================

def apply_kernel(img, kernel):
    """החלת מסנן (kernel) על תמונה"""
    rows, cols = len(img), len(img[0])
    k_size = len(kernel)
    k_half = k_size // 2

    result = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(k_half, rows - k_half):
        for j in range(k_half, cols - k_half):
            total = 0
            for ki in range(k_size):
                for kj in range(k_size):
                    total += img[i + ki - k_half][j + kj - k_half] * kernel[ki][kj]
            result[i][j] = max(0, min(255, int(total)))

    return result


def blur(img):
    """טשטוש (blur) - ממוצע של סביבה"""
    kernel = [[1/9, 1/9, 1/9],
              [1/9, 1/9, 1/9],
              [1/9, 1/9, 1/9]]
    return apply_kernel(img, kernel)


def sharpen(img):
    """חידוד (sharpen)"""
    kernel = [[0, -1, 0],
              [-1, 5, -1],
              [0, -1, 0]]
    return apply_kernel(img, kernel)


def edge_detect(img):
    """זיהוי קצוות (Sobel)"""
    kernel = [[-1, -1, -1],
              [-1, 8, -1],
              [-1, -1, -1]]
    return apply_kernel(img, kernel)


# ========================================
# חציון מקומי (מבחינה!)
# ========================================

def local_median(img, kx=1, ky=1):
    """
    חציון מקומי - מסנן רעשים
    kx, ky = רדיוס הסביבה
    """
    rows, cols = len(img), len(img[0])
    result = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            # אסוף ערכים מהסביבה
            neighbors = []
            for di in range(-kx, kx + 1):
                for dj in range(-ky, ky + 1):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbors.append(img[ni][nj])

            # מצא חציון
            neighbors.sort()
            result[i][j] = neighbors[len(neighbors) // 2]

    return result


def main():
    print("=" * 60)
    print("עיבוד תמונות")
    print("=" * 60)

    # יצירת תמונה לדוגמה
    img = create_sample_image(8, 16, "gradient")
    print_image(img, "תמונה מקורית (gradient)")

    # נגטיב
    neg = negative(img)
    print_image(neg, "נגטיב")

    # סף
    thresh = threshold(img, 128)
    print_image(thresh, "סף (threshold=128)")

    # לוח שחמט
    chess = create_sample_image(8, 16, "checkerboard")
    print_image(chess, "לוח שחמט")

    # היפוך
    flipped = flip_horizontal(chess)
    print_image(flipped, "היפוך אופקי")

    # סיכום קרנלים
    print("\n" + "=" * 60)
    print("קרנלים נפוצים")
    print("=" * 60)
    print("""
    Blur (ממוצע):           Sharpen (חידוד):
    [1/9  1/9  1/9]         [ 0  -1   0]
    [1/9  1/9  1/9]         [-1   5  -1]
    [1/9  1/9  1/9]         [ 0  -1   0]

    Edge Detection:          Gaussian Blur:
    [-1  -1  -1]            [1/16  2/16  1/16]
    [-1   8  -1]            [2/16  4/16  2/16]
    [-1  -1  -1]            [1/16  2/16  1/16]
    """)

    # חציון מקומי
    print("=" * 60)
    print("חציון מקומי (local median)")
    print("=" * 60)
    print("""
    def local_median(img, kx=1, ky=1):
        # לכל פיקסל:
        # 1. אסוף את הסביבה (2*kx+1) × (2*ky+1)
        # 2. מיין
        # 3. קח את האיבר האמצעי

    שימוש: הסרת רעש "מלח ופלפל"
    """)


if __name__ == "__main__":
    main()
