# DSA Interview Curriculum — Entry-Level SWE (Python)

**Source of truth for what to solve *and when*.** Companion to `JOB_SEARCH.md` (apps / networking / projects live there).
Difficulty rules: **Easy-majority per sub-pattern · Easies listed first · zero Hards anywhere.**

| | |
|---|---|
| Core problems | **114** (71 Easy / 43 Medium) · 0 Hard · 62% Easy |
| Core patterns | 11 (0 Setup implementation, plus 1–10) |
| Optional (in-list) | 2095 · 290 · 345 · 367 · 541 · 917 · 3254 · 3318 — skip first if behind, clear later |
| Optional (blocks) | 6.2 rotated BS · 3.2 stretch (713/904/1493) · 9 heap add-on |
| Access | **LeetCode Premium — no problem is gated.** Premium-only problems stay in. |
| List order | = drill order. Top → bottom inside each sub-pattern, easiest → hardest. |
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
- **That you have an offer by Dec 6 doing everything in both files: NOT 95%.** Realistically ~40–65%, driven mostly by how many interviews you generate and the market — not by LeetCode. It may take longer than this timeline, and that is normal, not failure.

**What this means for you:** after a year of applying, your bottleneck is almost certainly *getting interviews*, not DSA depth. More LeetCode past this list has sharply diminishing returns. If you want to move the real number up, the highest-leverage hours are resume + referrals + interview volume in `JOB_SEARCH.md`. This file's promise is narrow and real: **DSA will not be the reason you get rejected.**

**Gaps I found and just added** to hit the ~85–90% technical-pass bar: complexity analysis (pacing rule 8), **Grid BFS/DFS 9** (Number of Islands family — one of the most-asked entry-level questions, was wrongly excluded), and **Trees promoted from optional to core 8** (they show up too often to be optional).

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
9. **Optional is delayed, not deleted.** If you fall behind, **skip `Optional` items first** and keep moving through Core. Finish every Core block, then come back and clear the Optional backlog. Core order is never broken to fit the calendar — if dates overflow, the block shifts forward. You are completing this whole curriculum; the only question is when.

**Why this is doable:** ~5 new weekdays/week × ~21 weeks (Aug 12 → Jan 7) ≈ 100 weekdays, minus 5 holiday rest days ≈ 95 usable. The 114-problem Core list needs ~80 study days at the 2E/1M rate (many Easies pair up), plus 13 lock-in days ≈ 93 — which fits with a little slack. The old “Phase 1 = Two Pointers + Hashing” packing (~43 problems / 20 days) was not retention-safe — redistributed below.

---

## Master calendar (sub-pattern → dates)

