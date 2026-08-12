# Entry-Level SWE Job Search Plan

**Source of truth** — edit this file whenever the plan changes.  
Pin this tab (right-click → Pin). Cmd+P → `JOB_SEARCH` opens it instantly.

From-zero plan starting **Wednesday, August 12, 2026** · Python · US-wide (remote + onsite) · startups / less competitive entry-level. You’re not actually at zero — compress Setup + Phase 1, don’t skip them.

| | |
|---|---|
| Core job-search timeline | ~17 weeks (Aug 12 – Dec 6), then ongoing loop |
| DSA learning tail | Runs to **Jan 7, 2027** (Trees → Grid → Intervals), overlaps early loop |
| Weekday load | ~5 hrs structured |
| Applications | ~55/week (tiered) |
| LeetCode | **114 Core** problems (+8 Optional), each re-solved 2–3× |

---

## Direct answers

### Applications — keep ~10/day, change the shape
~60/week is fine for a wide US net. After a year of applying, volume is probably not the bottleneck — **positioning** is. Tier daily applies: **3 tailored** (referral hunt + resume tweak) + **7 fast** to postings **&lt;3 days old**. If response rate is under ~2%, more volume multiplies a broken resume — fix resume first (Setup Sprint).

### New vs review — you’re right for your case
“Only new problems” assumes retention you don’t have (looked-up solutions forgotten). Do **1 new + 1–2 spaced reviews** per day. A looked-up problem counts as solved only after **two cold re-solves** from a blank editor (~2 days, ~1 week, ~3 weeks).

### Pattern drilling — agree, with one fix
Depth-first pattern blocks are right for learning. Pure blocking hides recognition skill. Fix: every **Saturday**, 3 mixed problems from covered patterns (unlabeled, timed). From Phase 4 on, majority-mixed.

---

## Pillars you were missing

1. **Resume / LinkedIn / GitHub** — highest ROI after a year of low conversion. Week one.
2. **Behavioral** — ~6 STAR stories by late September.
3. **Mocks** — Pramp / peers starting late September / early October.
4. **Practical skills** — Git, SQL, HTTP/APIs, debugging, take-homes (many startups skip LeetCode).
5. **Tracker + Sunday retro** — catches drift in a week, not a month.

---

## Timeline

```
Aug 12 ── Setup ── Aug 16 ── Phase1 ── Sep 13 ── Phase2 ── Oct 11 ── Phase3 ── Nov 8 ── Phase4 ── Dec 6 ── loop →
          5 days            4 wks             4 wks             4 wks             4 wks
                                                                 (DSA tail: trees/grid/intervals → Jan 7, 2027)
```

### Setup Sprint — Wed Aug 12 – Sun Aug 16
Drop apps to ~5/day this week only. Fix the machine:

- Rewrite resume (1 page, metrics, links). Get **2 outside reviews** (r/EngineeringResumes wiki format).
- LinkedIn: headline, About, open-to-work (recruiters), skills, location **US Remote + Boston**.
- GitHub: pin 2–3 best repos, READMEs + screenshots, hide junk.
- Tracker sheet: company, role, date, source, tier, referral?, response, stage.
- Python warm-up: re-solve 8–10 easy array problems cold (seeds review queue) + 3 new implementation Easies (13, 14, 66) — see `DSA_CURRICULUM.md` **0 Setup warm-up**.
- Book one Boston tech meetup for August/September.

**Five days, not ten.** Submit the resume for outside review on **day 1** — reviews take days to come back, so start that clock immediately and keep doing the rest of the list while you wait. **Phase 1 DSA starts Mon Aug 17 regardless of whether the reviews have landed.** Never block LeetCode on a resume review.

### Phase 1 — Mon Aug 17 – Sun Sep 13 · Two Pointers core only
- DSA: Curriculum **1.1–1.4** only (Converging → Fast/Slow → Fixed Separation → In-place). Hashing waits for Phase 2 — packing both into 4 weeks was too much new for retention.
- Full app volume resumes Aug 17 (~55/wk).
- Project 1 starts Aug 17: deployed Python web app (FastAPI/Flask + DB + simple UI). Ship by mid-Oct. Commit every project day.
- Networking: 10 outreach/week.
- First mixed Saturday: Aug 29. **Sat Sep 12 = 1 lock-in** (mixed Two Pointers only).

**Checkpoint Sun Sep 13:** ~150 apps since Aug 12. Responses &lt;2% → professional resume review before Phase 2.

