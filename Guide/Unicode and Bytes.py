"""
Unicode & Bytes in Python for DSA (Entry-Level SWE) — What You Actually Need

────────────────────────────────────────────────────────
1) What “Unicode” means (simple)
────────────────────────────────────────────────────────
• Unicode = a global standard that assigns a unique code point to characters.
• Covers: English letters, accents (é), other scripts (你, 안), symbols (€, ✓), emoji (😀).

────────────────────────────────────────────────────────
2) Python strings are Unicode by default (VERY important)
────────────────────────────────────────────────────────
• In Python 3, `str` is Unicode text.
• All common DSA operations just work on Unicode:
  - Sorting: sorted(s)
  - Hashing: dict / set keys
  - Comparison: ==, <, >

→ This is why most Python string solutions already handle Unicode without changes.

────────────────────────────────────────────────────────
3) Characters vs Bytes (high-level, interview-relevant)
────────────────────────────────────────────────────────
• `str`   = human-readable text (Unicode characters)
• `bytes` = raw binary data (8-bit values, often from files/network)

Key idea:
• DSA problems almost always use `str`, NOT `bytes`.

You only deal with `bytes` when:
• Reading files
• Handling network data
• Explicitly encoding/decoding text

────────────────────────────────────────────────────────
Code example: str vs bytes
────────────────────────────────────────────────────────
"""

# str   = Unicode text → len() counts characters
# bytes = raw data    → len() counts bytes

text = "café 😊"           # 6 characters
print(len(text))           # → 6   (counts characters)

b = text.encode("utf-8")   # str → bytes
print(len(b))              # → 10  (counts bytes: c a f é(2) space 😊(4))
print(b)                   # b'caf\xc3\xa9 \xf0\x9f\x98\x8a'

s = b.decode("utf-8")      # bytes → str (back to original text)
print(s == text)           # True


"""
DSA interview rule:
• If the problem says “string”, assume `str`.
• Do NOT encode/decode unless explicitly required.

────────────────────────────────────────────────────────
4) Unicode-safe frequency counting (core DSA takeaway)
────────────────────────────────────────────────────────
• Dict / Counter / defaultdict work for ALL Unicode characters:
    count[c] += 1
• No special handling needed in Python.

This is why Python anagram solutions are Unicode-safe by default.

────────────────────────────────────────────────────────
5) Space complexity: O(1) vs O(U)
────────────────────────────────────────────────────────
• If input is guaranteed lowercase a–z:
    - At most 26 keys → O(1) space.
• If input allows Unicode / arbitrary characters:
    - Dictionary can grow with unique characters → O(U).

Where:
• U = number of distinct characters
• U ≤ N (string length)

────────────────────────────────────────────────────────
6) Sorting Unicode strings
────────────────────────────────────────────────────────
• `sorted(s)` sorts by Unicode code point order.
• For DSA, this is fine because you usually check equality:
    sorted(s) == sorted(t)
• Locale-aware sorting is NOT expected in interviews.

────────────────────────────────────────────────────────
7) Case handling: lower vs casefold (edge knowledge)
────────────────────────────────────────────────────────
• `.lower()` works for most cases.
• `.casefold()` is more correct for Unicode-wide case-insensitive comparison.

Interview rule:
• If constraints say “lowercase English letters”, ignore this.
• Mention casefold only if interviewer asks about Unicode + case-insensitive logic.

────────────────────────────────────────────────────────
8) Characters ≠ visual symbols (advanced, rarely needed)
────────────────────────────────────────────────────────
• Some visible characters are multiple code points:
    "é" = "e" + combining accent
• Emoji can be composed (skin tones, flags).

DSA reality:
• Problems treat Python characters as units.
• Mention this only if interviewer pushes on Unicode edge cases.

────────────────────────────────────────────────────────
9) Normalization (very rare, bonus knowledge)
────────────────────────────────────────────────────────
• Same-looking text can have different internal representations.
• `unicodedata.normalize` can standardize them.

Only bring this up if explicitly asked.

────────────────────────────────────────────────────────
10) Practical interview rule of thumb (MOST IMPORTANT)
────────────────────────────────────────────────────────
• Lowercase English only → O(1) space is valid.
• Unicode / any characters → use dict/Counter, say O(U) space.
• Python string solutions already support Unicode.
• Don’t overcomplicate unless prompted.

────────────────────────────────────────────────────────
Mini DSA Examples
────────────────────────────────────────────────────────
"""

# Unicode counting just works
s = "a😀a你"
counts = {}
for c in s:
    counts[c] = counts.get(c, 0) + 1
print(counts)  # {'a': 2, '😀': 1, '你': 1}

"""
Space intuition:
• "anagram"      → max 26 unique chars → O(1)
• "😀🚀你好吗éñü"  → many unique chars → O(U)

────────────────────────────────────────────────────────
Bottom line
────────────────────────────────────────────────────────
• Python `str` is Unicode.
• Dict/set/string algorithms are Unicode-safe by default.
• Space becomes O(U) when the alphabet is unbounded.
• Bytes matter only when converting to/from external data.
"""
