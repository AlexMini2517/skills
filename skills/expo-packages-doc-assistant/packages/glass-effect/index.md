---
title: GlassEffect
description: React components that render a liquid glass effect using iOS's native UIVisualEffectView.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-glass-effect'
packageName: 'expo-glass-effect'
platforms: ['ios', 'tvos', 'expo-go']
---

# Expo GlassEffect

React components that render a liquid glass effect using iOS's native UIVisualEffectView.
iOS, tvOS, Included in Expo Go

> `GlassView` is only available on iOS 26 and above. It will fallback to regular `View` on unsupported platforms.

React components that render native iOS liquid glass effect using [`UIVisualEffectView`](https://developer.apple.com/documentation/uikit/uivisualeffectview). Supports customizable glass styles and tint color.

#### Known issues

-   Setting `opacity` to `0` on `GlassView` or any of its parent views causes the glass effect to not render at all. To fade in/out the glass effect, use the built-in [`animate` and `animationDuration`](/versions/latest/sdk/glass-effect#animated-glass-effect-style) props in `glassEffectStyle` instead of changing opacity. If you still want to use `opacity`, see the [opacity animation workaround](/versions/latest/sdk/glass-effect#opacity-animation-workaround) example. For more details, see [Apple's documentation](https://developer.apple.com/documentation/uikit/uivisualeffectview#Set-the-correct-alpha-value) and [GitHub issue #41024](https://github.com/expo/expo/issues/41024).

## Installation

```sh
npx expo install expo-glass-effect
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Usage

### `GlassView`

The `GlassView` component renders the native iOS glass effect. It supports different glass effect styles and can be customized with tint colors for various aesthetic needs.

```jsx
import { StyleSheet, View, Image } from 'react-native';
import { GlassView } from 'expo-glass-effect';

export default function App() {
  return (
    <View style={styles.container}>
      <Image
        style={styles.backgroundImage}
        source={{
          uri: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=400&fit=crop',
        }}
      />

      {/* Basic Glass View */}
      <GlassView style={styles.glassView} />

      {/* Glass View with clear style */}
      <GlassView style={styles.tintedGlassView} glassEffectStyle="clear" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  backgroundImage: {
    ...StyleSheet.absoluteFill,
    width: '100%',
    height: '100%',
  },
  glassView: {
    position: 'absolute',
    top: 100,
    left: 50,
    width: 200,
    height: 100,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  tintedGlassView: {
    position: 'absolute',
    top: 250,
    left: 50,
    width: 200,
    height: 100,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  text: {
    fontSize: 16,
    fontWeight: '600',
    color: '#000',
    textAlign: 'center',
  },
});
```

### `GlassContainer`

The `GlassContainer` component allows you to combine multiple glass views into a combined effect.

```jsx
import { StyleSheet, View, Image } from 'react-native';
import { GlassView, GlassContainer } from 'expo-glass-effect';

export default function GlassContainerDemo() {
  return (
    <View style={styles.container}>
      <Image
        style={styles.backgroundImage}
        source={{
          uri: 'https://images.unsplash.com/photo-1547036967-23d11aacaee0?w=400&h=600&fit=crop',
        }}
      />
      <GlassContainer spacing={10} style={styles.containerStyle}>
        <GlassView style={styles.glass1} isInteractive />
        <GlassView style={styles.glass2} />
        <GlassView style={styles.glass3} />
      </GlassContainer>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  backgroundImage: {
    ...StyleSheet.absoluteFillObject,
    width: '100%',
    height: '100%',
  },
  containerStyle: {
    position: 'absolute',
    top: 200,
    left: 50,
    width: 250,
    height: 100,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
  },
  glass1: {
    width: 60,
    height: 60,
    borderRadius: 30,
  },
  glass2: {
    width: 50,
    height: 50,
    borderRadius: 25,
  },
  glass3: {
    width: 40,
    height: 40,
    borderRadius: 20,
  },
});
```

### Animated glass effect style

The `glassEffectStyle` prop accepts a config object with `animate` and `animationDuration` properties to natively animate transitions between glass styles. This is the recommended way to fade in/out the glass effect without modifying `opacity`.

```jsx
import { useState } from 'react';
import { StyleSheet, Text, View, Image, Pressable } from 'react-native';
import { GlassView } from 'expo-glass-effect';

export default function AnimatedGlassStyleExample() {
  const [visible, setVisible] = useState(true);

  return (
    <View style={styles.container}>
      <View style={styles.backgroundImage}>
        <Image
          style={{
            width: 300,
            height: 200,
          }}
          source={{
            uri: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=400&fit=crop',
          }}
        />
        <GlassView
          style={styles.glassView}
          glassEffectStyle={{
            style: visible ? 'clear' : 'none',
            animate: true,
            animationDuration: 0.5,
          }}
        />
      </View>
      <Pressable style={styles.toggleButton} onPress={() => setVisible(prev => !prev)}>
        <Text style={styles.toggleButtonText}>{visible ? 'Hide' : 'Show'} Glass Effect</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    height: 300,
    width: 300,
  },
  backgroundImage: {
    position: 'absolute',
  },
  glassView: {
    position: 'absolute',
    width: 200,
    height: 120,
    borderRadius: 12,
  },
  toggleButton: {
    position: 'absolute',
    bottom: 100,
    alignSelf: 'center',
    backgroundColor: '#007AFF',
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 12,
  },
  toggleButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
});
```

### Opacity animation workaround

Since setting `opacity` to `0` on `GlassView` or its parent views causes the glass effect to not render at all, you can use Reanimated to animate a wrapper view's opacity while toggling the `glassEffectStyle` between the desired style and `'none'`.

```jsx
import { GlassView } from 'expo-glass-effect';
import { StyleSheet, Text, View, Image, Pressable } from 'react-native';
import Animated, {
  useAnimatedProps,
  useAnimatedStyle,
  useSharedValue,
  withTiming,
} from 'react-native-reanimated';

const AnimatedGlassView = Animated.createAnimatedComponent(GlassView);

export default function GlassOpacityAnimationExample() {
  const fadeOpacity = useSharedValue(0);

  const glassViewProps = useAnimatedProps(() => {
    const glassEffectStyle = fadeOpacity.value > 0.01 ? 'regular' : 'none';
    return {
      glassEffectStyle,
      style: {
        width: 150,
        height: 100,
        borderRadius: 12,
        position: 'absolute',
      },
    };
  });

  const fadeOpacityStyle = useAnimatedStyle(() => ({
    position: 'absolute',
    opacity: fadeOpacity.value,
    width: 150,
    height: 100,
    borderRadius: 12,
  }));

  return (
    <>
      <Text style={styles.title}>Opacity Animation Workaround (iOS 26.1+)</Text>
      <View style={styles.backgroundContainer}>
        <Image
          style={styles.backgroundImage}
          source={{
            uri: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=400&fit=crop',
          }}
        />
        <Animated.View style={fadeOpacityStyle}>
          <AnimatedGlassView animatedProps={glassViewProps} />
        </Animated.View>
      </View>

      <Pressable
        style={styles.toggleButton}
        onPress={() => {
          fadeOpacity.value = withTiming(fadeOpacity.value > 0.5 ? 0 : 1, { duration: 500 });
        }}>
        <Text style={styles.toggleButtonText}>Toggle Glass Visibility</Text>
      </Pressable>
    </>
  );
}

const styles = StyleSheet.create({
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  backgroundContainer: {
    height: 300,
    borderRadius: 12,
    overflow: 'hidden',
    position: 'relative',
  },
  backgroundImage: {
    width: '100%',
    height: '100%',
  },
  toggleButton: {
    backgroundColor: '#007AFF',
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 12,
    alignItems: 'center',
  },
  toggleButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
});
```

### `isLiquidGlassAvailable`

The `isLiquidGlassAvailable` function let's you check, if the Liquid Glass effect is available in the compiled application. It validates the system and compiler versions, as well as the [**Info.plist**](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIDesignRequiresCompatibility) settings.

```tsx
import { isLiquidGlassAvailable } from 'expo-glass-effect';

export default function CheckLiquidGlass() {
  return (
    <Text>
      {isLiquidGlassAvailable()
        ? 'Liquid Glass effect is available'
        : 'Liquid Glass effect is not available'}
    </Text>
  );
}
```

### `isGlassEffectAPIAvailable`

The `isGlassEffectAPIAvailable` function checks whether the Liquid Glass API is available at runtime on the device.

> This API was added because some iOS 26 beta versions do not have the Liquid Glass API available, which can lead to crashes. You should check this before using `GlassView` in your app to ensure compatibility. See [GitHub issue #40911](https://github.com/expo/expo/issues/40911) for more information.

```tsx
import { isGlassEffectAPIAvailable } from 'expo-glass-effect';

export default function CheckGlassEffectAPI() {
  return (
    <Text>
      {isGlassEffectAPIAvailable()
        ? 'Glass Effect API is available'
        : 'Glass Effect API is not available'}
    </Text>
  );
}
```

## API

```js
import {
  GlassView,
  GlassContainer,
  isLiquidGlassAvailable,
  isGlassEffectAPIAvailable,
} from 'expo-glass-effect';
```

## Components

### `GlassContainer`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[GlassContainerProps](#glasscontainerprops)\>

GlassContainerProps

### `ref`

Supported platforms: iOS, tvOS.

Optional • Type: Ref<[View](https://reactnative.dev/docs/view)\>

### `spacing`

Supported platforms: iOS, tvOS.

Optional • Type: `number` • Default: `undefined`

The distance at which glass elements start affecting each other. Controls when glass elements begin to merge together.

#### Inherited Props

-   [ViewProps](https://reactnative.dev/docs/view#props)

### `GlassView`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[GlassViewProps](#glassviewprops)\>

GlassViewProps

### `colorScheme`

Supported platforms: iOS, tvOS.

Optional • Type: [GlassColorScheme](#glasscolorscheme) • Default: `'auto'`

The color scheme for the glass effect appearance. Use this to override the system appearance when your app has its own theme toggle.

### `glassEffectStyle`

Supported platforms: iOS, tvOS.

Optional • Literal type: `union` • Default: `'regular'`

Glass effect style to apply to the view. Can be a simple string ('clear', 'regular', 'none') or a config object for controlling animation behavior.

Acceptable values are: [GlassStyle](#glassstyle) | [GlassEffectStyleConfig](#glasseffectstyleconfig)

### `isInteractive`

Supported platforms: iOS, tvOS.

Optional • Type: `boolean` • Default: `false`

Whether the glass effect should be interactive.

### `ref`

Supported platforms: iOS, tvOS.

Optional • Type: Ref<[View](https://reactnative.dev/docs/view)\>

### `tintColor`

Supported platforms: iOS, tvOS.

Optional • Type: `string`

Tint color to apply to the glass effect.

#### Inherited Props

-   [ViewProps](https://reactnative.dev/docs/view#props)

## Methods

### `isGlassEffectAPIAvailable()`

Supported platforms: iOS.

Checks whether the Liquid Glass API is available at runtime on the device.

This method was added because some iOS 26 beta versions do not have this API available, which can lead to crashes. You should check this before using `GlassView` and `GlassContainer` in your app to ensure compatibility.

Returns: `boolean`

> **See:** [https://github.com/expo/expo/issues/40911](https://github.com/expo/expo/issues/40911)

### `isLiquidGlassAvailable()`

Supported platforms: iOS, tvOS.

Indicates whether the app is using the Liquid Glass design. The value will be `true` when the Liquid Glass components are available in the app.

This only checks for component availability. The value may also be `true` if the user has enabled accessibility settings that limit the Liquid Glass effect. To check if the user has disabled the Liquid Glass effect via accessibility settings, use [`AccessibilityInfo.isReduceTransparencyEnabled()`](https://reactnative.dev/docs/accessibilityinfo#isreducetransparencyenabled-ios).

Returns: `boolean`

## Types

### `GlassColorScheme`

Supported platforms: iOS, tvOS.

Literal Type: `string`

Acceptable values are: `'auto'` | `'light'` | `'dark'`

### `GlassEffectStyleConfig`

Supported platforms: iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| animate(optional) | `boolean` | Whether to animate the style change. Default: `false` |
| animationDuration(optional) | `number` | Duration of the animation in seconds. Uses system default if not specified. |
| style | [GlassStyle](#glassstyle) | The glass effect style to apply. |

### `GlassStyle`

Supported platforms: iOS, tvOS.

Literal Type: `string`

Acceptable values are: `'clear'` | `'regular'` | `'none'`
