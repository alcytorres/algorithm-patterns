# DSA Interview Curriculum — Entry-Level SWE (Python)

**Source of truth for what to solve *and when*.** Companion to `JOB_SEARCH.md` (apps / networking / projects live there).
Difficulty rules: **Easy-majority per sub-pattern · Easies listed first · zero Hards anywhere.**

| | |
|---|---|
| Core problems | **~96 free** (skip 2 Premium if no sub) · 0 Hard |
| Optional | §6.2 rotated BS · §3.2 stretch · §8 Trees |
| List order | = drill order. Top → bottom inside each sub-pattern. |
| Calendar below | = target dates. Slip is expected — see pacing rules. |

**Structural note:** Sliding Window drills **after** Hashing. Variable windows (424, 1004, 438, 567) all use frequency maps — hashing first makes them stick.

---

## Pacing rules (retention > speed)

These are non-negotiable for *your* retention profile (looked-up solutions that don’t stick):

1. **Mon–Fri only for new problems.** One current sub-pattern at a time. Finish it before starting the next.
2. **Daily new cap:** `1 Medium` **or** `up to 2 Easies`. Second Easy only if the first took **≤25 minutes** without a lookup. If it took longer or you peeked → that Easy is your only new for the day; re-attempt tomorrow before advancing.
3. **Looked-up ≠ done.** If you read/watched the solution, close it and re-implement the same day. It still enters the review queue and does **not** count as mastered until **two cold re-solves** (≈2 days later, ≈1 week later).
4. **Lock-in day** (marked below): no new pattern. Cold re-solve 2–3 problems from the block you just finished. This is what makes depth-first drilling stick.
5. **Saturday:** mixed set from *finished* sub-patterns only (see `JOB_SEARCH.md`). No new sub-pattern starts on Saturday.
6. **Sunday:** rest + 30-min retro. Zero new problems.
7. **If you slip:** push dates forward. Never skip lock-in or Saturday mixed to “catch up.” Catch-up by dropping Optional/stretch only — never by skipping reviews.

**Why this is doable:** ~5 new weekdays/week × ~16 weeks (Aug 3 → Nov 20) ≈ 80 slots. Core free list needs ~75 slots at the 2E/1M rate, leaving room for lock-ins and slip. The old “Phase 1 = Two Pointers + Hashing” packing (~43 problems / 20 days) was not retention-safe — redistributed below.

---

## Master calendar (sub-pattern → dates)

