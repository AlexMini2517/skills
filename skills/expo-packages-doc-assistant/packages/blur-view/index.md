---
title: BlurView
description: A React component that blurs everything underneath the view.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-blur'
packageName: 'expo-blur'
iconUrl: '/static/images/packages/expo-blur.png'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
---

# Expo BlurView

A React component that blurs everything underneath the view.
Android, iOS, tvOS, Web, Included in Expo Go

A React component that blurs everything underneath the view. Common usage of this is for navigation bars, tab bars, and modals.

> In SDK 55 and later, `expo-blur` is stable on Android, but some code changes are required for the `BlurView` to work. See the [Android support](/versions/latest/sdk/blur-view#android-support) section to learn more.

#### Known issues

The blur effect does not update when `BlurView` is rendered before dynamic content is rendered using, for example, `FlatList`. To fix this, make sure that `BlurView` is rendered after the dynamic content component. For example:

```jsx
<View>
  <FlatList />
  <BlurView />
</View>
```

## Installation

```sh
npx expo install expo-blur
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Usage

Basic iOS and web-only `BlurView` usage

This is the legacy way of creating a `BlurView`, which will result in a blur only on iOS. On Android, this will result in a view with a semi-transparent background.

```jsx
import { Text, StyleSheet, View } from 'react-native';
import { BlurView } from 'expo-blur';

export default function App() {
  const text = 'Hello, my container is blurring contents underneath!';
  return (
    <View style={styles.container}>
      <View style={styles.background}>
        {[...Array(20).keys()].map(i => (
          <View
            key={`box-${i}`}
            style={[styles.box, i % 2 === 1 ? styles.boxOdd : styles.boxEven]}
          />
        ))}
      </View>
      <BlurView intensity={100} style={styles.blurContainer}>
        <Text style={styles.text}>{text}</Text>
      </BlurView>
      <BlurView intensity={80} tint="light" style={styles.blurContainer}>
        <Text style={styles.text}>{text}</Text>
      </BlurView>
      <BlurView intensity={90} tint="dark" style={styles.blurContainer}>
        <Text style={[styles.text, { color: '#fff' }]}>{text}</Text>
      </BlurView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  blurContainer: {
    flex: 1,
    padding: 20,
    margin: 16,
    textAlign: 'center',
    justifyContent: 'center',
    overflow: 'hidden',
    borderRadius: 20,
  },
  background: {
    flex: 1,
    flexWrap: 'wrap',
    ...StyleSheet.absoluteFill,
  },
  box: {
    width: '25%',
    height: '20%',
  },
  boxEven: {
    backgroundColor: 'orangered',
  },
  boxOdd: {
    backgroundColor: 'gold',
  },
  text: {
    fontSize: 24,
    fontWeight: '600',
  },
});
```
Basic `BlurView` usage with Android support

To blur the background of a view on Android, wrap the content to be blurred in a `BlurTargetView` component and pass its ref to the `BlurView`.

> **Note:** Notice that, as long as all of the `BlurViews` fit into the bounds of a single `BlurTargetView`, you can use the single `BlurTargetView` for multiple `BlurViews`. This is more efficient than creating multiple `BlurTargetViews`.

```tsx
import { BlurView, BlurTargetView } from 'expo-blur';
import { useRef } from 'react';
import { Text, StyleSheet, View } from 'react-native';

export default function App() {
  const targetRef = useRef<View | null>(null);
  const text = 'Hello, my container is blurring contents underneath!';

  return (
    <View style={styles.container}>
      <BlurTargetView ref={targetRef} style={styles.background}>
        {[...Array(20).keys()].map(i => (
          <View
            key={`box-${i}`}
            style={[styles.box, i % 2 === 1 ? styles.boxOdd : styles.boxEven]}
          />
        ))}
      </BlurTargetView>
      <BlurView
        blurTarget={targetRef}
        intensity={100}
        style={styles.blurContainer}
        blurMethod="dimezisBlurView">
        <Text style={styles.text}>{text}</Text>
      </BlurView>
      <BlurView
        blurTarget={targetRef}
        intensity={80}
        tint="light"
        style={styles.blurContainer}
        blurMethod="dimezisBlurView">
        <Text style={styles.text}>{text}</Text>
      </BlurView>
      <BlurView
        blurTarget={targetRef}
        intensity={90}
        tint="dark"
        style={styles.blurContainer}
        blurMethod="dimezisBlurView">
        <Text style={[styles.text, { color: '#fff' }]}>{text}</Text>
      </BlurView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  blurContainer: {
    flex: 1,
    padding: 20,
    margin: 16,
    textAlign: 'center',
    justifyContent: 'center',
    overflow: 'hidden',
    borderRadius: 20,
  },
  background: {
    flex: 1,
    flexWrap: 'wrap',
    ...StyleSheet.absoluteFill,
  },
  box: {
    width: '25%',
    height: '20%',
  },
  boxEven: {
    backgroundColor: 'orangered',
  },
  boxOdd: {
    backgroundColor: 'gold',
  },
  text: {
    fontSize: 24,
    fontWeight: '600',
  },
});
```

## Android support

The blurring feature is stable on Android. There are a few things to keep in mind when migrating:

### API

To blur the background of a view on Android, wrap the content to be blurred in a `BlurTargetView` component and pass its ref to the `BlurView`. You can see an example in the [Usage](/versions/latest/sdk/blur-view#basic-blurview-usage-with-android-support) section.

### Performance

The blur can be achieved efficiently only by using the [RenderNode](https://developer.android.com/reference/android/graphics/RenderNode) Android API, which was introduced in Android SDK 31 (Android 9.0). Due to this, on older versions of Android `expo-blur` uses the much less efficient [RenderScript](https://developer.android.com/guide/topics/renderscript/compute) API. If you want to avoid the performance penalty on older platforms you can use the `dimezisBlurViewSdk31Plus` [BlurMethod](/versions/latest/sdk/blur-view#blurmethod-1) which will only blur on newer versions of Android and fall back to the [`none`](/versions/latest/sdk/blur-view#blurmethod-1) on older versions.

## API

```js
import { BlurView } from 'expo-blur';
```

## Components

### `BlurView`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Component](https://react.dev/reference/react/Component)<[BlurViewProps](#blurviewprops), BlurViewState\>

BlurViewProps

### `blurMethod`

Supported platforms: Android.

Optional • Type: [BlurMethod](#blurmethod) • Default: `'none'`

Blur method to use on Android.

### `blurReductionFactor`

Supported platforms: Android.

Optional • Type: `number` • Default: `4`

A number by which the blur intensity will be divided on Android.

When using experimental blur methods on Android, the perceived blur intensity might differ from iOS at different intensity levels. This property can be used to fine tune it on Android to match it more closely with iOS.

### `blurTarget`

Supported platforms: Android.

Optional • Type: [RefObject](https://react.dev/reference/react/useRef)<[View](https://reactnative.dev/docs/view) | null\>

A ref to a BlurTargetView, which this BlurView will blur as its background.

### `intensity`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `number` • Default: `50`

A number from `1` to `100` to control the intensity of the blur effect.

You can animate this property using `react-native-reanimated`.

### `tint`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [BlurTint](#blurtint) • Default: `'default'`

A tint mode which will be applied to the view.

#### Inherited Props

-   [ViewProps](https://reactnative.dev/docs/view#props)

### `BlurTargetView`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BlurTargetViewProps](#blurtargetviewprops)\>

BlurTargetViewProps

### `ref`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [RefObject](https://react.dev/reference/react/useRef)<[View](https://reactnative.dev/docs/view) | null\>

#### Inherited Props

-   [ViewProps](https://reactnative.dev/docs/view#props)

## Types

### `BlurMethod`

Supported platforms: Android.

Literal Type: `string`

Blur method to use on Android.

-   `'none'` - Renders a semi-transparent view instead of rendering a blur effect.
    
-   `'dimezisBlurView'` - Uses a native blur view implementation based on [BlurView](https://github.com/Dimezis/BlurView) library. This method may lead to decreased performance on Android SDK 30 and below.
    
-   `'dimezisBlurViewSdk31Plus'` - Uses a native blur view implementation based on [BlurView](https://github.com/Dimezis/BlurView) library on Android SDK 31 and above, for older versions of Android falls back to 'none'. This is due to performance limitations on older versions of Android, see the [performance](#performance) section to learn more.
    

Acceptable values are: `'none'` | `'dimezisBlurView'` | `'dimezisBlurViewSdk31Plus'`

### `BlurTint`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `string`

Acceptable values are: `'light'` | `'dark'` | `'default'` | `'extraLight'` | `'regular'` | `'prominent'` | `'systemUltraThinMaterial'` | `'systemThinMaterial'` | `'systemMaterial'` | `'systemThickMaterial'` | `'systemChromeMaterial'` | `'systemUltraThinMaterialLight'` | `'systemThinMaterialLight'` | `'systemMaterialLight'` | `'systemThickMaterialLight'` | `'systemChromeMaterialLight'` | `'systemUltraThinMaterialDark'` | `'systemThinMaterialDark'` | `'systemMaterialDark'` | `'systemThickMaterialDark'` | `'systemChromeMaterialDark'`

## Using `borderRadius` with `BlurView`

When using `BlurView` on Android and iOS, the `borderRadius` property is not applied when provided explicitly. To fix this, you can use the `overflow: 'hidden'` style since `BlurView` inherits props from `<View>`. See [Usage](/versions/latest/sdk/blur-view#usage) for an example.
