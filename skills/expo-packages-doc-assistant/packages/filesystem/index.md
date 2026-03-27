---
title: FileSystem
description: A library that provides access to the local file system on the device.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-file-system'
packageName: 'expo-file-system'
iconUrl: '/static/images/packages/expo-file-system.png'
platforms: ['android', 'ios', 'tvos', 'expo-go']
---

# Expo FileSystem

A library that provides access to the local file system on the device.
Android, iOS, tvOS, Included in Expo Go

`expo-file-system` provides access to files and directories stored on a device or bundled as assets into the native project. It also allows downloading files from the network.

## Installation

```sh
npx expo install expo-file-system
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Configuration in app config

You can configure `expo-file-system` using its built-in [config plugin](/config-plugins/introduction) if you use config plugins in your project ([Continuous Native Generation (CNG)](/workflow/continuous-native-generation)). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect. If your app does **not** use CNG, then you'll need to manually configure the library.

### Example app.json with config plugin

```json
{
  "expo": {
    "plugins": [
      [
        "expo-file-system",
        {
          "supportsOpeningDocumentsInPlace": true,
          "enableFileSharing": true
        }
      ]
    ]
  }
}
```

### Configurable properties

| Name | Default | Description |
| --- | --- | --- |
| `supportsOpeningDocumentsInPlace` | `false` | Only for: iOS. A boolean to enable `LSSupportsOpeningDocumentsInPlace` in **Info.plist**. This allows the app to open documents in place. |
| `enableFileSharing` | `false` | Only for: iOS. A boolean to enable `UIFileSharingEnabled` in **Info.plist**. This enables file sharing in the iOS Files app, making the app's Documents directory accessible to users through the Files app, iTunes File Sharing, and other file management tools. |

Are you using this library in an existing React Native app?

If you're not using Continuous Native Generation ([CNG](/workflow/continuous-native-generation)) or you're using native **ios** project manually, then you need to add the `LSSupportsOpeningDocumentsInPlace` and `UIFileSharingEnabled` keys to your project's **ios/[app]/Info.plist**:

```xml
<key>LSSupportsOpeningDocumentsInPlace</key>
<true/>
<key>UIFileSharingEnabled</key>
<true/>
```

## Usage

```js
import { File, Directory, Paths } from 'expo-file-system';
```

The `File` and `Directory` instances hold a reference to a file, content, or asset URI.

The file or directory does not need to exist — an error will be thrown from the constructor only if the wrong class is used to represent an existing path (so if you try to create a `File` instance passing a path to an already existing directory).

## Features

-   Both synchronous and asynchronous, read and write access to file contents
-   Creation, modification and deletion
-   Available properties, such as `type`, `size`, `creationDate`, and more
-   Ability to read and write files as streams or using the `FileHandle` class
-   Easy file download/upload using `downloadFileAsync` or `expo/fetch`

## Examples

Writing and reading text files

```ts
import { File, Paths } from 'expo-file-system';

try {
  const file = new File(Paths.cache, 'example.txt');
  file.create(); // can throw an error if the file already exists or no permission to create it
  file.write('Hello, world!');
  console.log(file.textSync()); // Hello, world!
} catch (error) {
  console.error(error);
}
```
Picking files using system pickers

Usage with `expo-document-picker`:

```ts
import { File } from 'expo-file-system';
import * as DocumentPicker from 'expo-document-picker';

try {
  const result = await DocumentPicker.getDocumentAsync({ copyToCacheDirectory: true });
  if (!result.canceled) {
    const { uri } = result.assets[0];
    const file = new File(uri);
    console.log(file.textSync());
  }
} catch (error) {
  console.error(error);
}
```

Using the built-in `pickFileAsync` or `pickDirectoryAsync` method on Android:

```ts
import { File } from 'expo-file-system';

try {
  const file = new File.pickFileAsync();
  console.log(file.textSync());
} catch (error) {
  console.error(error);
}
```
Downloading files

Using `downloadFileAsync`:

```ts
import { Directory, File, Paths } from 'expo-file-system';

const url = 'https://pdfobject.com/pdf/sample.pdf';
const destination = new Directory(Paths.cache, 'pdfs');
try {
  destination.create();
  const output = await File.downloadFileAsync(url, destination);
  console.log(output.exists); // true
  console.log(output.uri); // path to the downloaded file, e.g., '${cacheDirectory}/pdfs/sample.pdf'
} catch (error) {
  console.error(error);
}
```

Or using `expo/fetch`:

```ts
import { fetch } from 'expo/fetch';
import { File, Paths } from 'expo-file-system';

