# Entry-Level SWE Job Search Plan

**Source of truth** — edit this file whenever the plan changes.  
Pin this tab (right-click → Pin). Cmd+P → `JOB_SEARCH` opens it instantly.

From-zero plan starting **Friday, July 24, 2026** · Python · US-wide (remote + onsite) · startups / less competitive entry-level. You’re not actually at zero — compress Setup + Phase 1, don’t skip them.

| | |
|---|---|
| Core timeline | 17.5 weeks (then ongoing loop) |
| Weekday load | ~5 hrs structured |
| Applications | ~55/week (tiered) |
| LeetCode | ~110 new problems, each re-solved 2–3× |

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
2. **Behavioral** — ~6 STAR stories by mid-September.
3. **Mocks** — Pramp / peers starting September.
4. **Practical skills** — Git, SQL, HTTP/APIs, debugging, take-homes (many startups skip LeetCode).
5. **Tracker + Sunday retro** — catches drift in a week, not a month.

---

## Timeline

```
Jul 24 ── Setup ── Aug 2 ── Phase1 ── Aug 30 ── Phase2 ── Sep 27 ── Phase3 ── Oct 25 ── Phase4 ── Nov 22 ── loop →
         1.5 wks           4 wks             4 wks             4 wks             4 wks
```

### Setup Sprint — Fri Jul 24 – Sun Aug 2
Drop apps to ~5/day this week only. Fix the machine:

- Rewrite resume (1 page, metrics, links). Get **2 outside reviews** (r/EngineeringResumes wiki format).
- LinkedIn: headline, About, open-to-work (recruiters), skills, location **US Remote + Boston**.
- GitHub: pin 2–3 best repos, READMEs + screenshots, hide junk.
- Tracker sheet: company, role, date, source, tier, referral?, response, stage.
- Python warm-up: re-solve 8–10 easy array problems cold (seeds review queue).
- Book one Boston tech meetup for August.

### Phase 1 — Mon Aug 3 – Sun Aug 30 · Two Pointers core only
- DSA: Curriculum **§1.1–1.4** only (Converging → Fast/Slow → Fixed Separation → In-place). Hashing waits for Phase 2 — packing both into 4 weeks was too much new for retention.
- Full app volume resumes Aug 3 (~55/wk).
- Project 1 starts Aug 3: deployed Python web app (FastAPI/Flask + DB + simple UI). Ship by late Sep. Commit every project day.
- Networking: 10 outreach/week.
- First mixed Saturday: Aug 15. **Sat Aug 29 = §1 lock-in** (mixed Two Pointers only).

**Checkpoint Sun Aug 30:** ~150 apps since Jul 24. Responses &lt;2% → professional resume review before Phase 2.

### Phase 2 — Mon Aug 31 – Sun Sep 27 · Hashing + string Two Pointers
- DSA: Curriculum **§2** Hashing → **§1.5–1.7** (string skips / expand-center / reversal). Day-level dates in `DSA_CURRICULUM.md`.
- Draft 6 STAR stories by Sun Sep 13. Practice “tell me about yourself” out loud.
- Mocks: Sat Sep 12, Sat Sep 26.
- Ship Project 1 by Sun Sep 27 (deployed, README, demo GIF, on resume).

**Checkpoint Sun Sep 27:** zero interviews → move 30 min/day from apps to networking/referrals.

### Phase 3 — Mon Sep 28 – Sun Oct 25 · Sliding Window + Prefix Sum + start Stack
- DSA: Curriculum **§3** Sliding Window → **§4** Prefix Sum → start **§5.1** Stack (from ~Oct 23).
- Mixed Saturdays from 6+ patterns.
- Mocks: Oct 10, Oct 24.
- Project 2 starts Sep 28: real data/users + tests + CI (GitHub Actions). SQLBolt ~2 hrs.

**Checkpoint Sun Oct 25:** re-solve rate &lt;80% on review queue → Phase 4 drops remaining new topics and goes consolidation-only.

### Phase 4 — Mon Oct 26 – Sun Nov 22 · Finish Stack → BS → Linked List → mixed
- DSA: finish **§5** → **§6.1** Binary Search → **§7** Linked List (dates in curriculum). Then majority-mixed. **§8 Trees only if §1–7 are ≥80% cold.**
- Weekly mocks: Oct 31, Nov 7, Nov 14, Nov 21.
- Project 2 shipped by Nov 15; resume updated.
- Apps + networking stay at full volume.

**Checkpoint Sun Nov 22:** no traction → reposition (contract-to-hire, apprenticeships, QA automation / support eng as SWE on-ramps) — change positioning, not effort.

### Maintenance loop — Mon Nov 23 → ongoing
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
| 1 | Two Pointers core | §1.1–1.4 | Aug 3–29 | Highest-frequency easy/medium array pattern |
| 2 | Hashing (freq / seen) | §2 | Aug 31–Sep 15 | Most common entry-level “trick”; unlocks windows |
| 3 | String Two Pointers | §1.5–1.7 | Sep 16–24 | After hashing; bridges into stacks |
| 4 | Sliding Window | §3 | Sep 28–Oct 15 | Needs hashing first |
| 5 | Prefix Sum | §4 | Oct 16–22 | Cheap, high-ROI Mediums (560, 238) |
| 6 | Stacks | §5 | Oct 23–Nov 2 | Parentheses family |
| 7 | Binary Search (basic) | §6.1 | Nov 3–12 | One template, many easy wins |
| 8 | Linked Lists (basic) | §7 | Nov 13–19 | Reverse / merge — low depth |
| 9* | Trees BFS/DFS (optional) | §8 | Nov 20–22 if ahead | Only if §1–7 are ≥80% cold |

**Defer:** graphs, DP, backtracking, heaps, tries, matrix spiral/rotation. Wrong tier for your targets.

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
| HN “Who’s Hiring” | 1st of month; email founders; high reply rate | Aug–Nov 1st |
| Boring industries (insurance, banks, healthcare, logistics, gov) | Far less competition | Weekly batch |
| Staffing / contract-to-hire | Fast placement; real on-ramp | Profiles in Aug; lean in from Oct if needed |

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
| Aug 2 | Resume rewritten + reviewed 2×, LinkedIn, GitHub, tracker | Not done → Phase 1 waits |
| Aug 30 | ~150 apps, ~24 problems mastered | Response rate &lt;2% → professional resume review |
| Sep 27 | Project 1 live, 2 mocks, story bank | Zero interviews → 30 min/day apps → networking |
| Oct 25 | 7 patterns covered | Re-solve &lt;80% → Phase 4 consolidation only |
| Nov 22 | 4-month review | No traction → contract-to-hire / apprenticeships / adjacent roles |

**Standing rule:** a scheduled interview overrides the calendar.

---

*Built Jul 23, 2026 · updated Jul 23 (start → Jul 24; LinkedIn primary; Built In + YC WaaS dropped; curriculum moved to `DSA_CURRICULUM.md`). Assumes job search is primary (~5 hrs/day). Part-time: same block order, half durations — cut project time last, application time first.*