| When | Sub-pattern | New #s (approx) | Notes |
|---|---|---|---|
| **Wed Aug 12 – Sun Aug 16** | **0 Setup warm-up** | 3 | Re-solves + implementation Easies 13, 14, 66 |
| **Mon Aug 17 – Tue Aug 25** | 1.1 Converging | 9 | First Two Pointers block |
| **Wed Aug 26 – Tue Sep 1** | 1.2 Fast & Slow | 7 | |
| **Wed Sep 2 – Thu Sep 3** | 1.3 Fixed Separation | 1 + 1 Opt | Tiny; no separate lock-in |
| **Fri Sep 4 – Fri Sep 11** | 1.4 In-place Modification | 9 | |
| **Sat Sep 12** | **Lock-in: 1.1–1.4** | 0 | Mixed Two Pointers only |
| **Sun Sep 13** | Phase 1 checkpoint | — | See `JOB_SEARCH.md` |
| **Mon Sep 14 – Fri Sep 18** | 2.1 Seen Set | 7 | |
| **Mon Sep 21 – Mon Sep 28** | 2.2 Frequency Map | 8 + 1 Opt | |
| **Tue Sep 29** | **Lock-in: 2** | 0 | Hashing re-solves |
| **Wed Sep 30 – Thu Oct 1** | 1.5 String Skips | 3 | Bridge into Stack |
| **Fri Oct 2 – Mon Oct 5** | 1.6 Expand From Center | 2 | Exception: all Medium |
| **Tue Oct 6 – Thu Oct 8** | 1.7 String Reversal | 2 + 3 Opt | Core is just 344 + 151 |
| **Fri Oct 9** | **Buffer / catch-up** | 0 | Use for any slipped 1.5–1.7 or 2 |
| **Sat Oct 10** | Mock (plan) | — | Mixed from everything done so far |
| **Sun Oct 11** | Phase 2 checkpoint | — | |
| **Mon Oct 12 – Thu Oct 15** | 3.1 Fixed Window | 5 + 2 Opt | 346 restored (Premium) |
| **Fri Oct 16** | Lock-in 3.1 | 0 | |
| **Mon Oct 19 – Mon Oct 26** | 3.2 Variable Window | 8 | Stretch 713/904/1493 only if cruising |
| **Tue Oct 27** | Lock-in 3.2 | 0 | |
| **Wed Oct 28 – Thu Oct 29** | 3.3 Anagram Windows | 2 | After 2.2 only |
| **Fri Oct 30 – Thu Nov 5** | 4 Prefix Sum | 7 | **+53 Kadane's** |
| **Fri Nov 6** | Lock-in 3–4 | 0 | |
| **Mon Nov 9 – Thu Nov 12** | 5.1 Stack Matching | 6 | Opens Phase 4 |
| **Fri Nov 13** | Lock-in 5.1 | 0 | |
| **Mon Nov 16 – Tue Nov 17** | 5.2 Monotonic Stack (light) | 3 | |
| **Wed Nov 18 – Wed Nov 25** | 6.1 Classic Binary Search | 7 + 1 Opt | Mon Nov 23 = buffer day |
| **Thu Nov 26** | **Thanksgiving — rest** | 0 | No new problems |
| **Fri Nov 27** | Lock-in 6.1 | 0 | 6.2 optional after this |
| **Mon Nov 30 – Thu Dec 3** | 7 Linked List | 6 | Cross-refs from 1.2/1.3 already done |
| **Fri Dec 4** | Lock-in 7 | 0 | |
| **Mon Dec 7 – Fri Dec 18** | 8 Trees (BFS/DFS) — **core** | 11 | Expanded 7 → 11. Recursion block — go one/day |
| **Mon Dec 21** | Lock-in 8 | 0 | |
| **Tue Dec 22 – Tue Dec 29** | 9 Grid BFS/DFS — **core** | 5 | Number of Islands family — very common |
| **Wed Dec 30** | Lock-in 9 | 0 | |
| **Thu Dec 31** | **New Year's Eve — rest** | 0 | No new problems |
| **Fri Jan 1** | **New Year — rest** | 0 | No new problems |
| **Mon Jan 4 – Wed Jan 6** | 10 Intervals | 3 | Merge Intervals family |
| **Thu Jan 7** | Lock-in 10 | 0 | **DSA new-learning complete** |
| **Fri Jan 8 →** | Maintenance loop | — | Majority-mixed timed + reviews. Interviewing continues. Add-ons only if hunting cold. |

