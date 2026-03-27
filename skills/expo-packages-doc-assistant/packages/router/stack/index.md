---
title: Router Stack
description: An Expo Router API that provides Stack navigator, toolbar, and screen components.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-router'
packageName: 'expo-router'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
---

# Expo Router Stack

An Expo Router API that provides Stack navigator, toolbar, and screen components.
Android, iOS, tvOS, Web, Included in Expo Go

An Expo Router API that provides Stack navigator, toolbar, and screen components.

> See the [Expo Router](/versions/latest/sdk/router/index) reference for installation and configuration.

## Usage

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return <Stack />;
}
```

For more information about using stack navigator, read the stack layout guide:

[Stack layout](/router/basics/layout-types/stack) — Learn how to use the Stack layout in Expo Router.

## API

```js
import { Stack } from 'expo-router';
```

## Components

### `Stack`

Supported platforms: Android, iOS, tvOS, Web.

Renders a native stack navigator.

### `Stack.Header`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackHeaderProps](#stackheaderprops)\>

The component used to configure header styling for a stack screen.

Use this component to set header appearance properties like blur effect, background color, and shadow visibility.

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Header
        blurEffect="systemMaterial"
        style={{ backgroundColor: '#fff' }}
      />
      <ScreenContent />
    </>
  );
}
```

Example

When used inside a layout with Stack.Screen:

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Header blurEffect="systemMaterial" />
      </Stack.Screen>
    </Stack>
  );
}
```

> **Note:** If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

StackHeaderProps

### `asChild`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

When `true`, renders children as a custom header component, replacing the default header entirely. Use this to implement fully custom header layouts.

### `blurEffect`

Supported platforms: iOS.

Optional • Type: `BlurEffectTypes`

The blur effect to apply to the header background on iOS. Common values include 'regular', 'prominent', 'systemMaterial', etc.

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Child elements for custom header when `asChild` is true.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether to hide the header completely. When set to `true`, the header will not be rendered.

### `largeStyle`

Supported platforms: iOS.

Optional • Type: StyleProp<{ backgroundColor: [ColorValue](https://reactnative.dev/docs/colors), shadowColor: 'transparent' }\>

Style properties for the large title header (iOS).

-   `backgroundColor`: Background color of the large title header
-   `shadowColor`: Set to 'transparent' to hide the large title shadow/border

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: StyleProp<{ backgroundColor: [ColorValue](https://reactnative.dev/docs/colors), color: [ColorValue](https://reactnative.dev/docs/colors), shadowColor: 'transparent' }\>

Style properties for the standard-sized header.

-   `color`: Tint color for header elements (similar to tintColor in React Navigation)
-   `backgroundColor`: Background color of the header
-   `shadowColor`: Set to 'transparent' to hide the header shadow/border

### `transparent`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the header should be transparent. When `true`, the header is absolutely positioned and content scrolls underneath.

Auto-enabled when:

-   `style.backgroundColor` is 'transparent'
-   `blurEffect` is set (required for blur to work)

### `Stack.Screen`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackScreenProps](#stackscreenprops)\>

StackScreenProps

### `dangerouslySingular`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [SingularOptions](#singularoptions)

When enabled, the navigator will reuse an existing screen instead of pushing a new one.

Only supported when used inside a Layout component.

> **Deprecated:** Use `dangerouslySingular` instead.
> 
> Only supported when used inside a Layout component.

### `getId`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `(__namedParameters: { params: Record<string, any> }) => string | undefined`

Function to determine a unique ID for the screen.

### `initialParams`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `Record<string, any>`

Initial params to pass to the route.

Only supported when used inside a Layout component.

### `listeners`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Listeners for navigation events.

Only supported when used inside a Layout component.

Acceptable values are: [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<undefined\> | (prop: { navigation: any, route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string\> }) => ScreenListeners<TState, TEventMap\>

### `name`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

Name is required when used inside a Layout component.

### `options`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Options to configure the screen.

Accepts an object or a function returning an object. The function form `options={({ route }) => ({})}` is only supported when used inside a Layout component. When used inside a page component, pass an options object directly.

Acceptable values are: [NativeStackNavigationOptions](https://reactnavigation.org/docs/native-stack-navigator#options) | (prop: { navigation: any, route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string\> }) => [NativeStackNavigationOptions](https://reactnavigation.org/docs/native-stack-navigator#options)

### `redirect`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Redirect to the nearest sibling route. If all children are `redirect={true}`, the layout will render `null` as there are no children to render.

Only supported when used inside a Layout component.

#### Inherited Props

-   `PropsWithChildren`

### `Stack.SearchBar`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackSearchBarProps](#stacksearchbarprops)\>

A search bar component that integrates with the native stack header.

> **Note:** Using `Stack.SearchBar` will automatically make the header visible (`headerShown: true`), as the search bar is rendered as part of the native header.

To display the search bar in the bottom toolbar on iOS 26+, use `Stack.Toolbar.SearchBarSlot` inside `Stack.Toolbar`.

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.SearchBar
        placeholder="Search..."
        onChangeText={(text) => console.log(text)}
      />
     <ScreenContent />
    </>
  );
}
```

