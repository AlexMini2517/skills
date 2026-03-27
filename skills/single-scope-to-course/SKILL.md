---
name: single-scope-to-course
description: "Create a detailed, beginner-friendly interactive lesson from exactly one target: either one file or one folder. Use this skill whenever the user asks to explain a specific file/folder in depth, says 'spiegami questo file/cartella', asks for a focused code walkthrough, or wants to avoid full-codebase analysis. Prefer this skill over broad codebase-course skills when scope must stay narrow and explicit."
---

# Single Scope to Course

Turn exactly one user-selected target into a detailed learning artifact for non-technical users.

## What This Skill Does

Given one file OR one folder, create a deep and practical explanation focused only on that scope:
- explain what it does
- explain how it works internally
- explain how it connects to nearby code (without drifting into full codebase analysis)
- explain why design choices matter
- teach vocabulary and debugging intuition

Default output is a single self-contained HTML learning page. If the user explicitly asks for a text-only explanation, return structured Markdown instead.

## Trigger Rules

Use this skill when the user asks things like:
- "spiegami questo file"
- "analizza solo questa cartella"
- "voglio una spiegazione dettagliata ma solo di X"
- "non voglio tutta la codebase, solo questo pezzo"
- "make a focused walkthrough of this module"

Do not use this skill when the user clearly asks for full-project architecture coverage.

## Scope Guardrails (Critical)

1. Require exactly one target path.
2. If the user gives multiple paths, ask them to choose one.
3. Do not expand scope beyond the selected file/folder.
4. You may read minimal neighboring files only when needed to explain imports, types, or external calls used by the target.
5. If you read neighboring files, explicitly label them as context-only and keep the main narrative centered on the selected target.

## Workflow

### 1) Confirm the target

Collect:
- target path
- target type: file or folder
- learner level (default: non-technical)
- preferred output: HTML lesson (default) or Markdown walkthrough

If target does not exist, ask for a corrected path.

### 2) Inspect with focused depth

If target is a file:
- identify responsibilities
- parse control flow
- map inputs, outputs, side effects
- explain key functions, types, and data transforms
- identify edge cases and failure modes

If target is a folder:
- map each important file briefly
- identify internal roles and boundaries
- trace one or two core flows through the folder
- explain folder-level architecture and conventions

### 3) Build explanation for learning, not just summary

Always include:
- What this target is for
- Mental model (simple metaphor)
- Step-by-step execution path
- Key code snippets + plain-English translation
- Vocabulary glossary for technical terms
- Common bugs and how to debug them
- Safe ways to modify/extend the target

### 4) Produce output

#### A) HTML mode (default)

Generate one self-contained `.html` file with:
- clear module sections
- visual hierarchy
- at least one flow diagram (CSS/SVG or simple animated DOM)
- quiz questions that test application
- mobile-friendly layout

Design direction:
- warm neutral background
- high-contrast readable text
- expressive headings (not default system look)
- avoid generic template feel

#### B) Markdown mode

Use this structure exactly:

# Focused Walkthrough: <target>
## 1. What It Does
## 2. Mental Model
## 3. How It Works Step by Step
## 4. Important Snippets Explained
## 5. Terms You Should Know
## 6. Typical Bugs and Debug Strategy
## 7. How to Change It Safely
## 8. Quick Knowledge Check

## Quality Bar

- Depth over breadth
- Keep narrative tied to the chosen target
- Avoid unexplained jargon
- Explain why choices matter in real maintenance work
- Include actionable debugging guidance

## Example Prompts That Should Trigger

- "Prendi solo app/(tabs)/search/index.tsx e spiegamelo in dettaglio come se non fossi tecnico."
- "Fammi una mini-lezione solo sulla cartella services/api."
- "I only want a deep walkthrough of utils/torrentParser.ts, not the full app."

## Example Prompts That Should Not Trigger

- "Turn this whole repo into a full course"
- "Generate a complete architecture class for the entire codebase"