**Holiday rest days (no new problems):** Thu Nov 26 (Thanksgiving) · Thu Dec 24 – Fri Dec 25 (Christmas) · Thu Dec 31 – Fri Jan 1 (New Year's Eve + New Year). These are built into the dates above, not slip.

**Note:** DSA new-learning runs to **Thu Jan 7, 2027**, past the Dec 6 job-search checkpoint. That's intentional — trees + grid + intervals are too common to cut, and **interviewing does not stop on Dec 6.** Applications, networking, and mocks in `JOB_SEARCH.md` continue straight through; the DSA tail just overlaps the early maintenance loop.

**Why Jan 7 and not Dec 24:** the Aug 12 audit added 10 problems (53 Kadane's, four Trees, 346, 463, and the three Setup Easies), which is about 7 extra study days. Add the holiday rest blocks (including New Year's Eve) and the tail lands in the first week of January. That is the correct trade — per pacing rule 9, blocks shift forward and Core is never dropped. The only content past Dec 24 is **9 Grid (finishing)** and **10 Intervals**, and by then you're deep in the maintenance loop anyway.

```
Aug 12        Aug 17             Sep 14            Oct 12            Nov 9         Dec 6      Jan 7
  │ Setup │······ Phase 1 ······│··· Phase 2 ·····│··· Phase 3 ·····│· Phase 4 ·│···· tail ····│→ loop
  │warm-up│ 1.1–1.4 Two Pointers│ 2 Hash + 1.5–1.7│ 3 Window + 4    │ 5→6.1→7   │ 8 → 9 → 10   │
  │13/14/66│                    │   string TP     │ + start 5       │           │ trees/grid/iv │
  └───────┘                                                                       ↑ holidays built in
```

---

## Phase map (synced with JOB_SEARCH.md)

| Phase | Dates | DSA focus |
|---|---|---|
| Setup | Aug 12 – Aug 16 | **0** Warm-up re-solves + implementation Easies (13, 14, 66) |
| Phase 1 | Aug 17 – Sep 13 | **1.1–1.4** Two Pointers core only |
| Phase 2 | Sep 14 – Oct 11 | **2** Hashing → **1.5–1.7** string TP |
| Phase 3 | Oct 12 – Nov 8 | **3** Sliding Window → **4** Prefix Sum (incl. 53) |
| Phase 4 | Nov 9 – Dec 6 | **5** Stack → **6.1** Binary Search → **7** Linked List → start **8** Trees |
| Phase 4 tail | Dec 7 – Jan 7 | **8** Trees → **9** Grid → **10** Intervals (core; overlaps loop) |
| Loop | Jan 8 → | Reviews + mixed timed; add-ons only if hunting cold |

---

## 0 Setup warm-up — Core (no new patterns)

**When: Wed Aug 12 – Sun Aug 16** (5 days, before Phase 1 opens Mon Aug 17)

Two jobs this week: seed the review queue with problems you've seen, and get three **implementation** Easies under your belt. These three aren't pattern problems — there's no trick to spot. They're "can you write careful code and handle edge cases," which is exactly what online assessments and weaker startup screens lean on. Your whole curriculum after this is pattern drilling, so this is the one place that skill gets practiced directly.

| Day | Do |
|---|---|
| Wed Aug 12 | Cold re-solve 27, 26, 283 · new: **13 Roman to Integer (E)** |
| Thu Aug 13 | Cold re-solve 905, 977 · new: **14 Longest Common Prefix (E)** |
| Fri Aug 14 | Cold re-solve 217, 242, 1 · new: **66 Plus One (E)** |
| Sat Aug 15 – Sun Aug 16 | Finish the `JOB_SEARCH.md` setup checklist (resume / LinkedIn / GitHub / tracker). No new problems. |

**Unlocks:** careful-coding fluency — string scanning with edge cases (14), map + rule lookup (13), array digit carry (66). Low pattern content, high OA/take-home frequency.

---

## 1 Two Pointers

**Phase 1 block: Mon Aug 17 – Sat Sep 12** (string sub-patterns 1.5–1.7 wait until Phase 2, after Hashing).

### 1.1 Converging (opposite ends) — Core
**When: Mon Aug 17 – Tue Aug 25** (7 weekdays)
**Theory:** [`Theory/1.1_Two_Pointers_Converging.md`](Theory/1.1_Two_Pointers_Converging.md) — read before Day 1.

| Day | Solve |
|---|---|
| Mon Aug 17 | 125 Valid Palindrome (E), 977 Squares of a Sorted Array (E) |
| Tue Aug 18 | 2824 Count Pairs Whose Sum is Less than Target (E), 349 Intersection of Two Arrays (E) |
| Wed Aug 19 | 680 Valid Palindrome II (E) |
| Thu Aug 20 | 167 Two Sum II – Input Array Is Sorted (M) |
| Fri Aug 21 | 11 Container With Most Water (M) |
| Mon Aug 24 | 15 3Sum (M) |
| Tue Aug 25 | 881 Boats to Save People (M) · if time: cold re-solve 125 or 167 |

**Unlocks:** any "sorted array + pair/condition" problem — the most common two-pointer setup.
**Changes to your list:** removed 16, 18, 259. Added 125, 680, 2824. Re-sorted easiest→hardest: 2824 before 349 (plain counting before set intersection), and 11 before 15 (3Sum adds a sort plus an outer loop, so it's the harder of the two).

### 1.2 Fast & Slow — Core
**When: Wed Aug 26 – Tue Sep 1** (5 weekdays)

| Day | Solve |
|---|---|
| Wed Aug 26 | 392 Is Subsequence (E), 141 Linked List Cycle (E) |
| Thu Aug 27 | 876 Middle of the Linked List (E), 202 Happy Number (E) |
| Fri Aug 28 | 234 Palindrome Linked List (E) |
| Mon Aug 31 | 142 Linked List Cycle II (M) |
| Tue Sep 1 | 287 Find the Duplicate Number (M) |

**Unlocks:** cycle detection + middle-finding.
**Changes:** added 234, 142; moved 876 here from Fixed Separation. 392 is parallel pointers (one-off), parked here.
**Re-sorted easiest→hardest:** 392 opens the block — it's two pointers on plain strings, no linked list involved. 234 moved last of the Easies because it needs find-middle *and* reverse, so it depends on 876.

### 1.3 Fixed Separation (n apart) — Important
**When: Wed Sep 2 – Thu Sep 3**

| Day | Solve |
|---|---|
| Wed Sep 2 | 19 Remove Nth Node From End of List (M) |
| Thu Sep 3 | 2095 Delete the Middle Node of a Linked List (M) — **Optional** |

**Unlocks:** gap trick for one-pass linked-list deletion.
**Exception:** no Easies in this family — justified, the gap trick has no Easy form.
**Optional:** 2095 — 19 already teaches the gap trick and 19 is the one that actually gets asked. Skip 2095 first if behind, then come back for it.

### 1.4 In-place Array Modification — Core
**When: Fri Sep 4 – Fri Sep 11** (6 weekdays)

| Day | Solve |
|---|---|
| Fri Sep 4 | 27 Remove Element (E), 26 Remove Duplicates from Sorted Array (E) |
| Mon Sep 7 | 283 Move Zeroes (E), 905 Sort Array By Parity (E) |
| Tue Sep 8 | 88 Merge Sorted Array (E), 1089 Duplicate Zeros (E) |
| Wed Sep 9 | 80 Remove Duplicates from Sorted Array II (M) |
| Thu Sep 10 | 75 Sort Colors (M) |
| Fri Sep 11 | 443 String Compression (M) |

**Sat Sep 12 — Lock-in 1.1–1.4:** 3 mixed Two Pointers (unlabeled, timed). No new problems.
**Sun Sep 13 — Phase 1 checkpoint.**

**Unlocks:** reader/writer pointer separation.
**Changes:** removed 2337, 2938; added 88, 1089.

### 1.5 String Comparison with Skips — Important
**When: Wed Sep 30 – Thu Oct 1** *(Phase 2 — after Hashing)*

| Day | Solve |
|---|---|
| Wed Sep 30 | 844 Backspace String Compare (E), 1598 Crawler Log Folder (E) |
| Thu Oct 1 | 2390 Removing Stars From a String (M) |

**Unlocks:** “undo” characters; bridge into Stack (5).

### 1.6 Expanding From Center — Important ⚠
**When: Fri Oct 2 – Mon Oct 5**

| Day | Solve |
|---|---|
| Fri Oct 2 | 647 Palindromic Substrings (M) |
| Mon Oct 5 | 5 Longest Palindromic Substring (M) |

**Unlocks:** palindrome scanning without DP. Warm-up already done: 125.
**Exception:** no Easies exist; both are the same technique. Kept because #5 is extremely common.

### 1.7 String Reversal — Important
**When: Tue Oct 6 – Thu Oct 8**

| Day | Solve |
|---|---|
| Tue Oct 6 | 344 Reverse String (E) |
| Wed Oct 7 | 345 Reverse Vowels of a String (E) — **Optional** · 917 Reverse Only Letters (E) — **Optional** |
| Thu Oct 8 | 151 Reverse Words in a String (M) · 541 Reverse String II (E) — **Optional** |

**Fri Oct 9 — Buffer:** finish any slipped 2 / 1.5–1.7. Do not start 3 early unless fully caught up.
**Unlocks:** in-place swaps + word-level parsing (151).
**Core here is just 344 + 151.** 344 teaches the swap in about two minutes; 151 is the one with real interview presence (word-level parsing). 345, 917, and 541 are low-frequency variations on a technique you'll already own — **Optional**, skip first if behind, clear them later.

---

## 2 Hashing

**Phase 2 start: Mon Sep 14 – Tue Sep 29**

### 2.1 Seen Set / Existence Check — Core
**When: Mon Sep 14 – Fri Sep 18**

| Day | Solve |
|---|---|
| Mon Sep 14 | 217 Contains Duplicate (E), 1 Two Sum (E) |
| Tue Sep 15 | 136 Single Number (E), 268 Missing Number (E) |
| Wed Sep 16 | 448 Find All Numbers Disappeared in an Array (E) |
| Thu Sep 17 | 128 Longest Consecutive Sequence (M) |
| Fri Sep 18 | 36 Valid Sudoku (M) |

**Unlocks:** “have I seen this before?”
**Changes:** 1 Two Sum moved here from your old Sliding Window list.

### 2.2 Frequency Map / Counting — Core
**When: Mon Sep 21 – Mon Sep 28**

| Day | Solve |
|---|---|
| Mon Sep 21 | 242 Valid Anagram (E), 383 Ransom Note (E) |
| Tue Sep 22 | 387 First Unique Character in a String (E), 169 Majority Element (E) |
| Wed Sep 23 | 205 Isomorphic Strings (E), 290 Word Pattern (E) — **Optional** |
| Thu Sep 24 | 1207 Unique Number of Occurrences (E) |
| Fri Sep 25 | 49 Group Anagrams (M) |
| Mon Sep 28 | 347 Top K Frequent Elements (M) |

**Tue Sep 29 — Lock-in 2:** cold re-solve 217, 242, and either 1 or 49.

**Unlocks:** `Counter`/dict fluency; required before 3.3.
**Optional:** 290 — structurally the same two-way-mapping problem as 205, which you solve the same day. Free slot if you're behind.

---

## 3 Sliding Window

**Phase 3: Mon Oct 12 – Thu Oct 29**

### 3.1 Fixed Size — Core
**When: Mon Oct 12 – Thu Oct 15** · **Fri Oct 16 lock-in**

| Day | Solve |
|---|---|
| Mon Oct 12 | 346 Moving Average from Data Stream (E), 643 Maximum Average Subarray I (E) |
| Tue Oct 13 | 1652 Defuse the Bomb (E), 1876 Substrings of Size Three with Distinct Characters (E) |
| Wed Oct 14 | 2461 Maximum Sum of Distinct Subarrays With Length K (M) |
| Thu Oct 15 | 3318 Find X-Sum of All K-Long Subarrays I (E) — **Optional** · 3254 Find the Power of K-Size Subarrays I (M) — **Optional** |
| Fri Oct 16 | Lock-in: re-solve 643 + 2461 |

**Unlocks:** add-one / remove-one window update.
**Changes:** added 1652, 1876; moved 2461 from Variable Size. **Added 346** (Premium, now accessible) as the opener — it's the purest statement of the pattern: maintain a running sum, add the new element, drop the old one.
**Optional:** 3318 and 3254 are 2024 contest problems with no interview presence — they don't appear in Grind 75, NeetCode 150, or Sean Prashad's list. Core here is 346 → 643 → 1652 → 1876 → 2461 (4E/1M), which fully covers the pattern. Skip the two Optionals first if behind.

### 3.2 Variable Size — Core
**When: Mon Oct 19 – Mon Oct 26** · **Tue Oct 27 lock-in**

| Day | Solve |
|---|---|
| Mon Oct 19 | 121 Best Time to Buy and Sell Stock (E), 219 Contains Duplicate II (E) |
| Tue Oct 20 | 485 Max Consecutive Ones (E), 674 Longest Continuous Increasing Subsequence (E) |
| Wed Oct 21 | 209 Minimum Size Subarray Sum (M) |
| Thu Oct 22 | 3 Longest Substring Without Repeating Characters (M) |
| Fri Oct 23 | 424 Longest Repeating Character Replacement (M) |
| Mon Oct 26 | 1004 Max Consecutive Ones III (M) |
| Tue Oct 27 | Lock-in: re-solve 209 + 3 |

**Stretch (only if Oct 27 lock-in felt easy):** 713, 904, 1493 — do not steal time from 3.3/4.
**Unlocks:** grow-right / shrink-left with an invariant.
**Changes:** removed Hard 76 and Hard 3347; trimmed grindy Mediums; added Easies 121, 219, 485, 674. Lands 4E/4M (tie) — flagged ceiling for this family.

### 3.3 Frequency-Matching Windows — Important ⚠
**When: Wed Oct 28 – Thu Oct 29**

| Day | Solve |
|---|---|
| Wed Oct 28 | 567 Permutation in String (M) |
| Thu Oct 29 | 438 Find All Anagrams in a String (M) |

**Unlocks:** fixed window + frequency map (top phone-screen type).
**Exception:** no Easies; warm-ups were 2.2 (242, 383).

### ~~3.4 Monotonic Queue~~ — REMOVED
Hard-gated (239, 862). Wrong tier for entry-level.

---

## 4 Prefix Sum — Core

**When: Fri Oct 30 – Thu Nov 5** · **Fri Nov 6 lock-in 3–4**

| Day | Solve |
|---|---|
| Fri Oct 30 | 1480 Running Sum of 1d Array (E), 724 Find Pivot Index (E) |
| Mon Nov 2 | 1732 Find the Highest Altitude (E), 303 Range Sum Query – Immutable (E) |
| Tue Nov 3 | 53 Maximum Subarray (M) — **new** |
| Wed Nov 4 | 560 Subarray Sum Equals K (M) |
| Thu Nov 5 | 238 Product of Array Except Self (M) |
| Fri Nov 6 | Lock-in: 724 + 53 or 560 |

**Unlocks:** precompute-then-query; 53, 560, and 238 are all high-frequency Mediums.
**Added 53 Maximum Subarray (Kadane's algorithm)** — this was the clearest gap in the whole curriculum. It's in Blind 75 and it's one of the most-asked Mediums at every tier. It sits before 560 deliberately: both carry a running accumulator across one pass, and 53's version (reset when the sum goes negative) is the easier of the two to internalize.
**Sun Nov 8 — Phase 3 checkpoint** (`JOB_SEARCH.md`).

---

## 5 Stack

**Opens Phase 4 (Mon Nov 9).** Prefix Sum grew by one problem, so Stack now starts with the phase instead of straddling it.

### 5.1 Matching / Processing — Core
**When: Mon Nov 9 – Thu Nov 12** · **Fri Nov 13 lock-in**

| Day | Solve |
|---|---|
| Mon Nov 9 | 20 Valid Parentheses (E), 682 Baseball Game (E) |
| Tue Nov 10 | 1047 Remove All Adjacent Duplicates in String (E), 232 Implement Queue using Stacks (E) |
| Wed Nov 11 | 150 Evaluate Reverse Polish Notation (M) |
| Thu Nov 12 | 155 Min Stack (M) |
| Fri Nov 13 | Lock-in: 20 + 155 |

**Unlocks:** push/pop-on-match. 20 is among the most-asked entry-level questions.
**Re-sorted easiest→hardest:** 682 is a plain push/pop simulation, gentler than 1047's collapse-on-match. Among the Mediums, 150 is a direct application of the same push/pop reflex, while 155 requires inventing the auxiliary-minimum trick to hit O(1) — so 155 closes the block.

### 5.2 Monotonic Stack (light) — Important
**When: Mon Nov 16 – Tue Nov 17**

| Day | Solve |
|---|---|
| Mon Nov 16 | 496 Next Greater Element I (E), 1475 Final Prices With a Special Discount in a Shop (E) |
| Tue Nov 17 | 739 Daily Temperatures (M) |

**Unlocks:** next greater/smaller. Deeper monotonic stack (84, 42) is Hard — excluded.

---

## 6 Binary Search

### 6.1 Classic on Sorted Data — Core
**When: Wed Nov 18 – Wed Nov 25** · **Fri Nov 27 lock-in**

| Day | Solve |
|---|---|
| Wed Nov 18 | 704 Binary Search (E), 35 Search Insert Position (E) |
| Thu Nov 19 | 744 Find Smallest Letter Greater Than Target (E), 278 First Bad Version (E) |
| Fri Nov 20 | 69 Sqrt(x) (E), 367 Valid Perfect Square (E) — **Optional** |
| Mon Nov 23 | *(buffer / re-solve template if any Easy felt shaky)* |
| Tue Nov 24 | 34 Find First and Last Position of Element in Sorted Array (M) |
| Wed Nov 25 | 74 Search a 2D Matrix (M) |
| Thu Nov 26 | **Thanksgiving — rest.** No new problems. |
| Fri Nov 27 | Lock-in 6.1: cold re-solve 704 + 34 |

**Unlocks:** one `lo/hi/mid` template without off-by-ones; 34 is the real interview skill (boundaries).
**Optional:** 367 — same binary-search-on-a-number-range shape as 69, solved the same day. Nice reinforcement, not a new idea.

### 6.2 Rotated Arrays — Optional
**When: only after the Fri Nov 27 lock-in, and only if 6.1 is cold** — else skip until a company is known to ask it.

| LC # | Problem | Difficulty |
|---|---|---|
| 153 | Find Minimum in Rotated Sorted Array | Medium |
| 33 | Search in Rotated Sorted Array | Medium |

Excluded: binary-search-on-answer (875, 1011) — low entry-level frequency.

---

## 7 Linked List Manipulation — Core

**When: Mon Nov 30 – Thu Dec 3** · **Fri Dec 4 lock-in**

| Day | Solve |
|---|---|
| Mon Nov 30 | 206 Reverse Linked List (E), 21 Merge Two Sorted Lists (E) |
| Tue Dec 1 | 83 Remove Duplicates from Sorted List (E), 203 Remove Linked List Elements (E) |
| Wed Dec 2 | 2 Add Two Numbers (M) |
| Thu Dec 3 | 24 Swap Nodes in Pairs (M) |
| Fri Dec 4 | Lock-in: 206 + 21 |

Already done via 1: 141, 142, 234, 876, 19, 2095.
**Unlocks:** pointer rewiring + dummy head. Excluded: 146 LRU (add-back), 25 (Hard).

---

## 8 Trees BFS/DFS — Core (promoted from optional)

**When: Mon Dec 7 – Fri Dec 18** · **Mon Dec 21 lock-in**
Promoted because trees appear too often at entry level to gamble on skipping. This is the recursion-heavy section — go slow, one per day is fine.

**This block was expanded from 7 to 11 problems.** Trees were the one real under-weighting in the curriculum: Blind 75 gives trees 14 slots and Grind 75 puts seven tree problems in Week 1 of 8, because they're the highest-frequency non-array topic at entry level — and unlike graphs, that's not FAANG-inflated. The four additions are all canonical.

| Day | Solve |
|---|---|
| Mon Dec 7 | 104 Maximum Depth of Binary Tree (E) — *solo; this is the template* |
| Tue Dec 8 | 226 Invert Binary Tree (E), 100 Same Tree (E) |
| Wed Dec 9 | 101 Symmetric Tree (E) |
| Thu Dec 10 | 112 Path Sum (E) |
| Fri Dec 11 | 110 Balanced Binary Tree (E) — **new** |
| Mon Dec 14 | 543 Diameter of Binary Tree (E) — **new** |
| Tue Dec 15 | 572 Subtree of Another Tree (E) — **new** |
| Wed Dec 16 | 102 Binary Tree Level Order Traversal (M) — *new template: BFS + queue* |
| Thu Dec 17 | 235 Lowest Common Ancestor of a BST (M) |
| Fri Dec 18 | 98 Validate Binary Search Tree (M) — **new** |
| Mon Dec 21 | Lock-in: re-solve 104 + 102 |

**Unlocks:** the recursive DFS template (`if not node: return ...; recurse left/right`) and the BFS-with-a-queue template — these two cover the vast majority of entry-level tree questions.
**Why these four, in this order:** 110 and 543 both build directly on 104 — you return a height up the call stack and do something with it on the way. 543 is the same recursion as 110 with a different accumulator, so doing them back to back makes the shape obvious. 572 introduces "recurse while calling another recursion." 98 closes the block because passing bounds down the tree is the one genuinely new idea here, and it's the classic trap question (checking only parent-child instead of the full range).
**Recursion note:** if recursion feels shaky, that's expected — trees are where it clicks. Trace a small tree by hand on paper before coding. 104 is the gentlest start. This is the block to slow down in; 11 problems at one per day is fine and better than pairing.
**Difficulty mix:** 8E / 3M — comfortably Easy-majority.
**Excluded (still):** balanced/AVL, segment trees, serialization (297 is Hard).

---

## 9 Grid BFS/DFS — Core (new — was wrongly excluded)

**When: Tue Dec 22 – Tue Dec 29** · **Wed Dec 30 lock-in**
**Number of Islands (200) is one of the single most-asked questions at startups and entry-level loops.** Excluding the whole "graphs" bucket accidentally cut it — a mistake for your target roles. A grid is just an implicit graph; with 8's templates this is mostly applying DFS/BFS to a 2D array.

| Day | Solve |
|---|---|
| Tue Dec 22 | 463 Island Perimeter (E) — **new**, 733 Flood Fill (E) |
| Wed Dec 23 | 200 Number of Islands (M) |
| Thu Dec 24 – Fri Dec 25 | **Christmas — rest.** No new problems. |
| Mon Dec 28 | 695 Max Area of Island (M) |
| Tue Dec 29 | 994 Rotting Oranges (M) |
| Wed Dec 30 | Lock-in: re-solve 200 |

**Unlocks:** the "visit every cell, flood its neighbors, mark visited" pattern — 733/200/695 are one DFS template; 994 is the same idea with BFS + a queue (multi-source). Covers the grid-traversal family startups love.
**Added 463 Island Perimeter** as the on-ramp — it's iterate-every-cell-and-check-neighbors without any recursion, so it gets you comfortable indexing a 2D array before 733 adds the flood fill. Pairs with 733 on one day since both are Easy.
**Optional heap add-on** (only if hunting and everything else is cold): 703 Kth Largest in a Stream (E), 1046 Last Stone Weight (E), 215 Kth Largest Element in an Array (M). One evening; `heapq` fluency, occasionally asked.
**Excluded (still):** Dijkstra, union-find, topological sort, word-ladder — genuinely FAANG-tier, low ROI for you.

---

## 10 Intervals — Core (light)

**When: Mon Jan 4 – Wed Jan 6** · **Thu Jan 7 lock-in — last day of new learning**
Promoted from add-back to core: "sort by start, then merge/compare overlaps" is a high-frequency entry-level pattern that stands alone and is cheap to learn.

| Day | Solve |
|---|---|
| Thu Dec 31 – Fri Jan 1 | **New Year's Eve + New Year — rest.** No new problems. |
| Mon Jan 4 | 252 Meeting Rooms (E, *Premium — you have it*) |
| Tue Jan 5 | 56 Merge Intervals (M) |
| Wed Jan 6 | 57 Insert Interval (M) |
| Thu Jan 7 | Lock-in: re-solve 56 · **curriculum complete** |

**Unlocks:** the sort-then-sweep pattern — 56 is the canonical version; recognizing "these are intervals" is most of the battle.
**Exception:** interval Easies are thin, so this leans Medium (1E/2M) — kept small on purpose.
**Order fix:** 252 now runs first. It was listed last, after both Mediums, which broke the Easies-first rule — and it's the right warm-up anyway, since "sort by start, then check if the next start beats the current end" is the whole pattern in its simplest form.

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
| Trees + Grid last | They reuse recursion/DFS/BFS — easier once 1–7 built the base |
| Slip pushes dates; never skip reviews | Reviews are the product; the calendar is a guide |

**Still excluded on purpose:** DP, advanced graphs (Dijkstra / union-find / topo sort), backtracking, tries, monotonic deques, every Hard (including 76 and 3347 from your seed). *(Trees, grid BFS/DFS, and basic intervals were promoted to core — see 8, 9, 10.)*

**First add-backs** (only in the loop, still hunting): heap add-on (9) → 146 LRU Cache → 6.2 → 875 Koko → 2 intro DP (70 Climbing Stairs, 198 House Robber).

---

## Summary of edits to your seed lists

| Change | Detail |
|---|---|
| **Hards removed** | 76, 3347, 239, 862 (Pattern 10 dropped) |
| **Mediums trimmed** | 16, 18, 259 · 2337, 2938 · variable-window grind list |
| **Moved** | 1 → 2.1 · 876 → 1.2 · 2461 → 3.1 |
| **Easies added** | 125, 680, 2824, 234, 88, 1089, 917, 1652, 1876, 121, 485, 674 (+142 M) |
| **Gaps closed** | 8 Trees promoted to **core**; new 9 **Grid BFS/DFS** (200/695/733/994); new 10 **Intervals** (56/57); complexity-analysis rule (pacing 8); optional heap add-on |
| **Timeline** | Day-level dates Aug 17 → **Jan 7**; lock-ins; Phase 1 no longer includes Hashing; DSA tail overlaps early loop |

### Second audit (Aug 12) — verified against Grind 75 / Blind 75

| Change | Detail |
|---|---|
| **Verified** | All 114 problems checked for difficulty label. **Zero Hards; every label correct.** |
| **Added** | **53** Maximum Subarray (Kadane's — biggest single gap, Blind 75) · **110, 543, 572, 98** (Trees, under-weighted) · **346** Moving Average (Premium now accessible) · **463** Island Perimeter (Grid on-ramp) · **13, 14, 66** (Setup implementation Easies) |
| **Tagged Optional** | 2095, 290, 345, 367, 541, 917 (near-duplicates / low-frequency variations) · 3318, 3254 (2024 contest problems, no interview presence) — kept in the file, skipped first only if behind |
| **Re-sorted easiest→hardest** | 1.1 · 1.2 · 5.1 · 8 Trees · 10 Intervals (252 moved ahead of the Mediums) |
| **Access** | Premium confirmed — removed every "skip if no sub" gate; 252 and 346 restored to Core |
| **Kept deliberately** | **Two Pointers volume unchanged.** On a list this narrow, arrays/strings *should* be the largest share — the seven sub-patterns are genuinely different skills, not repetition. **Order kept as 6.1 → 7 → 8 → 9 → 10**: Binary Search and Linked List first is the better learning ramp (templates, then pointer rewiring, then recursion, then recursion on a grid). |

---

*Curriculum calendar built for start **Wed Aug 12, 2026**; DSA new-learning runs to **Thu Jan 7, 2027** (Trees → Grid → Intervals in the tail). If a weekday is lost (travel, interview, holiday), shift this file’s dates forward as a block — don’t compress, and don’t drop Core (pacing rule 9). Reminder: this file maximizes your technical-screen pass rate; it does not by itself get you the job — interview volume in `JOB_SEARCH.md` is the binding constraint.*