StackSearchBarProps

#### Inherited Props

-   `SearchBarProps`

### `Stack.Toolbar`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackToolbarProps](#stacktoolbarprops)\>

The component used to configure the stack toolbar.

-   Use `placement="left"` to customize the left side of the header.
-   Use `placement="right"` to customize the right side of the header.
-   Use `placement="bottom"` (default) to show a bottom toolbar (iOS only).

If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

> **Note:** Using `Stack.Toolbar` with `placement="left"` or `placement="right"` will automatically make the header visible (`headerShown: true`), as the toolbar is rendered as part of the native header.

> **Note:** `Stack.Toolbar` with `placement="bottom"` can only be used inside **page** components, not in layout components.

Example

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Toolbar placement="left">
          <Stack.Toolbar.Button icon="sidebar.left" onPress={() => alert('Left button pressed!')} />
        </Stack.Toolbar>
        <Stack.Toolbar placement="right">
          <Stack.Toolbar.Button icon="ellipsis.circle" onPress={() => alert('Right button pressed!')} />
        </Stack.Toolbar>
      </Stack.Screen>
    </Stack>
  );
}
```

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Toolbar placement="left">
        <Stack.Toolbar.Button icon="sidebar.left" onPress={() => alert('Left button pressed!')} />
      </Stack.Toolbar>
      <Stack.Toolbar>
        <Stack.Toolbar.Spacer />
        <Stack.Toolbar.Button icon="magnifyingglass" onPress={() => {}} />
        <Stack.Toolbar.Spacer />
      </Stack.Toolbar>
      <ScreenContent />
    </>
  );
}
```

StackToolbarProps

### `asChild`

Supported platforms: iOS.

Optional • Type: `boolean` • Default: `false`

When `true`, renders children as a custom component in the header area, replacing the default header layout.

Only applies to `placement="left"` and `placement="right"`.

### `children`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Child elements to compose the toolbar. Can include Stack.Toolbar.Button, Stack.Toolbar.Menu, Stack.Toolbar.View, Stack.Toolbar.Spacer, and Stack.Toolbar.SearchBarSlot (bottom only) components.

### `placement`

Supported platforms: iOS.

Optional • Type: `ToolbarPlacement` • Default: `'bottom'`

The placement of the toolbar.

-   `'left'`: Renders items in the left area of the header.
-   `'right'`: Renders items in the right area of the header.
-   `'bottom'`: Renders items in the bottom toolbar (iOS only).

### `Stack.Screen.BackButton`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackScreenBackButtonProps](#stackscreenbackbuttonprops)\>

Component to configure the back button.

Can be used inside Stack.Screen in a layout or directly inside a screen component.

Example

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="detail">
        <Stack.Screen.BackButton displayMode="minimal">Back</Stack.Screen.BackButton>
      </Stack.Screen>
    </Stack>
  );
}
```

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Screen.BackButton hidden />
      <ScreenContent />
    </>
  );
}
```

> **Note:** If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

StackScreenBackButtonProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

The title to display for the back button.

### `displayMode`

Supported platforms: iOS.

Optional • Type: `BackButtonDisplayMode`

The display mode for the back button.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Whether to hide the back button.

### `src`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource)

Custom image source for the back button.

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `StyleProp<undefined>`

Style for the back button title.

### `withMenu`

Supported platforms: iOS.

Optional • Type: `boolean`

Whether to show a context menu when long pressing the back button.

### `Stack.Screen.Title`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackScreenTitleProps](#stackscreentitleprops)\>

Component to set the screen title.

Can be used inside Stack.Screen in a layout or directly inside a screen component.

Example

