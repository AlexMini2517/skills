---
title: Router Native tabs
description: An Expo Router submodule that provides native tabs layout.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-router'
packageName: 'expo-router'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
isBeta: true
---

# Expo Router Native tabs

An Expo Router submodule that provides native tabs layout.
Android, iOS, tvOS, Web, Included in Expo Go

> Native tabs is a beta feature available in SDK 55 and later, and its API is subject to change.

`expo-router/unstable-native-tabs` is a submodule of `expo-router` and exports components to build tab layouts using platform-native system tabs.

> See the [Expo Router](/versions/latest/sdk/router/index) reference for more information about the file-based routing library for native and web app.

## Installation

To use `expo-router/unstable-native-tabs` in your project, you need to install `expo-router` in your project. Follow the instructions from Expo Router's installation guide:

[Install Expo Router](/router/installation) — Learn how to install Expo Router in your project.

## Configuration in app config

If you are using the [default](/more/create-expo#--template) template to create a new project, `expo-router`'s [config plugin](/config-plugins/introduction) is already configured in your app config.

### Example app.json with config plugin

```json
{
  "expo": {
    "plugins": ["expo-router"]
  }
}
```

## Usage

To learn how to use native tabs, with Expo Router, read the native tabs guide:

[Native tabs](/router/advanced/native-tabs) — Learn how to use native tabs in your Expo Router app.

## API

```js
import { NativeTabs } from 'expo-router/unstable-native-tabs';
```

## Components

### `NativeTabs`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[NativeTabsProps](#nativetabsprops)\>

The component used to create native tabs layout.

Example

```tsx
import { NativeTabs } from 'expo-router/unstable-native-tabs';

export default function Layout() {
  return (
    <NativeTabs>
      <NativeTabs.Trigger name="home" />
      <NativeTabs.Trigger name="settings" />
    </NativeTabs>
  );
}
```

NativeTabsProps

### `backBehavior`

Supported platforms: Android.

Optional • Literal type: `string`

The behavior when navigating back with the back button.

Acceptable values are: `'history'` | `'none'` | `'initialRoute'`

### `backgroundColor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The background color of the tab bar.

### `badgeBackgroundColor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The background color of every badge in the tab bar.

### `badgeTextColor`

Supported platforms: Android, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The color of the badge text.

### `blurEffect`

Supported platforms: iOS.

Optional • Literal type: `string`

The blur effect applied to the tab bar.

Acceptable values are: `'light'` | `'dark'` | `'none'` | `'extraLight'` | `'regular'` | `'prominent'` | `'systemUltraThinMaterial'` | `'systemThinMaterial'` | `'systemMaterial'` | `'systemThickMaterial'` | `'systemChromeMaterial'` | `'systemUltraThinMaterialLight'` | `'systemThinMaterialLight'` | `'systemMaterialLight'` | `'systemThickMaterialLight'` | `'systemChromeMaterialLight'` | `'systemUltraThinMaterialDark'` | `'systemThinMaterialDark'` | `'systemMaterialDark'` | `'systemThickMaterialDark'` | `'systemChromeMaterialDark'` | `'systemDefault'`

### `disableIndicator`

Supported platforms: Android.

Optional • Type: `boolean`

Disables the active indicator for the tab bar.

### `disableTransparentOnScrollEdge`

Supported platforms: iOS.

Optional • Type: `boolean`

When set to `true`, the tab bar will not become transparent when scrolled to the edge.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

When set to `true`, hides the tab bar.

### `iconColor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

The color of every tab icon in the tab bar.

Acceptable values are: [ColorValue](https://reactnative.dev/docs/colors) | `{ default: ColorValue | undefined, selected: ColorValue | undefined }`

### `indicatorColor`

Supported platforms: Android, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The color of the tab indicator.

### `labelStyle`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

The style of the every tab label in the tab bar.

Acceptable values are: StyleProp<[NativeTabsLabelStyle](#nativetabslabelstyle)\> | { default: StyleProp<[NativeTabsLabelStyle](#nativetabslabelstyle)\>, selected: StyleProp<[NativeTabsLabelStyle](#nativetabslabelstyle)\> }

### `labelVisibilityMode`

Supported platforms: Android.

Optional • Literal type: `string`

The visibility mode of the tab item label.

> **See:** [Material Components documentation](https://github.com/material-components/material-components-android/blob/master/docs/components/BottomNavigation.md#making-navigation-bar-accessible)

Acceptable values are: `'auto'` | `'selected'` | `'labeled'` | `'unlabeled'`

### `minimizeBehavior`

Supported platforms: iOS 26+.

Optional • Literal type: `string` • Default: `automatic`

Specifies the minimize behavior for the tab bar.

Available starting from iOS 26.

The following values are currently supported:

-   `automatic` - resolves to the system default minimize behavior
-   `never` - the tab bar does not minimize
-   `onScrollDown` - the tab bar minimizes when scrolling down and expands when scrolling back up
-   `onScrollUp` - the tab bar minimizes when scrolling up and expands when scrolling back down

> **See:** The supported values correspond to the official [Apple documentation](https://developer.apple.com/documentation/uikit/uitabbarcontroller/minimizebehavior).

Acceptable values are: `'automatic'` | `'never'` | `'onScrollDown'` | `'onScrollUp'`

### `rippleColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The color of the ripple effect when the tab is pressed.

### `screenListeners`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Listeners for navigation events on all tabs.

Supported events:

-   `tabPress` - called when a tab is pressed
-   `focus` - called when the screen comes into focus
-   `blur` - called when the screen loses focus

Example

```tsx
<NativeTabs
  screenListeners={{
    tabPress: (e) => {
      console.log('Any tab pressed');
    },
  }}
>
  ...
</NativeTabs>
```

Acceptable values are: (prop: { route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string\> }) => ScreenListeners<[TabNavigationState](https://reactnavigation.org/docs/custom-navigators/#type-checking-navigators)<ParamListBase\>, NativeTabNavigationEventMap\> | [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<{ tabPress: EventListenerCallback<NativeTabNavigationEventMap & EventMapCore<[TabNavigationState](https://reactnavigation.org/docs/custom-navigators/#type-checking-navigators)<ParamListBase\>\>, 'tabPress', false\> }\>

### `shadowColor`

Supported platforms: iOS.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The color of the shadow.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uibarappearance/shadowcolor)

### `sidebarAdaptable`

Supported platforms: iOS 18+.

Optional • Type: `boolean`

When set to `true`, enables the sidebarAdaptable tab bar style on iPadOS and macOS. This prop has no effect on iPhone.

### `tintColor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The tint color of the tab icon.

Can be overridden by icon color and label color for each tab individually.

### `titlePositionAdjustment`

Supported platforms: iOS.

Optional • Type: `{ horizontal: number, vertical: number }`

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uitabbaritem/titlepositionadjustment)

#### Inherited Props

-   `PropsWithChildren`

### `NativeTabs.Trigger`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[NativeTabTriggerProps](#nativetabtriggerprops)\>

The component used to customize the native tab options both in the _layout file and from the tab screen.

When used in the _layout file, you need to provide a `name` prop. When used in the tab screen, the `name` prop takes no effect.

Example

```tsx
import { NativeTabs } from 'expo-router/unstable-native-tabs';

export default function Layout() {
  return (
    <NativeTabs>
      <NativeTabs.Trigger name="home" />
      <NativeTabs.Trigger name="settings" />
    </NativeTabs>
  );
}
```

Example

```tsx
import { NativeTabs } from 'expo-router/unstable-native-tabs';

export default function HomeScreen() {
  return (
    <View>
      <NativeTabs.Trigger>
        <NativeTabs.Trigger.Label>Home</NativeTabs.Trigger.Label>
      </NativeTabs.Trigger>
      <Text>This is home screen!</Text>
    </View>
  );
}
```

NativeTabTriggerProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The children of the trigger.

Use `Icon`, `Label`, and `Badge` components to customize the tab.

### `contentStyle`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'backgroundColor' | 'experimental_backgroundImage' | 'alignContent' | 'alignItems' | 'flexDirection' | 'gap' | 'justifyContent' | 'padding' | 'paddingBottom' | 'paddingEnd' | 'paddingHorizontal' | 'paddingLeft' | 'paddingRight' | 'paddingStart' | 'paddingTop' | 'paddingVertical' | 'paddingBlock' | 'paddingBlockEnd' | 'paddingBlockStart' | 'paddingInline' | 'paddingInlineEnd' | 'paddingInlineStart'\>

The style applied to the content of the tab

Note: Only certain style properties are supported.

### `disableAutomaticContentInsets`

Supported platforms: Android, iOS.

Optional • Type: `boolean`

The default behavior differs between iOS and Android.

On **Android**, the content of a native tabs screen is automatically wrapped in a `SafeAreaView`, and the **bottom** inset is applied. Other insets must be handled manually.

On **iOS**, the first scroll view nested inside a native tabs screen has [automatic content inset adjustment](https://reactnative.dev/docs/scrollview#contentinsetadjustmentbehavior-ios) enabled

When this property is set to `true`, automatic content inset adjustment is disabled for the screen and must be managed manually. You can use `SafeAreaView` from `react-native-screens/experimental` to handle safe area insets.

### `disablePopToTop`

Supported platforms: iOS.

Optional • Type: `boolean` • Default: `false`

If true, the tab will not pop stack to the root when selected again.

### `disableScrollToTop`

Supported platforms: iOS.

Optional • Type: `boolean` • Default: `false`

If true, the tab will not scroll to the top when selected again.

### `disableTransparentOnScrollEdge`

Supported platforms: iOS.

Optional • Type: `boolean`

When set to `true`, the tab bar will not become transparent when scrolled to the edge.

When set on a trigger, it takes precedence over the value set on `NativeTabs`.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If true, the tab will be hidden from the tab bar.

> **Note**: Marking a tab as `hidden` means it cannot be navigated to in any way.

> **Note**: Dynamically hiding tabs will remount the navigator and the state will be reset.

### `listeners`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Listeners for navigation events on this tab.

Supported events:

-   `tabPress` - called when this tab is pressed
-   `focus` - called when this screen comes into focus
-   `blur` - called when this screen loses focus

Example

```tsx
<NativeTabs.Trigger
  name="home"
  listeners={{
    tabPress: (e) => {
      console.log('Home tab pressed');
    },
  }}
/>
```

Acceptable values are: [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<undefined\> | (prop: { route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string\> }) => ScreenListeners<[NavigationState](https://reactnavigation.org/docs/navigation-state), EventMapBase\>

### `name`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

The name of the route.

This is required when used inside a Layout component.

When used in a route it has no effect.

### `role`

Supported platforms: iOS.

Optional • Literal type: `string`

System-provided tab bar item with predefined icon and title

Uses Apple's built-in tab bar items (e.g., bookmarks, contacts, downloads) with standard iOS styling and localized titles. Custom `icon` or `selectedIcon` properties will override the system icon, but the system-defined title cannot be customized.

> **See:** The supported values correspond to the official [Apple documentation](https://developer.apple.com/documentation/uikit/uitabbaritem/systemitem).

Acceptable values are: `'search'` | `'history'` | `'bookmarks'` | `'contacts'` | `'downloads'` | `'favorites'` | `'featured'` | `'more'` | `'mostRecent'` | `'mostViewed'` | `'recents'` | `'topRated'`

### `unstable_nativeProps`

Supported platforms: Android, iOS.

Optional • Type: [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<[Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<TabsScreenProps, 'isFocused' | 'tabKey'\>\>

Props passed to the underlying native tab screen implementation. Use this to configure props not directly exposed by Expo Router, but available in `react-native-screens`.

> **Note**: This will override any other props set by Expo Router and may lead to unexpected behavior.

> **Note**: This is an unstable API and may change or be removed in minor versions.

### `NativeTabs.BottomAccessory`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[NativeTabsBottomAccessoryProps](#nativetabsbottomaccessoryprops)\> & { usePlacement: () => 'regular' | 'inline' }\>

NativeTabsBottomAccessoryProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `NativeTabs.Trigger.Badge`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[NativeTabsTriggerBadgeProps](/versions/v55.0.0/sdk/router/native-tabs#nativetabstriggerbadgeprops)\>\>

NativeTabsTriggerBadgeProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

The text to display as the badge for the tab. If not provided, the badge will not be displayed.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

If true, the badge will be hidden.

### `selectedBackgroundColor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

### `NativeTabs.Trigger.Icon`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[NativeTabsTriggerIconProps](/versions/v55.0.0/sdk/router/native-tabs#nativetabstriggericonprops)\>\>

NativeTabsTriggerIconProps

### `selectedColor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

### `NativeTabs.Trigger.Label`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[NativeTabsTriggerLabelProps](/versions/v55.0.0/sdk/router/native-tabs#nativetabstriggerlabelprops)\>\>

NativeTabsTriggerLabelProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

The text to display as the label for the tab.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

If true, the label will be hidden.

### `selectedStyle`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: StyleProp<[NativeTabsLabelStyle](#nativetabslabelstyle)\>

### `NativeTabs.Trigger.VectorIcon`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[VectorIconProps](/versions/v55.0.0/sdk/router#vectoriconprops)<NameT\>\>

Helper component for loading vector icons.

Prefer using the `md` and `sf` props on `Icon` rather than using this component directly. Only use this component when you need to load a specific icon from a vector icon family.

Example

```tsx
import { Icon, VectorIcon } from 'expo-router';
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';

<Icon src={<VectorIcon family={MaterialCommunityIcons} name="home" />} />
```

## Interfaces

### `DrawableIcon`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| drawable(optional) | `string` | Supported platforms: Android. The name of the drawable resource to use as an icon. |

### `MaterialIcon`

Supported platforms: Android.

Material icon name for Android native tabs.

| Property | Type | Description |
| --- | --- | --- |
| md | `See description for available values.` | Material icon glyph name. See the [Material icons for the complete catalog](https://fonts.google.com/icons). |

### `SFSymbolIcon`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| sf(optional) | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript) | { default: SFSymbols7_0 | undefined, selected: [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript) } | Supported platforms: iOS. The name of the SF Symbol to use as an icon. The value can be provided in two ways:
-   As a string with the SF Symbol name
-   As an object specifying the default and selected states

. Example

```tsx
<Icon sf="magnifyingglass" />
```

. Example

```tsx
<Icon sf={{ default: "house", selected: "house.fill" }} />
```

 |

### `SrcIcon`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| renderingMode(optional) | `'template' | 'original'` | Supported platforms: iOS. Controls how the image icon is rendered on iOS.
-   `'template'`: iOS applies tint color to the icon (selected/unselected states)
-   `'original'`: Preserves original icon colors

. **Default behavior:**

-   If tab bar icon color is configured, defaults to `'template'`
-   If no icon color is set, defaults to `'original'`

See: Apple documentation for more information. |
| src(optional) | ReactElement<unknown, string | JSXElementConstructor<any>\> | [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | { default: ReactElement<unknown, string | JSXElementConstructor<any>> | ImageSourcePropType | undefined, selected: ReactElement<unknown, string | JSXElementConstructor<any>> | ImageSourcePropType } | Supported platforms: Android, iOS. The image source to use as an icon. When `sf` prop is used it will override this prop on iOS. When `drawable` or `material` prop is used it will override this prop on Android. The value can be provided in two ways:

-   As an image source
-   As an object specifying the default and selected states

. Example

```tsx
<Icon src={require('./path/to/icon.png')} />
```

. Example

```tsx
<Icon src={{ default: require('./path/to/icon.png'), selected: require('./path/to/icon-selected.png') }} />
```

 |

### `XcassetIcon`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| xcasset(optional) | `string | { default: string, selected: string }` | Supported platforms: iOS. The name of the iOS asset catalog image to use as an icon. Xcassets provide automatic multi-resolution (@1x/@2x/@3x), dark mode variants, and device-specific images via `[UIImage imageNamed:]`. The rendering mode (template vs original) can be controlled via the `renderingMode` prop on the `Icon` component. By default, icons are tinted when `iconColor` is set, and rendered as original otherwise. The value can be provided in two ways:
-   As a string with the asset catalog image name
-   As an object specifying the default and selected states

. Example

```tsx
<Icon xcasset="custom-icon" />
```

. Example

```tsx
<Icon xcasset={{ default: "home-outline", selected: "home-filled" }} />
```

 |

## Types

### `NativeTabsLabelStyle`

Supported platforms: Android, iOS, tvOS, Web.

Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[TextStyle](https://reactnative.dev/docs/text-style-props), 'fontFamily' | 'fontSize' | 'fontStyle' | 'fontWeight' | 'color'\>

### `SymbolOrImageSource`

Supported platforms: Android, iOS, tvOS, Web.

Type: `object` shaped as below:

| Property | Type | Description |
| --- | --- | --- |
| drawable(optional) | `string` | Supported platforms: Android. The name of the drawable resource to use as an icon. |
| sf(optional) | [SFSymbol](https://github.com/nandorojo/sf-symbols-typescript) | Supported platforms: iOS. The name of the SF Symbol to use as an icon. |
| xcasset(optional) | `string` | Supported platforms: iOS. The name of the iOS asset catalog image to use as an icon. |

Or `object` shaped as below:

| Property | Type | Description |
| --- | --- | --- |
| renderingMode(optional) | `'template' | 'original'` | Supported platforms: iOS. Controls how the icon is rendered on iOS. Default: `'template'` |
| src(optional) | [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | null\> | The image source to use as an icon. |
