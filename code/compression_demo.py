"""
דחיסת מידע - האפמן ו-LZ
מבוא למדעי המחשב
"""

from collections import Counter
import heapq


# ========================================
# קידוד האפמן
# ========================================

class HuffmanNode:
    """צומת בעץ האפמן"""

    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def is_leaf(self):
        return self.left is None and self.right is None


def build_huffman_tree(text):
    """בניית עץ האפמן מטקסט"""
    # ספירת תדירויות
    freq = Counter(text)
    print(f"תדירויות: {dict(freq)}")

    # יצירת ערימת מינימום
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    # בניית העץ
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def build_codes(node, prefix="", codes=None):
    """בניית טבלת קידוד מעץ האפמן"""
    if codes is None:
        codes = {}

    if node is None:
        return codes

    if node.is_leaf():
        codes[node.char] = prefix if prefix else "0"
    else:
        build_codes(node.left, prefix + "0", codes)
        build_codes(node.right, prefix + "1", codes)

    return codes


def huffman_encode(text):
    """קידוד האפמן"""
    tree = build_huffman_tree(text)
    codes = build_codes(tree)
    encoded = ''.join(codes[char] for char in text)
    return encoded, codes, tree


def huffman_decode(encoded, tree):
    """פענוח האפמן"""
    if tree is None:
        return ""

    result = []
    node = tree

    for bit in encoded:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.is_leaf():
            result.append(node.char)
            node = tree

    return ''.join(result)


# ========================================
# אלגוריתם LZ (Lempel-Ziv)
# ========================================

def lz_encode(text, window_size=10):
    """קידוד LZ פשוט"""
    result = []
    i = 0

    while i < len(text):
        # חפש התאמה בחלון
        best_offset = 0
        best_length = 0

        start = max(0, i - window_size)
        for j in range(start, i):
            length = 0
            while (i + length < len(text) and
                   j + length < i and
                   text[j + length] == text[i + length]):
                length += 1

            if length > best_length:
                best_length = length
                best_offset = i - j

        if best_length > 0:
            # מצאנו התאמה
            next_char = text[i + best_length] if i + best_length < len(text) else ''
            result.append((best_offset, best_length, next_char))
            i += best_length + 1
        else:
            # אין התאמה
            result.append((0, 0, text[i]))
            i += 1

    return result


def lz_decode(encoded):
    """פענוח LZ"""
    result = []

    for offset, length, char in encoded:
        if length > 0:
            # העתק מהחלון
            start = len(result) - offset
            for i in range(length):
                result.append(result[start + i])
        if char:
            result.append(char)

    return ''.join(result)


def main():
    print("=" * 60)
    print("דחיסת מידע")
    print("=" * 60)

    # האפמן
    print("\n--- קידוד האפמן ---")
    text = "abracadabra"
    print(f"טקסט מקורי: '{text}'")
    print(f"אורך מקורי: {len(text) * 8} ביטים ({len(text)} תווים × 8 ביטים)")

    encoded, codes, tree = huffman_encode(text)

    print(f"\nטבלת קידוד:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}' -> {code}")

    print(f"\nמקודד: {encoded}")
    print(f"אורך מקודד: {len(encoded)} ביטים")
    print(f"יחס דחיסה: {len(encoded) / (len(text) * 8):.2%}")

    decoded = huffman_decode(encoded, tree)
    print(f"\nמפוענח: '{decoded}'")
    print(f"נכון: {decoded == text}")

    # LZ
    print("\n" + "=" * 60)
    print("--- אלגוריתם LZ ---")
    text = "abracadabra"
    print(f"טקסט מקורי: '{text}'")

    encoded_lz = lz_encode(text)
    print(f"\nמקודד (offset, length, char):")
    for triple in encoded_lz:
        print(f"  {triple}")

    decoded_lz = lz_decode(encoded_lz)
    print(f"\nמפוענח: '{decoded_lz}'")
    print(f"נכון: {decoded_lz == text}")

    # השוואה
    print("\n" + "=" * 60)
    print("השוואה בין השיטות")
    print("=" * 60)
    print("""
    | תכונה          | האפמן           | LZ              |
    |-----------------|-----------------|-----------------|
    | סוג             | סטטיסטי         | מילוני          |
    | צריך 2 מעברים   | כן (לבנות עץ)  | לא (online)     |
    | טוב ל...        | תדירויות שונות | חזרות ארוכות    |
    | שומר עץ/מילון  | כן              | לא              |
    """)


if __name__ == "__main__":
    main()