| When | Sub-pattern | New #s (approx) | Notes |
|---|---|---|---|
| **Fri Jul 24 – Sun Aug 2** | **Setup warm-up** | 0 new | Cold re-solve: 27, 26, 283, 905, 977, 217, 242, 1 |
| **Mon Aug 3 – Tue Aug 11** | §1.1 Converging | 9 | First Two Pointers block |
| **Wed Aug 12 – Tue Aug 18** | §1.2 Fast & Slow | 7 | |
| **Wed Aug 19 – Thu Aug 20** | §1.3 Fixed Separation | 2 | Tiny; no separate lock-in |
| **Fri Aug 21 – Fri Aug 28** | §1.4 In-place Modification | 9 | |
| **Sat Aug 29** | **Lock-in: §1.1–1.4** | 0 | Mixed Two Pointers only |
| **Sun Aug 30** | Phase 1 checkpoint | — | See `JOB_SEARCH.md` |
| **Mon Aug 31 – Fri Sep 4** | §2.1 Seen Set | 7 | |
| **Mon Sep 7 – Mon Sep 14** | §2.2 Frequency Map | 9 | Sep 7 is Labor Day — still a study day if you can |
| **Tue Sep 15** | **Lock-in: §2** | 0 | Hashing re-solves |
| **Wed Sep 16 – Thu Sep 17** | §1.5 String Skips | 3 | Bridge into Stack |
| **Fri Sep 18 – Mon Sep 21** | §1.6 Expand From Center | 2 | Exception: all Medium |
| **Tue Sep 22 – Thu Sep 24** | §1.7 String Reversal | 5 | |
| **Fri Sep 25** | **Buffer / catch-up** | 0 | Use for any slipped §1.5–1.7 or §2 |
| **Sat Sep 26** | Mock (plan) | — | Mixed from everything done so far |
| **Sun Sep 27** | Phase 2 checkpoint | — | |
| **Mon Sep 28 – Thu Oct 1** | §3.1 Fixed Window | 6 free | Skip 346/2985 if no Premium |
| **Fri Oct 2** | Lock-in §3.1 | 0 | |
| **Mon Oct 5 – Mon Oct 12** | §3.2 Variable Window | 8 | Stretch 713/904/1493 only if cruising |
| **Tue Oct 13** | Lock-in §3.2 | 0 | |
| **Wed Oct 14 – Thu Oct 15** | §3.3 Anagram Windows | 2 | After §2.2 only |
| **Fri Oct 16 – Wed Oct 21** | §4 Prefix Sum | 6 | |
| **Thu Oct 22** | Lock-in §3–§4 | 0 | |
| **Fri Oct 23 – Wed Oct 28** | §5.1 Stack Matching | 6 | Spans Phase 3 → 4 |
| **Thu Oct 29** | Lock-in §5.1 | 0 | |
| **Fri Oct 30 – Mon Nov 2** | §5.2 Monotonic Stack (light) | 3 | |
| **Tue Nov 3 – Wed Nov 11** | §6.1 Classic Binary Search | 8 | |
| **Thu Nov 12** | Lock-in §6.1 | 0 | §6.2 optional after this |
| **Fri Nov 13 – Wed Nov 18** | §7 Linked List | 6 | Cross-refs from §1.2/1.3 already done |
| **Thu Nov 19** | Lock-in §7 | 0 | |
| **Fri Nov 20 – Sun Nov 22** | **Phase 4 wrap** | 0–few | Majority mixed · §8 Trees only if §1–7 cold |
| **Mon Nov 23 →** | Maintenance loop | — | 1 mixed timed + reviews; no new curriculum unless add-backs |

```
Jul 24          Aug 3              Aug 31             Sep 28             Oct 26              Nov 22
  │ Setup │········ Phase 1 ········│···· Phase 2 ······│···· Phase 3 ······│···· Phase 4 ······│→ loop
  │warm-up│  §1.1–1.4 Two Pointers  │ §2 Hash + §1.5–1.7│ §3 Window + §4    │ §5→§6→§7 + mixed │
  └───────┘                         │   string TP       │ + start §5        │  consolidate     │
```

---

## Phase map (synced with JOB_SEARCH.md)

| Phase | Dates | DSA focus |
|---|---|---|
| Setup | Jul 24 – Aug 2 | Warm-up re-solves only (no new patterns) |
| Phase 1 | Aug 3 – Aug 30 | **§1.1–1.4** Two Pointers core only |
| Phase 2 | Aug 31 – Sep 27 | **§2** Hashing → **§1.5–1.7** string TP |
| Phase 3 | Sep 28 – Oct 25 | **§3** Sliding Window → **§4** Prefix Sum → start **§5.1** |
| Phase 4 | Oct 26 – Nov 22 | Finish **§5** → **§6.1** → **§7** → mixed consolidation · **§8** optional |
| Loop | Nov 23 → | Reviews + mixed timed; curriculum add-backs only if hunting cold |

---

## §1 Two Pointers

**Phase 1 block: Mon Aug 3 – Sat Aug 29** (string sub-patterns §1.5–1.7 wait until Phase 2, after Hashing).

### 1.1 Converging (opposite ends) — Core
**When: Mon Aug 3 – Tue Aug 11** (7 weekdays)

