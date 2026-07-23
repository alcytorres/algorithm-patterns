# DSA Interview Curriculum — Entry-Level SWE (Python)

**Source of truth for what to solve *and when*.** Companion to `JOB_SEARCH.md` (apps / networking / projects live there).
Difficulty rules: **Easy-majority per sub-pattern · Easies listed first · zero Hards anywhere.**

| | |
|---|---|
| Core problems | **~107 free** (skip 2 Premium if no sub) · 0 Hard |
| Core patterns | 9 (added §8 Trees, §9 Grid BFS/DFS) |
| Optional | §6.2 rotated BS · §3.2 stretch · §9 heap add-on |
| List order | = drill order. Top → bottom inside each sub-pattern. |
| Calendar below | = target dates. Slip is expected — see pacing rules. |

**Structural note:** Sliding Window drills **after** Hashing. Variable windows (424, 1004, 438, 567) all use frequency maps — hashing first makes them stick.

---

## Read this first — honest confidence (you asked for 95%)

**I cannot honestly tell you "do this file and you're 95% to get a job." Anyone who does is selling you something.** Here is the real breakdown, because you asked me to verify claims rather than flatter you:

Getting hired = **(interviews you get) × (technical screens you pass) × (behavioral you pass) × (fit / timing / market luck)**. DSA only controls the second term.

| Term | What controls it | This file's job |
|---|---|---|
| Get interviews | Resume, applications, networking, referrals | ❌ Not this file — **that's the binding constraint** (`JOB_SEARCH.md`) |
| Pass technical screen | DSA pattern recognition + communication | ✅ **This file** |
| Pass behavioral | STAR stories, comms | ❌ `JOB_SEARCH.md` |
| Offer / timing / market | Mostly outside your control | ❌ Nobody controls this |

**My honest confidence levels, if you fully execute:**
- **That this DSA set (fully retained) makes you pass the large majority of entry-level technical screens you reach: ~85–90%.** That part I *can* get near your bar, and the additions below push it there.
- **That you have an offer by Nov 22 doing everything in both files: NOT 95%.** Realistically ~40–65%, driven mostly by how many interviews you generate and the market — not by LeetCode. It may take longer than this timeline, and that is normal, not failure.

**What this means for you:** after a year of applying, your bottleneck is almost certainly *getting interviews*, not DSA depth. More LeetCode past this list has sharply diminishing returns. If you want to move the real number up, the highest-leverage hours are resume + referrals + interview volume in `JOB_SEARCH.md`. This file's promise is narrow and real: **DSA will not be the reason you get rejected.**

**Gaps I found and just added** to hit the ~85–90% technical-pass bar: complexity analysis (pacing rule 8), **Grid BFS/DFS §9** (Number of Islands family — one of the most-asked entry-level questions, was wrongly excluded), and **Trees promoted from optional to core §8** (they show up too often to be optional).

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
8. **State the complexity out loud, every problem.** Before you look at any solution, say the time and space Big-O of your approach and *why*. Interviewers ask "what's the complexity?" on essentially every screen — a correct solution you can't analyze still fails. If you can't state it, you haven't finished the problem.

**Why this is doable:** ~5 new weekdays/week × ~18 weeks (Aug 3 → Dec 4) ≈ 90 slots. Core free list (~107 problems, many paired 2-Easy days) needs ~85 slots at the 2E/1M rate, leaving room for lock-ins and slip. The old “Phase 1 = Two Pointers + Hashing” packing (~43 problems / 20 days) was not retention-safe — redistributed below.

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
| **Fri Nov 20 – Fri Nov 27** | §8 Trees (BFS/DFS) — **now core** | 7 | Common at entry level; don't skip |
| **Sat Nov 28** | Lock-in §8 | 0 | |
| **Mon Nov 30 – Thu Dec 3** | §9 Grid BFS/DFS — **now core** | 4 | Number of Islands family — very common |
| **Fri Dec 4** | Lock-in §9 | 0 | |
| **Mon Dec 7 →** | Maintenance loop | — | Majority-mixed timed + reviews. Interviewing continues. Add-ons only if hunting cold. |

**Note:** DSA new-learning now runs to ~Dec 4, past the Nov 22 job-search checkpoint. That's intentional — trees + grid are too common to cut, and **interviewing does not stop on Nov 22.** Applications, networking, and mocks in `JOB_SEARCH.md` continue straight through; the DSA tail just overlaps the early maintenance loop.

```
Jul 24          Aug 3              Aug 31             Sep 28             Oct 26          Nov 22    Dec 4
  │ Setup │········ Phase 1 ········│···· Phase 2 ······│···· Phase 3 ······│·· Phase 4 ··│· tail ·│→ loop
  │warm-up│  §1.1–1.4 Two Pointers  │ §2 Hash + §1.5–1.7│ §3 Window + §4    │ §5→§6→§7    │ §8 §9  │
  └───────┘                         │   string TP       │ + start §5        │             │trees/grid│
```

---

## Phase map (synced with JOB_SEARCH.md)

| Phase | Dates | DSA focus |
|---|---|---|
| Setup | Jul 24 – Aug 2 | Warm-up re-solves only (no new patterns) |
| Phase 1 | Aug 3 – Aug 30 | **§1.1–1.4** Two Pointers core only |
| Phase 2 | Aug 31 – Sep 27 | **§2** Hashing → **§1.5–1.7** string TP |
| Phase 3 | Sep 28 – Oct 25 | **§3** Sliding Window → **§4** Prefix Sum → start **§5.1** |
| Phase 4 | Oct 26 – Nov 22 | Finish **§5** → **§6.1** → **§7** → start **§8** Trees |
| Phase 4 tail | Nov 22 – Dec 4 | **§8** Trees → **§9** Grid BFS/DFS (both core; overlaps loop) |
| Loop | Dec 7 → | Reviews + mixed timed; add-ons only if hunting cold |

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

