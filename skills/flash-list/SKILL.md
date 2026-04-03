---
name: flash-list
description: Use this skill whenever the user wants to implement, modify, fix, or optimize a FlashList from @shopify/flash-list in a React Native or Expo app. This skill forces you to read the local documentation before proceeding to ensure high performance and correct usage.
---

This skill acts as your expert guide for using `@shopify/flash-list`. Due to the nuanced way FlashList handles recycling and performance, you MUST deeply understand how it works before you write or modify any list code.

## Instructions
Whenever you are asked to work with a FlashList, you must FIRST read the local documentation provided in the `docs` directory. Use the relative paths provided below to read the files before implementing the code.

### 1. Mandatory Reading
Before writing or modifying any code involving FlashList, you MUST read the following documentation files to understand its performance characteristics and view recycling mechanism:
- `docs/usage.md`: Core API, props, and general usage instructions.
- `docs/recycling.md`: How FlashList recycles views and what you need to do to support it correctly.
- `docs/performant-components.md`: Best practices for writing performant list items and properly memoizing them.
- `docs/layout-commit-observer.md`: Advanced usage and how to observe layout commits.

### 2. Implementation Rules
Once you have read the relevant documentation files:
- Be very careful to understand view recycling and prevent bug states inside list items.
- Ensure that the item component is correctly memoized when necessary.
- Double-check your code against the principles outlined in the documentation.