String title in a layout:

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Screen.Title large>Home</Stack.Screen.Title>
      </Stack.Screen>
    </Stack>
  );
}
```

Example

String title inside a screen:

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Screen.Title>My Page</Stack.Screen.Title>
      <ScreenContent />
    </>
  );
}
```

Example

Custom component as the title using `asChild`:

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Screen.Title asChild>
          <MyCustomTitle />
        </Stack.Screen.Title>
      </Stack.Screen>
    </Stack>
  );
}
```

> **Note:** If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

StackScreenTitleProps

### `asChild`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Use this to render a custom component as the header title.

Example

```tsx
<Stack.Screen.Title asChild>
  <MyCustomTitle />
</Stack.Screen.Title>
```

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `React.ReactNode`

The title content. Pass a string for a plain text title, or a custom component when `asChild` is enabled.

### `large`

Supported platforms: iOS.

Optional • Type: `boolean`

Enables large title mode.

### `largeStyle`

Supported platforms: iOS.

Optional • Type: StyleProp<{ color: string, fontFamily: TextStyle[fontFamily], fontSize: TextStyle[fontSize], fontWeight: [Exclude](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers)<TextStyle[fontWeight], number\> }\>

Style properties for the large title header.

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: StyleProp<{ color: string, fontFamily: TextStyle[fontFamily], fontSize: TextStyle[fontSize], fontWeight: [Exclude](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers)<TextStyle[fontWeight], number\>, textAlign: 'left' | 'center' }\>

### `Stack.Toolbar.Badge`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarBadgeProps](#stacktoolbarbadgeprops)\>\>

StackToolbarBadgeProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

The text to display as the badge

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: StyleProp<[Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[TextStyle](https://reactnative.dev/docs/text-style-props), 'fontFamily' | 'fontSize' | 'fontWeight' | 'backgroundColor' | 'color'\>\>

### `Stack.Toolbar.Button`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarButtonProps](#stacktoolbarbuttonprops)\>\>

StackToolbarButtonProps

### `accessibilityHint`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

### `accessibilityLabel`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

There are two ways to specify the content of the button:

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Toolbar placement="left">
        <Stack.Toolbar.Button icon="star.fill">As text passed as children</Stack.Toolbar.Button>
      </Stack.Toolbar>
      <ScreenContent />
    </>
  );
}
```

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Toolbar placement="left">
        <Stack.Toolbar.Button>
          <Stack.Toolbar.Icon sf="star.fill" />
          <Stack.Toolbar.Label>As components</Stack.Toolbar.Label>
          <Stack.Toolbar.Badge>3</Stack.Toolbar.Badge>
        </Stack.Toolbar.Button>
      </Stack.Toolbar>
      <ScreenContent />
    </>
  );
}
```

> **Note**: When icon is used, the label will not be shown and will be used for accessibility purposes only. Badge is only supported in left/right placements, not in bottom (iOS toolbar limitation).

### `disabled`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the button should be hidden.

### `hidesSharedBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether to hide the shared background.

### `icon`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Icon to display in the button.

Can be a string representing an SFSymbol or an image source.

> **Note**: When used in `placement="bottom"`, only string SFSymbols are supported. Use the `image` prop to provide custom images.

Acceptable values are: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

### `iconRenderingMode`

Supported platforms: iOS.

Optional • Literal type: `string`

Controls how image-based icons are rendered on iOS.

-   `'template'`: iOS applies tint color to the icon
-   `'original'`: Preserves original icon colors (useful for multi-color icons)

**Default behavior:**

-   If `tintColor` is specified, defaults to `'template'`
-   If no `tintColor`, defaults to `'original'`

This prop only affects image-based icons (not SF Symbols).

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are: `'template'` | `'original'`

### `image`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `ImageRef`

Image to display in the button.

> **Note**: This prop is only supported in toolbar with `placement="bottom"`.

### `onPress`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `() => void`

### `selected`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Whether the button is in a selected state

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/isselected) for more information

### `separateBackground`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether to separate the background of this item from other header items.

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: StyleProp<[TextStyle](https://reactnative.dev/docs/text-style-props)\>

Style for the label of the header item.

### `tintColor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The tint color to apply to the button item

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/tintcolor) for more information.

### `variant`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `string` • Default: `'plain'`

Acceptable values are: `'done'` | `'prominent'` | `'plain'`

### `Stack.Toolbar.Icon`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarIconProps](#stacktoolbariconprops)\>\>

StackToolbarIconProps

