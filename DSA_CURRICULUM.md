# DSA Interview Curriculum — Entry-Level SWE (Python)

**Source of truth for what to solve.** Companion to `JOB_SEARCH.md` (which says *when*; this says *what*).
Difficulty rules enforced throughout: **Easy-majority per sub-pattern · Easies listed first · zero Hards anywhere.**

| | |
|---|---|
| Core problems | **100** (63% Easy, 37% Medium, 0 Hard) |
| Optional problems | 12 (rotated binary search, trees, stretch mediums) |
| Patterns | 8 · 19 sub-patterns |
| List order | = drill order. Within each sub-pattern, solve top to bottom. |
| Pacing rule | **1 new Medium OR 2 new Easies per day.** Easies are half-days. |

**One structural change from your seed:** Sliding Window moved to **after Hashing** (your sheet had it second). Nearly every variable-window problem (424, 904, 1004, 438, 567) uses a frequency map internally — drilling Hashing first makes Sliding Window dramatically easier.

---

## Phase map (matches JOB_SEARCH.md)

| Phase | Dates | Sections |
|---|---|---|
| Setup warm-up | Jul 24 – Aug 2 | Re-solve cold 8–10 Easies you've seen: 27, 26, 283, 905, 977, 217, 242, 1 |
| Phase 1 | Aug 3 – Aug 30 | §1.1–1.4 Two Pointers + §2 Hashing |
| Phase 2 | Aug 31 – Sep 27 | §3 Sliding Window + §1.5–1.7 Strings + §4 Prefix Sum |
| Phase 3 | Sep 28 – Oct 25 | §5 Stack + §6 Binary Search + §7 Linked List |
| Phase 4 → loop | Oct 26 → | Mixed re-solves + leftovers + §8 Trees (only if ahead) |

---

## §1 Two Pointers

### 1.1 Converging (opposite ends) — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 125 | Valid Palindrome | Easy |
| 977 | Squares of a Sorted Array | Easy |
| 349 | Intersection of Two Arrays | Easy |
| 2824 | Count Pairs Whose Sum is Less than Target | Easy |
| 680 | Valid Palindrome II | Easy |
| 167 | Two Sum II – Input Array Is Sorted | Medium |
| 15 | 3Sum | Medium |
| 11 | Container With Most Water | Medium |
| 881 | Boats to Save People | Medium |

**Unlocks:** any "sorted array + pair/condition" problem — the single most common two-pointer setup.
**Changes to your list:** removed **16. 3Sum Closest**, **18. 4Sum**, **259. 3Sum Smaller** (all Mediums; 16/18 are grindy variants of 15 with near-zero new technique, 259 is also Premium). Added Easies 125, 680, 2824 to restore Easy-majority (was 2E/7M, now 5E/4M).

### 1.2 Fast & Slow — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 141 | Linked List Cycle | Easy |
| 876 | Middle of the Linked List | Easy |
| 202 | Happy Number | Easy |
| 234 | Palindrome Linked List | Easy |
| 392 | Is Subsequence | Easy |
| 142 | Linked List Cycle II | Medium |
| 287 | Find the Duplicate Number | Medium |

**Unlocks:** cycle detection + middle-finding, the two moves behind most linked-list interview questions.
**Changes:** added 234 (fast/slow + reverse = classic combo), 142 (asked constantly, tiny step past 141), and **moved 876 here from your Fixed Separation list** — it's textbook fast & slow. Note: 392 is really "parallel pointers over two sequences," not fast/slow, but it's a one-off — leaving it here rather than inventing a sub-pattern for one problem.

### 1.3 Fixed Separation (n apart) — Important

| LC # | Problem | Difficulty |
|---|---|---|
| 19 | Remove Nth Node From End of List | Medium |
| 2095 | Delete the Middle Node of a Linked List | Medium |

**Unlocks:** the "gap trick" for one-pass linked-list deletion.
**Changes:** 876 moved to §1.2. That leaves a 2-Medium micro-pattern — **flagged exception** to Easy-majority: no Easies exist in this family, and both problems are small twists on §1.2 skills, so they're scheduled immediately after it. If you want to drop one, drop 2095.

### 1.4 In-place Array Modification — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 27 | Remove Element | Easy |
| 26 | Remove Duplicates from Sorted Array | Easy |
| 283 | Move Zeroes | Easy |
| 905 | Sort Array By Parity | Easy |
| 88 | Merge Sorted Array | Easy |
| 1089 | Duplicate Zeros | Easy |
| 80 | Remove Duplicates from Sorted Array II | Medium |
| 75 | Sort Colors | Medium |
| 443 | String Compression | Medium |

