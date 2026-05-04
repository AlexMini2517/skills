---
name: code-polish
description: >
  Rewrites and improves a code file to maximize quality, readability, and adherence to best practices —
  without changing the external behavior or architecture. Use this skill whenever the user says things like
  "improve my code", "polish this file", "make this code cleaner", "rewrite this better", "clean up my code",
  "migliorami questo codice", "riscrivi meglio", "pulizia del codice", or sends a file asking for a better version.
  Also trigger when the user mentions bad naming, messy code, poor readability, or wants a "clean version"
  of an existing file. Do NOT use for architectural refactoring (restructuring logic, splitting modules,
  changing design patterns) — that is handled by the refactor skill.
---

# Code Polish Skill

Transform a code file into a cleaner, higher-quality version. The goal is to improve the code
**as written** — same logic, same structure, same behavior — but with better naming, style,
readability, consistency, and adherence to language-specific best practices.

---

## When to use this skill

- User sends a file or code snippet and wants a "better version"
- Code has poor naming, inconsistent style, magic numbers, unclear logic flow
- Code works but is hard to read, maintain, or understand
- User wants to apply best practices or idiomatic patterns for the language

**Not this skill:**
- Architectural changes, splitting into modules → use refactor skill
- Bug fixing (unless the fix is cosmetic/trivial)
- Optimization for performance (unless trivially achievable with no trade-offs)

---

## Workflow

### Step 1 — Understand the code

Before doing anything, read the file carefully and identify:
- Language and version (Python 3.11, TypeScript 5, Java 17, etc.)
- Purpose of the code (what it does)
- Obvious quality issues (see checklist below)
- Any constraints the user mentioned (keep library X, don't rename public API, etc.)

If the file is large (>300 lines), ask the user if they want the full file polished or a specific section.

### Step 2 — Polish the code

Apply all relevant improvements from the checklist below. The output should be a **complete, working rewrite** of the file — not a diff, not a partial snippet. The user should be able to drop it in and use it immediately.

Key principle: **preserve behavior exactly**. If something looks like a bug, flag it as a comment but do not silently change it.

### Step 3 — Deliver the output

Apply all improvements and deliver the polished file. After delivering, include a concise **"What changed"** summary grouped by category (naming, style, clarity, docs, etc.), and a **"Worth noting"** section for any bugs or design issues spotted outside the scope of polishing.

---

## Polish Checklist

### Naming
- [ ] Variables, functions, classes have clear, descriptive names
- [ ] No single-letter variables (except conventional: `i`, `j`, `k` in loops; `e` in catch blocks)
- [ ] No misleading names (e.g., `data` for a list of users → `users`)
- [ ] Boolean names are phrased as predicates (`isValid`, `hasPermission`, `isEmpty`)
- [ ] Functions named as verbs (`getUserById`, not `userById`)
- [ ] Constants are UPPER_SNAKE_CASE (if language convention)

### Constants & Magic Numbers
- [ ] Magic numbers extracted to named constants
- [ ] Magic strings extracted to constants or enums
- [ ] No hardcoded config values in business logic

### Code Clarity
- [ ] Complex expressions broken into named intermediate variables
- [ ] Nested ternaries replaced with readable conditionals
- [ ] Long functions broken into smaller helpers (only if it improves clarity without restructuring)
- [ ] Dead code, commented-out code, and debug prints removed
- [ ] Redundant conditions or variables eliminated

### Comments & Documentation
- [ ] Inline comments explain *why*, not *what* (obvious code needs no comment)
- [ ] Function/method docstrings added where behavior is non-obvious (follow language conventions: JSDoc, Python docstrings, Javadoc, etc.)
- [ ] TODO/FIXME comments preserved (they are intentional)
- [ ] Misleading or outdated comments removed or corrected

### Style & Consistency
- [ ] Consistent indentation (use the dominant style in the file; default to language standard)
- [ ] Consistent quote style (single vs double — pick one)
- [ ] Consistent spacing (around operators, after commas, blank lines between sections)
- [ ] Import/include statements organized (standard lib first, third-party, local — language convention)
- [ ] No trailing whitespace, no inconsistent blank lines

### Idiomatic Code
- [ ] Use language-idiomatic patterns (list comprehensions in Python, optional chaining in JS/TS, streams in Java, etc.)
- [ ] Replace verbose patterns with idiomatic equivalents (e.g., `if x is None` instead of `if x == None` in Python)
- [ ] Use built-in functions/methods instead of reimplementing them
- [ ] Avoid anti-patterns common to the language

### Error Handling
- [ ] Exceptions/errors have descriptive messages
- [ ] Catch blocks are specific (not bare `except:` or `catch (e) {}` unless intentional)
- [ ] Error handling is consistent throughout the file

---

## Language-Specific Notes

**Python**
- Follow PEP 8 (naming, spacing, line length ~88 chars with Black convention)
- Prefer f-strings over `.format()` or `%`
- Use `pathlib` over `os.path` for path operations
- Type hints on function signatures if the codebase uses them

**JavaScript / TypeScript**
- Prefer `const` over `let`; avoid `var`
- Use arrow functions for callbacks; named functions for top-level
- TypeScript: ensure types are explicit on function signatures; avoid `any`
- Async: prefer `async/await` over raw `.then()` chains

**Java**
- Use `var` (Java 10+) where the type is obvious from the right-hand side
- Prefer `List.of()`, `Map.of()` for immutable collections
- Use enhanced for-loops and streams idiomatically
- Ensure `@Override` annotations are present

**C / C++**
- Consistent use of `const` correctness
- Prefer `nullptr` over `NULL` (C++)
- Resource management: RAII, smart pointers (C++)

**General**
- If the language has a widely-used formatter (Black, Prettier, gofmt), apply its conventions manually

---

## Output Format

```
**What changed:**
- **Naming:** [specific changes]
- **Constants:** [specific changes]
- **Clarity:** [specific changes]
- **Style:** [specific changes]
- **Docs:** [specific changes]

**Worth noting (outside polish scope):**
- [Optional — flag bugs, design issues, or improvement opportunities]
```