| Day | Solve |
|---|---|
| Mon Aug 3 | 125 Valid Palindrome (E), 977 Squares of a Sorted Array (E) |
| Tue Aug 4 | 349 Intersection of Two Arrays (E), 2824 Count Pairs Whose Sum is Less than Target (E) |
| Wed Aug 5 | 680 Valid Palindrome II (E) |
| Thu Aug 6 | 167 Two Sum II – Input Array Is Sorted (M) |
| Fri Aug 7 | 15 3Sum (M) |
| Mon Aug 10 | 11 Container With Most Water (M) |
| Tue Aug 11 | 881 Boats to Save People (M) · if time: cold re-solve 125 or 167 |

**Unlocks:** any "sorted array + pair/condition" problem — the most common two-pointer setup.
**Changes to your list:** removed 16, 18, 259. Added 125, 680, 2824.

### 1.2 Fast & Slow — Core
**When: Wed Aug 12 – Tue Aug 18** (5 weekdays)

| Day | Solve |
|---|---|
| Wed Aug 12 | 141 Linked List Cycle (E), 876 Middle of the Linked List (E) |
| Thu Aug 13 | 202 Happy Number (E), 234 Palindrome Linked List (E) |
| Fri Aug 14 | 392 Is Subsequence (E) |
| Mon Aug 17 | 142 Linked List Cycle II (M) |
| Tue Aug 18 | 287 Find the Duplicate Number (M) |

**Unlocks:** cycle detection + middle-finding.
**Changes:** added 234, 142; moved 876 here from Fixed Separation. 392 is parallel pointers (one-off), parked here.

### 1.3 Fixed Separation (n apart) — Important
**When: Wed Aug 19 – Thu Aug 20**

| Day | Solve |
|---|---|
| Wed Aug 19 | 19 Remove Nth Node From End of List (M) |
| Thu Aug 20 | 2095 Delete the Middle Node of a Linked List (M) |

**Unlocks:** gap trick for one-pass linked-list deletion.
**Exception:** no Easies in this family. Drop 2095 if you need to cut.

### 1.4 In-place Array Modification — Core
**When: Fri Aug 21 – Fri Aug 28** (6 weekdays)

| Day | Solve |
|---|---|
| Fri Aug 21 | 27 Remove Element (E), 26 Remove Duplicates from Sorted Array (E) |
| Mon Aug 24 | 283 Move Zeroes (E), 905 Sort Array By Parity (E) |
| Tue Aug 25 | 88 Merge Sorted Array (E), 1089 Duplicate Zeros (E) |
| Wed Aug 26 | 80 Remove Duplicates from Sorted Array II (M) |
| Thu Aug 27 | 75 Sort Colors (M) |
| Fri Aug 28 | 443 String Compression (M) |

**Sat Aug 29 — Lock-in §1.1–1.4:** 3 mixed Two Pointers (unlabeled, timed). No new problems.
**Sun Aug 30 — Phase 1 checkpoint.**

**Unlocks:** reader/writer pointer separation.
**Changes:** removed 2337, 2938; added 88, 1089.

### 1.5 String Comparison with Skips — Important
**When: Wed Sep 16 – Thu Sep 17** *(Phase 2 — after Hashing)*

| Day | Solve |
|---|---|
| Wed Sep 16 | 844 Backspace String Compare (E), 1598 Crawler Log Folder (E) |
| Thu Sep 17 | 2390 Removing Stars From a String (M) |

**Unlocks:** “undo” characters; bridge into Stack (§5).

### 1.6 Expanding From Center — Important ⚠
**When: Fri Sep 18 – Mon Sep 21**

| Day | Solve |
|---|---|
| Fri Sep 18 | 647 Palindromic Substrings (M) |
| Mon Sep 21 | 5 Longest Palindromic Substring (M) |

**Unlocks:** palindrome scanning without DP. Warm-up already done: 125.
**Exception:** no Easies exist; both are the same technique. Kept because #5 is extremely common.

### 1.7 String Reversal — Important
**When: Tue Sep 22 – Thu Sep 24**