**Unlocks:** reader/writer pointer separation — the foundation for every "modify without extra space" question.
**Changes:** removed **2337. Move Pieces** and **2938. Separate Black and White Balls** (niche Mediums, low transfer; 2938 is 283 with counting). Added 88 (merge-from-the-end is a must-know Easy) and 1089. Was 4E/5M, now 6E/3M.

### 1.5 String Comparison with Skips — Important

| LC # | Problem | Difficulty |
|---|---|---|
| 844 | Backspace String Compare | Easy |
| 1598 | Crawler Log Folder | Easy |
| 2390 | Removing Stars From a String | Medium |

**Unlocks:** processing strings with "undo" characters — also your bridge into Stack thinking (§5).
**Changes:** none. Already compliant.

### 1.6 Expanding From Center — Important ⚠ exception

| LC # | Problem | Difficulty |
|---|---|---|
| 647 | Palindromic Substrings | Medium |
| 5 | Longest Palindromic Substring | Medium |

**Unlocks:** palindrome scanning without DP.
**Exception flagged:** zero Easy problems exist in this family — it's the only all-Medium sub-pattern kept, because #5 is one of the most-asked interview questions anywhere and both problems are literally the same technique. Warm-up: 125 (§1.1). Scheduled last within Two Pointers.

### 1.7 String Reversal — Important

| LC # | Problem | Difficulty |
|---|---|---|
| 344 | Reverse String | Easy |
| 345 | Reverse Vowels of a String | Easy |
| 541 | Reverse String II | Easy |
| 917 | Reverse Only Letters | Easy |
| 151 | Reverse Words in a String | Medium |

**Unlocks:** in-place swap mechanics; 151 adds word-level parsing (a real interview favorite).
**Changes:** reordered Easies first (151 was listed first); added 917.

---

## §2 Hashing

### 2.1 Seen Set / Existence Check — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 217 | Contains Duplicate | Easy |
| 1 | Two Sum | Easy |
| 136 | Single Number | Easy |
| 268 | Missing Number | Easy |
| 448 | Find All Numbers Disappeared in an Array | Easy |
| 128 | Longest Consecutive Sequence | Medium |
| 36 | Valid Sudoku | Medium |

**Unlocks:** the "have I seen this before?" reflex — the most common optimization in all of entry-level interviewing.
**Changes:** **1. Two Sum moved here from your Sliding Window §11** — it's a hash-map problem, not a window problem.

### 2.2 Frequency Map / Counting — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 242 | Valid Anagram | Easy |
| 383 | Ransom Note | Easy |
| 387 | First Unique Character in a String | Easy |
| 169 | Majority Element | Easy |
| 205 | Isomorphic Strings | Easy |
| 290 | Word Pattern | Easy |
| 1207 | Unique Number of Occurrences | Easy |
| 49 | Group Anagrams | Medium |
| 347 | Top K Frequent Elements | Medium |

**Unlocks:** `Counter`/dict fluency, anagram family, and the prerequisite for §3.3 frequency-matching windows.

---

## §3 Sliding Window

### 3.1 Fixed Size — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 643 | Maximum Average Subarray I | Easy |
| 1652 | Defuse the Bomb | Easy |
| 1876 | Substrings of Size Three with Distinct Characters | Easy |
| 3318 | Find X-Sum of All K-Long Subarrays I | Easy |
| 346 | Moving Average from Data Stream *(Premium — skip if no sub)* | Easy |
| 2985 | Calculate Compressed Mean *(Premium — skip if no sub)* | Easy |
| 2461 | Maximum Sum of Distinct Subarrays With Length K | Medium |
| 3254 | Find the Power of K-Size Subarrays I | Medium |