## §8 Trees BFS/DFS — Core (promoted from optional)

**When: Fri Nov 20 – Fri Nov 27** · **Sat Nov 28 lock-in**
Promoted because trees appear too often at entry level to gamble on skipping. This is the recursion-heavy section — go slow, one per day is fine.

| Day | Solve |
|---|---|
| Fri Nov 20 | 104 Maximum Depth of Binary Tree (E) |
| Mon Nov 23 | 226 Invert Binary Tree (E), 100 Same Tree (E) |
| Tue Nov 24 | 101 Symmetric Tree (E) |
| Wed Nov 25 | 112 Path Sum (E) |
| Thu Nov 26 | 102 Binary Tree Level Order Traversal (M) |
| Fri Nov 27 | 235 Lowest Common Ancestor of a BST (M) |
| Sat Nov 28 | Lock-in: re-solve 104 + 102 |

**Unlocks:** the recursive DFS template (`if not node: return ...; recurse left/right`) and the BFS-with-a-queue template — these two cover the vast majority of entry-level tree questions.
**Recursion note:** if recursion feels shaky, that's expected — trees are where it clicks. Trace a small tree by hand on paper before coding. 104 is the gentlest start.
**Excluded (still):** balanced/AVL, segment trees, serialization (297 is Hard).

---

## §9 Grid BFS/DFS — Core (new — was wrongly excluded)

**When: Mon Nov 30 – Thu Dec 3** · **Fri Dec 4 lock-in**
**Number of Islands (200) is one of the single most-asked questions at startups and entry-level loops.** Excluding the whole "graphs" bucket accidentally cut it — a mistake for your target roles. A grid is just an implicit graph; with §8's templates this is mostly applying DFS/BFS to a 2D array.

| Day | Solve |
|---|---|
| Mon Nov 30 | 733 Flood Fill (E) |
| Tue Dec 1 | 200 Number of Islands (M) |
| Wed Dec 2 | 695 Max Area of Island (M) |
| Thu Dec 3 | 994 Rotting Oranges (M) |
| Fri Dec 4 | Lock-in: re-solve 200 |

**Unlocks:** the "visit every cell, flood its neighbors, mark visited" pattern — 733/200/695 are one DFS template; 994 is the same idea with BFS + a queue (multi-source). Covers the grid-traversal family startups love.
**Optional heap add-on** (only if hunting and everything else is cold): 703 Kth Largest in a Stream (E), 1046 Last Stone Weight (E), 215 Kth Largest Element in an Array (M). One evening; `heapq` fluency, occasionally asked.
**Excluded (still):** Dijkstra, union-find, topological sort, word-ladder — genuinely FAANG-tier, low ROI for you.

---

## Why this timeline favors retention

| Design choice | Why it helps you |
|---|---|
| One sub-pattern at a time | Stops the “random problems → zero retention” failure mode |
| 2 Easy / 1 Medium cap + 25-min gate | Prevents fake progress from rushing Easies you didn’t own |
| Lock-in days after every block | Forces retrieval practice when the pattern is still warm |
| Hashing before Sliding Window | Removes the “I need a map but don’t feel it yet” wall |
| Phase 1 = Two Pointers only | Old plan crammed hashing into the same 4 weeks — too much new for weak retention |
| Phase 4 = finish Stack/BS/LL → Trees → Grid | New topics taper while mixed practice rises (matches how interviews feel) |
| Trees + Grid last | They reuse recursion/DFS/BFS — easier once §1–7 built the base |
| Slip pushes dates; never skip reviews | Reviews are the product; the calendar is a guide |

**Still excluded on purpose:** DP, advanced graphs (Dijkstra / union-find / topo sort), backtracking, tries, intervals deep-dives, monotonic deques, every Hard (including 76 and 3347 from your seed). *(Trees and grid BFS/DFS were promoted to core — see §8, §9.)*

**First add-backs** (only in the loop, still hunting): heap add-on (§9) → 56 Merge Intervals → 146 LRU Cache → §6.2 → 875 Koko.

---

## Summary of edits to your seed lists

| Change | Detail |
|---|---|
| **Hards removed** | 76, 3347, 239, 862 (Pattern 10 dropped) |
| **Mediums trimmed** | 16, 18, 259 · 2337, 2938 · variable-window grind list |
| **Moved** | 1 → §2.1 · 876 → §1.2 · 2461 → §3.1 |
| **Easies added** | 125, 680, 2824, 234, 88, 1089, 917, 1652, 1876, 121, 485, 674 (+142 M) |
| **Gaps closed (this pass)** | §8 Trees promoted to **core**; new §9 **Grid BFS/DFS** (200/695/733/994); complexity-analysis rule (pacing 8); optional heap add-on |
| **Timeline** | Day-level dates Aug 3 → **Dec 4**; lock-ins; Phase 1 no longer includes Hashing; DSA tail overlaps early loop |

---

*Curriculum calendar built for start Fri Jul 24, 2026; DSA new-learning runs to ~Dec 4 (Trees + Grid added as core). If a weekday is lost (travel, interview), shift this file’s dates forward as a block — don’t compress. Reminder: this file maximizes your technical-screen pass rate; it does not by itself get you the job — interview volume in `JOB_SEARCH.md` is the binding constraint.*