const url = 'https://pdfobject.com/pdf/sample.pdf';
const response = await fetch(url);
const src = new File(Paths.cache, 'file.pdf');
src.write(await response.bytes());
```
Uploading files using `expo/fetch`

You can upload files as blobs directly with `fetch` built into the Expo package:

```ts
import { fetch } from 'expo/fetch';
import { File, Paths } from 'expo-file-system';

const file = new File(Paths.cache, 'file.txt');
file.write('Hello, world!');

const response = await fetch('https://example.com', {
  method: 'POST',
  body: file,
});
```

Or using the `FormData` constructor:

```ts
import { fetch } from 'expo/fetch';
import { File, Paths } from 'expo-file-system';

const file = new File(Paths.cache, 'file.txt');
file.write('Hello, world!');
const formData = new FormData();
formData.append('data', file);
const response = await fetch('https://example.com', {
  method: 'POST',
  body: formData,
});
```
Moving and copying files

```ts
import { Directory, File, Paths } from 'expo-file-system';
try {
  const file = new File(Paths.document, 'example.txt');
  file.create();
  console.log(file.uri); // '${documentDirectory}/example.txt'
  const copiedFile = new File(Paths.cache, 'example-copy.txt');
  file.copy(copiedFile);
  console.log(copiedFile.uri); // '${cacheDirectory}/example-copy.txt'
  file.move(Paths.cache);
  console.log(file.uri); // '${cacheDirectory}/example.txt'
  file.move(new Directory(Paths.cache, 'newFolder'));
  console.log(file.uri); // '${cacheDirectory}/newFolder/example.txt'
} catch (error) {
  console.error(error);
}
```
Using legacy FileSystem API

```ts
import * as FileSystem from 'expo-file-system/legacy';
import { File, Paths } from 'expo-file-system';

try {
  const file = new File(Paths.cache, 'example.txt');
  const content = await FileSystem.readAsStringAsync(file.uri);
  console.log(content);
} catch (error) {
  console.error(error);
}
```
Listing directory contents recursively

```ts
import { Directory, Paths } from 'expo-file-system';

function printDirectory(directory: Directory, indent: number = 0) {
  console.log(`${' '.repeat(indent)} + ${directory.name}`);
  const contents = directory.list();
  for (const item of contents) {
    if (item instanceof Directory) {
      printDirectory(item, indent + 2);
    } else {
      console.log(`${' '.repeat(indent + 2)} - ${item.name} (${item.size} bytes)`);
    }
  }
}