**Unlocks:** the add-one/remove-one window update — never recompute the window from scratch.
**Changes:** added 1652, 1876; **moved 2461 here from your Variable Size list** (it's a fixed length-K window). Premium items kept but flagged — they're skippable, four free Easies cover the same skill.

### 3.2 Variable Size — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 121 | Best Time to Buy and Sell Stock | Easy |
| 219 | Contains Duplicate II | Easy |
| 485 | Max Consecutive Ones | Easy |
| 674 | Longest Continuous Increasing Subsequence | Easy |
| 209 | Minimum Size Subarray Sum | Medium |
| 3 | Longest Substring Without Repeating Characters | Medium |
| 424 | Longest Repeating Character Replacement | Medium |
| 1004 | Max Consecutive Ones III | Medium |

Stretch (optional, only if cruising): 713 (M), 904 (M), 1493 (M — note 1004 generalizes it).

**Unlocks:** grow-right/shrink-left with an invariant — solves the entire "longest/shortest subarray such that X" family.
**Changes — the big cleanup:**
- **Removed 76. Minimum Window Substring — it is HARD**, not Medium. Non-negotiable rule violation.
- Removed 12 grindy Mediums: 1438, 1658, 1838, 2516, 2762, 2779, 2981, 3026, 3346, and **3347 (also HARD)**, plus 713/904/1493 demoted to stretch. They're interchangeable reps of the same shrink-loop; 3/209/424/1004 teach everything they teach.
- Added the only 4 worthwhile Easies in this family (121, 219, 485, 674). ⚠ Even so this lands 4E/4M — a tie, not a majority. That's the ceiling: variable-window is inherently Medium territory on LeetCode. Flagged, not hidden.

### 3.3 Frequency-Matching Windows (anagram windows) — Important ⚠ exception

| LC # | Problem | Difficulty |
|---|---|---|
| 567 | Permutation in String | Medium |
| 438 | Find All Anagrams in a String | Medium |

**Unlocks:** fixed window + frequency map combo — a top-5 startup phone-screen question type.
**Exception flagged:** no Easies exist; kept because both are one technique and your §2.2 Easies (242, 383) are the real warm-ups. Do this sub-pattern only after §2.2.

### ~~3.4 Monotonic Queue for Max/Min~~ — REMOVED

Your Pattern 10 is **dropped entirely**: 239 Sliding Window Maximum and 862 Shortest Subarray with Sum at Least K are both **Hard** (rule violation), and 1696 alone doesn't justify learning monotonic deques. This is FAANG-tier technique, wrong tier for your targets.

---

## §4 Prefix Sum — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 1480 | Running Sum of 1d Array | Easy |
| 724 | Find Pivot Index | Easy |
| 1732 | Find the Highest Altitude | Easy |
| 303 | Range Sum Query – Immutable | Easy |
| 560 | Subarray Sum Equals K | Medium |
| 238 | Product of Array Except Self | Medium |

**Unlocks:** precompute-then-query thinking; 560 (prefix + hashmap) and 238 (prefix/suffix) are two of the most-asked array Mediums in existence.

---

## §5 Stack

### 5.1 Matching / Processing — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 20 | Valid Parentheses | Easy |
| 1047 | Remove All Adjacent Duplicates in String | Easy |
| 682 | Baseball Game | Easy |
| 232 | Implement Queue using Stacks | Easy |
| 155 | Min Stack | Medium |
| 150 | Evaluate Reverse Polish Notation | Medium |

**Unlocks:** push/pop-on-match reflex. 20 is arguably the single most-asked entry-level question; 155 is a design favorite. §1.5 already primed you for this.

### 5.2 Monotonic Stack (light) — Important

| LC # | Problem | Difficulty |
|---|---|---|
| 496 | Next Greater Element I | Easy |
| 1475 | Final Prices With a Special Discount in a Shop | Easy |
| 739 | Daily Temperatures | Medium |

**Unlocks:** "next greater/smaller element" — kept light on purpose; deeper monotonic-stack problems (84, 42) are Hard and excluded.

---

## §6 Binary Search

### 6.1 Classic on Sorted Data — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 704 | Binary Search | Easy |
| 35 | Search Insert Position | Easy |
| 744 | Find Smallest Letter Greater Than Target | Easy |
| 278 | First Bad Version | Easy |
| 69 | Sqrt(x) | Easy |
| 367 | Valid Perfect Square | Easy |
| 34 | Find First and Last Position of Element in Sorted Array | Medium |
| 74 | Search a 2D Matrix | Medium |

**Unlocks:** one memorized template (`lo, hi, mid`, no off-by-ones) → eight problems fall. 34 teaches the leftmost/rightmost boundary variant, which is the actual interview skill.

### 6.2 Rotated Arrays — Optional

| LC # | Problem | Difficulty |
|---|---|---|
| 153 | Find Minimum in Rotated Sorted Array | Medium |
| 33 | Search in Rotated Sorted Array | Medium |

Both Medium, no Easies exist — do only after 6.1 is cold, or skip until an interviewer's company is known to ask it. **Excluded:** binary-search-on-answer (875, 1011) — clever but low frequency at entry level.

---

## §7 Linked List Manipulation — Core

| LC # | Problem | Difficulty |
|---|---|---|
| 206 | Reverse Linked List | Easy |
| 21 | Merge Two Sorted Lists | Easy |
| 83 | Remove Duplicates from Sorted List | Easy |
| 203 | Remove Linked List Elements | Easy |
| 2 | Add Two Numbers | Medium |
| 24 | Swap Nodes in Pairs | Medium |

Cross-refs already covered elsewhere: 141, 142, 234, 876 (§1.2), 19, 2095 (§1.3).
**Unlocks:** pointer rewiring + dummy-head trick. 206 and 21 are near-guaranteed to appear somewhere in an entry-level loop. **Excluded:** 146 LRU Cache (M, first add-back below), 25 Reverse Nodes in k-Group (Hard).

---

## §8 Trees BFS/DFS — Optional (Phase 4 only, if §1–7 are solid)

| LC # | Problem | Difficulty |
|---|---|---|
| 104 | Maximum Depth of Binary Tree | Easy |
| 226 | Invert Binary Tree | Easy |
| 100 | Same Tree | Easy |
| 101 | Symmetric Tree | Easy |
| 112 | Path Sum | Easy |
| 102 | Binary Tree Level Order Traversal | Medium |
| 235 | Lowest Common Ancestor of a BST | Medium |

**Unlocks:** recursive DFS template + BFS queue — enough to survive the one tree question a startup might ask, without opening the full trees rabbit hole.

---

## Why this set is sufficient (and what's deliberately missing)

**Sufficiency:** every sub-pattern above is a *template family* — master the 3–9 listed problems cold and unseen problems in the family are re-skins (same loop shape, different wrapper story). The set covers ~90% of what small/mid companies actually ask at entry level: arrays, strings, hash maps, windows, stacks, basic search, basic linked lists. Combined with the plan's spaced re-solves and Saturday mixed sets, ~100 problems deeply retained beats 300 half-remembered — which is the exact failure mode of your first 54.

**Excluded on purpose (don't second-guess these):**

| Excluded | Why |
|---|---|
| Dynamic Programming | Biggest time sink in all of interview prep; rare in entry-level startup screens; mostly Medium/Hard |
| Graphs (DFS/BFS on grids, topo sort, union-find) | Almost entirely Medium+; FAANG-tier frequency |
| Backtracking (subsets, permutations, combination sum) | All Medium+; low startup frequency |
| Heaps / Priority Queues | 347 (bucket-sortable) is the only common one and it's already in §2.2 |
| Tries, intervals, greedy theory, bit manipulation, math tricks | One-off topics; learn on demand if a specific company asks |
| Monotonic deque (239, 862) | Hard-gated — removed per your rules |
| Matrix spiral/rotation, cyclic sort | Ceremony-heavy, low transfer |
| **Every Hard problem** | Including 76 and 3347, which were hiding in your seed lists |

**First add-backs** if you finish everything and are still hunting: 56 Merge Intervals (M) → 146 LRU Cache (M) → 33/153 (§6.2) → 875 Koko Eating Bananas (M).

---

## Summary of edits to your seed lists

| Change | Detail |
|---|---|
| **Hards removed** | 76 Minimum Window Substring, 3347 Max Frequency II, 239 Sliding Window Maximum, 862 Shortest Subarray (→ Pattern 10 dropped entirely) |
| **Mediums trimmed** | 16, 18, 259 (3Sum variants) · 2337, 2938 (in-place niche) · 1438, 1658, 1838, 2516, 2762, 2779, 2981, 3026, 3346, 1696 (variable-window grind) |
| **Moved** | 1 Two Sum → §2.1 Hashing · 876 → §1.2 Fast & Slow · 2461 → §3.1 Fixed Size |
| **Easies added** | 125, 680, 2824, 234, 88, 1089, 917, 1652, 1876, 121, 485, 674 (+142 M) |
| **Reordered** | All lists now Easy-first; Sliding Window now drills after Hashing |
| **Exceptions kept & flagged** | §1.3 (2M), §1.6 (2M), §3.2 (4E/4M tie), §3.3 (2M), §6.2 optional (2M) — families where Easies don't exist |
