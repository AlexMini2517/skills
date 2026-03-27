---
id: statusbar
title: StatusBar
description: A library that provides the same interface as the React Native StatusBar API, but with slightly different defaults to work great in Expo environments.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-status-bar'
packageName: 'expo-status-bar'
iconUrl: '/static/images/packages/expo-status-bar.png'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
---

# Expo StatusBar

A library that provides the same interface as the React Native StatusBar API, but with slightly different defaults to work great in Expo environments.
Android, iOS, tvOS, Web, Included in Expo Go

`expo-status-bar` gives you a component and imperative interface to control the app status bar to change its text color, background color, hide it, make it translucent or opaque, and apply animations to any of these changes. Exactly what you are able to do with the `StatusBar` component depends on the platform you're using.

> **tvOS and web support**
> 
> For **tvOS**, the `expo-status-bar` code will compile and run, but no status bar will show.
> 
> For **web**, there is no API available to control the operating system's status bar, so `expo-status-bar` will do nothing and won't throw an error.

## Installation

```sh
npx expo install expo-status-bar
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Usage

```jsx
import { StyleSheet, Text, View } from 'react-native';
import { StatusBar } from 'expo-status-bar';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Notice that the status bar has light text!</Text>
      <StatusBar style="light" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    color: '#fff',
  },
});
```

## API

```js
import { StatusBar } from 'expo-status-bar';
```

## Component

### `StatusBar`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StatusBarProps](#statusbarprops)\>

A component that allows you to configure your status bar without directly calling imperative methods like `setBarStyle`.

You will likely have multiple `StatusBar` components mounted in the same app at the same time. For example, if you have multiple screens in your app, you may end up using one per screen. The props of each `StatusBar` component will be merged in the order that they were mounted. This component is built on top of the [StatusBar](https://reactnative.dev/docs/statusbar) component exported from React Native, and it provides defaults that work better for Expo users.

StatusBarProps

### `animated`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If the transition between status bar property changes should be animated. Supported for `backgroundColor`, `barStyle` and `hidden`.

> **Deprecated:** Due to Android edge-to-edge enforcement, setting the status bar background color is deprecated and has no effect. This will be removed in a future release.

### `backgroundColor`

Supported platforms: Android.

Optional • Type: `string`

The background color of the status bar.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If the status bar is hidden.

### `hideTransitionAnimation`

Supported platforms: iOS.

Optional • Type: [StatusBarAnimation](#statusbaranimation) • Default: `'fade'`

The transition effect when showing and hiding the status bar using the hidden prop.

> **Deprecated:** The status bar network activity indicator is not supported in iOS 13 and later. This will be removed in a future release.

### `networkActivityIndicatorVisible`

Supported platforms: iOS.

Optional • Type: `boolean`

If the network activity indicator should be visible.

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [StatusBarStyle](#statusbarstyle) • Default: `'auto'`

Sets the color of the status bar text. Default value is `"auto"` which picks the appropriate value according to the active color scheme, eg: if your app is dark mode, the style will be `"light"`.

> **Deprecated:** Due to Android edge-to-edge enforcement, setting the status bar as translucent is deprecated and has no effect. This will be removed in a future release.

### `translucent`

Supported platforms: Android.

Optional • Type: `boolean`

If the status bar is translucent. When translucent is set to `true`, the app will draw under the status bar. This is the default behaviour in projects created with Expo tools because it is consistent with iOS.

## Methods

> **Deprecated:** Due to Android edge-to-edge enforcement, setting the status bar background color is deprecated and has no effect. This will be removed in a future release.

### `StatusBar.setStatusBarBackgroundColor(backgroundColor, animated)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `backgroundColor` | [ColorValue](https://reactnative.dev/docs/colors) | The background color of the status bar. |
| `animated`(optional) | `boolean` | `true` to animate the background color change, `false` to change immediately. |

  

Set the background color of the status bar.

Returns: `void`

### `StatusBar.setStatusBarHidden(hidden, animation)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `hidden` | `boolean` | If the status bar should be hidden. |
| `animation`(optional) | [StatusBarAnimation](#statusbaranimation) | Animation to use when toggling hidden, defaults to `'none'`. |

  

Toggle visibility of the status bar.

Returns: `void`

> **Deprecated:** The status bar network activity indicator is not supported in iOS 13 and later. This will be removed in a future release.

### `StatusBar.setStatusBarNetworkActivityIndicatorVisible(visible)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `visible` | `boolean` | If the network activity indicator should be visible. |

  

Toggle visibility of the network activity indicator.

Returns: `void`

### `StatusBar.setStatusBarStyle(style, animated)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `style` | [StatusBarStyle](#statusbarstyle) | The color of the status bar text. |
| `animated`(optional) | `boolean` | If the transition should be animated. |

  

Set the bar style of the status bar.

Returns: `void`

> **Deprecated:** Due to Android edge-to-edge enforcement, setting the status bar as translucent is deprecated and has no effect. This will be removed in a future release.

### `StatusBar.setStatusBarTranslucent(translucent)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `translucent` | `boolean` | Whether the app can draw under the status bar. When `true`, content will be rendered under the status bar. This is always `true` on iOS and cannot be changed. |

  

Set the translucency of the status bar.

Returns: `void`

## Types

### `StatusBarAnimation`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `string`

Acceptable values are: `'none'` | `'fade'` | `'slide'`

### `StatusBarStyle`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `string`

Acceptable values are: `'auto'` | `'inverted'` | `'light'` | `'dark'`