| Day | Solve |
|---|---|
| Tue Sep 22 | 344 Reverse String (E), 345 Reverse Vowels of a String (E) |
| Wed Sep 23 | 541 Reverse String II (E), 917 Reverse Only Letters (E) |
| Thu Sep 24 | 151 Reverse Words in a String (M) |

**Fri Sep 25 — Buffer:** finish any slipped §2 / §1.5–1.7. Do not start §3 early unless fully caught up.
**Unlocks:** in-place swaps + word-level parsing (151).

---

## §2 Hashing

**Phase 2 start: Mon Aug 31 – Tue Sep 15**

### 2.1 Seen Set / Existence Check — Core
**When: Mon Aug 31 – Fri Sep 4**

| Day | Solve |
|---|---|
| Mon Aug 31 | 217 Contains Duplicate (E), 1 Two Sum (E) |
| Tue Sep 1 | 136 Single Number (E), 268 Missing Number (E) |
| Wed Sep 2 | 448 Find All Numbers Disappeared in an Array (E) |
| Thu Sep 3 | 128 Longest Consecutive Sequence (M) |
| Fri Sep 4 | 36 Valid Sudoku (M) |

**Unlocks:** “have I seen this before?”
**Changes:** 1 Two Sum moved here from your old Sliding Window list.

### 2.2 Frequency Map / Counting — Core
**When: Mon Sep 7 – Mon Sep 14**

| Day | Solve |
|---|---|
| Mon Sep 7 | 242 Valid Anagram (E), 383 Ransom Note (E) |
| Tue Sep 8 | 387 First Unique Character in a String (E), 169 Majority Element (E) |
| Wed Sep 9 | 205 Isomorphic Strings (E), 290 Word Pattern (E) |
| Thu Sep 10 | 1207 Unique Number of Occurrences (E) |
| Fri Sep 11 | 49 Group Anagrams (M) |
| Mon Sep 14 | 347 Top K Frequent Elements (M) |

**Tue Sep 15 — Lock-in §2:** cold re-solve 217, 242, and either 1 or 49.

**Unlocks:** `Counter`/dict fluency; required before §3.3.

---

## §3 Sliding Window

**Phase 3: Mon Sep 28 – Thu Oct 15**

### 3.1 Fixed Size — Core
**When: Mon Sep 28 – Thu Oct 1** · **Fri Oct 2 lock-in**

| Day | Solve |
|---|---|
| Mon Sep 28 | 643 Maximum Average Subarray I (E), 1652 Defuse the Bomb (E) |
| Tue Sep 29 | 1876 Substrings of Size Three with Distinct Characters (E), 3318 Find X-Sum of All K-Long Subarrays I (E) |
| Wed Sep 30 | 2461 Maximum Sum of Distinct Subarrays With Length K (M) |
| Thu Oct 1 | 3254 Find the Power of K-Size Subarrays I (M) |
| Fri Oct 2 | Lock-in: re-solve 643 + 2461 |

Skip if no Premium: 346 Moving Average, 2985 Calculate Compressed Mean.
**Unlocks:** add-one / remove-one window update.
**Changes:** added 1652, 1876; moved 2461 from Variable Size.

### 3.2 Variable Size — Core
**When: Mon Oct 5 – Mon Oct 12** · **Tue Oct 13 lock-in**

| Day | Solve |
|---|---|
| Mon Oct 5 | 121 Best Time to Buy and Sell Stock (E), 219 Contains Duplicate II (E) |
| Tue Oct 6 | 485 Max Consecutive Ones (E), 674 Longest Continuous Increasing Subsequence (E) |
| Wed Oct 7 | 209 Minimum Size Subarray Sum (M) |
| Thu Oct 8 | 3 Longest Substring Without Repeating Characters (M) |
| Fri Oct 9 | 424 Longest Repeating Character Replacement (M) |
| Mon Oct 12 | 1004 Max Consecutive Ones III (M) |
| Tue Oct 13 | Lock-in: re-solve 209 + 3 |

