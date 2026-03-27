---
title: SwiftUI
description: SwiftUI components for building native iOS interfaces with @expo/ui.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos']
isBeta: true
---

# SwiftUI

SwiftUI components for building native iOS interfaces with @expo/ui.
iOS, tvOS

> **This library is currently in beta and subject to breaking changes.** It is not available in the Expo Go app — use [development builds](/develop/development-builds/introduction) to try it out.

The SwiftUI components in `@expo/ui/swift-ui` allow you to build fully native iOS interfaces using SwiftUI from React Native.

## Installation

```sh
npx expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Usage

Using a component from `@expo/ui/swift-ui` requires wrapping it in a [`Host`](/versions/latest/sdk/ui/swift-ui/host) component. The `Host` is a container for SwiftUI views.

```tsx
import { Host, Button } from '@expo/ui/swift-ui';

export function SaveButton() {
  return (
    <Host style={{ flex: 1 }}>
      <Button label="Save changes" />
    </Host>
  );
}
```

For more information, see the following resources:

[Expo UI guide for Swift UI](/guides/expo-ui-swift-ui) — Learn about the basics of @expo/ui/swift-ui — @expo/ui/swift-ui

[Extending with SwiftUI](/guides/expo-ui-swift-ui/extending) — Create custom SwiftUI components and modifiers that integrate with Expo UI.

[Expo UI iOS Liquid Glass Tutorial](https://www.youtube.com/watch?v=2wXYLWz3YEQ) — Learn how to build real SwiftUI views in your React Native app with the new Expo UI.
