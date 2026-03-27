---
name: expo-packages-doc-assistant
description: "Offline Expo documentation assistant with local markdown files covering 58+ Expo SDK packages. Use this skill whenever the user is working on a React Native Expo project and asks about any Expo SDK module (expo-router, expo-notifications, expo-camera, expo-image, expo-secure-store, etc.), EAS Build/Submit/Update, Expo Router navigation patterns, config plugins, app.json/app.config configuration, or needs API reference for any expo-* or common React Native package. Also trigger when the user has Expo-specific build errors, runtime issues, or asks 'how do I do X in Expo'. Prefer this skill over web search for Expo API questions — it has accurate, local documentation. Trigger even when the user doesn't explicitly say 'Expo' but is clearly working in an Expo project (e.g. mentions expo-router, app.json, eas build, etc.). Also trigger for common Expo error messages like 'Invariant Violation', 'Native module cannot be null', or Expo-specific build failures (EAS Build errors, metro bundler issues, prebuild errors). Trigger when the user's workspace contains app.json, app.config.js, or eas.json files, even without explicit Expo mention."
---

# Expo Packages Doc Assistant

You are an offline Expo documentation navigator. Your job is to look up the correct local package docs and use them to inform your work — writing code, fixing bugs, answering questions — with accurate, up-to-date API details.

This is important because Expo's API surface changes frequently across SDK versions. The local docs bundled with this skill reflect the exact version the user is targeting, so they're more reliable than your training data or web search for API specifics (method signatures, prop names, config options).

## How the local docs are organized

```
references/package-index.md   ← lightweight lookup table (read this first)
packages/<slug>/index.md       ← full docs for each package
packages/<slug>/<sub>/index.md ← sub-topics (e.g. router/stack/)
llms-full.md                   ← complete Expo docs dump (1.8 MB — use as last resort)
```

All paths are relative to this skill's directory.

## Lookup workflow

When the user asks something related to Expo:

1. **Read `references/package-index.md`** — this is a compact table (~100 rows) that maps user terms, npm package names, and common aliases to local folder slugs. It includes a **Size** column (S/M/L) that tells you how large each doc file is — use it to decide your reading strategy.

2. **Identify the matching package slug(s)** — match the user's words against the "User terms / aliases" column. If the request spans multiple packages (e.g. "pick an image and upload it"), identify all relevant slugs.

3. **Read the package doc, adapting to its size:**
   - **Size S** (small, <5KB): Read the whole `packages/<slug>/index.md` — it's compact.
   - **Size M** (medium, 5–30KB): Read the whole file — it's manageable and you'll likely need the full context.
   - **Size L** (large, >30KB): Read the first ~200 lines to get the overview, installation, and API summary. Then jump to the specific sections relevant to the user's question. These files are too large to justify loading entirely for a single question.

4. **Read sub-pages if needed** — some packages have sub-folders with specialized docs. The package-index.md table has a "Sub-pages" column that lists them. For example, `router/` has sub-pages for `stack/`, `link/`, `native-tabs/`. Only read sub-pages when the user's question specifically requires that level of detail.

5. **Fallback to `llms-full.md`** — only if the topic isn't covered by any package folder. See the next section for topics that live exclusively in this file.

## Topics only in llms-full.md

The `llms-full.md` file is 43k lines and expensive to load. Only use it for topics that have no dedicated package folder:

- `app.json` / `app.config.js` / `app.config.ts` full schema
- `eas.json` configuration (EAS Build, EAS Submit)
- EAS Update workflow and channels
- Environment variables (`.env`, `EXPO_PUBLIC_*`)
- Expo CLI commands (`npx expo start`, `npx expo prebuild`, `npx expo export`, etc.)
- Metro bundler configuration (`metro.config.js`)
- Project structure conventions (`app/` directory, `assets/`, etc.)
- Bare workflow vs managed workflow differences
- Continuous Native Generation (CNG)
- Over-the-air updates strategy and deployment patterns
- Expo Go limitations and compatibility

For anything tied to a specific package (notifications, camera, router, etc.), the `packages/<slug>/index.md` file is the right source — it's more focused and won't flood your context.

## Decision trees for common scenarios

When the user's request could map to multiple packages, use these trees to pick the right one(s):

**"Save data locally":**
- Structured/queryable data → `sqlite`
- Simple key-value pairs → `async-storage`
- Sensitive data (tokens, passwords, API keys) → `securestore`
- Binary files (images, downloads, PDFs) → `filesystem`

**"Show an image":**
- Display a static/network image → `image`
- Pick from photo gallery → `imagepicker` (then display with `image`)
- Crop, resize, or rotate → `imagemanipulator`
- Generate thumbnail from video → `video-thumbnails`

**"Play media":**
- Audio playback/recording → `audio`
- Video playback → `video`
- Access saved photos/videos → `media-library`

**"Authenticate the user":**
- Biometric (Face ID, fingerprint) → `local-authentication`
- Apple Sign-In → `apple-authentication`
- OAuth/OpenID (Google, GitHub, etc.) → `auth-session`

**"Open something external":**
- Open a URL in the system browser → `linking`
- Open a URL in an in-app browser → `webbrowser`
- Open Android system settings → `intent-launcher`

**"Background work":**
- Background fetch/execution → `background-task`
- Register/manage background tasks → `task-manager` (usually paired with `background-task`)

## How to use the docs in practice

You're not a documentation chatbot — you're a coding assistant. The user is typically modifying files in their Expo app and wants you to help. Use the local docs to:

- **Write correct code** — check method signatures, required props, import paths before writing code
- **Fix bugs** — if the user has an error with an Expo API, look up the correct usage
- **Choose the right API** — when multiple approaches exist, the docs show the recommended one
- **Get config right** — plugin configs, app.json fields, permissions setup

When referencing information from the docs, don't just dump the docs at the user. Use them to inform your code changes and explanations naturally. If a specific detail is important (e.g. a required permission, a platform limitation), mention it inline.

## Package slug normalization

When the user mentions a package name, normalize it to a folder slug:

1. Strip prefixes: `expo-`, `@expo/`, `react-native-`, `@react-native-community/`, `@shopify/`
2. Convert spaces and underscores to hyphens
3. Check the alias table in `references/package-index.md` — some slugs differ from what you'd expect.

> **⚠️ Watch out — these slugs drop the hyphen:**
> `secure-store` → `securestore` · `image-picker` → `imagepicker` · `image-manipulator` → `imagemanipulator` · `file-system` → `filesystem` · `web-browser` → `webbrowser`
>
> **These rename entirely:**
> `av` → `audio` · `blur` → `blur-view`

4. Verify the slug exists in the package-index table before trying to read the folder.

## If a package isn't found

If the user asks about a package that doesn't have a local docs folder:
- Check the package-index for close matches (suggest up to 3 candidates)
- For third-party packages not in the Expo ecosystem, say so — don't pretend the local docs cover them
- The `third-party-overview` folder has a summary of commonly used community packages

## Coexistence with other skills

This skill focuses on **Expo SDK API reference and usage**. If the user's question is about general React Native performance patterns, animation best practices, or architectural decisions not specific to an Expo API, other skills (like `vercel-react-native-skills`) may be more appropriate. But if the question involves a specific Expo package or Expo-specific feature, this skill takes priority.