**Stretch (only if Oct 13 lock-in felt easy):** 713, 904, 1493 — do not steal time from §3.3/§4.
**Unlocks:** grow-right / shrink-left with an invariant.
**Changes:** removed Hard 76 and Hard 3347; trimmed grindy Mediums; added Easies 121, 219, 485, 674. Lands 4E/4M (tie) — flagged ceiling for this family.

### 3.3 Frequency-Matching Windows — Important ⚠
**When: Wed Oct 14 – Thu Oct 15**

| Day | Solve |
|---|---|
| Wed Oct 14 | 567 Permutation in String (M) |
| Thu Oct 15 | 438 Find All Anagrams in a String (M) |

**Unlocks:** fixed window + frequency map (top phone-screen type).
**Exception:** no Easies; warm-ups were §2.2 (242, 383).

### ~~3.4 Monotonic Queue~~ — REMOVED
Hard-gated (239, 862). Wrong tier for entry-level.

---

## §4 Prefix Sum — Core

**When: Fri Oct 16 – Wed Oct 21** · **Thu Oct 22 lock-in §3–§4**

| Day | Solve |
|---|---|
| Fri Oct 16 | 1480 Running Sum of 1d Array (E), 724 Find Pivot Index (E) |
| Mon Oct 19 | 1732 Find the Highest Altitude (E), 303 Range Sum Query – Immutable (E) |
| Tue Oct 20 | 560 Subarray Sum Equals K (M) |
| Wed Oct 21 | 238 Product of Array Except Self (M) |
| Thu Oct 22 | Lock-in: 724 + 560 or 238 |

**Unlocks:** precompute-then-query; 560 and 238 are high-frequency Mediums.
**Sun Oct 25 — Phase 3 checkpoint** (`JOB_SEARCH.md`).

---

## §5 Stack

**Starts end of Phase 3, finishes early Phase 4.**

### 5.1 Matching / Processing — Core
**When: Fri Oct 23 – Wed Oct 28** · **Thu Oct 29 lock-in**

| Day | Solve |
|---|---|
| Fri Oct 23 | 20 Valid Parentheses (E), 1047 Remove All Adjacent Duplicates in String (E) |
| Mon Oct 26 | 682 Baseball Game (E), 232 Implement Queue using Stacks (E) |
| Tue Oct 27 | 155 Min Stack (M) |
| Wed Oct 28 | 150 Evaluate Reverse Polish Notation (M) |
| Thu Oct 29 | Lock-in: 20 + 155 |

**Unlocks:** push/pop-on-match. 20 is among the most-asked entry-level questions.

### 5.2 Monotonic Stack (light) — Important
**When: Fri Oct 30 – Mon Nov 2**

| Day | Solve |
|---|---|
| Fri Oct 30 | 496 Next Greater Element I (E), 1475 Final Prices With a Special Discount in a Shop (E) |
| Mon Nov 2 | 739 Daily Temperatures (M) |

**Unlocks:** next greater/smaller. Deeper monotonic stack (84, 42) is Hard — excluded.

---

## §6 Binary Search

### 6.1 Classic on Sorted Data — Core
**When: Tue Nov 3 – Wed Nov 11** · **Thu Nov 12 lock-in**

| Day | Solve |
|---|---|
| Tue Nov 3 | 704 Binary Search (E), 35 Search Insert Position (E) |
| Wed Nov 4 | 744 Find Smallest Letter Greater Than Target (E), 278 First Bad Version (E) |
| Thu Nov 5 | 69 Sqrt(x) (E), 367 Valid Perfect Square (E) |
| Fri Nov 6 | *(buffer / re-solve template if any Easy felt shaky)* |
| Mon Nov 9 | 34 Find First and Last Position of Element in Sorted Array (M) |
| Tue Nov 10 | 74 Search a 2D Matrix (M) |
| Wed Nov 11 | cold re-solve 704 + 34 |
| Thu Nov 12 | Lock-in §6.1 |

**Unlocks:** one `lo/hi/mid` template without off-by-ones; 34 is the real interview skill (boundaries).