try {
  printDirectory(new Directory(Paths.cache));
} catch (error) {
  console.error(error);
}
```

## API

## Classes

### `Directory`

Supported platforms: Android, iOS, tvOS.

Type: Class extends `FileSystemDirectory`

Represents a directory on the filesystem.

A `Directory` instance can be created for any path, and does not need to exist on the filesystem during creation.

The constructor accepts an array of strings that are joined to create the directory URI. The first argument can also be a `Directory` instance (like `Paths.cache`).

Example

```ts
const directory = new Directory(Paths.cache, "subdirName");
```

Directory Properties

### `exists`

Supported platforms: Android, iOS, tvOS.

Type: `boolean`

A boolean representing if a directory exists and can be accessed.

### `size`

Supported platforms: Android, iOS, tvOS.

Literal type: `union`

A size of the directory in bytes. Null if the directory does not exist, or it cannot be read.

Acceptable values are: `number` | `null`

### `uri`

Supported platforms: Android, iOS, tvOS.

Read Only • Type: `string`

Represents the directory URI. The field is read-only, but it may change as a result of calling some methods such as `move`.

### `name`

Supported platforms: Android, iOS, tvOS.

Type: `string`

Directory name.

### `parentDirectory`

Supported platforms: Android, iOS, tvOS.

Type: [Directory](#directory)

Directory containing the file.

Directory Methods

### `copy(destination)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `destination` | [Directory](#directory) | [File](#file) |

  

Copies a directory.

Returns: `void`

### `create(options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `options`(optional) | [DirectoryCreateOptions](#directorycreateoptions) |

  

Creates a directory that the current uri points to.

Returns: `void`

### `createDirectory(name)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `name` | `string` |

  

Returns: `Directory`

### `createFile(name, mimeType)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `name` | `string` |
| `mimeType` | `string | null` |

  

Returns: `File`

### `delete()`

Supported platforms: Android, iOS, tvOS.

Deletes a directory. Also deletes all files and directories inside the directory.

Returns: `void`

### `info()`

Supported platforms: Android, iOS, tvOS.

Retrieves an object containing properties of a directory.

Returns: `DirectoryInfo`

An object with directory metadata (for example, size, creation date, and so on).

### `list()`

Supported platforms: Android, iOS, tvOS.

Lists the contents of a directory. Calling this method if the parent directory does not exist will throw an error.

Returns: `(File | Directory)[]`

An array of `Directory` and `File` instances.

### `move(destination)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `destination` | [Directory](#directory) | [File](#file) |

  

Moves a directory. Updates the `uri` property that now points to the new location.

Returns: `void`

### `rename(newName)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `newName` | `string` |

  

Renames a directory.

Returns: `void`

### `File`

Supported platforms: Android, iOS, tvOS.

Type: Class extends `FileSystemFile` implements [Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob)

Represents a file on the filesystem.

A `File` instance can be created for any path, and does not need to exist on the filesystem during creation.

The constructor accepts an array of strings that are joined to create the file URI. The first argument can also be a `Directory` instance (like `Paths.cache`) or a `File` instance (which creates a new reference to the same file).

Example

```ts
const file = new File(Paths.cache, "subdirName", "file.txt");
```

File Properties

### `contentUri`

Supported platforms: Android.

Type: `string`

A content URI to the file that can be shared to external applications.

### `creationTime`

Supported platforms: Android, iOS, tvOS.

Literal type: `union`

A creation time of the file expressed in milliseconds since epoch. Returns null if the file does not exist, cannot be read or the Android version is earlier than API 26.

Acceptable values are: `number` | `null`

### `exists`

Supported platforms: Android, iOS, tvOS.

Type: `boolean`

A boolean representing if a file exists. `true` if the file exists, `false` otherwise. Also, `false` if the application does not have read access to the file.

### `md5`

Supported platforms: Android, iOS, tvOS.

Literal type: `union`

A md5 hash of the file. Null if the file does not exist, or it cannot be read.

Acceptable values are: `string` | `null`

### `modificationTime`

Supported platforms: Android, iOS, tvOS.

Literal type: `union`

A last modification time of the file expressed in milliseconds since epoch. Returns a Null if the file does not exist, or it cannot be read.

Acceptable values are: `number` | `null`

### `size`

Supported platforms: Android, iOS, tvOS.

Type: `number`

A size of the file in bytes. 0 if the file does not exist, or it cannot be read.

### `type`

Supported platforms: Android, iOS, tvOS.

Type: `string`

A mime type of the file. An empty string if the file does not exist, or it cannot be read.

### `uri`

Supported platforms: Android, iOS, tvOS.

Read Only • Type: `string`

Represents the file URI. The field is read-only, but it may change as a result of calling some methods such as `move`.

### `extension`

Supported platforms: Android, iOS, tvOS.

Type: `string`

File extension.

Example

`'.png'`

### `name`

Supported platforms: Android, iOS, tvOS.

Type: `string`

File name. Includes the extension.

### `parentDirectory`

Supported platforms: Android, iOS, tvOS.

Type: [Directory](#directory)

Directory containing the file.

File Methods

### `arrayBuffer()`

Supported platforms: Android, iOS, tvOS.

The **`arrayBuffer()`** method of the Blob interface returns a Promise that resolves with the contents of the blob as binary data contained in an ArrayBuffer.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Blob/arrayBuffer)

Returns: `Promise<arraybuffer>`

### `base64()`

Supported platforms: Android, iOS, tvOS.

Retrieves content of the file as base64.

Returns: `Promise<string>`

A promise that resolves with the contents of the file as a base64 string.

### `base64Sync()`

Supported platforms: Android, iOS, tvOS.

Retrieves content of the file as base64.

Returns: `string`

The contents of the file as a base64 string.

### `bytes()`

Supported platforms: Android, iOS, tvOS.

Retrieves byte content of the entire file.

Returns: `Promise<uint8array</uint8array`

A promise that resolves with the contents of the file as a `Uint8Array`.

### `bytesSync()`

Supported platforms: Android, iOS, tvOS.

Retrieves byte content of the entire file.

Returns: `Uint8Array`

The contents of the file as a `Uint8Array`.

### `copy(destination)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `destination` | [Directory](#directory) | [File](#file) |

  

Copies a file.

Returns: `void`

### `create(options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `options`(optional) | [FileCreateOptions](#filecreateoptions) |

  

Creates a file.

Returns: `void`

### `delete()`

Supported platforms: Android, iOS, tvOS.

Deletes a file.

Returns: `void`

### `info(options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `options`(optional) | [InfoOptions](#infooptions) |

  

Retrieves an object containing properties of a file

Returns: `FileInfo`

An object with file metadata (for example, size, creation date, and so on).

### `move(destination)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `destination` | [Directory](#directory) | [File](#file) |

  

Moves a directory. Updates the `uri` property that now points to the new location.

Returns: `void`

### `open()`

Supported platforms: Android, iOS, tvOS.

Returns A `FileHandle` object that can be used to read and write data to the file.

Returns: `FileHandle`

### `readableStream()`

Supported platforms: Android, iOS, tvOS.

Returns: `ReadableStream<uint8array</uint8array`

### `rename(newName)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `newName` | `string` |

  

Renames a file.

Returns: `void`

### `slice(start, end, contentType)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `start`(optional) | `number` |
| `end`(optional) | `number` |
| `contentType`(optional) | `string` |

  

The **`slice()`** method of the Blob interface creates and returns a new `Blob` object which contains data from a subset of the blob on which it's called.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Blob/slice)

Returns: `Blob`

### `stream()`

Supported platforms: Android, iOS, tvOS.

The **`stream()`** method of the Blob interface returns a ReadableStream which upon reading returns the data contained within the `Blob`.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Blob/stream)

