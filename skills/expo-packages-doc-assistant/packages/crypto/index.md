---
title: Crypto
description: A universal library for crypto operations.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-crypto'
packageName: 'expo-crypto'
iconUrl: '/static/images/packages/expo-crypto.png'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
---

# Expo Crypto

A universal library for crypto operations.
Android, iOS, tvOS, Web, Included in Expo Go

`expo-crypto` enables you to hash data in an equivalent manner to the Node.js core `crypto` API, and perform crypto operations such as AES encryption and decryption.

## Installation

```sh
npx expo install expo-crypto
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Usage

```jsx
import { useEffect } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import * as Crypto from 'expo-crypto';

export default function App() {
  useEffect(() => {
    (async () => {
      const digest = await Crypto.digestStringAsync(
        Crypto.CryptoDigestAlgorithm.SHA256,
        'GitHub stars are neat 🌟'
      );
      console.log('Digest: ', digest);
      /* Some crypto operation... */
    })();
  }, []);

  return (
    <View style={styles.container}>
      <Text>Crypto Module Example</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```

### AES encryption and decryption

```tsx
import { useEffect } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import { AESEncryptionKey, aesEncryptAsync, aesDecryptAsync } from 'expo-crypto';

export default function App() {
  useEffect(() => {
    (async () => {
      const plaintext = 'Hello, world!';
      const plaintextBase64 = btoa(plaintext);

      const encryptionKey = await AESEncryptionKey.generate();
      const sealedData = await aesEncryptAsync(plaintextBase64, key);
      const decryptedBase64 = await aesDecryptAsync(sealedData, key, {
        output: 'base64',
      });

      const decrypted = atob(decryptedBase64);
      console.log('Decrypted: ', decrypted);
    })();
  }, []);

  return (
    <View style={styles.container}>
      <Text>Crypto Module Example</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```

Encrypt data and save it to the file

```ts
import { AESEncryptionKey, aesEncryptAsync } from 'expo-crypto';
import { File, Paths } from 'expo-file-system';
import * as SecureStore from 'expo-secure-store';

async function encryptAndSaveData(plaintextData: Uint8Array) {
  // Generate encryption key
  const encryptionKey = await AESEncryptionKey.generate();

  // Encrypt data
  const sealedData = await aesEncryptAsync(plaintextData, encryptionKey);
  const encryptedBytes = await sealedData.combined();

  // Store encryption key
  const keyHex = await encryptionKey.encoded('hex');
  await SecureStore.setItemAsync('aes-encryption-key', keyHex);

  // Save encrypted file
  const file = new File(Paths.cache, 'encrypted.dat');
  file.create({ overwrite: true });
  file.write(encryptedBytes);
}
```
Load file and decrypt data

```ts
import { AESEncryptionKey, AESSealedData, aesDecryptAsync } from 'expo-crypto';
import { File, Paths } from 'expo-file-system';
import * as SecureStore from 'expo-secure-store';

async function loadAndDecryptData(): Promise<Uint8Array | null> {
  // Load encryption key
  const keyHex = await SecureStore.getItemAsync('aes-encryption-key');
  if (!keyHex) {
    return null;
  }
  const encryptionKey = await AESEncryptionKey.import(keyHex, 'hex');

  // Load encrypted file
  const file = new File(Paths.cache, 'encrypted.dat');
  if (!file.exists) {
    return null;
  }
  const encryptedBytes = await file.bytes();
  const sealedData = AESSealedData.fromCombined(encryptedBytes);

  // Decrypt data
  const plaintextBytes = await aesDecryptAsync(data, encryptionKey);
  return plaintextBytes;
}
```

## API

```js
import * as Crypto from 'expo-crypto';
```

## Classes

### `AESEncryptionKey`

Supported platforms: Android, iOS, tvOS, Web.

Type: Class extends `EncryptionKey`

Represents an AES encryption key that can be used for encryption and decryption operations. This class provides methods to generate, import, and export encryption keys.

AESEncryptionKey Properties

### `size`

Supported platforms: Android, iOS, tvOS, Web.

Type: [AESKeySize](#aeskeysize)

The size of the encryption key in bits (128, 192, or 256).

AESEncryptionKey Methods

### `bytes()`

Supported platforms: Android, iOS, tvOS, Web.

Retrieves the key as a byte array. Asynchronous due to the use of [`SubtleCrypto` `exportKey`](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/exportKey) API.

Returns: `Promise<uint8array</uint8array`

A promise that resolves to the byte array representation of the key.

### `encoded(encoding)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `encoding` | `'hex' | 'base64'` | The encoding format to use ('hex' or 'base64'). |

  

Retrieves the key encoded as a string in the specified format. Asynchronous due to the use of [`SubtleCrypto` `exportKey`](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/exportKey) API.

Returns: `Promise<string>`

A promise that resolves to the string representation of the key.

### `generate(size)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `size`(optional) | [AESKeySize](#aeskeysize) | The size of the key (128, 192, or 256). Defaults to 256. |

  

Generates a new AES encryption key of the specified size.

Returns: `Promise<encryptionkey>`

A promise that resolves to an EncryptionKey instance.

### `import(bytes)`

Supported platforms: Android, iOS, tvOS, Web.

Overload #1

| Parameter | Type | Description |
| --- | --- | --- |
| `bytes` | [Uint8Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) | The key as a byte array. |

  

Imports an encryption key from a byte array. Validates the size of the key.

Returns: `Promise<encryptionkey>`

A promise that resolves to an `EncryptionKey` instance.

### `import(hexString, encoding)`

Supported platforms: Android, iOS, tvOS, Web.

Overload #2

| Parameter | Type | Description |
| --- | --- | --- |
| `hexString` | `string` | The key as a string. |
| `encoding` | `'hex' | 'base64'` | The encoding used in the string ('hex' or 'base64'). |

  

Imports an encryption key from a string representation (hex or base64). Validates the size of the key.

Returns: `Promise<encryptionkey>`

A promise that resolves to an `EncryptionKey` instance.

### `AESSealedData`

Supported platforms: Android, iOS, tvOS, Web.

Type: Class extends `SealedData`

Represents encrypted data including the ciphertext, initialization vector, and authentication tag. This class provides methods to create sealed data from various formats and extract its components.

AESSealedData Properties

### `combinedSize`

Supported platforms: Android, iOS, tvOS, Web.

Read Only • Type: `number`

Total size of the combined data (IV + ciphertext + tag) in bytes.

### `ivSize`

Supported platforms: Android, iOS, tvOS, Web.

Read Only • Type: `number`

Size of the initialization vector in bytes.

### `tagSize`

Supported platforms: Android, iOS, tvOS, Web.

Read Only • Type: [GCMTagByteLength](#gcmtagbytelength)

Size of the authentication tag in bytes.

AESSealedData Methods

### `ciphertext(options)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `options` | `{ encoding: 'base64' | 'bytes', includeTag: boolean }` | Options controlling whether to include the authentication tag and output encoding. |

  

Retrieves the ciphertext from the sealed data.

Returns: `Promise<string>></string>`

The ciphertext as a `Uint8Array` or `base64` string depending on encoding option.

### `combined(encoding)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `encoding`(optional) | `'base64' | 'bytes'` | Output encoding format. Defaults to `bytes`. |

  

Retrieves a combined representation of the IV, ciphertext, and tag.

Returns: `Promise<string>></string>`

The combined data as a `Uint8Array` or `base64` string depending on encoding.

### `fromCombined(combined, config)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `combined` | [BinaryInput](#binaryinput) | The combined data array. When providing a string, it must be base64-encoded. |
| `config`(optional) | [AESSealedDataConfig](#aessealeddataconfig) | Configuration specifying IV and tag lengths. |

  

Static method. Creates a SealedData instance from a combined byte array, including the IV, ciphertext, and tag.

Returns: `AESSealedData`

A SealedData object.

### `fromParts(iv, ciphertext, tag)`

Supported platforms: Android, iOS, tvOS, Web.

Overload #1

| Parameter | Type | Description |
| --- | --- | --- |
| `iv` | [BinaryInput](#binaryinput) | The initialization vector. When providing a string, it must be base64-encoded. |
| `ciphertext` | [BinaryInput](#binaryinput) | The encrypted data. Should not include GCM tag. When providing a string, it must be base64-encoded. |
| `tag` | [BinaryInput](#binaryinput) | The authentication tag. When providing a string, it must be base64-encoded. |

  

Static method. Creates a SealedData instance from separate nonce, ciphertext, and optionally a tag.

Returns: `AESSealedData`

A SealedData object.

### `fromParts(iv, ciphertextWithTag, tagLength)`

Supported platforms: Android, iOS, tvOS, Web.

Overload #2

| Parameter | Type | Description |
| --- | --- | --- |
| `iv` | [BinaryInput](#binaryinput) | The initialization vector. When providing a string, it must be base64-encoded. |
| `ciphertextWithTag` | [BinaryInput](#binaryinput) | The encrypted data with GCM tag appended. When providing a string, it must be base64-encoded. |
| `tagLength`(optional) | `number` | Authentication tag length in bytes. Defaults to 16. |

  

Static method. Creates a SealedData instance from separate nonce, ciphertext, and optionally a tag.

Returns: `AESSealedData`

A SealedData object.

### `iv(encoding)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `encoding`(optional) | `'base64' | 'bytes'` | Output encoding format. Defaults to `bytes`. |

  

Retrieves the initialization vector (nonce) from the sealed data.

Returns: `Promise<string>></string>`

The initialization vector as a `Uint8Array` or `base64` string depending on encoding.

### `tag(encoding)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `encoding`(optional) | `'base64' | 'bytes'` | Output encoding format. Defaults to `bytes`. |

  

Retrieves the authentication tag from the sealed data.

Returns: `Promise<string>></string>`

The authentication tag as a `Uint8Array` or `base64` string depending on encoding.

## Methods

### `Crypto.aesDecryptAsync(sealedData, key, options)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `sealedData` | [AESSealedData](#aessealeddata) | The data to decrypt. |
| `key` | [AESEncryptionKey](#aesencryptionkey) | The key to use for decryption. |
| `options`(optional) | [AESDecryptOptions](#aesdecryptoptions) | Options for decryption, including output encoding and additional data. |

  

Decrypts the given sealed data using the specified key and options.

Returns: `Promise<string>></string>`

A promise that resolves to the decrypted data buffer or string, depending on encoding option.

### `Crypto.aesEncryptAsync(plaintext, key, options)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `plaintext` | [BinaryInput](#binaryinput) | The data to encrypt. When providing a string, it must be base64-encoded. |
| `key` | [AESEncryptionKey](#aesencryptionkey) | The encryption key to use. |
| `options`(optional) | [AESEncryptOptions](#aesencryptoptions) | Optional encryption parameters including nonce, tag length, and additional data. Default: `{}` |

  

Encrypts the given plaintext using AES-GCM with the specified key.

Returns: `Promise<aessealeddata>`

A promise that resolves to a SealedData instance containing the encrypted data.

### `Crypto.digest(algorithm, data)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `algorithm` | [CryptoDigestAlgorithm](#cryptodigestalgorithm) | The cryptographic hash function to use to transform a block of data into a fixed-size output. |
| `data` | `BufferSource` | The value that will be used to generate a digest. |

  

The `digest()` method of `Crypto` generates a digest of the supplied `TypedArray` of bytes `data` with the provided digest `algorithm`. A digest is a short fixed-length value derived from some variable-length input. **Cryptographic digests** should exhibit _collision-resistance_, meaning that it's very difficult to generate multiple inputs that have equal digest values. On web, this method can only be called from a secure origin (HTTPS) otherwise, an error will be thrown.

Returns: `Promise<arraybuffer>`

A Promise which fulfills with an ArrayBuffer representing the hashed input.

Example

```ts
const array = new Uint8Array([1, 2, 3, 4, 5]);
const digest = await Crypto.digest(Crypto.CryptoDigestAlgorithm.SHA512, array);
console.log('Your digest: ' + digest);
```

### `Crypto.digestStringAsync(algorithm, data, options)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `algorithm` | [CryptoDigestAlgorithm](#cryptodigestalgorithm) | The cryptographic hash function to use to transform a block of data into a fixed-size output. |
| `data` | `string` | The value that will be used to generate a digest. |
| `options`(optional) | [CryptoDigestOptions](#cryptodigestoptions) | Format of the digest string. Defaults to: `CryptoDigestOptions.HEX`. |

  

The `digestStringAsync()` method of `Crypto` generates a digest of the supplied `data` string with the provided digest `algorithm`. A digest is a short fixed-length value derived from some variable-length input. **Cryptographic digests** should exhibit _collision-resistance_, meaning that it's very difficult to generate multiple inputs that have equal digest values. You can specify the returned string format as one of `CryptoEncoding`. By default, the resolved value will be formatted as a `HEX` string. On web, this method can only be called from a secure origin (HTTPS) otherwise, an error will be thrown.

Returns: `Promise<string>`

Return a Promise which fulfills with a value representing the hashed input.

Example

```ts
const digest = await Crypto.digestStringAsync(
  Crypto.CryptoDigestAlgorithm.SHA512,
  '🥓 Easy to Digest! 💙'
);
```

### `Crypto.getRandomBytes(byteCount)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `byteCount` | `number` | A number within the range from `0` to `1024`. Anything else will throw a `TypeError`. |

  

Generates completely random bytes using native implementations. The `byteCount` property is a `number` indicating the number of bytes to generate in the form of a `Uint8Array`. Falls back to `Math.random` during development to prevent issues with React Native Debugger.

Returns: `Uint8Array`

An array of random bytes with the same length as the `byteCount`.

### `Crypto.getRandomBytesAsync(byteCount)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `byteCount` | `number` | A number within the range from `0` to `1024`. Anything else will throw a `TypeError`. |

  

Generates completely random bytes using native implementations. The `byteCount` property is a `number` indicating the number of bytes to generate in the form of a `Uint8Array`.

Returns: `Promise<uint8array</uint8array`

A promise that fulfills with an array of random bytes with the same length as the `byteCount`.

### `Crypto.getRandomValues(typedArray)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `typedArray` | `T` | An integer based [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) to fill with cryptographically secure random values. It modifies the input array in place. |

  

The `getRandomValues()` method of `Crypto` fills a provided `TypedArray` with cryptographically secure random values.

Returns: `T`

The input array filled with cryptographically secure random values.

Example

```ts
const byteArray = new Uint8Array(16);
Crypto.getRandomValues(byteArray);
console.log('Your lucky bytes: ' + byteArray);
```

### `Crypto.randomUUID()`

Supported platforms: Android, iOS, tvOS, Web.

The `randomUUID()` method returns a unique identifier based on the V4 UUID spec (RFC4122). It uses cryptographically secure random values to generate the UUID.

Returns: `string`

A string containing a newly generated UUIDv4 identifier

Example

```ts
const UUID = Crypto.randomUUID();
console.log('Your UUID: ' + UUID);
```

## Interfaces

### `AESDecryptOptions`

Supported platforms: Android, iOS, tvOS, Web.

Options for the decryption process.

| Property | Type | Description |
| --- | --- | --- |
| additionalData(optional) | [BinaryInput](#binaryinput) | Additional authenticated data (AAD) for GCM mode. When provided as a string, it must be base64-encoded. |
| output(optional) | `'base64' | 'bytes'` | Output format for the decrypted data. Default: `'bytes'` |

### `AESEncryptOptions`

Supported platforms: Android, iOS, tvOS, Web.

Options for the encryption process.

| Property | Type | Description |
| --- | --- | --- |
| additionalData(optional) | [BinaryInput](#binaryinput) | Additional authenticated data (AAD) for GCM mode. When provided as a string, it must be base64-encoded. |
| nonce(optional) | [GCMNonceParam](#gcmnonceparam) | Parameters for nonce generation. |
| tagLength(optional) | [GCMTagByteLength](#gcmtagbytelength) | Supported platforms: Android, Web. The length of the authentication tag in bytes. Note: On Apple, this option is ignored. The tag will always have 16 bytes. Default: `16` |

### `AESSealedDataConfig`

Supported platforms: Android, iOS, tvOS, Web.

Configuration for parsing sealed data from combined format.

| Property | Type | Description |
| --- | --- | --- |
| ivLength(optional) | `number` | The length of the initialization vector in bytes. Default: `12` |
| tagLength(optional) | [GCMTagByteLength](#gcmtagbytelength) | The length of the authentication tag in bytes. Default: `16` |

## Types

### `BinaryInput`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `union`

Represents binary input data that can be processed by AES APIs. When providing a string, it must be base64-encoded.

Acceptable values are: `string` | [Uint8Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) | [ArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)

### `CryptoDigestOptions`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| encoding | [CryptoEncoding](#cryptoencoding) | Format the digest is returned in. |

### `Digest`

Supported platforms: Android, iOS, tvOS, Web.

Type: `string`

### `GCMNonceParam`

Supported platforms: Android, iOS, tvOS, Web.

Configuration for the nonce (initialization vector) during encryption. Can specify either the byte length of the IV to generate or provide an IV directly.

Type: `object` shaped as below:

| Property | Type | Description |
| --- | --- | --- |
| length(optional) | `number` | Byte length of nonce to be generated. Default: `12` |

Or `object` shaped as below:

| Property | Type | Description |
| --- | --- | --- |
| bytes | [BinaryInput](#binaryinput) | Provided nonce bytes. |

### `GCMTagByteLength`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `number`

Byte length of the GCM authentication tag, is a security parameter. The AES-GCM specification recommends that it should be 16, 15, 14, 13, or 12 bytes, although 8 or 4 bytes may be acceptable in some applications. For additional guidance, see [Appendix C](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf) of the NIST Publication on "Recommendation for Block Cipher Modes of Operation".

Default and recommended value is 16. On Apple, the only supported value for encryption is 16.

Acceptable values are: `'16'` | `'15'` | `'14'` | `'13'` | `'12'` | `'8'` | `'4'`

## Enums

### `AESKeySize`

Supported platforms: Android, iOS, tvOS, Web.

AES key sizes in bits.

#### `AES128`

`AESKeySize.AES128 = 128`

128-bit AES key

#### `AES192`

Supported platforms: Android, Apple.

`AESKeySize.AES192 = 192`

192-bit AES key. It is unsupported on Web.

#### `AES256`

`AESKeySize.AES256 = 256`

256-bit AES key

### `CryptoDigestAlgorithm`

Supported platforms: Android, iOS, tvOS, Web.

[`Cryptographic hash function`](https://developer.mozilla.org/en-US/docs/Glossary/Cryptographic_hash_function)

#### `MD2`

Supported platforms: iOS.

`CryptoDigestAlgorithm.MD2 = "MD2"`

`128` bits.

#### `MD4`

Supported platforms: iOS.

`CryptoDigestAlgorithm.MD4 = "MD4"`

`128` bits.

#### `MD5`

Supported platforms: Android, iOS.

`CryptoDigestAlgorithm.MD5 = "MD5"`

`128` bits.

#### `SHA1`

`CryptoDigestAlgorithm.SHA1 = "SHA-1"`

`160` bits.

#### `SHA256`

`CryptoDigestAlgorithm.SHA256 = "SHA-256"`

`256` bits. Collision Resistant.

#### `SHA384`

`CryptoDigestAlgorithm.SHA384 = "SHA-384"`

`384` bits. Collision Resistant.

#### `SHA512`

`CryptoDigestAlgorithm.SHA512 = "SHA-512"`

`512` bits. Collision Resistant.

### `CryptoEncoding`

Supported platforms: Android, iOS, tvOS, Web.

#### `BASE64`

`CryptoEncoding.BASE64 = "base64"`

Has trailing padding. Does not wrap lines. Does not have a trailing newline.

#### `HEX`

`CryptoEncoding.HEX = "hex"`

## Error codes

| Code | Description |
| --- | --- |
| `ERR_CRYPTO_UNAVAILABLE` | **Web Only.** Access to the WebCrypto API is restricted to secure origins (localhost/https). |
| `ERR_CRYPTO_DIGEST` | An invalid encoding type provided. |