### 6.2 Rotated Arrays — Optional
**When: only after Thu Nov 12, and only if §6.1 is cold** — else skip until a company is known to ask it.

| LC # | Problem | Difficulty |
|---|---|---|
| 153 | Find Minimum in Rotated Sorted Array | Medium |
| 33 | Search in Rotated Sorted Array | Medium |

Excluded: binary-search-on-answer (875, 1011) — low entry-level frequency.

---

## §7 Linked List Manipulation — Core

**When: Fri Nov 13 – Wed Nov 18** · **Thu Nov 19 lock-in**

| Day | Solve |
|---|---|
| Fri Nov 13 | 206 Reverse Linked List (E), 21 Merge Two Sorted Lists (E) |
| Mon Nov 16 | 83 Remove Duplicates from Sorted List (E), 203 Remove Linked List Elements (E) |
| Tue Nov 17 | 2 Add Two Numbers (M) |
| Wed Nov 18 | 24 Swap Nodes in Pairs (M) |
| Thu Nov 19 | Lock-in: 206 + 21 |

Already done via §1: 141, 142, 234, 876, 19, 2095.
**Unlocks:** pointer rewiring + dummy head. Excluded: 146 LRU (add-back), 25 (Hard).

---

## §8 Trees BFS/DFS — Optional

**When: Fri Nov 20 – Sun Nov 22 only if §1–7 re-solve rate is ≥80% cold.** Otherwise spend these days on mixed reviews from weak sub-patterns.

| LC # | Problem | Difficulty |
|---|---|---|
| 104 | Maximum Depth of Binary Tree | Easy |
| 226 | Invert Binary Tree | Easy |
| 100 | Same Tree | Easy |
| 101 | Symmetric Tree | Easy |
| 112 | Path Sum | Easy |
| 102 | Binary Tree Level Order Traversal | Medium |
| 235 | Lowest Common Ancestor of a BST | Medium |

If you start this block: 2 Easies/day Nov 20–21, then 102 or 235 on Nov 22 — or skip Mediums and bank confidence.

---

## Why this timeline favors retention

| Design choice | Why it helps you |
|---|---|
| One sub-pattern at a time | Stops the “random problems → zero retention” failure mode |
| 2 Easy / 1 Medium cap + 25-min gate | Prevents fake progress from rushing Easies you didn’t own |
| Lock-in days after every block | Forces retrieval practice when the pattern is still warm |
| Hashing before Sliding Window | Removes the “I need a map but don’t feel it yet” wall |
| Phase 1 = Two Pointers only | Old plan crammed hashing into the same 4 weeks — too much new for weak retention |
| Phase 4 = finish Stack/BS/LL + mixed | New topics taper while mixed practice rises (matches how interviews feel) |
| Slip pushes dates; never skip reviews | Reviews are the product; the calendar is a guide |

**Still excluded on purpose:** DP, graphs, backtracking, heaps, tries, intervals deep-dives, monotonic deques, every Hard (including 76 and 3347 from your seed).

**First add-backs** (only after Nov 22 loop, still hunting): 56 Merge Intervals → 146 LRU Cache → §6.2 → 875 Koko.

---

## Summary of edits to your seed lists

| Change | Detail |
|---|---|
| **Hards removed** | 76, 3347, 239, 862 (Pattern 10 dropped) |
| **Mediums trimmed** | 16, 18, 259 · 2337, 2938 · variable-window grind list |
| **Moved** | 1 → §2.1 · 876 → §1.2 · 2461 → §3.1 |
| **Easies added** | 125, 680, 2824, 234, 88, 1089, 917, 1652, 1876, 121, 485, 674 (+142 M) |
| **Timeline** | Day-level dates Aug 3 → Nov 19; lock-ins; Phase 1 no longer includes Hashing |

---

*Curriculum calendar built for start Fri Jul 24, 2026. If a weekday is lost (travel, interview), shift this file’s dates forward as a block — don’t compress.*