Returns: `ReadableStream<uint8array</uint8array`

### `text()`

Supported platforms: Android, iOS, tvOS.

Retrieves text from the file.

Returns: `Promise<string>`

A promise that resolves with the contents of the file as string.

### `textSync()`

Supported platforms: Android, iOS, tvOS.

Retrieves text from the file.

Returns: `string`

The contents of the file as string.

### `writableStream()`

Supported platforms: Android, iOS, tvOS.

Returns: `WritableStream<uint8array</uint8array`

### `write(content, options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `content` | string | [Uint8Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)<ArrayBufferLike\> | The content to write into the file. |
| `options`(optional) | `FileWriteOptions` | - |

  

Writes content to the file.

Returns: `void`

### `Paths`

Supported platforms: Android, iOS, tvOS.

Type: Class extends `PathUtilities`

Paths Properties

### `appleSharedContainers`

Supported platforms: Android, iOS, tvOS.

Type: Record<string, [Directory](#directory)\>

### `availableDiskSpace`

Supported platforms: Android, iOS, tvOS.

Type: `number`

A property that represents the available space on device's internal storage, represented in bytes.

### `bundle`

Supported platforms: Android, iOS, tvOS.

Type: [Directory](#directory)

A property containing the bundle directory – the directory where assets bundled with the application are stored.

### `cache`

Supported platforms: Android, iOS, tvOS.

Type: [Directory](#directory)

A property containing the cache directory – a place to store files that can be deleted by the system when the device runs low on storage.

### `document`

Supported platforms: Android, iOS, tvOS.

Type: [Directory](#directory)

A property containing the document directory – a place to store files that are safe from being deleted by the system.

### `totalDiskSpace`

Supported platforms: Android, iOS, tvOS.

Type: `number`

A property that represents the total space on device's internal storage, represented in bytes.

Paths Methods

### `basename(path, ext)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | string | [File](#file) | [Directory](#directory) | The path to get the base name from. |
| `ext`(optional) | `string` | An optional file extension. |

  

Returns the base name of a path.

Returns: `string`

A string representing the base name.

### `dirname(path)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | string | [File](#file) | [Directory](#directory) | The path to get the directory name from. |

  

Returns the directory name of a path.

Returns: `string`

A string representing the directory name.

### `extname(path)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | string | [File](#file) | [Directory](#directory) | The path to get the extension from. |

  

Returns the extension of a path.

Returns: `string`

A string representing the extension.

### `info(...uris)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `. .uris` | `string[]` |

  

Returns an object that indicates if the specified path represents a directory.

Returns: `PathInfo`

### `isAbsolute(path)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | string | [File](#file) | [Directory](#directory) | The path to check. |

  

Checks if a path is absolute.

Returns: `boolean`

`true` if the path is absolute, `false` otherwise.

### `join(...paths)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `. .paths` | (string | [File](#file) | [Directory](#directory))[] | An array of path segments. |

  

Joins path segments into a single path.

Returns: `string`

A string representing the joined path.

### `normalize(path)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | string | [File](#file) | [Directory](#directory) | The path to normalize. |

  

Normalizes a path.

Returns: `string`

A string representing the normalized path.

### `parse(path)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | string | [File](#file) | [Directory](#directory) | The path to parse. |

  

Parses a path into its components.

Returns: `{ base: string, dir: string, ext: string, name: string, root: string }`

An object containing the parsed path components.

### `relative(from, to)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `from` | string | [File](#file) | [Directory](#directory) | The base path. |
| `to` | string | [File](#file) | [Directory](#directory) | The relative path. |

  

Resolves a relative path to an absolute path.

Returns: `string`

A string representing the resolved path.

### `FileHandle`

Supported platforms: Android, iOS, tvOS.

FileHandle Properties

### `offset`

Supported platforms: Android, iOS, tvOS.

Literal type: `union`

A property that indicates the current byte offset in the file. Calling `readBytes` or `writeBytes` will read or write a specified amount of bytes starting from this offset. The offset is incremented by the number of bytes read or written. The offset can be set to any value within the file size. If the offset is set to a value greater than the file size, the next write operation will append data to the end of the file. Null if the file handle is closed.

Acceptable values are: `number` | `null`

### `size`

Supported platforms: Android, iOS, tvOS.

Literal type: `union`

A size of the file in bytes or `null` if the file handle is closed.

Acceptable values are: `number` | `null`

FileHandle Methods

### `close()`

Supported platforms: Android, iOS, tvOS.

Closes the file handle. This allows the file to be deleted, moved or read by a different process. Subsequent calls to `readBytes` or `writeBytes` will throw an error.

Returns: `void`

### `readBytes(length)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `length` | `number` | The number of bytes to read. |

  

Reads the specified amount of bytes from the file at the current offset. Max amount of bytes read at once is capped by ArrayBuffer max size (32 bit signed MAX_INT on Android and 64 bit on iOS), but you can read from a FileHandle multiple times.

Returns: `Uint8Array<arraybuffer>`

### `writeBytes(bytes)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `bytes` | [Uint8Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) | A `Uint8Array` array containing bytes to write. |

  

Writes the specified bytes to the file at the current offset.

Returns: `void`

## Methods

> **Deprecated:** Use `new File().copy()` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.copyAsync(options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `options` | `RelocatingOptions` |

  

Returns: `Promise<void>`

> **Deprecated:** Import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.createDownloadResumable(uri, fileUri, options, callback, resumeData)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `uri` | `string` |
| `fileUri` | `string` |
| `options`(optional) | [DownloadOptions](#downloadoptions) |
| `callback`(optional) | `FileSystemNetworkTaskProgressCallback<DownloadProgressData>` |
| `resumeData`(optional) | `string` |

  

Returns: `any`

> **Deprecated:** Import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.createUploadTask(url, fileUri, options, callback)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `url` | `string` |
| `fileUri` | `string` |
| `options`(optional) | `FileSystemUploadOptions` |
| `callback`(optional) | `FileSystemNetworkTaskProgressCallback<UploadProgressData>` |

  

Returns: `any`

> **Deprecated:** Use `new File().delete()` or `new Directory().delete()` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.deleteAsync(fileUri, options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `fileUri` | `string` |
| `options`(optional) | `DeletingOptions` |

  

Returns: `Promise<void>`

> **Deprecated**

### `FileSystem.deleteLegacyDocumentDirectoryAndroid()`

Supported platforms: Android, iOS, tvOS.

Returns: `Promise<void>`

> **Deprecated:** Use `File.downloadFileAsync` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.downloadAsync(uri, fileUri, options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `uri` | `string` |
| `fileUri` | `string` |
| `options`(optional) | [DownloadOptions](#downloadoptions) |

  

Returns: `Promise<filesystemdownloadresult>`

> **Deprecated:** Import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.getContentUriAsync(fileUri)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `fileUri` | `string` |

  

Returns: `Promise<string>`

> **Deprecated:** Use `Paths.availableDiskSpace` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.getFreeDiskStorageAsync()`

Supported platforms: Android, iOS, tvOS.

Returns: `Promise<number>`

> **Deprecated:** Use `new File().info` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.getInfoAsync(fileUri, options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `fileUri` | `string` |
| `options`(optional) | [InfoOptions](#infooptions) |

  

Returns: `Promise<fileinfo>`

> **Deprecated:** Use `Paths.totalDiskSpace` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.getTotalDiskCapacityAsync()`

Supported platforms: Android, iOS, tvOS.

Returns: `Promise<number>`

> **Deprecated:** Use `new Directory().create()` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.makeDirectoryAsync(fileUri, options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `fileUri` | `string` |
| `options`(optional) | `MakeDirectoryOptions` |

  

Returns: `Promise<void>`

> **Deprecated:** Use `new File().move()` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.moveAsync(options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `options` | `RelocatingOptions` |

  

Returns: `Promise<void>`

> **Deprecated:** Use `new File().text()` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.readAsStringAsync(fileUri, options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `fileUri` | `string` |
| `options`(optional) | `ReadingOptions` |

  

Returns: `Promise<string>`

> **Deprecated:** Use `new Directory().list()` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.readDirectoryAsync(fileUri)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `fileUri` | `string` |

  

Returns: `Promise<string[]>`

> **Deprecated:** Use `@expo/fetch` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.uploadAsync(url, fileUri, options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `url` | `string` |
| `fileUri` | `string` |
| `options`(optional) | `FileSystemUploadOptions` |

  

Returns: `Promise<filesystemuploadresult>`

> **Deprecated:** Use `new File().write()` or import this method from `expo-file-system/legacy`. This method will throw in runtime.

### `FileSystem.writeAsStringAsync(fileUri, contents, options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `fileUri` | `string` |
| `contents` | `string` |
| `options`(optional) | `WritingOptions` |

  

Returns: `Promise<void>`

## Types

### `DirectoryCreateOptions`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| idempotent(optional) | `boolean` | This flag controls whether the `create` operation is idempotent (safe to call multiple times without error). If `true`, creating a file or directory that already exists will succeed silently. If `false`, an error will be thrown when the target already exists. Default: `false` |
| intermediates(optional) | `boolean` | Whether to create intermediate directories if they do not exist. Default: `false` |
| overwrite(optional) | `boolean` | Whether to overwrite the directory if it exists. Default: `false` |

### `DirectoryInfo`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| creationTime(optional) | `number` | A creation time of the directory expressed in milliseconds since epoch. Returns null if the Android version is earlier than API 26. |
| exists | `boolean` | Indicates whether the directory exists. |
| files(optional) | `string[]` | A list of file names contained within a directory. |
| modificationTime(optional) | `number` | The last modification time of the directory expressed in milliseconds since epoch. |
| size(optional) | `number` | The size of the file in bytes. |
| uri(optional) | `string` | A `file://` URI pointing to the directory. |

### `DownloadOptions`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| headers(optional) | `undefined` | The headers to send with the request. |
| idempotent(optional) | `boolean` | This flag controls whether the `download` operation is idempotent (safe to call multiple times without error). If `true`, downloading a file that already exists overwrites the previous one. If `false`, an error is thrown when the target file already exists. Default: `false` |

### `FileCreateOptions`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| intermediates(optional) | `boolean` | Whether to create intermediate directories if they do not exist. Default: `false` |
| overwrite(optional) | `boolean` | Whether to overwrite the file if it exists. Default: `false` |

### `FileInfo`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| creationTime(optional) | `number` | A creation time of the file expressed in milliseconds since epoch. Returns null if the Android version is earlier than API 26. |
| exists | `boolean` | Indicates whether the file exists. |
| md5(optional) | `string` | Present if the `md5` option was truthy. Contains the MD5 hash of the file. |
| modificationTime(optional) | `number` | The last modification time of the file expressed in milliseconds since epoch. |
| size(optional) | `number` | The size of the file in bytes. |
| uri(optional) | `string` | A URI pointing to the file. This is the same as the `fileUri` input parameter and preserves its scheme (for example, `file://` or `content://`). |

### `InfoOptions`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| md5(optional) | `boolean` | Whether to return the MD5 hash of the file. Default: `false` |

### `PathInfo`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| exists | `boolean` | Indicates whether the path exists. Returns true if it exists; false if the path does not exist or if there is no read permission. |
| isDirectory | `boolean | null` | Indicates whether the path is a directory. Returns true or false if the path exists; otherwise, returns null. |