### Phase 2 — Mon Sep 14 – Sun Oct 11 · Hashing + string Two Pointers
- DSA: Curriculum **2** Hashing → **1.5–1.7** (string skips / expand-center / reversal). Day-level dates in `DSA_CURRICULUM.md`.
- Draft 6 STAR stories by Sun Sep 27. Practice “tell me about yourself” out loud.
- Mocks: Sat Sep 26, Sat Oct 10.
- Ship Project 1 by Sun Oct 11 (deployed, README, demo GIF, on resume).

**Checkpoint Sun Oct 11:** zero interviews → move 30 min/day from apps to networking/referrals.

### Phase 3 — Mon Oct 12 – Sun Nov 8 · Sliding Window + Prefix Sum
- DSA: Curriculum **3** Sliding Window → **4** Prefix Sum (now includes **53 Maximum Subarray / Kadane's**). Stack now opens Phase 4 on Nov 9.
- Mixed Saturdays from 6+ patterns.
- Mocks: Oct 24, Nov 7.
- Project 2 starts Oct 12: real data/users + tests + CI (GitHub Actions). SQLBolt ~2 hrs.

**Checkpoint Sun Nov 8:** re-solve rate &lt;80% on review queue → Phase 4 drops remaining new topics and goes consolidation-only.

### Phase 4 — Mon Nov 9 – Sun Dec 6 · Stack → BS → Linked List → start Trees
- DSA: **5** Stack → **6.1** Binary Search → **7** Linked List → start **8** Trees on Dec 7 (dates in curriculum). **8 Trees, 9 Grid BFS/DFS, and 10 Intervals are all core** and run through **Jan 7, 2027** — interviewing continues past Dec 6, so DSA does too.
- Weekly mocks: Nov 14, Nov 21, Nov 28, Dec 5.
- Project 2 shipped by Nov 29; resume updated.
- Apps + networking stay at full volume.

**Checkpoint Sun Dec 6:** no traction → reposition (contract-to-hire, apprenticeships, QA automation / support eng as SWE on-ramps) — change positioning, not effort.

### Maintenance loop — Mon Dec 7 → ongoing
Dec 7 – Jan 7 the loop overlaps the DSA tail (Trees → Grid → Intervals per curriculum). From **Fri Jan 8** onward it's pure loop:
1 mixed timed + 1 review daily · ~40 apps/week · networking quota · 1 mock/week · project iteration.  
**Interview scheduled → prep overrides the calendar.**

---

## Daily routine (Mon–Fri)

| Time | Block | What you do |
|---|---|---|
| 9:00–10:30 | LeetCode (90 min) | 1 new in current pattern (30-min struggle cap → solution → re-implement). Then 1–2 reviews from blank editor. |
| 10:30–11:00 | Pattern theory (30 min) | Thita or NeetCode for current pattern. Hand-write the template once. |
| 11:00–12:15 | Applications (75 min) | 3 tailored + 7 fast (&lt;3 days old). Log every one. |
| 12:15–1:00 | Break | Eat, walk, no screens. |
| 1:00–1:30 | Networking (30 min) | 2–3 outreach/follow-ups. Follow up anything 3+ days stale. |
| 1:30–3:00 | Project (90 min) | One visible increment. Commit daily. |

**Saturday (~2.5 hrs):** 3 mixed timed problems (25 min each) + 5 quick applies + meetup if scheduled.  
**Sunday (30 min):** Rest + retro — apps, responses, retention, outreach. One sentence: what changes next week?

### Bad-day minimum (~45 min)
1 review + 5 applies + 1 follow-up. **Never zero.** One zero day becoming a zero week is the failure mode.

---

## Pattern priority (entry-level ROI)

Sliding Window was missing from your original list — it’s Core for arrays/strings.
**Full problem-by-problem list: [`DSA_CURRICULUM.md`](DSA_CURRICULUM.md)** — section numbers below refer to it.

| # | Topic | Curriculum | When | Why |
|---|---|---|---|---|
| 0 | Implementation Easies | 0 | Aug 12–14 | OA / take-home style; no pattern to spot, just careful code |
| 1 | Two Pointers core | 1.1–1.4 | Aug 17–Sep 12 | Highest-frequency easy/medium array pattern |
| 2 | Hashing (freq / seen) | 2 | Sep 14–Sep 29 | Most common entry-level “trick”; unlocks windows |
| 3 | String Two Pointers | 1.5–1.7 | Sep 30–Oct 8 | After hashing; bridges into stacks |
| 4 | Sliding Window | 3 | Oct 12–Oct 29 | Needs hashing first |
| 5 | Prefix Sum + Kadane's | 4 | Oct 30–Nov 6 | Cheap, high-ROI Mediums (53, 560, 238) |
| 6 | Stacks | 5 | Nov 9–Nov 17 | Parentheses family |
| 7 | Binary Search (basic) | 6.1 | Nov 18–27 | One template, many easy wins |
| 8 | Linked Lists (basic) | 7 | Nov 30–Dec 4 | Reverse / merge — low depth |
| 9 | Trees BFS/DFS | 8 | Dec 7–Dec 21 | Highest-frequency non-array topic — 11 problems, go slow |
| 10 | Grid BFS/DFS | 9 | Dec 22–Dec 30 | Number of Islands family — very common |
| 11 | Intervals | 10 | Jan 4–Jan 7 | Merge Intervals — high-frequency, cheap |

**Defer:** DP, advanced graphs (Dijkstra/union-find/topo), backtracking, tries, matrix spiral/rotation. Wrong tier for your targets. *(Trees, grid BFS/DFS, and basic intervals were promoted to core — see `DSA_CURRICULUM.md`.)*

---

## Resource stack (max 2 active at once)

| Role | Resource | How | Cost |
|---|---|---|---|
| Spine | `DSA_CURRICULUM.md` (this repo) | The exact problem set: pattern → sub-pattern → problems, Easy-first, zero Hards. Work through it in order. | Free |
| Theory / visuals | Thita DSA Patterns (free tier) | Read the subpattern page before starting each block. ~40% Pro-locked; 2 weeks free before paying. | Free → maybe Pro |
| Explanations | NeetCode (site + YouTube) | Watch after every attempt. | Free |
| Written lookup | LeetCode Crash Course (owned) | Don’t go linear. Lookup only for priority topics. | Owned |
| Practical | Projects + SQLBolt + Exercism | Ship projects. SQLBolt ~2 hrs in Phase 3. Exercism only for syntax gaps. | Free |

**Rule:** no resource-switching mid-phase. Re-evaluate only at checkpoints.

---

## Where applications go

| Channel | Why | Cadence |
|---|---|---|
| **LinkedIn (saved alerts) — PRIMARY** | Entry level, US remote + Boston/NYC; apply within 3 days of posting; most daily volume goes here | Daily |
| Wellfound | Startup roles; founders sometimes reply directly | Daily |
| Welcome to the Jungle | Mid-size / startup filters | 3×/week |
| HN “Who’s Hiring” | 1st of month; email founders; high reply rate | Sep–Dec 1st |
| Boring industries (insurance, banks, healthcare, logistics, gov) | Far less competition | Weekly batch |
| Staffing / contract-to-hire | Fast placement; real on-ramp | Profiles in Aug/Sep; lean in from Nov if needed |

*Dropped Jul 23: Built In + YC Work at a Startup (repeated apps, zero responses — too competitive for the return).*

### Networking weekly quota

| Action | Quota | Notes |
|---|---|---|
| New outreach | 10/week | Short, specific; ask for 15 min / one question — never “a job” |
| Referral asks | 2/week | After warm exchange only |
| Boston meetup | 1 per 2 weeks | Boston New Tech, Python meetups, etc. |
| Follow-ups | Everything 3+ days stale | Most replies come from the follow-up |

---

## Checkpoints and kill-switches

| Date (Sun) | Checkpoint | Decision rule |
|---|---|---|
| Aug 16 | Resume rewritten + reviewed 2×, LinkedIn, GitHub, tracker | Not done → **DSA still starts Aug 17.** Only the application ramp waits: stay at ~5/day until the resume is reviewed, then go to full volume. |
| Sep 13 | ~150 apps, ~24 problems mastered | Response rate &lt;2% → professional resume review |
| Oct 11 | Project 1 live, 2 mocks, story bank | Zero interviews → 30 min/day apps → networking |
| Nov 8 | Patterns 1–4 done (TP, Hash, Window, Prefix incl. Kadane's) | Re-solve &lt;80% → Phase 4 slows new-topic pace, mixed reviews rise. **Never drop Core — shift dates instead.** |
| Dec 6 | 4-month review · patterns 5–7 done, 8 Trees starting Dec 7 | No traction → reposition (contract-to-hire / apprenticeships / adjacent roles) |
| Jan 7 | DSA new-learning complete (patterns 0–10, 114 Core) | From here, curriculum stops adding; only reviews + mixed. Clear any Optional backlog. |

**Standing rule:** a scheduled interview overrides the calendar.

---

*Built Jul 23, 2026 · updated Aug 12, 2026 (start → **Aug 12**; Setup compressed to 5 days so Phase 1 still opens Mon Aug 17; resume-review gate no longer blocks DSA; curriculum audited → 114 Core problems, Trees expanded, Kadane's added; **DSA tail → Jan 7, 2027** with holiday rest days built in). Assumes job search is primary (~5 hrs/day). Part-time: same block order, half durations — cut project time last, application time first.*