### `renderingMode`

Supported platforms: iOS.

Optional • Literal type: `string`

Controls how the image icon is rendered on iOS.

-   `'template'`: iOS applies tint color to the icon
-   `'original'`: Preserves original icon colors

Defaults based on parent component's `tintColor`:

-   With `tintColor`: defaults to `'template'`
-   Without `tintColor`: defaults to `'original'`

Acceptable values are: `'template'` | `'original'`

### `src`

Supported platforms: Android, iOS, tvOS, Web.

Type: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource)

### `sf`

Supported platforms: Android, iOS, tvOS, Web.

Type: [SFSymbol](https://github.com/nandorojo/sf-symbols-typescript)

### `xcasset`

Supported platforms: iOS.

Type: `string`

Name of an image in your Xcode asset catalog (`.xcassets`).

### `Stack.Toolbar.Label`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarLabelProps](#stacktoolbarlabelprops)\>\>

StackToolbarLabelProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

The text to display as the label for the tab.

### `Stack.Toolbar.Menu`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarMenuProps](#stacktoolbarmenuprops)\>\>

StackToolbarMenuProps

### `accessibilityHint`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

### `accessibilityLabel`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Menu content - can include icons, labels, badges and menu actions.

Example

```tsx
<Stack.Toolbar.Menu>
  <Stack.Toolbar.Icon sfSymbol="ellipsis.circle" />
  <Stack.Toolbar.Label>Options</Stack.Toolbar.Label>
  <Stack.Toolbar.MenuAction onPress={() => {}}>Action 1</Stack.Toolbar.MenuAction>
</Stack.Toolbar.Menu>
```

### `destructive`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as destructive.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/destructive) for more information.

### `disabled`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

### `elementSize`

Supported platforms: iOS 16.0+.

Optional • Literal type: `string`

The preferred size of the menu elements.

> **Note**: This prop is only supported in `Stack.Toolbar.Bottom`.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/preferredelementsize) for more information.

Acceptable values are: `'small'` | `'auto'` | `'medium'` | `'large'`

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the menu should be hidden.

### `hidesSharedBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether to hide the shared background.

> **See:** [Official Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/hidessharedbackground) for more information.

### `icon`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Icon for the menu item.

Can be an SF Symbol name or an image source.

> **Note**: When used in `placement="bottom"`, only string SFSymbols are supported. Use the `image` prop to provide custom images.

Acceptable values are: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

### `iconRenderingMode`

Supported platforms: iOS.

Optional • Literal type: `string`

Controls how image-based icons are rendered on iOS.

-   `'template'`: iOS applies tint color to the icon (useful for monochrome icons)
-   `'original'`: Preserves original icon colors (useful for multi-color icons)

**Default behavior:**

-   If `tintColor` is specified, defaults to `'template'`
-   If no `tintColor`, defaults to `'original'`

This prop only affects image-based icons (not SF Symbols).

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are: `'template'` | `'original'`

### `image`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `ImageRef`

Image to display for the menu item.

> **Note**: This prop is only supported in toolbar with `placement="bottom"`.

### `inline`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu will be displayed inline. This means that the menu will not be collapsed

> **Note**: Inline menus are only supported in submenus.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/displayinline) for more information.

### `palette`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu will be displayed as a palette. This means that the menu will be displayed as one row

> **Note**: Palette menus are only supported in submenus.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/displayaspalette) for more information.

### `separateBackground`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether to separate the background of this item from other header items.

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `StyleProp<BasicTextStyle>`

Style for the label of the header item.

### `tintColor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The tint color to apply to the button item

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/tintcolor) for more information.

### `title`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

Optional title to show on top of the menu.

### `variant`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `string` • Default: `'plain'`

Acceptable values are: `'done'` | `'prominent'` | `'plain'`

### `Stack.Toolbar.MenuAction`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarMenuActionProps](#stacktoolbarmenuactionprops)\>\>

StackToolbarMenuActionProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Can be an Icon, Label or string title.

### `destructive`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as destructive.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/destructive) for more information.

### `disabled`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu item will be disabled and not selectable.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/disabled) for more information.

### `discoverabilityLabel`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

An elaborated title that explains the purpose of the action.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

### `icon`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Acceptable values are: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

### `iconRenderingMode`

Supported platforms: iOS.

Optional • Literal type: `string`

Controls how image-based icons are rendered on iOS.

