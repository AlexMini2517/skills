---
title: react-native-safe-area-context
description: A library with a flexible API for accessing the device's safe area inset information.
sourceCodeUrl: 'https://github.com/AppAndFlow/react-native-safe-area-context'
packageName: react-native-safe-area-context
platforms: ['android', 'ios', 'web', 'tvos', 'expo-go']
inExpoGo: true
---

# react-native-safe-area-context

A library with a flexible API for accessing the device's safe area inset information.
Android, iOS, tvOS, Web, Included in Expo Go

`react-native-safe-area-context` provides a flexible API for accessing device safe area inset information. This allows you to position your content appropriately around notches, status bars, home indicators, and other such device and operating system interface elements. It also provides a `SafeAreaView` component that you can use in place of `View` to automatically inset your views to account for safe areas.

## Installation

```sh
npx expo install react-native-safe-area-context
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project. Then, follow the [installation instructions](https://appandflow.github.io/react-native-safe-area-context/) provided in the library's README or documentation.

## API

```js
import {
  SafeAreaView,
  SafeAreaProvider,
  SafeAreaInsetsContext,
  useSafeAreaInsets,
} from 'react-native-safe-area-context';
```

## Components

### `SafeAreaView`

`SafeAreaView` is a regular `View` component with the safe area edges applied as padding.

If you set your own padding on the view, it will be added to the padding from the safe area.

> If you are targeting web, you must set up `SafeAreaProvider` as described in the [Context](/versions/latest/sdk/safe-area-context#context) section.

```jsx
import { SafeAreaView } from 'react-native-safe-area-context';

function SomeComponent() {
  return (
    <SafeAreaView>
      <View />
    </SafeAreaView>
  );
}
```

SafeAreaView Props

### `edges`

Optional • Type: [`Edge[]`](#edge) • Default: `["top", "right", "bottom", "left"]`

  

Sets the edges to apply the safe area insets to.

### `emulateUnlessSupported`

Optional • Type: `boolean` • Default: `true`

  

On iOS 10+, emulate the safe area using the status bar height and home indicator sizes.

## Hooks

### `useSafeAreaInsets()`

Hook gives you direct access to the safe area insets. This is a more advanced use-case, and might perform worse than `SafeAreaView` when rotating the device.

Example

```jsx
import { useSafeAreaInsets } from 'react-native-safe-area-context';

function HookComponent() {
  const insets = useSafeAreaInsets();

  return <View style={{ paddingTop: insets.top }} />;
}
```

Returns

[`EdgeInsets`](/versions/latest/sdk/safe-area-context#edgeinsets)

## Types

### `Edge`

String union of possible edges.

Acceptable values are: `'top'`, `'right'`, `'bottom'`, `'left'`.

### `EdgeInsets`

Represent the hook result.

EdgeInsets Properties

| Name | Type | Description |
| --- | --- | --- |
| `bottom` | `number` | Value of bottom inset. |
| `left` | `number` | Value of left inset. |
| `right` | `number` | Value of right inset. |
| `top` | `number` | Value of top inset. |

## Guides

### Context

To use safe area context, you need to add `SafeAreaProvider` in your app root component.

> You may need to add it in other places too, including at the root of any modals any routes when using `react-native-screen`.

```jsx
import { SafeAreaProvider } from 'react-native-safe-area-context';

function App() {
  return <SafeAreaProvider>...</SafeAreaProvider>;
}
```

Then, you can use [`useSafeAreaInsets()`](/versions/latest/sdk/safe-area-context#usesafeareainsets) hook and also consumer API to access inset data:

```jsx
import { SafeAreaInsetsContext } from 'react-native-safe-area-context';

function Component() {
  return (
    <SafeAreaInsetsContext.Consumer>
      {insets => <View style={{ paddingTop: insets.top }} />}
    </SafeAreaInsetsContext.Consumer>
  );
}
```

### Optimization

If you can, use `SafeAreaView`. It's implemented natively so when rotating the device, there is no delay from the asynchronous bridge.

To speed up the initial render, you can import `initialWindowMetrics` from this package and set as the `initialMetrics` prop on the provider as described in Web SSR. You cannot do this if your provider remounts, or you are using `react-native-navigation`.

```jsx
import { SafeAreaProvider, initialWindowMetrics } from 'react-native-safe-area-context';

function App() {
  return <SafeAreaProvider initialMetrics={initialWindowMetrics}>...</SafeAreaProvider>;
}
```

### Web SSR

If you are doing server side rendering on the web, you can use `initialSafeAreaInsets` to inject values based on the device the user has, or simply pass zero. Otherwise, insets measurement will break rendering your page content since it is async.

### Migrating from CSS

#### Before

In a web-only app, you would use CSS environment variables to get the size of the screen's safe area insets.

```css
div {
  padding-top: env(safe-area-inset-top);
  padding-left: env(safe-area-inset-left);
  padding-bottom: env(safe-area-inset-bottom);
  padding-right: env(safe-area-inset-right);
}
```

#### After

Universally, the hook `useSafeAreaInsets()` can provide access to this information.

```jsx
import { useSafeAreaInsets } from 'react-native-safe-area-context';

function App() {
  const insets = useSafeAreaInsets();
  return (
    <View
      style={{
        paddingTop: insets.top,
        paddingLeft: insets.left,
        paddingBottom: insets.bottom,
        paddingRight: insets.right,
      }}
    />
  );
}
```
