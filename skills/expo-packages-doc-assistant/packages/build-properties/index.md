---
title: BuildProperties
description: A config plugin that allows customizing native build properties during prebuild.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-build-properties'
packageName: 'expo-build-properties'
platforms: ['android', 'ios', 'tvos']
---

# Expo BuildProperties

A config plugin that allows customizing native build properties during prebuild.
Android, iOS, tvOS

`expo-build-properties` is a [config plugin](/config-plugins/introduction) configuring the native build properties of your **android/gradle.properties** and **ios/Podfile.properties.json** directories during [Prebuild](/workflow/continuous-native-generation).

> This config plugin configures how [Prebuild command](/workflow/continuous-native-generation#usage) generates the native **android** and **ios** directories and therefore cannot be used with projects that don't run `npx expo prebuild` (bare projects).

## Installation

```sh
npx expo install expo-build-properties
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Usage

### Example app.json with config plugin

```json
{
  "expo": {
    "plugins": [
      [
        "expo-build-properties",
        {
          "android": {
            "compileSdkVersion": 35,
            "targetSdkVersion": 35,
            "buildToolsVersion": "35.0.0"
          },
          "ios": {
            "deploymentTarget": "15.1"
          }
        }
      ]
    ]
  }
}
```

### All configurable properties

[`PluginConfigType`](/versions/latest/sdk/build-properties#pluginconfigtype) interface represents currently available configuration properties.

## API

## Methods

### `BuildProperties.resolveConfigValue(config, platform, key)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `config` | [PluginConfigType](#pluginconfigtype) |
| `platform` | `'android' | 'ios'` |
| `key` | `K` |

  

Resolves a shared config value with platform-specific override. Platform-specific values take precedence over top-level values.

Returns: `SharedBuildConfigFields[K]`

### `BuildProperties.withBuildProperties(config, props)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `config` | [ExpoConfig](https://github.com/expo/expo/blob/main/packages/%40expo/config-types/src/ExpoConfig.ts) | Expo config for application. |
| `props` | [PluginConfigType](#pluginconfigtype) | Configuration for the build properties plugin. |

  

Config plugin allowing customizing native Android and iOS build properties for managed apps.

Returns: `ExpoConfig`

## Interfaces

### `AndroidMavenRepository`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| authentication(optional) | `'basic' | 'digest' | 'header'` | The authentication scheme to use when accessing the Maven repository. |
| credentials(optional) | [AndroidMavenRepositoryCredentials](#androidmavenrepositorycredentials) | The credentials to use when accessing the Maven repository. May be of type PasswordCredentials, HttpHeaderCredentials, or AWSCredentials.See: The authentication schemes section of Gradle documentation for more information. |
| url | `string` | The URL of the Maven repository. |

### `AndroidMavenRepositoryAWSCredentials`

Supported platforms: Android.

The Android Maven repository credentials for AWS S3.

| Property | Type | Description |
| --- | --- | --- |
| accessKey | `string` | The credential value. You can also pass `"System.getenv('ENV_VAR_NAME')"` to get the value from an environment variable. |
| secretKey | `string` | The credential value. You can also pass `"System.getenv('ENV_VAR_NAME')"` to get the value from an environment variable. |
| sessionToken(optional) | `string` | The credential value. You can also pass `"System.getenv('ENV_VAR_NAME')"` to get the value from an environment variable. |

### `AndroidMavenRepositoryHttpHeaderCredentials`

Supported platforms: Android.

The Android Maven repository credentials that are passed as HTTP headers.

| Property | Type | Description |
| --- | --- | --- |
| name | `string` | The credential value. You can also pass `"System.getenv('ENV_VAR_NAME')"` to get the value from an environment variable. |
| value | `string` | The credential value. You can also pass `"System.getenv('ENV_VAR_NAME')"` to get the value from an environment variable. |

### `AndroidMavenRepositoryPasswordCredentials`

Supported platforms: Android.

The Android Maven repository credentials for basic authentication.

| Property | Type | Description |
| --- | --- | --- |
| password | `string` | The credential value. You can also pass `"System.getenv('ENV_VAR_NAME')"` to get the value from an environment variable. |
| username | `string` | The credential value. You can also pass `"System.getenv('ENV_VAR_NAME')"` to get the value from an environment variable. |

### `ExtraIosPodDependency`

Supported platforms: iOS.

Interface representing extra CocoaPods dependency.

> **See:** [Podfile syntax reference](https://guides.cocoapods.org/syntax/podfile.html#pod)

| Property | Type | Description |
| --- | --- | --- |
| branch(optional) | `string` | The git branch to fetch. See the `git` property for more information. |
| commit(optional) | `string` | The git commit to fetch. See the `git` property for more information. |
| configurations(optional) | `string[]` | Build configurations for which the pod should be installed. . Example`['Debug', 'Release']` |
| git(optional) | `string` | Use the bleeding edge version of a Pod. . Example
```json
{
  "name": "AFNetworking",
  "git": "https://github.com/gowalla/AFNetworking.git",
  "tag": "0.7.0"
}
```

. This acts like to add this pod dependency statement:

```rb
pod 'AFNetworking', :git => 'https://github.com/gowalla/AFNetworking.git', :tag => '0.7.0'
```

 |
| modular_headers(optional) | `boolean` | Whether this pod should use modular headers. |
| name | `string` | Name of the pod. |
| path(optional) | `string` | Custom local filesystem path to add the dependency. . Example`~/Documents/AFNetworking` |
| podspec(optional) | `string` | Custom podspec path. . Example. `https://example.com/JSONKit.podspec` |
| source(optional) | `string` | Custom source to search for this dependency. . Example`https://github.com/CocoaPods/Specs.git` |
| tag(optional) | `string` | The git tag to fetch. See the `git` property for more information. |
| testspecs(optional) | `string[]` | Test specs can be optionally included via the :testspecs option. By default, none of a Pod's test specs are included. . Example`['UnitTests', 'SomeOtherTests']` |
| version(optional) | `string` | Version of the pod. CocoaPods supports various [versioning options](https://guides.cocoapods.org/using/the-podfile.html#pod). . Example`~> 0.1.2` |

### `PluginConfigType`

Supported platforms: Android, iOS, tvOS.

Extends: [SharedBuildConfigFields](#sharedbuildconfigfields)

Interface representing base build properties configuration.

| Property | Type | Description |
| --- | --- | --- |
| android(optional) | [PluginConfigTypeAndroid](#pluginconfigtypeandroid) | Supported platforms: Android. Interface representing available configuration for Android native build properties. |
| ios(optional) | [PluginConfigTypeIos](#pluginconfigtypeios) | Supported platforms: iOS. Interface representing available configuration for iOS native build properties. |

### `PluginConfigTypeAndroid`

Supported platforms: Android.

Extends: [SharedBuildConfigFields](#sharedbuildconfigfields)

Interface representing available configuration for Android native build properties.

| Property | Type | Description |
| --- | --- | --- |
| buildArchs(optional) | `string[]` | Override the default `reactNativeArchitectures` list of ABIs to build in **gradle.properties**. Default: `["armeabi-v7a", "arm64-v8a", "x86", "x86_64"]`See: Android documentation for more information. . Example
```json
["arm64-v8a", "x86_64"]
```

 |
| buildFromSource(optional) | `boolean` | Deprecated: Use buildReactNativeFromSource instead. . Enable building React Native from source. Turning this on will significantly increase the build times. Default: `false` |
| buildToolsVersion(optional) | `string` | Override the default `buildToolsVersion` version number in **build.gradle**. |
| compileSdkVersion(optional) | `number` | Override the default `compileSdkVersion` version number in **build.gradle**. |
| enableBundleCompression(optional) | `boolean` | Enable JavaScript Bundle compression. Turning this on will result in a smaller APK size but may have slower app startup times. Default: `false`See: Faster App Startup |
| enableMinifyInReleaseBuilds(optional) | `boolean` | Enable [R8](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) in release builds to obfuscate Java code and reduce app size. |
| enablePngCrunchInReleaseBuilds(optional) | `boolean` | Enable [`crunchPngs`](https://developer.android.com/topic/performance/reduce-apk-size#crunch) in release builds to optimize PNG files. This property is enabled by default, but "might inflate PNG files that are already compressed", so you may want to disable it if you do your own PNG optimization. Default: `true` |
| enableShrinkResourcesInReleaseBuilds(optional) | `boolean` | Enable [`shrinkResources`](https://developer.android.com/studio/build/shrink-code#shrink-resources) in release builds to remove unused resources from the app. This property should be used in combination with `enableMinifyInReleaseBuilds`. |
| exclusiveMavenMirror(optional) | `string` | Specifies a single Maven repository to be used as an exclusive mirror for all dependency resolution. When set, all other Maven repositories will be ignored and only this repository will be used to fetch dependencies.See: Using a Maven Mirror |
| extraMavenRepos(optional) | (string | [AndroidMavenRepository](#androidmavenrepository))[] | Add extra maven repositories to all gradle projects. Takes an array of objects or strings. Strings are passed as the `url` property of the object with no credentials or authentication scheme. This adds the following code to **android/build.gradle**:

```groovy
allprojects {
 repositories {
  maven {
   url "https://foo.com/maven-releases"
 }
}
```

. By using an `AndroidMavenRepository` object, you can specify credentials and an authentication scheme.

```groovy
allprojects {
  repositories {
    maven {
      url "https://foo.com/maven-releases"
      credentials {
       username = "bar"
       password = "baz"
      }
      authentication {
       basic(BasicAuthentication)
      }
    }
  }
}
```

See: Gradle documentation |
| extraProguardRules(optional) | `string` | Append custom [Proguard rules](https://www.guardsquare.com/manual/configuration/usage) to **android/app/proguard-rules.pro**. |
| kotlinVersion(optional) | `string` | Override the Kotlin version used when building the app. |
| manifestQueries(optional) | [PluginConfigTypeAndroidQueries](#pluginconfigtypeandroidqueries) | Specifies the set of other apps that an app intends to interact with. These other apps are specified by package name, by intent signature, or by provider authority.See: Android documentation |
| minSdkVersion(optional) | `number` | Override the default `minSdkVersion` version number in **build.gradle**. |
| networkInspector(optional) | `boolean` | Enable the Network Inspector. Default: `true` |
| packagingOptions(optional) | [PluginConfigTypeAndroidPackagingOptions](#pluginconfigtypeandroidpackagingoptions) | Interface representing available configuration for Android Gradle plugin [`PackagingOptions`](https://developer.android.com/reference/tools/gradle-api/7.0/com/android/build/api/dsl/PackagingOptions). |
| targetSdkVersion(optional) | `number` | Override the default `targetSdkVersion` version number in **build.gradle**. |
| useDayNightTheme(optional) | `boolean` | Changes the apps theme to a DayNight variant to correctly support dark mode.See: Android documentation |
| useLegacyPackaging(optional) | `boolean` | Instructs the Android Gradle plugin to compress native libraries in the APK using the legacy packaging system. Default: `false`See: Android documentation |
| usesCleartextTraffic(optional) | `boolean` | Indicates whether the app intends to use cleartext network traffic. For Android 8 and below, the default platform-specific value is `true`. For Android 9 and above, the default platform-specific value is `false`.See: Android documentation |

### `PluginConfigTypeAndroidPackagingOptions`

Supported platforms: Android.

Interface representing available configuration for Android Gradle plugin [`PackagingOptions`](https://developer.android.com/reference/tools/gradle-api/7.0/com/android/build/api/dsl/PackagingOptions).

| Property | Type | Description |
| --- | --- | --- |
| doNotStrip(optional) | `string[]` | Array of patterns for native libraries that should not be stripped of debug symbols. |
| exclude(optional) | `string[]` | Array of patterns for native libraries that should be excluded from being packaged in the APK. |
| merge(optional) | `string[]` | Array of patterns for native libraries where all occurrences are concatenated and packaged in the APK. |
| pickFirst(optional) | `string[]` | Array of patterns for native libraries where only the first occurrence is packaged in the APK. |

### `PluginConfigTypeAndroidQueries`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| intent(optional) | [PluginConfigTypeAndroidQueriesIntent[]](#pluginconfigtypeandroidqueriesintent) | Specifies an intent filter signature. Your app can discover other apps that have matching `<intent-filter>` elements. These intents have restrictions compared to typical intent filter signatures.See: Android documentation for more information. |
| package(optional) | `string[]` | Specifies one or more apps that your app intends to access. These other apps might integrate with your app, or your app might use services that these other apps provide. |
| provider(optional) | `string[]` | Specifies one or more content provider authorities. Your app can discover other apps whose content providers use the specified authorities. There are some restrictions on the options that you can include in this `<provider>` element, compared to a typical `<provider>` manifest element. You may only specify the `android:authorities` attribute. |

### `PluginConfigTypeAndroidQueriesData`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| host(optional) | `string` | Specify a URI authority host that is handled |
| mimeType(optional) | `string` | Specify a MIME type that is handled |
| scheme(optional) | `string` | Specify a URI scheme that is handled |

### `PluginConfigTypeAndroidQueriesIntent`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| action(optional) | `string` | A string naming the action to perform. Usually one of the platform-defined values, such as `SEND` or `VIEW`.See: Android documentation for more information. |
| category(optional) | `string | string[]` | Provides an additional way to characterize the activity handling the intent, usually related to the user gesture or location from which it's started. |
| data(optional) | [PluginConfigTypeAndroidQueriesData](#pluginconfigtypeandroidqueriesdata) | A description of the data associated with the intent. |

### `PluginConfigTypeIos`

Supported platforms: iOS.

Extends: [SharedBuildConfigFields](#sharedbuildconfigfields)

Interface representing available configuration for iOS native build properties.

| Property | Type | Description |
| --- | --- | --- |
| ccacheEnabled(optional) | `boolean` | Enable C++ compiler cache for iOS builds. This speeds up compiling C++ code by caching the results of previous compilations.See: React Native's documentation on local caches and Ccache documentation. |
| deploymentTarget(optional) | `string` | Override the default iOS "Deployment Target" version in the following projects:
-   in CocoaPods projects,
-   `PBXNativeTarget` with "com.apple.product-type.application" `productType` in the app project.

 |
| extraPods(optional) | [ExtraIosPodDependency[]](#extraiospoddependency) | Add extra CocoaPods dependencies for all targets. This configuration is responsible for adding the new Pod entries to **ios/Podfile**. . Example. Creating entry in the configuration like below:

```json
[
  {
    name: "Protobuf",
    version: "~> 3.14.0",
  }
]
```

. Will produce the following entry in the generated **ios/Podfile**:

```ruby
pod 'Protobuf', '~> 3.14.0'
```

 |
| forceStaticLinking(optional) | `string[]` | List of CocoaPods that should be linked statically instead of as frameworks. This is only relevant when `use_frameworks!` is enabled. Some pods— especially React Native prebuilt binaries—can fail due to modular header issues when built as dynamic frameworks. Declaring them here ensures they are linked statically, avoiding those compatibility problems. This property is consumed by the `use_expo_modules` function in `expo-modules-autolinking`. |
| networkInspector(optional) | `boolean` | Enable the Network Inspector. Default: `true` |
| privacyManifestAggregationEnabled(optional) | `boolean` | Enable aggregation of Privacy Manifests (`PrivacyInfo.xcprivacy`) from CocoaPods resource bundles. If enabled, the manifests will be merged into a single file. If not enabled, developers will need to manually aggregate them.See: Privacy manifests guide and Apple's documentation on Privacy manifest files. |
| useFrameworks(optional) | `'static' | 'dynamic'` | Enable [`use_frameworks!`](https://guides.cocoapods.org/syntax/podfile.html#use_frameworks_bang) in `Podfile` to use frameworks instead of static libraries for Pods. |

### `SharedBuildConfigFields`

Supported platforms: Android, iOS, tvOS.

Shared build configuration fields that can be set at the top level or overridden per-platform. Platform-specific values take precedence.

| Property | Type | Description |
| --- | --- | --- |
| buildReactNativeFromSource(optional) | `boolean` | Enable building React Native from source. Turning this on will significantly increase the build times. On iOS, this controls support for precompiled React Native iOS dependencies (`ReactNativeDependencies.xcframework`). Setting this value to `true` will enable building React Native from source and disable the use of precompiled xcframeworks. This feature is available from React Native 0.80 and later when using the new architecture. From React Native 0.81, this setting will also control the use of a precompiled React Native Core (`React.xcframework`). Default: `false`See: Precompiled React Native for iOS: Faster builds are coming in 0.81 for more information. |
| reactNativeReleaseLevel(optional) | `'stable' | 'canary' | 'experimental'` | The React Native release level to use for the project. This can be used to enable different sets of internal React Native feature flags. Default: `'stable'` |
| useHermesV1(optional) | `boolean` | Enable the experimental Hermes V1 engine. In React Native 0.83, using Hermes V1 requires building React Native from source. You must set `buildReactNativeFromSource` to `true` when enabling this option. Default: `false` |

## Types

### `AndroidMavenRepositoryCredentials`

Supported platforms: Android.

Literal Type: `union`

Acceptable values are: [AndroidMavenRepositoryPasswordCredentials](#androidmavenrepositorypasswordcredentials) | [AndroidMavenRepositoryHttpHeaderCredentials](#androidmavenrepositoryhttpheadercredentials) | [AndroidMavenRepositoryAWSCredentials](#androidmavenrepositoryawscredentials)
