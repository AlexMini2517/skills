---
name: expo-packages-doc-assistant
description: "Offline API reference for Expo and React Native. Trigger when working in an Expo project (workspace contains app.json or eas.json), when the user asks about Expo SDK packages (e.g., expo-router, expo-camera), EAS workflows, config plugins, or encounters Expo/React Native build and runtime errors. Always prefer this over web search."
---

## How the local docs are organized

```
packages/<slug>.mdx                           ← full docs for most packages
packages/<slug>/index.mdx                     ← root docs for complex packages (e.g. router/)
packages/<slug>/<sub-topic>.mdx               ← sub-topics (e.g. router/stack.mdx)
packages/<slug>/<sub-topic>/<component>.mdx   ← deeply nested topics (e.g. ui/jetpack-compose/button.mdx)
```

All paths are relative to this skill's directory.

## Lookup workflow

When the user asks something related to Expo:

1. **Identify the matching package slug(s)** — match the user's words to the corresponding package in the `packages/` directory. If the request spans multiple packages (e.g. "pick an image and upload it"), identify all relevant slugs.
2. **Read the package doc:** Start by checking `packages/<slug>.mdx` (or `packages/<slug>/index.mdx`). Note that some files are quite large, so if a file is large, read the first ~200 lines to get the overview and API summary, then jump to the specific sections relevant to the user's question.
3. **Read sub-pages if needed** — some complex packages like `router/` or `ui/` have sub-folders with specialized docs (including deeply nested ones like `ui/jetpack-compose/`). Only read sub-pages when the user's question specifically requires that level of detail.
4. **General topics** — For topics like `app.json`, `eas.json`, Metro bundler configuration, etc., either search for a related `.mdx` file in the `packages/` directory, use `grep_search`, or rely on your general knowledge.

For anything tied to a specific package (notifications, camera, router, etc.), the `packages/` files are the primary source.

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

When the user mentions a package name, normalize it to find the file:

1. Strip prefixes: `expo-`, `@expo/`, `react-native-`, `@react-native-community/`, `@shopify/`
2. Convert spaces and underscores to hyphens

> **⚠️ Watch out — these slugs drop the hyphen:**
> `secure-store` → `securestore` · `image-picker` → `imagepicker` · `image-manipulator` → `imagemanipulator` · `file-system` → `filesystem` · `web-browser` → `webbrowser`
>
> **These rename entirely:**
> `av` → `audio` · `blur` → `blur-view`

3. Verify the slug exists in the `packages/` directory before trying to read the file.

## If a package isn't found

If the user asks about a package that doesn't have a local docs file:
- Check the `packages/` directory for any close matches (e.g., related terms).
- For third-party packages not in the Expo ecosystem, say so — don't pretend the local docs cover them.
- `packages/third-party-overview.mdx` has a summary of commonly used community packages.

## Coexistence with other skills

This skill focuses on **Expo SDK API reference and usage**. If the user's question is about general React Native performance patterns, animation best practices, or architectural decisions not specific to an Expo API, other skills (like `vercel-react-native-skills`) may be more appropriate. But if the question involves a specific Expo package or Expo-specific feature, this skill takes priority.