-   `'template'`: iOS applies tint color to the icon (useful for monochrome icons)
-   `'original'`: Preserves original icon colors (useful for multi-color icons)

**Default behavior:**

-   If `tintColor` is specified, defaults to `'template'`
-   If no `tintColor`, defaults to `'original'`

This prop only affects image-based icons (not SF Symbols).

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are: `'template'` | `'original'`

### `image`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `ImageRef`

Image to display for the menu action.

> **Note**: This prop is only supported in `Stack.Toolbar.Bottom`.

### `isOn`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as selected.

### `onPress`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `() => void`

### `subtitle`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

An optional subtitle for the menu item.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/subtitle) for more information.

### `unstable_keepPresented`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu will be kept presented after the action is selected.

This is marked as unstable, because when action is selected it will recreate the menu, which will close all opened submenus and reset the scroll position.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/keepsmenupresented) for more information.

### `Stack.Toolbar.SearchBarSlot`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarSearchBarSlotProps](#stacktoolbarsearchbarslotprops)\>\>

StackToolbarSearchBarSlotProps

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the search bar slot should be hidden.

### `hidesSharedBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether to hide the shared background.

### `separateBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether this search bar slot has a separate background from adjacent items. When this prop is `true`, the search bar will always render as `integratedButton`.

In order to render the search bar with a separate background, ensure that adjacent toolbar items have `separateBackground` set to `true` or use `Stack.Toolbar.Spacer` to create spacing.

Example

```tsx
<Stack.SearchBar onChangeText={()=>{}} />
<Stack.Toolbar placement="bottom">
  <Stack.Toolbar.SearchBarSlot />
  <Stack.Toolbar.Spacer />
  <Stack.Toolbar.Button icon="square.and.pencil" />
</Stack.Toolbar>
```

### `Stack.Toolbar.Spacer`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarSpacerProps](#stacktoolbarspacerprops)\>\>

StackToolbarSpacerProps

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the spacer should be hidden.

### `sharesBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether this spacer shares background with adjacent items.

Only available in bottom placement.

### `width`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `number`

The width of the spacing element.

In Left/Right placements, width is required. In Bottom placement, if width is not provided, the spacer will be flexible and expand to fill available space.

### `Stack.Toolbar.View`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarViewProps](#stacktoolbarviewprops)\>\>

StackToolbarViewProps

### `asChild`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

When `true`, renders children as a custom component in the header area, replacing the default header layout.

Only applies to `placement="left"` and `placement="right"`.

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Child elements to compose the toolbar. Can include Stack.Toolbar.Button, Stack.Toolbar.Menu, Stack.Toolbar.View, Stack.Toolbar.Spacer, and Stack.Toolbar.SearchBarSlot (bottom only) components.

### `placement`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `ToolbarPlacement` • Default: `'bottom'`

The placement of the toolbar.

-   `'left'`: Renders items in the left area of the header.
-   `'right'`: Renders items in the right area of the header.
-   `'bottom'`: Renders items in the bottom toolbar (iOS only).

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `ReactElement<unknown, string | JSXElementConstructor<any>>`

Can be any React node.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the view should be hidden.

### `hidesSharedBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether to hide the shared background.

> **See:** [Official Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/hidessharedbackground) for more information.

### `separateBackground`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether to separate the background of this item from other items.

Only available in bottom placement.

## Interfaces

### `StackHeaderItemSharedProps`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| accessibilityHint(optional) | `string` | - |
| accessibilityLabel(optional) | `string` | - |
| children(optional) | [ReactNode](https://reactnative.dev/docs/react-node) | - |
| disabled(optional) | `boolean` | - |
| hidesSharedBackground(optional) | `boolean` | - |
| icon(optional) | [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript) | - |
| iconRenderingMode(optional) | `'template' | 'original'` | Supported platforms: iOS. Controls how image-based icons are rendered on iOS.
-   `'template'`: iOS applies tint color to the icon
-   `'original'`: Preserves original icon colors (useful for multi-color icons)

. **Default behavior:**

-   If `tintColor` is specified, defaults to `'template'`
-   If no `tintColor`, defaults to `'original'`

. This prop only affects image-based icons (not SF Symbols).See: Apple documentation for more information. |
| separateBackground(optional) | `boolean` | - |
| style(optional) | `StyleProp<BasicTextStyle>` | - |
| tintColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| variant(optional) | `'done' | 'prominent' | 'plain'` | Default: `'plain'` |
