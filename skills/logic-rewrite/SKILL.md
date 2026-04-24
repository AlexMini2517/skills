---
name: logic-rewrite
description: Rewrite code logic from scratch when the current approach is fundamentally wrong or suboptimal. Use this skill whenever the problem needs a better algorithm, data structure, computational strategy, or design approach rather than cleanup. Trigger on code with poor asymptotic complexity, the wrong abstraction for the access pattern, overcomplicated control flow, or designs that cannot be fixed by simple refactoring.
license: MIT
---

# Logic Rewrite

## Overview

Use this skill when the code's structure is not the real problem. The real problem is that it solves the task in the wrong way.

`logic-rewrite` is not a cleanup skill. It is for cases where the current implementation should be rethought and replaced with a better algorithm, a better data structure, or a better design model. The output may look very different from the original code because preserving the old structure is not the goal.

Use `refactor` for incremental cleanup that preserves behavior and overall structure. Use `logic-rewrite` when the structure follows from a bad approach and keeping it would preserve the mistake.

## When to Use

Use this skill when:

- The code uses a suboptimal algorithm and a materially better one is available
- The code uses the wrong data structure for how the data is queried, updated, or indexed
- The implementation takes a roundabout path to solve something that can be solved directly
- Control flow is complicated because the model is wrong, not because names are bad
- Performance problems come from the core approach, not from micro-optimizations
- The code works only because of patches, flags, or special cases piled onto a weak design
- The user asks for a rewrite, a smarter approach, a better algorithm, or a new design for the logic

Typical examples:

- Replacing nested scans with sorting, hashing, heaps, prefix sums, binary search, graph traversal, or dynamic programming
- Replacing repeated list membership checks with sets or maps
- Replacing imperative state spaghetti with a state machine, rule engine, or pipeline
- Replacing duplicate recomputation with caching, indexing, batching, or precomputation
- Replacing fragile branching with a more suitable model of the domain

## When NOT to Use

Do not use this skill when:

- The task is mostly renaming, extraction, file organization, or cleanup
- The user explicitly wants behavior-preserving refactoring only
- The current algorithm is already appropriate and the main issue is readability
- The problem is a local bug rather than a flawed overall approach
- The proposed rewrite would add complexity without meaningful gains

If the right answer is "keep the same logic, just make it cleaner", use `refactor`, not this skill.

## Core Mindset

Start from intent, not implementation.

Ask:

1. What is this code actually trying to achieve?
2. What constraints matter here: performance, correctness, memory, simplicity, extensibility?
3. Why is the current logic weak: algorithm, data structure, abstraction, state model, or decomposition?
4. What would you build if you were solving this problem fresh today?

Do not become attached to the current call graph, helper layout, or class structure. Those are outputs of the current design, not requirements.

## Rewrite Workflow

### 1. Recover intent

Before changing code, identify:

- Required behavior
- Important invariants
- Edge cases the current code is trying to handle
- Complexity hotspots
- Data access patterns: lookup-heavy, append-heavy, ordered traversal, random access, deduplication, graph relationships, streaming, etc.

Preserve intent and externally required behavior unless the user asked to change behavior too.

### 2. Diagnose the real flaw

Name the root issue explicitly. Prefer concrete diagnoses such as:

- "This does repeated linear scans inside another scan"
- "This stores lookup-oriented data in an array instead of a map"
- "This models a state transition problem as ad hoc booleans"
- "This recalculates derived values on every call instead of indexing once"
- "This branches on types manually when polymorphism or table-driven dispatch fits better"

Avoid vague claims like "the code is messy." Messiness is often a symptom, not the reason to rewrite.

### 3. Choose a better model

Pick the replacement approach deliberately:

- Better algorithm
- Better data structure
- Better ownership boundaries
- Better state representation
- Better processing pipeline
- Better domain abstraction

State the trade-offs. A rewrite is justified only when the new approach is meaningfully better in at least one important dimension without unacceptable regressions elsewhere.

### 4. Rewrite from first principles

Implement the new logic as if the old structure did not exist.

That does not mean ignoring useful pieces. You may reuse tests, domain types, interfaces, or helper utilities when they still fit. But do not force the new implementation to mimic the old decomposition if it no longer makes sense.

### 5. Compare before and after

Always explain:

- What the old logic was doing
- Why it was suboptimal
- What the new logic does differently
- Why the new approach is better
- What trade-offs changed

Focus on complexity, correctness, clarity, maintainability, and operational behavior.

## Decision Rules

Prefer the simplest approach that fixes the real problem.

Good rewrites:

- Remove whole categories of special-case logic
- Replace implicit behavior with explicit invariants
- Improve asymptotic complexity when it matters
- Match the data structure to the dominant access pattern
- Make correctness easier to reason about

Bad rewrites:

- Rebuild everything because the code looks ugly
- Swap one clever solution for another even more clever solution
- Introduce abstract patterns with no concrete payoff
- Preserve accidental behavior just because the old code had it
- Claim performance wins without identifying the original bottleneck

## Output Expectations

When using this skill, include:

1. A short explanation of the original intent
2. A clear diagnosis of why the current logic is the wrong approach
3. The rewritten implementation
4. A before/after comparison with explicit trade-offs
5. Any important complexity change, such as `O(n^2) -> O(n log n)` or array lookups -> map lookups

If the rewrite is large, summarize the new architecture first so the reader understands the replacement model before reading code.

## Comparison Template

Use a comparison shaped like this when relevant:

```markdown
## Logic rewrite summary
- Intent: ...
- Old approach: ...
- Problem: ...
- New approach: ...
- Why it is better: ...
- Trade-offs: ...
```

## Examples

### Example 1: Wrong algorithm

**Bad fit for refactor**

The code checks every item against every other item to find overlaps, then asks for "clean up" because the function is long. The real issue is the `O(n^2)` algorithm.

**Good fit for logic-rewrite**

Sort intervals first, then merge in one pass. The function may still be renamed later, but the main value is replacing the algorithm.

### Example 2: Wrong data structure

**Bad fit for refactor**

The code stores records in an array and repeatedly does `.find()` for ID lookup in hot paths. Extracting helpers does not solve the repeated linear search.

**Good fit for logic-rewrite**

Rebuild the logic around a `Map` keyed by ID, with clear update and lookup semantics.

### Example 3: Wrong domain model

**Bad fit for refactor**

The code represents workflow status with many booleans like `isPending`, `isRunning`, `isRetrying`, `isComplete`, and branches on combinations.

**Good fit for logic-rewrite**

Replace the boolean mesh with an explicit state machine or discriminated union so valid transitions are obvious and invalid states become harder to represent.

## Guardrails

- Do not default to preserving old structure
- Do not present cosmetic cleanup as a logic rewrite
- Do not rewrite without naming the flaw in the original approach
- Do not optimize blindly; connect the rewrite to actual usage or maintainability pain
- Do not hide trade-offs; mention memory cost, implementation complexity, migration risk, or lost flexibility when relevant

## Relationship to Refactor

Use this distinction:

- `refactor`: same solution, better shape
- `logic-rewrite`: better solution, new shape

If both are needed, do the logic rewrite first. Cleanup is easier after the core approach is sound.
