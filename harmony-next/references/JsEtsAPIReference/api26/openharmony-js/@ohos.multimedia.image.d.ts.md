# @ohos.multimedia.image.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2022 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @file
 * @kit ImageKit
 */
import { AsyncCallback } from './@ohos.base';
import type colorSpaceManager from './@ohos.graphics.colorSpaceManager';
import type resourceManager from './@ohos.resourceManager';
import type rpc from './@ohos.rpc';
/**
 * # SVG Tags
 *
 * The SVG tags are supported since API version 10. The used version is (SVG) 1.1, and the width and height of the SVG
 * tag must be set. An XML declaration can be added to an SVG file and start with **<?xml**. The following tags are
 * supported:
 *
 * - a
 * - circle
 * - clipPath
 * - defs
 * - ellipse
 * - feBlend
 * - feColorMatrix
 * - feComposite
 * - feDiffuseLighting
 * - feDisplacementMap
 * - feDistantLight
 * - feFlood
 * - feGaussianBlur
 * - feImage
 * - feMorphology
 * - feOffset
 * - fePointLight
 * - feSpecularLighting
 * - feSpotLight
 * - feTurbulence
 * - filter
 * - g
 * - image
 * - line
 * - linearGradient
 * - mask
 * - path
 * - pattern
 * - polygon
 * - polyline
 * - radialGradient
 * - rect
 * - stop
 * - svg
 * - text
 * - textPath
 * - tspan
 * - use
 */
/**
 * The module provides capabilities for image decoding, encoding, editing, metadata processing, and image receiving.
 * This module contains the following classes:
 *
 * - [ImageSource]{@link @ohos.multimedia.image:image.ImageSource}: provides the capabilities of obtaining
 * [image information]{@link @ohos.multimedia.image:image.ImageInfo}, decoding images to PixelMaps or Pictures, and
 * reading and modifying [image properties]{@link @ohos.multimedia.image:image.PropertyKey}.
 * [Supported image formats for decoding]{@link @ohos.multimedia.image: image.ImageSource#supportedFormats}
 * include png, jpeg, bmp, gif, webp, dng, and heic<sup>12+</sup>.
 * - [ImagePacker]{@link @ohos.multimedia.image:image.ImagePacker}: provides the capability of encoding images into
 * compressed data streams or files. Encoding requires the ImageSource, PixelMap, or Picture of an image as the input.
 * [Supported image formats for encoding]{@link @ohos.multimedia.image: image.ImagePacker#supportedFormats}
 * include jpeg, webp, png, heic<sup>12+</sup>, and gif<sup>18+</sup>.
 * - [PixelMap]{@link @ohos.multimedia.image:image.PixelMap}: contains pixel data and
 * [image information]{@link @ohos.multimedia.image:image.ImageInfo}. It can be used for reading/writing pixel data and
 * performing operations such as cropping, scaling, translating, rotating, and mirroring. It can also be directly passed
 * to the [Image component]{@link Image} for display. Additionally, it provides APIs for
 * obtaining and setting the color gamut and HDR metadata of images.
 * - [Picture]{@link @ohos.multimedia.image:image.Picture}: a multi-picture object composed of a main picture,
 * auxiliary pictures, and metadata. The main picture contains the primary image information; auxiliary pictures store
 * additional information related to the main picture; metadata stores other information related to the image.
 * Picture provides methods for obtaining the main picture, compositing HDR images, obtaining and setting auxiliary
 * pictures, and obtaining and setting metadata.
 * - [AuxiliaryPicture]{@link @ohos.multimedia.image:image.AuxiliaryPicture}: used to display special information
 * alongside the main picture, enriching the overall content of the image. The supported types of auxiliary pictures
 * can be found in [AuxiliaryPictureType]{@link @ohos.multimedia.image:image.AuxiliaryPictureType}.
 * - [Metadata]{@link @ohos.multimedia.image:image.Metadata}: used to store image metadata. The supported metadata types
 * can be found in [MetadataType]{@link @ohos.multimedia.image:image.MetadataType}. It includes Exif metadata and
 * watermark cropping metadata, both stored in Key-Value pairs. The keys for Exif metadata can be found in
 * [PropertyKey]{@link @ohos.multimedia.image:image.PropertyKey}, and the keys for watermark cropping metadata can be
 * found in [FragmentPropertyKey]{@link @ohos.multimedia.image:image.FragmentMapPropertyKey}.
 * - [ImageReceiver]{@link @ohos.multimedia.image:image.ImageReceiver}: acts as a consumer of images, used for receiving
 * and reading images from a surface.
 * - [ImageCreator]{@link @ohos.multimedia.image:image.ImageCreator}: acts as a producer of images, used for writing
 * images into a surface.
 * - [Image]{@link @ohos.multimedia.image:image.Image}: used by ImageReceiver and ImageCreator for transferring image
 * objects, with the actual content determined by the producer. For example, the Image object provided by
 * a camera preview stream contains YUV data, whereas the Image object provided by a camera photo contains a JPEG file.
 *
 * @syscap SystemCapability.Multimedia.Image.Core
 * @crossplatform [since 11]
 * @form [since 12]
 * @atomicservice [since 11]
 * @since 6
 */
declare namespace image {
    /**
     * Enumerates the pixel formats of images.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 7
     */
    enum PixelMapFormat {
        /**
         * Unknown format.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        UNKNOWN = 0,
        /**
         * Indicates that each pixel is stored on 32 bits. Each pixel contains 4 components：R(8bits), G(8bits),
         * B(8bits), A(8bits) and are stored from the higher-order to the lower-order bits.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 18
         */
        ARGB_8888 = 1,
        /**
         * The color information consists of three components: R (Red), G (Green), and B (Blue), which occupies five bits,
         * six bits, and five bits, respectively. The total length is 16 bits.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        RGB_565 = 2,
        /**
         * The color information consists of four components: R (Red), G (Green), B (Blue), and alpha. Each component
         * occupies 8 bits, and the total length is 32 bits. It corresponds to
         * [CAMERA_FORMAT_RGBA_8888 in CameraFormat]{@link @ohos.multimedia.camera:camera.CameraFormat}.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        RGBA_8888 = 3,
        /**
         * The color information consists of four components: B (Blue), G (Green), R (Red), and alpha. Each component
         * occupies 8 bits, and the total length is 32 bits.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        BGRA_8888 = 4,
        /**
         * The color information consists of three components: R (Red), G (Green), and B (Blue). Each component occupies 8
         * bits, and the total length is 24 bits.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        RGB_888 = 5,
        /**
         * The color information consists of only the alpha component, which occupies eight bits. Each row of pixels is
         * composed of one or more pixels, and the data for each row is aligned to 4 bytes. If the byte count of a row is
         * not a multiple of 4, blank bytes are padded at the end to ensure proper alignment.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        ALPHA_8 = 6,
        /**
         * The color information consists of four components: R (Red), G (Green), B (Blue), and alpha. Each component
         * occupies 16 bits, and the total length is 64 bits.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        RGBA_F16 = 7,
        /**
         * YVU pixel arrangement, where the V component precedes the U component. The color information consists of the
         * luminance component Y and the interleaved chrominance components V and U. The Y component occupies 8 bits, and
         * the UV components occupy 4 bits on average due to 4:2:0 sampling. The total length is 12 bits on average. It
         * corresponds to [CAMERA_FORMAT_YUV_420_SP in CameraFormat]{@link @ohos.multimedia.camera:camera.CameraFormat}.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        NV21 = 8,
        /**
         * YUV pixel arrangement, where the U component precedes the V component. The color information consists of the
         * luminance component Y and the interleaved chrominance components U and V. The Y component occupies 8 bits, and
         * the UV components occupy 4 bits on average due to 4:2:0 sampling. The total length is 12 bits on average.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        NV12 = 9,
        /**
         * The color information consists of four components: R (Red), G (Green), B (Blue), and alpha. R, G, and B each
         * occupy 10 bits, and alpha occupies 2 bits. The total length is 32 bits.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        RGBA_1010102 = 10,
        /**
         * The color information consists of the luminance component Y and the chrominance components Cb and Cr. Each
         * component has effective 10 bits. In storage, the Y plane uses 16 bits per pixel (10 of which are effective). The
         * UV plane is interleaved, with every four pixels taking up 32 bits of data (each chrominance component having 10
         * effective bits), resulting in an average of 15 effective bits overall. It corresponds to
         * [CAMERA_FORMAT_YCBCR_P010 in CameraFormat]{@link @ohos.multimedia.camera:camera.CameraFormat}.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        YCBCR_P010 = 11,
        /**
         * The color information consists of the luminance component Y and the chrominance components Cr and Cb. Each
         * component has effective 10 bits. In storage, the Y plane uses 16 bits per pixel (10 of which are effective). The
         * UV plane is interleaved, with every four pixels taking up 32 bits of data (each chrominance component having 10
         * effective bits), resulting in an average of 15 effective bits overall. It corresponds to
         * [CAMERA_FORMAT_YCRCB_P010 in CameraFormat]{@link @ohos.multimedia.camera:camera.CameraFormat}.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        YCRCB_P010 = 12,
        /**
         * Indicates that each pixel is stored on 8 bits, a YUV planar format comprised of Y plane only.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        Y8 = 14,
        /**
         * Indicates that each pixel is stored on 8 bits, without 4-byte stride alignment.
         * Each pixel contains 1 component: ALPHA(8bits) and is stored from the higher-order to the lower-order bits.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @since 26.0.0
         */
        ALPHA_U8 = 15,
        /**
         * Indicates that each pixel is stored on 16 bits.
         * Each pixel contains 1 component: ALPHA(16bits) and is stored from the higher-order to the lower-order bits in
         * FP16.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @since 26.0.0
         */
        ALPHA_F16 = 16,
        /**
         * The storage format is ASTC 4x4 format, and the memory usage is only 1/4 of RGBA_8888.
         * This format is only used for direct display scenes and does not support pixel access or post-
         * processing editing.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 18
         */
        ASTC_4x4 = 102
    }
    /**
     * Describes the size of an image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 6
     */
    interface Size {
        /**
         * Height
         *
         * Unit:px.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 6
         */
        height: number;
        /**
         * Width
         *
         * Unit:px.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 6
         */
        width: number;
    }
    /**
     * Enumerates the types of Exchangeable Image File Format (Exif) data of an image.
     *
     * - The key in the format example is **image.PropertyKey.*XXX*** (where *XXX* is the name of an enumeration name, for
     * example, **image.PropertyKey.NEW_SUBFILE_TYPE**).
     * - The format example is used only to show how to modify values and read results. For details about how to use them,
     * see
     * [modifyImageProperty]{@link @ohos.multimedia.image:image.ImageSource.modifyImageProperty(key: PropertyKey, value: string)}
     * (to modify a single Exif field),
     * [modifyImageProperties]{@link @ohos.multimedia.image:image.ImageSource.modifyImageProperties(records: Record<PropertyKey, string|null>)}
     * (to modify multiple Exif fields),
     * [getImageProperty]{@link @ohos.multimedia.image:image.ImageSource.getImageProperty(key: PropertyKey, options?: ImagePropertyOptions)}
     * (to read a single Exif field), and
     * [getImageProperties]{@link @ohos.multimedia.image:image.ImageSource.getImageProperties(key: Array<PropertyKey>)} (
     * to read multiple Exif fields).
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @since 7
     */
    enum PropertyKey {
        /**
         * Number of bits per sample. For example, for RGB, which has three components, the format is 8,8,8.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 7
         */
        BITS_PER_SAMPLE = 'BitsPerSample',
        /**
         * Image orientation.
         *
         * 1: **Top-left**: The image is not rotated.
         *
         * 2: **Top-right**: The image is flipped horizontally.
         *
         * 3: **Bottom-right**: The image is rotated by 180°.
         *
         * 4: **Bottom-left**: The image is flipped vertically.
         *
         * 5: **Left-top**: The image is flipped horizontally and then rotated clockwise by 270°.
         *
         * 6: **Right-top**: The image is rotated clockwise by 90°.
         *
         * 7: **Right-bottom**: The image is vertically flipped and then rotated clockwise by 90°.
         *
         * 8: **Left-bottom**: The image is rotated clockwise by 270°.
         *
         * If an undefined value x is read, **Unknown Value x** is returned. The value of the property obtained is returned
         * as a string. When modifying the property, you can specify the property either in the form of a number or a
         * string.
         *
         * For details about the image rotation angle, see
         * [Obtaining the Rotation Angle of an Image](docroot://media/image/image-faqs/image-rotate-faq.md).
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 7
         */
        ORIENTATION = 'Orientation',
        /**
         * Image length.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 7
         */
        IMAGE_LENGTH = 'ImageLength',
        /**
         * Image width.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 7
         */
        IMAGE_WIDTH = 'ImageWidth',
        /**
         * Image latitude. The value must be in the format of degree,minute,second, for example, 39,54,7.542.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 7
         */
        GPS_LATITUDE = 'GPSLatitude',
        /**
         * Image longitude. The value must be in the format of degree,minute,second, for example, 116,19,42.16.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 7
         */
        GPS_LONGITUDE = 'GPSLongitude',
        /**
         * Latitude reference (Northern or Southern Hemisphere) of the image capture location.
         *
         * 78: "North".
         *
         * 83: "South".
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 7
         */
        GPS_LATITUDE_REF = 'GPSLatitudeRef',
        /**
         * Longitude reference (Eastern or Western Hemisphere) of the image capture location.
         *
         * 69: "East".
         *
         * 87: "West".
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 7
         */
        GPS_LONGITUDE_REF = 'GPSLongitudeRef',
        /**
         * Time when the original image data was generated, for example, 2022:09:06 15:48:00.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 9
         */
        DATE_TIME_ORIGINAL = 'DateTimeOriginal',
        /**
         * Exposure time, for example, 1/33 seconds.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 9
         */
        EXPOSURE_TIME = 'ExposureTime',
        /**
         * Type of the scene, for example, portrait, scenery, motion, and night.
         *
         * 1: "Directly photographed", indicating that the image is directly captured by the image sensor.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 9
         */
        SCENE_TYPE = 'SceneType',
        /**
         * ISO sensitivity or ISO speed, for example, 400.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 9
         */
        ISO_SPEED_RATINGS = 'ISOSpeedRatings',
        /**
         * F number, for example, f/1.8.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @since 9
         */
        F_NUMBER = 'FNumber',
        /**
         * Date and time of image creation.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        DATE_TIME = 'DateTime',
        /**
         * GPS timestamp.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        GPS_TIME_STAMP = 'GPSTimeStamp',
        /**
         * GPS date stamp.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        GPS_DATE_STAMP = 'GPSDateStamp',
        /**
         * Image description.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        IMAGE_DESCRIPTION = 'ImageDescription',
        /**
         * Manufacturer.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        MAKE = 'Make',
        /**
         * Device model.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        MODEL = 'Model',
        /**
         * Photographing mode.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        PHOTO_MODE = 'PhotoMode',
        /**
         * Sensitivity type.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        SENSITIVITY_TYPE = 'SensitivityType',
        /**
         * Standard output sensitivity.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        STANDARD_OUTPUT_SENSITIVITY = 'StandardOutputSensitivity',
        /**
         * Recommended exposure index.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        RECOMMENDED_EXPOSURE_INDEX = 'RecommendedExposureIndex',
        /**
         * ISO speed.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        ISO_SPEED = 'ISOSpeedRatings',
        /**
         * Lens aperture. An example in the correct format is 4/1.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        APERTURE_VALUE = 'ApertureValue',
        /**
         * Exposure bias.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        EXPOSURE_BIAS_VALUE = 'ExposureBiasValue',
        /**
         * Metering mode.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        METERING_MODE = 'MeteringMode',
        /**
         * Light source. An example value is **Fluorescent**.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        LIGHT_SOURCE = 'LightSource',
        /**
         * Flash status.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        FLASH = 'Flash',
        /**
         * Focal length of the lens.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        FOCAL_LENGTH = 'FocalLength',
        /**
         * User comments.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        USER_COMMENT = 'UserComment',
        /**
         * Pixel X dimension.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        PIXEL_X_DIMENSION = 'PixelXDimension',
        /**
         * Pixel Y dimension.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        PIXEL_Y_DIMENSION = 'PixelYDimension',
        /**
         * White balance.
         *
         * 0: "Auto white balance."
         *
         * 1: "Manual white balance."
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        WHITE_BALANCE = 'WhiteBalance',
        /**
         * Focal length in 35mm film.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        FOCAL_LENGTH_IN_35_MM_FILM = 'FocalLengthIn35mmFilm',
        /**
         * Capture mode.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        CAPTURE_MODE = 'HwMnoteCaptureMode',
        /**
         * Physical aperture.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        PHYSICAL_APERTURE = 'HwMnotePhysicalAperture',
        /**
         * Roll angle.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        ROLL_ANGLE = 'HwMnoteRollAngle',
        /**
         * Pitch angle.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        PITCH_ANGLE = 'HwMnotePitchAngle',
        /**
         * Photographing scene: food.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        SCENE_FOOD_CONF = 'HwMnoteSceneFoodConf',
        /**
         * Photographing scene: stage.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        SCENE_STAGE_CONF = 'HwMnoteSceneStageConf',
        /**
         * Photographing scene: blue sky.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        SCENE_BLUE_SKY_CONF = 'HwMnoteSceneBlueSkyConf',
        /**
         * Photographing scene: green plant.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        SCENE_GREEN_PLANT_CONF = 'HwMnoteSceneGreenPlantConf',
        /**
         * Photographing scene: beach.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        SCENE_BEACH_CONF = 'HwMnoteSceneBeachConf',
        /**
         * Photographing scene: snow.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        SCENE_SNOW_CONF = 'HwMnoteSceneSnowConf',
        /**
         * Photographing scene: sunset.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        SCENE_SUNSET_CONF = 'HwMnoteSceneSunsetConf',
        /**
         * Photographing scene: flowers.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        SCENE_FLOWERS_CONF = 'HwMnoteSceneFlowersConf',
        /**
         * Photographing scene: night.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        SCENE_NIGHT_CONF = 'HwMnoteSceneNightConf',
        /**
         * Photographing scene: text.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        SCENE_TEXT_CONF = 'HwMnoteSceneTextConf',
        /**
         * Number of faces.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        FACE_COUNT = 'HwMnoteFaceCount',
        /**
         * Focus mode.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        FOCUS_MODE = 'HwMnoteFocusMode',
        /**
         * Compression scheme used on the image data.
         *
         * 1: "Uncompressed".
         *
         * 2: "CCITT RLE".
         *
         * 3: "T4/Group 3 Fax".
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        COMPRESSION = 'Compression',
        /**
         * Color space of the image data, for example, RGB or YCbCr.
         *
         * 0: "Reversed mono".
         *
         * 1: "Normal mono".
         *
         * 2: "RGB".
         *
         * 3: "Palette".
         *
         * 5: "CMYK".
         *
         * 6: "YCbCr".
         *
         * 8: "CieLAB".
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        PHOTOMETRIC_INTERPRETATION = 'PhotometricInterpretation',
        /**
         * Byte offset of each strip.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        STRIP_OFFSETS = 'StripOffsets',
        /**
         * Number of components per pixel. The value is **3** for RGB and YCbCr images. The **JPEG** key is used in JPEG
         * compressed data.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SAMPLES_PER_PIXEL = 'SamplesPerPixel',
        /**
         * Number of rows per strip.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        ROWS_PER_STRIP = 'RowsPerStrip',
        /**
         * Number of bytes in each strip after compression.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        STRIP_BYTE_COUNTS = 'StripByteCounts',
        /**
         * Number of pixels per ResolutionUnit in the image width (X) direction.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        X_RESOLUTION = 'XResolution',
        /**
         * Number of pixels per ResolutionUnit in the image height (Y) direction.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        Y_RESOLUTION = 'YResolution',
        /**
         * Storage format of components of each pixel, which can be chunky or planar.
         *
         * 1: "Chunky format": chunky format.
         *
         * 2: "Planar format": planar format.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        PLANAR_CONFIGURATION = 'PlanarConfiguration',
        /**
         * Unit of measurement for XResolution and YResolution, in inches or centimeters.
         *
         * 2: "Inch": measured in inches.
         *
         * 3: "Centimeter": measured in centimeters.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        RESOLUTION_UNIT = 'ResolutionUnit',
        /**
         * Transfer function for the image, which is usually used for color correction.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        TRANSFER_FUNCTION = 'TransferFunction',
        /**
         * Name and version number of the software used to create the image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SOFTWARE = 'Software',
        /**
         * Person who created the image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        ARTIST = 'Artist',
        /**
         * Chromaticity coordinates of the white point, the reference for "white", in the color space of the image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        WHITE_POINT = 'WhitePoint',
        /**
         * Chromaticities of the primaries of the image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        PRIMARY_CHROMATICITIES = 'PrimaryChromaticities',
        /**
         * Coefficients for the conversion matrix that transforms image data from RGB to YCbCr.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        YCBCR_COEFFICIENTS = 'YCbCrCoefficients',
        /**
         * Subsampling factors used for the chrominance components of a YCbCr image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        YCBCR_SUB_SAMPLING = 'YCbCrSubSampling',
        /**
         * Positioning of subsampled chrominance components relative to luminance samples.
         *
         * 1: "Centered": Cb/Cr chrominance components are centered relative to the luminance pixels (common practice).
         *
         * 2: "Co-sited": Cb/Cr and Y sampling points align at the top-left corner.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        YCBCR_POSITIONING = 'YCbCrPositioning',
        /**
         * Reference values for black and white points.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        REFERENCE_BLACK_WHITE = 'ReferenceBlackWhite',
        /**
         * Copyright notice of the image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        COPYRIGHT = 'Copyright',
        /**
         * Offset of the SOI marker of a JPEG interchange format bitstream.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        JPEG_INTERCHANGE_FORMAT = 'JPEGInterchangeFormat',
        /**
         * Number of bytes of the JPEG stream.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        JPEG_INTERCHANGE_FORMAT_LENGTH = 'JPEGInterchangeFormatLength',
        /**
         * Class of the program used by the camera to set exposure when the image was captured.
         *
         * 0: "Not defined".
         *
         * 1: "Manual".
         *
         * 2: "Normal program".
         *
         * 3: "Aperture priority".
         *
         * 4: "Shutter priority".
         *
         * 5: "Creative program (biased toward depth of field)".
         *
         * 6: "Creative program (biased toward fast shutter speed)".
         *
         * 7: "Portrait mode (for closeup photos with the background out of focus)".
         *
         * 8: "Landscape mode (for landscape photos with the background in focus)".
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        EXPOSURE_PROGRAM = 'ExposureProgram',
        /**
         * Spectral sensitivity of each channel of the camera.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SPECTRAL_SENSITIVITY = 'SpectralSensitivity',
        /**
         * Opto-Electric Conversion Function (OECF) specified in ISO 14524.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        OECF = 'OECF',
        /**
         * Version of the supported Exif standard.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        EXIF_VERSION = 'ExifVersion',
        /**
         * Date and time when the image was stored as digital data, in the format of YYYY:MM:DD HH:mm:ss.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        DATE_TIME_DIGITIZED = 'DateTimeDigitized',
        /**
         * Specific information about compressed data.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        COMPONENTS_CONFIGURATION = 'ComponentsConfiguration',
        /**
         * Shutter speed, expressed in Additive System of Photographic Exposure (APEX) values.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SHUTTER_SPEED = 'ShutterSpeedValue',
        /**
         * Value of brightness, expressed in APEX values.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        BRIGHTNESS_VALUE = 'BrightnessValue',
        /**
         * Smallest F number of the lens.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        MAX_APERTURE_VALUE = 'MaxApertureValue',
        /**
         * Distance to the subject, in meters.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SUBJECT_DISTANCE = 'SubjectDistance',
        /**
         * Location and area of the main subject in the entire scene.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SUBJECT_AREA = 'SubjectArea',
        /**
         * Marker used by Exif/DCF manufacturers to record any required information.
         *
         * This field is read-only in API versions 12 to 19 and is readable and writable in API version 20 and later.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        MAKER_NOTE = 'MakerNote',
        /**
         * Tag used to record fractions of seconds for the **DateTime** tag.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SUBSEC_TIME = 'SubsecTime',
        /**
         * Tag used to record fractions of seconds for the **DateTimeOriginal** tag.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SUBSEC_TIME_ORIGINAL = 'SubsecTimeOriginal',
        /**
         * Tag used to record fractions of seconds for the **DateTimeDigitized** tag.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SUBSEC_TIME_DIGITIZED = 'SubsecTimeDigitized',
        /**
         * FlashPix format version supported by an FPXR file. It is used to enhance device compatibility.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FLASHPIX_VERSION = 'FlashpixVersion',
        /**
         * Color space information, which is usually recorded as a color space specifier.
         *
         * 1: "sRGB", indicating the standard sRGB color space. It is the typical default value.
         *
         * 2: "Adobe RGB", indicating the Adobe RGB color space. It is not formally defined in Exif, but commonly used in
         * practice.
         *
         * 0xffff: "Uncalibrated", indicating that the color space is uncalibrated and unknown.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        COLOR_SPACE = 'ColorSpace',
        /**
         * Name of an audio file related to the image data.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        RELATED_SOUND_FILE = 'RelatedSoundFile',
        /**
         * Strobe energy at the time the image was captured, in Beam Candle Power Seconds (BCPS).
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FLASH_ENERGY = 'FlashEnergy',
        /**
         * Spatial frequency table of the camera or input device.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SPATIAL_FREQUENCY_RESPONSE = 'SpatialFrequencyResponse',
        /**
         * Number of pixels in the image width (X) direction per FocalPlaneResolutionUnit.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FOCAL_PLANE_X_RESOLUTION = 'FocalPlaneXResolution',
        /**
         * Number of pixels in the image height (Y) direction per FocalPlaneResolutionUnit.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FOCAL_PLANE_Y_RESOLUTION = 'FocalPlaneYResolution',
        /**
         * Unit for measuring FocalPlaneXResolution and FocalPlaneYResolution.
         *
         * 2: "Inch": measured in inches.
         *
         * 3: "Centimeter": measured in centimeters.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FOCAL_PLANE_RESOLUTION_UNIT = 'FocalPlaneResolutionUnit',
        /**
         * Location of the main subject relative to the left edge.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SUBJECT_LOCATION = 'SubjectLocation',
        /**
         * Exposure index selected at the time the image is captured.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        EXPOSURE_INDEX = 'ExposureIndex',
        /**
         * Type of the image sensor on the camera.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SENSING_METHOD = 'SensingMethod',
        /**
         * Image source.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FILE_SOURCE = 'FileSource',
        /**
         * Color Filter Array (CFA) geometric pattern of the image sensor.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        CFA_PATTERN = 'CFAPattern',
        /**
         * Special processing on image data.
         *
         * 0: "Normal process", indicating normal processing (no custom rendering).
         *
         * 1: "Custom process", indicating custom processing (such as artistic effect, beauty, and HDR).
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        CUSTOM_RENDERED = 'CustomRendered',
        /**
         * Exposure mode set when the image was captured.
         *
         * 0: "Auto exposure."
         *
         * 1: "Manual exposure."
         *
         * 2: "Auto bracket."
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        EXPOSURE_MODE = 'ExposureMode',
        /**
         * Digital zoom ratio when the image was captured.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        DIGITAL_ZOOM_RATIO = 'DigitalZoomRatio',
        /**
         * Type of the scene that was captured.
         *
         * 0: "Standard."
         *
         * 1: "Landscape."
         *
         * 2: "Portrait."
         *
         * 3: "Night scene."
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SCENE_CAPTURE_TYPE = 'SceneCaptureType',
        /**
         * Degree of overall image gain adjustment.
         *
         * 0: "Normal", no gain control.
         *
         * 1: "Low gain up."
         *
         * 2: "High gain up."
         *
         * 3: "Low gain down."
         *
         * 4: "High gain down."
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GAIN_CONTROL = 'GainControl',
        /**
         * Direction of contrast processing used by the camera.
         *
         * 0: "Normal", normal contrast.
         *
         * 1: "Soft", soft contrast.
         *
         * 2: "Hard", hard contrast.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        CONTRAST = 'Contrast',
        /**
         * Direction of saturation processing used by the camera.
         *
         * 0:"Normal": normal saturation.
         *
         * 1: "Low saturation."
         *
         * 2: "High saturation."
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SATURATION = 'Saturation',
        /**
         * Direction of sharpness processing used by the camera.
         *
         * 0:"Normal": normal sharpness.
         *
         * 1: "Soft."
         *
         * 2: "Hard."
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SHARPNESS = 'Sharpness',
        /**
         * Information about the photographing conditions of a specific camera model.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        DEVICE_SETTING_DESCRIPTION = 'DeviceSettingDescription',
        /**
         * Distance to the subject.
         *
         * 0: "Unknown."
         *
         * 1: "Macro."
         *
         * 2: "Close view."
         *
         * 3: "Distant view."
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SUBJECT_DISTANCE_RANGE = 'SubjectDistanceRange',
        /**
         * Unique identifier assigned to each image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        IMAGE_UNIQUE_ID = 'ImageUniqueID',
        /**
         * GPS information version.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_VERSION_ID = 'GPSVersionID',
        /**
         * Whether the latitude is north or south latitude.
         *
         * 0: Sea level, which is above sea level.
         *
         * 1: "Sea level reference," which is below the sea level.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_ALTITUDE_REF = 'GPSAltitudeRef',
        /**
         * Altitude based on the reference in GPSAltitudeRef.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_ALTITUDE = 'GPSAltitude',
        /**
         * GPS satellites used for measurement.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_SATELLITES = 'GPSSatellites',
        /**
         * Status of the GPS receiver when the image was recorded.
         *
         * 'A': "Measurement in progress", GPS is working, satellite signals are locked, and location data is trustworthy.
         *
         * 'V': "Measurement interrupted", GPS is not working, current positioning is unavailable, and location data may be
         * missing or incorrect.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_STATUS = 'GPSStatus',
        /**
         * GPS measurement pmode. Whether the 2D (planar) or 3D (with height) measurement mode is used for GPS positioning.
         *
         * 2: "2-dimensional measurement", (latitude+longitude).
         *
         * 3: "3-dimensional measurement", (latitude + longitude + height).
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_MEASURE_MODE = 'GPSMeasureMode',
        /**
         * GPS Dilution of Precision (DOP), which reflects the precision of GPS measurements taken when the photo was
         * captured.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_DOP = 'GPSDOP',
        /**
         * Unit used to express the movement speed of the GPS receiver.
         *
         * 'K': "km/h".
         *
         * 'M': "mph".
         *
         * 'N': "knots".
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_SPEED_REF = 'GPSSpeedRef',
        /**
         * Movement speed of the GPS receiver.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_SPEED = 'GPSSpeed',
        /**
         * Which type of "North" is used as the reference for the direction angle.
         *
         * 'T': "True direction", which is the geographic North Pole direction. This is the standard used for maps and
         * navigation systems.
         *
         * 'M': "Magnetic direction", which is the direction pointed to by the Earth's magnetic field. Note that magnetic
         * declination varies by location and changes over time.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_TRACK_REF = 'GPSTrackRef',
        /**
         * Movement direction of the GPS receiver. Direction of movement (heading) of the camera at the moment the photo was
         * taken, measured in degrees.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_TRACK = 'GPSTrack',
        /**
         * Reference of the direction of the image when it was captured.
         *
         * 'T': "True direction", which is the geographic North Pole direction. This is the standard used for maps and
         * navigation systems.
         *
         * 'M': "Magnetic direction", which is the direction pointed to by the Earth's magnetic field. Note that magnetic
         * declination varies by location and changes over time.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_IMG_DIRECTION_REF = 'GPSImgDirectionRef',
        /**
         * Direction of the image when it was captured.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_IMG_DIRECTION = 'GPSImgDirection',
        /**
         * Geodetic survey data used by the GPS receiver.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_MAP_DATUM = 'GPSMapDatum',
        /**
         * Whether the latitude of the destination point is north or south latitude.
         *
         * 78: "North".
         *
         * 83: "South".
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_DEST_LATITUDE_REF = 'GPSDestLatitudeRef',
        /**
         * Latitude of the destination point.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_DEST_LATITUDE = 'GPSDestLatitude',
        /**
         * Whether the longitude of the destination point is east or west longitude.
         *
         * 69: "East".
         *
         * 87: "West".
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_DEST_LONGITUDE_REF = 'GPSDestLongitudeRef',
        /**
         * Longitude of the destination point.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_DEST_LONGITUDE = 'GPSDestLongitude',
        /**
         * Reference of the bearing to the destination point.
         *
         * 'T': "True direction", which is the geographic North Pole direction. This is the standard used for maps and
         * navigation systems.
         *
         * 'M': "Magnetic direction", which is the direction pointed to by the Earth's magnetic field. Note that magnetic
         * declination varies by location and changes over time.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_DEST_BEARING_REF = 'GPSDestBearingRef',
        /**
         * Bearing to the destination point.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_DEST_BEARING = 'GPSDestBearing',
        /**
         * Unit used to express the distance to the destination point.
         *
         * 'K': "km."
         *
         * 'M': "miles."
         *
         * 'N': "nautical miles."
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_DEST_DISTANCE_REF = 'GPSDestDistanceRef',
        /**
         * Distance to the destination point.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_DEST_DISTANCE = 'GPSDestDistance',
        /**
         * String that records the name of the method used for positioning.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_PROCESSING_METHOD = 'GPSProcessingMethod',
        /**
         * String that records the name of the GPS area.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_AREA_INFORMATION = 'GPSAreaInformation',
        /**
         * Whether differential correction is applied to the GPS receiver. It is critical to accurate location accuracy.
         *
         * 0: "Without correction", which indicates that no differential correction is used.
         *
         * 1:"Correction applied", which indicates that differential correction is used.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_DIFFERENTIAL = 'GPSDifferential',
        /**
         * Serial number of the camera body.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        BODY_SERIAL_NUMBER = 'BodySerialNumber',
        /**
         * Name of the camera owner.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        CAMERA_OWNER_NAME = 'CameraOwnerName',
        /**
         * Whether the image is a composite image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        COMPOSITE_IMAGE = 'CompositeImage',
        /**
         * Number of bits per pixel. It is specific to compressed data.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        COMPRESSED_BITS_PER_PIXEL = 'CompressedBitsPerPixel',
        /**
         * DNG version. It encodes the DNG 4-tier version number.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        DNG_VERSION = 'DNGVersion',
        /**
         * Size of the final image area, in raw image coordinates, taking into account extra pixels around the edges of the
         * final image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        DEFAULT_CROP_SIZE = 'DefaultCropSize',
        /**
         * Gamma value.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GAMMA = 'Gamma',
        /**
         * ISO speed latitude yyy value of the camera or input device, which is defined in ISO 12232.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        ISO_SPEED_LATITUDE_YYY = 'ISOSpeedLatitudeyyy',
        /**
         * ISO speed latitude zzz value of the camera or input device, which is defined in ISO 12232.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        ISO_SPEED_LATITUDE_ZZZ = 'ISOSpeedLatitudezzz',
        /**
         * Manufacturer of the lens.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        LENS_MAKE = 'LensMake',
        /**
         * Model of the lens.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        LENS_MODEL = 'LensModel',
        /**
         * Serial number of the lens.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        LENS_SERIAL_NUMBER = 'LensSerialNumber',
        /**
         * Specifications of the lens.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        LENS_SPECIFICATION = 'LensSpecification',
        /**
         * Data type of a subfile, such as a full-resolution image, a thumbnail, or a part of a multi-frame image. The value
         * is a bit mask. The value 0 indicates a full-resolution image, **1** indicates a thumbnail, and **2** indicates a
         * part of a multi-frame image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        NEW_SUBFILE_TYPE = 'NewSubfileType',
        /**
         * Time with an offset from UTC when the image was captured.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        OFFSET_TIME = 'OffsetTime',
        /**
         * Time with an offset from UTC when the image was digitized. It helps to accurately adjust the timestamp.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        OFFSET_TIME_DIGITIZED = 'OffsetTimeDigitized',
        /**
         * Time with an offset from UTC when the original image was created. It is critical for time-sensitive applications.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        OFFSET_TIME_ORIGINAL = 'OffsetTimeOriginal',
        /**
         * Exposure time of source images of the composite image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SOURCE_EXPOSURE_TIMES_OF_COMPOSITE_IMAGE = 'SourceExposureTimesOfCompositeImage',
        /**
         * Number of source images of the composite image.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SOURCE_IMAGE_NUMBER_OF_COMPOSITE_IMAGE = 'SourceImageNumberOfCompositeImage',
        /**
         * Type of data contained in this subfile. This tag has been deprecated. Use **NewSubfileType** instead.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SUBFILE_TYPE = 'SubfileType',
        /**
         * Horizontal positioning error, in meters.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GPS_H_POSITIONING_ERROR = 'GPSHPositioningError',
        /**
         * ISO sensitivity (ISO speed) used when the image was captured. It is the recommended field in Exif 2.3 and later.
         * The earlier field, ISOSpeedRatings (Tag 0x8827), has the same data type and meaning. However, if both fields are
         * present, the **PhotographicSensitivity** value should be used.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        PHOTOGRAPHIC_SENSITIVITY = 'PhotographicSensitivity',
        /**
         * Number of burst shooting times.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        BURST_NUMBER = 'HwMnoteBurstNumber',
        /**
         * Face confidence.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FACE_CONF = 'HwMnoteFaceConf',
        /**
         * Left eye centered.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FACE_LEYE_CENTER = 'HwMnoteFaceLeyeCenter',
        /**
         * Mouth centered.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FACE_MOUTH_CENTER = 'HwMnoteFaceMouthCenter',
        /**
         * Face pointer.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FACE_POINTER = 'HwMnoteFacePointer',
        /**
         * Face rectangle.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FACE_RECT = 'HwMnoteFaceRect',
        /**
         * Right eye centered.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FACE_REYE_CENTER = 'HwMnoteFaceReyeCenter',
        /**
         * Smile score of for faces.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FACE_SMILE_SCORE = 'HwMnoteFaceSmileScore',
        /**
         * Facial recognition algorithm version.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FACE_VERSION = 'HwMnoteFaceVersion',
        /**
         * Whether the front camera is used to take a selfie.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        FRONT_CAMERA = 'HwMnoteFrontCamera',
        /**
         * Pointer to the scene.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SCENE_POINTER = 'HwMnoteScenePointer',
        /**
         * Scene algorithm version.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        SCENE_VERSION = 'HwMnoteSceneVersion',
        /**
         * Whether XMAGE is supported.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        IS_XMAGE_SUPPORTED = 'HwMnoteIsXmageSupported',
        /**
         * XMAGE watermark mode.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        XMAGE_MODE = 'HwMnoteXmageMode',
        /**
         * X1 coordinate of the watermark region.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        XMAGE_LEFT = 'HwMnoteXmageLeft',
        /**
         * Y1 coordinate of the watermark region.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        XMAGE_TOP = 'HwMnoteXmageTop',
        /**
         * X2 coordinate of the watermark region.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        XMAGE_RIGHT = 'HwMnoteXmageRight',
        /**
         * Y2 coordinate of the watermark region.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        XMAGE_BOTTOM = 'HwMnoteXmageBottom',
        /**
         * Cloud enhancement mode.
         *
         * **Read/Write capability**: readable and writable.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        CLOUD_ENHANCEMENT_MODE = 'HwMnoteCloudEnhancementMode',
        /**
         * Motion snapshot mode.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        WIND_SNAPSHOT_MODE = 'HwMnoteWindSnapshotMode',
        /**
         * Number of GIF loops. The value **0** means an infinite loop, and other values means the number of loops.
         *
         * **Read/Write capability**: read-only
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        GIF_LOOP_COUNT = 'GIFLoopCount'
    }
    /**
     * Enumerates the image formats.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 9
     */
    enum ImageFormat {
        /**
         * YCBCR422 semi-planar format.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        YCBCR_422_SP = 1000,
        /**
         * JPEG encoding format.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        JPEG = 2000
    }
    /**
     * Enumerates the alpha types of images.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    enum AlphaType {
        /**
         * Unknown alpha type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        UNKNOWN = 0,
        /**
         * There is no alpha or the image is opaque.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        OPAQUE = 1,
        /**
         * Premultiplied alpha.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        PREMUL = 2,
        /**
         * RGB non-premultiplied alpha.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        UNPREMUL = 3
    }
    /**
     * Enumerates the desired dynamic range of an image during decoding.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 12
     */
    enum DecodingDynamicRange {
        /**
         * The image is decoded based on the format. If the image is in HDR format, it is decoded based on the HDR content;
         * otherwise, it is decoded based on the SDR content. The image source created by calling
         * [CreateIncrementalSource]{@link @ohos.multimedia.image:image.CreateIncrementalSource(buf: ArrayBuffer)} is
         * decoded into SDR content.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        AUTO = 0,
        /**
         * The image is decoded according to the standard dynamic range.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        SDR = 1,
        /**
         * The image is decoded according to the high dynamic range. The image source created by calling
         * [CreateIncrementalSource]{@link @ohos.multimedia.image:image.CreateIncrementalSource(buf: ArrayBuffer)} is
         * decoded into SDR content.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        HDR = 2
    }
    /**
     * Enumerates the desired dynamic range of an image during encoding.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 12
     */
    enum PackingDynamicRange {
        /**
         * Adaptive. The [pixelmap]{@link @ohos.multimedia.image:image.PixelMap} is encoded based on the format. If the
         * PixelMap is in HDR format, it is encoded based on the HDR content; otherwise, it is encoded based on the SDR
         * content.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        AUTO = 0,
        /**
         * The image is decoded according to the standard dynamic range.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        SDR = 1
    }
    /**
     * Enumerates the anti-aliasing levels.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @atomicservice [since 14]
     * @since 12
     */
    enum AntiAliasingLevel {
        /**
         * Nearest neighbor interpolation.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @atomicservice [since 14]
         * @since 12
         */
        NONE = 0,
        /**
         * Bilinear interpolation.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @atomicservice [since 14]
         * @since 12
         */
        LOW = 1,
        /**
         * Bilinear interpolation with mipmap enabled. You are advised to use this value when zooming out an image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @atomicservice [since 14]
         * @since 12
         */
        MEDIUM = 2,
        /**
         * Cubic interpolation.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @atomicservice [since 14]
         * @since 12
         */
        HIGH = 3
    }
    /**
     * Enumerates the scale modes of images.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    enum ScaleMode {
        /**
         * Reduces the image size to the dimensions of the target.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        FIT_TARGET_SIZE = 0,
        /**
         * Scales the image so that it fills the requested bounds of the target and crops the extra.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        CENTER_CROP = 1
    }
    /**
     * Enumerates the color component types of images.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageReceiver
     * @since 9
     */
    enum ComponentType {
        /**
         * Luminance component.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        YUV_Y = 1,
        /**
         * Chrominance component.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        YUV_U = 2,
        /**
         * Chrominance component.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        YUV_V = 3,
        /**
         * JPEG type.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        JPEG = 4
    }
    /**
     * Enumerates the keys of HDR metadata used by [pixelmap]{@link @ohos.multimedia.image:image.PixelMap}.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 12
     */
    enum HdrMetadataKey {
        /**
         * Metadata type used by [pixelmap]{@link @ohos.multimedia.image:image.PixelMap}.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        HDR_METADATA_TYPE = 0,
        /**
         * Static metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        HDR_STATIC_METADATA = 1,
        /**
         * Dynamic metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        HDR_DYNAMIC_METADATA = 2,
        /**
         * Metadata used by gain maps.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        HDR_GAINMAP_METADATA = 3
    }
    /**
     * Enumerates the values available for **HDR_METADATA_TYPE** in [HdrMetadataKey]{@link image.HdrMetadataKey}.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 12
     */
    enum HdrMetadataType {
        /**
         * No metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        NONE = 0,
        /**
         * Metadata used for base graphics.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        BASE = 1,
        /**
         * Metadata used for gain maps.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        GAINMAP = 2,
        /**
         * Metadata used for synthesized HDR graphics.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        ALTERNATE = 3
    }
    /**
     * Enumerates the types of the memory used for image decoding.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 15
     */
    enum AllocatorType {
        /**
         * The system determines whether DMA memory or shared memory is used.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 15
         */
        AUTO = 0,
        /**
         * DMA memory is used.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 15
         */
        DMA = 1,
        /**
         * Shared memory is used.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 15
         */
        SHARE_MEMORY = 2
    }
    /**
     * Enumerates the order of cropping and scaling.
     *
     * If the **cropAndScaleStrategy** parameter is not specified in
     * [DecodingOptions]{@link @ohos.multimedia.image:image.DecodingOptions} and both **desiredRegion** and
     * **desiredSize** are set, the final decoding result may vary slightly due to differences in decoding algorithms used
     * for different image formats.
     *
     * For example, if the original image size is 200x200, and you specify
     * **desiredSize:{width: 150, height: 150}, desiredRegion:{x: 0, y: 0, width: 100, height: 100}**, the expectation is
     * to decode the top-left 1/4 region of the original image and then scale the pixelMap size to 150x150.
     *
     * For JPEG and WebP images (as well as some DNG images that decode a JPEG preview within the file and therefore are
     * treated as JPEG format), the system first performs downsampling. For instance, it might downsample by 7/8 and then
     * crop the region based on a 175x175 image size. As a result, the final cropped region will be slightly larger than
     * the top-left 1/4 of the original image.
     *
     * For SVG images, which are vector-based and can be scaled without losing clarity, the system scales the image based
     * on the ratio of **desiredSize** to the original image size and then crops the region. This results in a decoded
     * region that may differ from the exact 1/4 region of the original image.
     *
     * To ensure consistent results when both **desiredRegion** and **desiredSize** are set, set the
     * **cropAndScaleStrategy** parameter to **CROP_FIRST**.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 18
     */
    enum CropAndScaleStrategy {
        /**
         * If both **desiredRegion** and **desiredSize** are specified, the image is first scaled based on **desiredSize**
         * and then cropped based on **desiredRegion**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 18
         */
        SCALE_FIRST = 1,
        /**
         * If both **desiredRegion** and **desiredSize** are specified, the image is first cropped based on
         * **desiredRegion** and then scaled based on **desiredSize**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 18
         */
        CROP_FIRST = 2
    }
    /**
     * Describes the region information.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 8
     */
    interface Region {
        /**
         * Region size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        size: Size;
        /**
         * X coordinate of the top-left corner of the region, in px.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        x: number;
        /**
         * Y coordinate of the top-left corner of the region, in px.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        y: number;
    }
    /**
     * Describes area information in an image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 7
     */
    interface PositionArea {
        /**
         * Pixels of the image. Only pixel data in BGRA_8888 format is supported.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        pixels: ArrayBuffer;
        /**
         * Offset for data reading, in bytes.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        offset: number;
        /**
         * Number of bytes from one row of pixels in memory to the next row of pixels in memory. The value of **stride**
         * must be greater than or equal to the value of **region.size.width** multiplied by 4.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        stride: number;
        /**
         * Region to read or write. The width of the region to write plus the X coordinate cannot be greater than the width
         * of the original image. The height of the region to write plus the Y coordinate cannot be greater than the height
         * of the original image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        region: Region;
    }
    /**
     * Describes image information.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 6
     */
    interface ImageInfo {
        /**
         * Image size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 6
         */
        size: Size;
        /**
         * Pixel density, in ppi.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        density: number;
        /**
         * Number of bytes from one row of pixels in memory to the next row of pixels in memory.stride >= region.size.width*
         * 4
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @form [since 12]
         * @atomicservice
         * @since 11
         */
        stride: number;
        /**
         * Pixel format.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @form
         * @atomicservice
         * @since 12
         */
        pixelFormat: PixelMapFormat;
        /**
         * Alpha type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @form
         * @atomicservice
         * @since 12
         */
        alphaType: AlphaType;
        /**
         * Actual image format (MIME type).
         *
         * The supported formats for image decoding and image encoding are different. Do not directly use the actual image
         * format obtained after decoding as the value of **format** in [PackingOption]{@link image.PackingOption} during
         * image encoding.
         *
         * You can use the **supportedFormats** property of
         * [ImageSource]{@link @ohos.multimedia.image: image.ImageSource#supportedFormats} and
         * [ImagePacker]{@link @ohos.multimedia.image: image.ImagePacker#supportedFormats} to view the
         * supported formats for decoding and encoding.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        mimeType: string;
        /**
         * Whether the image is an HDR image. The value **true** means an HDR image, and **false** means an SDR image. For
         * [ImageSource]{@link @ohos.multimedia.image:image.ImageSource}, this parameter specifies whether the source image is in HDR
         * format. For [PixelMap]{@link @ohos.multimedia.image:image.PixelMap}, this parameter specifies whether the decoded PixelMap
         * is in HDR format.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        isHdr: boolean;
    }
    /**
     * Describes the options for tiff image packing.
     *
     * @syscap SystemCapability.Multimedia.Image.ImagePacker
     * @stagemodelonly
     * @since 26.0.0
     */
    interface PackingOptionsForTiff {
        /**
         * Compression algorithm type: 3 (CCITT G3), 4 (CCITT G4), 5 (LZW).
         * - For binary image: must be 3 (G3) or 4 (G4), automatically uses 4 (G4).
         * - For Y8/RGB_888 format: automatically uses LZW (5), user setting is ignored.
         * The value should be an integer, Currently, only 3, 4, and 5 are supported.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        compression?: number;
        /**
         * Image orientation.Default value is 1 TOP_LEFT.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        orientation?: Orientation;
        /**
         * Horizontal resolution.
         * The value must be greater than 0.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        xResolution?: number;
        /**
         * Vertical resolution.
         * The value must be greater than 0.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        yResolution?: number;
        /**
         * Resolution unit: 1 (No unit), 2 (Inch), 3 (Centimeter).
         * Currently, only 1, 2, and 3 are supported.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        resolutionUnit?: number;
    }
    /**
     * Packing image size limit.
     *
     * @syscap SystemCapability.Multimedia.Image.ImagePacker
     * @stagemodelonly
     * @since 26.0.0
     */
    interface PackingSizeLimit {
        /**
         * Maximum packing size
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        maxSize: Size;
        /**
         * Specify the scaling algorithm during zooming.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        level: AntiAliasingLevel;
    }
    /**
     * Describes the options for image encoding.
     *
     * @syscap SystemCapability.Multimedia.Image.ImagePacker
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    interface PackingOption {
        /**
         * Format of the packed image.
         *
         * Currently, only the following formats are supported: image/jpeg, image/webp, image/png, image/heic (or image/heif
         * )<sup>12+</sup>, image/sdr_astc_4x4<sup>18+</sup>, image/sdr_sut_superfast_4x4<sup>18+</sup> (depending on the
         * hardware), and image/hdr_astc_4x4<sup>20+</sup>.
         *
         * **NOTE**: The JPEG format does not support the alpha channel. If the JPEG format with the alpha channel is used
         * for data encoding, the transparent color turns black.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        format: string;
        /**
         * Quality of the output image set. This parameter takes effect only for JPEG and HEIF images. The value range is
         * [0, 100]. The value **0** means the lowest quality, and **100** means the highest quality. The higher the quality
         * , the larger the space occupied by the generated image. WebP and PNG images are lossless.
         *
         * In the case of sdr_astc_4x4 encoding, the parameter can be set to **92** and **85**.
         *
         * In the case of sut encoding, the parameter can be set to **92**.
         *
         * (Available since API version 20) In the case of hdr_astc_4x4 encoding, the parameter can be set to **85**.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        quality: number;
        /**
         * Size of the buffer for receiving the encoded data, in bytes. If this parameter is not set, the default value 25
         * MB is used. If the size of an image exceeds 25 MB, you must specify the size. The value of **bufferSize** must be
         * greater than the size of the encoded image. The use of
         * [packToFile]{@link @ohos.multimedia.image:image.ImagePacker.packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback<void>)}
         * is not restricted by this parameter.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        bufferSize?: number;
        /**
         * Desired dynamic range. The default value is **SDR**.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @since 12
         */
        desiredDynamicRange?: PackingDynamicRange;
        /**
         * Whether encoding image property information, for example, Exif, is required. **true** if required, **false**
         * otherwise. The default value is **false**.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @since 12
         */
        needsPackProperties?: boolean;
        /**
         * This parameter is valid only when needsPackProperties is set to true. It specifies the maximum width and height
         *     of the thumbnail generated during encoding. If this parameter is not specified, no thumbnail will be
         *     generated during encoding.
         * The value should be an integer.
         * <br>Unit:px.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        maxEmbedThumbnailDimension?: number;
        /**
         * Options for tiff image packing.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        tiffPackingOptions?: PackingOptionsForTiff;
        /**
         * The background color used when the image pixels are in RGBA format but the target encoding format does not
         * support transparency, such as "image/jpeg" or "image/heif".
         * The value must be a 24‑bit RGB integer expressed in hexadecimal notation (e.g., 0xRRGGBB).
         * The alpha channel is ignored.
         * Valid range: 0x000000 – 0xFFFFFF.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        backgroundColor?: number;
        /**
         * Packing image size limit.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        sizeLimit?: PackingSizeLimit;
        /**
         * Indicates whether to carry GPS information when encoding the EXIF metadata.
         * Default value: true.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        needsPackGPS?: boolean;
    }
    /**
     * Defines the options for encoding animated images.
     *
     * @syscap SystemCapability.Multimedia.Image.ImagePacker
     * @since 18
     */
    interface PackingOptionsForSequence {
        /**
         * Number of frames specified in GIF encoding.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @since 18
         */
        frameCount: number;
        /**
         * Delay time of each frame in GIF encoding. The value must be greater than 0.
         *
         * The unit is 10 milliseconds. For example, if this parameter is set to 10, the actual delay per frame is 100 ms.
         *
         * If the array length is less than **frameCount**, the last value in the array will be used for the remaining
         * frames.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @since 18
         */
        delayTimeList: Array<number>;
        /**
         * Array that defines how each image frame transitions. If the array length is less than **frameCount**, the last
         * value in the array will be used for the remaining frames. The values can be:
         *
         * - **0**: No operation is required.
         * - **1**: Keeps the image unchanged.
         * - **2**: Restores the background color.
         * - **3**: Restores to the previous state.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @since 18
         */
        disposalTypes?: Array<number>;
        /**
         * Number of times that the output image in GIF encoding loops. The value range is [0, 65535].
         *
         * The value **0** means an infinite loop. If this field is not carried, loop playback is not performed.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @since 18
         */
        loopCount?: number;
    }
    /**
     * Describes the image properties.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @since 7
     * @deprecated since 11
     * @useinstead image.ImagePropertyOptions
     */
    interface GetImagePropertyOptions {
        /**
         * Index of the image. The default value is **0**.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 7
         * @deprecated since 11
         * @useinstead image.ImagePropertyOptions#index
         */
        index?: number;
        /**
         * Default property value. The default value is null.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 7
         * @deprecated since 11
         * @useinstead image.ImagePropertyOptions#defaultValue
         */
        defaultValue?: string;
    }
    /**
     * Describes the image properties.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform
     * @since 11
     */
    interface ImagePropertyOptions {
        /**
         * Index of the image. The default value is **0**.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 11
         */
        index?: number;
        /**
         * Default property value. The default value is null.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 11
         */
        defaultValue?: string;
    }
    /**
     * Describes the image decoding options.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 7
     */
    interface DecodingOptions {
        /**
         * Index of the image to decode. The default value is **0**, indicating the first image. If this parameter is set to
         * N, the (N+1)th image is used. For single-frame images, the value is always **0**. For multi-frame images such as
         * animations, the value ranges from 0 to (Number of frames – 1).
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        index?: number;
        /**
         * Sampling size of the thumbnail. The default value is **1**. Currently, the value can only be **1**.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        sampleSize?: number;
        /**
         * Rotation angle. The default value is **0**.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        rotate?: number;
        /**
         * Whether the image is editable. **true** if editable, **false** otherwise. The default value is **false**. If this
         * option is set to **false**, the image cannot be edited again, and operations such as writing pixels will fail.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        editable?: boolean;
        /**
         * Expected output size. The value must be a positive integer and defaults to the original image size. If the output
         * size is different from the original size, the output is stretched or scaled to the specified size.
         *
         * Note: If both **desiredSize** and **desiredRegion** are passed to the decoding API, you must also include
         * **cropAndScaleStrategy** to determine whether to crop or scale first. **CROP_FIRST** is recommended.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        desiredSize?: Size;
        /**
         * Rectangle specified by **Region** in the decoded image. When the original image is large and only a specific part
         * of the image is required, you can set this parameter to improve performance. The default value is the original
         * image size.
         *
         * Note: If both **desiredSize** and **desiredRegion** are passed to the decoding API, you must also include
         * **cropAndScaleStrategy** to determine whether to crop or scale first. **CROP_FIRST** is recommended.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        desiredRegion?: Region;
        /**
         * Pixel format for decoding. The default value is **RGBA_8888**. Only RGBA_8888, BGRA_8888, and RGB_565 are
         * supported. RGB_565 is not supported for images with alpha channels, such as PNG, GIF, ICO, and WEBP.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        desiredPixelFormat?: PixelMapFormat;
        /**
         * Pixel density, in ppi. The default value is **0**.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        fitDensity?: number;
        /**
         * Target color space. The default value is **UNKNOWN**.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 11
         */
        desiredColorSpace?: colorSpaceManager.ColorSpaceManager;
        /**
         * Desired dynamic range. The default value is **SDR**.
         *
         * This property cannot be set for an image source created using
         * [CreateIncrementalSource]{@link @ohos.multimedia.image:image.CreateIncrementalSource(buf: ArrayBuffer)}. By
         * default, the image source is decoded as SDR content.
         *
         * If the platform does not support HDR, the setting is invalid and the content is decoded as SDR content by
         * default.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @since 12
         */
        desiredDynamicRange?: DecodingDynamicRange;
        /**
         * If **desiredRegion** and **desiredSize** are both specified, the order of cropping and scaling is determined.
         *
         * Only **SCALE_FIRST** and **CROP_FIRST** are supported.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @since 18
         */
        cropAndScaleStrategy?: CropAndScaleStrategy;
    }
    /**
     * Describes the color components of an image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 9
     */
    interface Component {
        /**
         * Color component type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        readonly componentType: ComponentType;
        /**
         * Row stride. The camera preview stream data needs to be read by stride. For details, see
         * [Solution to Screen Artifacts During Camera Preview](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-deal-stride-solution)
         * .
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        readonly rowStride: number;
        /**
         * Pixel stride.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        readonly pixelStride: number;
        /**
         * Component buffer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        readonly byteBuffer: ArrayBuffer;
    }
    /**
     * Defines PixelMap initialization options.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 8
     */
    interface InitializationOptions {
        /**
         * Image size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        size: Size;
        /**
         * Pixel format of the passed-in buffer data. The default value is **BGRA_8888**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        srcPixelFormat?: PixelMapFormat;
        /**
         * Pixel format of the generated PixelMap. The default value is **RGBA_8888**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        pixelFormat?: PixelMapFormat;
        /**
         * Whether the image pixels are editable. **true** if editable, **false** otherwise. The value **false** provides
         * better image rendering and transmission performance. The default value is **false**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        editable?: boolean;
        /**
         * Alpha type. The default value is **IMAGE_ALPHA_TYPE_PREMUL**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        alphaType?: AlphaType;
        /**
         * Scale mode. The default value is **0**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        scaleMode?: ScaleMode;
    }
    /**
     * Defines image source initialization options.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    interface SourceOptions {
        /**
         * Pixel density of the image resource, in ppi.
         *
         * If **desiredSize** is not set in [DecodingOptions]{@link image.DecodingOptions} and
         * **SourceOptions.sourceDensity** and **DecodingOptions.fitDensity** are not 0, the PixelMap output after decoding
         * will be scaled.
         *
         * The formula for calculating the width after scaling is as follows (the same applies to the height): (width *
         * fitDensity + (sourceDensity >> 1)) / sourceDensity.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        sourceDensity: number;
        /**
         * Image pixel format. The default value is **UNKNOWN**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        sourcePixelFormat?: PixelMapFormat;
        /**
         * Image pixel size. The default value is null.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        sourceSize?: Size;
    }
    /**
     * Describes the static metadata keys, that is, the values available for **HDR_STATIC_METADATA** in
     * [HdrMetadataKey]{@link @ohos.multimedia.image:image.HdrMetadataKey}.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 12
     */
    interface HdrStaticMetadata {
        /**
         * The X-coordinate of the primary colors. Specifies the normalized X-coordinates of the display device's three
         * primary colors. The values are stored in an array of length 3, in the order of red, green, and blue (r, g, b).
         * Each value is represented in units of 0.00002 and must fall within the range [0.0, 1.0].
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        displayPrimariesX: Array<number>;
        /**
         * The Y-coordinate of the primary colors. Specifies the normalized Y-coordinates of the display device's three
         * primary colors. The values are stored in an array of length 3, in the order of red, green, and blue (r, g, b).
         * Each value is represented in units of 0.00002 and must fall within the range [0.0, 1.0].
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        displayPrimariesY: Array<number>;
        /**
         * The X-coordinate of the white point value. Specifies the normalized X-coordinate of the white point.
         *
         * The value is represented in units of 0.00002 and must fall within the range [0.0, 1.0].
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        whitePointX: number;
        /**
         * The Y-coordinate of the white point value. Specifies the normalized Y-coordinate of the white point.
         *
         * The value is represented in units of 0.00002 and must fall within the range [0.0, 1.0].
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        whitePointY: number;
        /**
         * Maximum luminance of the image's primary display.
         * The value is measured in units of 1, with a maximum allowed value of 65,535.
         *
         * Unit:nit.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        maxLuminance: number;
        /**
         * Minimum luminance of the image's primary display.
         *
         * The value is measured in units of 0.0001, with a maximum allowed value of 6.55535.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        minLuminance: number;
        /**
         * Maximum brightness of displayed content.
         *
         * The value is measured in units of 1, with a maximum allowed value of 65,535.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        maxContentLightLevel: number;
        /**
         * Maximum average brightness of displayed content.
         *
         * The value is measured in units of 1, with a maximum allowed value of 65,535.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        maxFrameAverageLightLevel: number;
    }
    /**
     * Describes the data content of a single channel of the gain map. For details, see ISO 21496-1.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 12
     */
    interface GainmapChannel {
        /**
         * The per-component max gain map values.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        gainmapMax: number;
        /**
         * The per-component min gain map values.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        gainmapMin: number;
        /**
         * The per-component gamma values.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        gamma: number;
        /**
         * The per-component baseline offset.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        baseOffset: number;
        /**
         * The per-component alternate offset.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        alternateOffset: number;
    }
    /**
     * Describes the metadata keys used by a gain map, that is, the values available for **HDR_GAINMAP_METADATA** in
     * [HdrMetadataKey]{@link @ohos.multimedia.image:image.HdrMetadataKey}. For details, see ISO 21496-1.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 12
     */
    interface HdrGainmapMetadata {
        /**
         * The version used by the writer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        writerVersion: number;
        /**
         * The minimum version a parser needs to understand.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        miniVersion: number;
        /**
         * The number of gain map channels, with a value of 1 or 3.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        gainmapChannelCount: number;
        /**
         * Indicate whether to use the color space of the base image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        useBaseColorFlag: boolean;
        /**
         * The baseline hdr headroom.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        baseHeadroom: number;
        /**
         * The alternate hdr headroom.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        alternateHeadroom: number;
        /**
         * The per-channel metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        channels: Array<GainmapChannel>;
    }
    /**
     * Describes the initialization options for ImageReceiver.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageReceiver
     * @stagemodelonly
     * @since 23
     */
    interface ImageReceiverOptions {
        /**
         * Image size, with both the width and height greater than 0.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @stagemodelonly
         * @since 23
         */
        size?: Size;
        /**
         * Maximum number of images that can be accessed simultaneously.
         * The value range is all integers, The value must be a positive integer less than
         * or equal to 64.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @stagemodelonly
         * @since 23
         */
        capacity?: number;
    }
    /**
     * Describes the image buffer data.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    interface ImageBufferData {
        /**
         * Row stride of each component.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        readonly rowStride: number[];
        /**
         * Pixel stride of each component.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        readonly pixelStride: number[];
        /**
         * Image data buffer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        readonly byteBuffer: ArrayBuffer;
    }
    /**
     * Describes the HDR metadata values used by a PixelMap, which corresponds to the values available for
     * [HdrMetadataKey]{@link @ohos.multimedia.image:image.HdrMetadataKey}.
     *
     * @unionmember { HdrMetadataType } Metadata value corresponding to the **HDR_METADATA_TYPE** key in
     *     [HdrMetadataKey]{@link @ohos.multimedia.image:image.HdrMetadataKey}.
     * @unionmember { HdrStaticMetadata } Metadata value corresponding to the **HDR_STATIC_METADATA** key in
     *     [HdrMetadataKey]{@link @ohos.multimedia.image:image.HdrMetadataKey}.
     * @unionmember { ArrayBuffer } Metadata value corresponding to the **HDR_DYNAMIC_METADATA** key in
     *     [HdrMetadataKey]{@link @ohos.multimedia.image:image.HdrMetadataKey}.
     * @unionmember { HdrGainmapMetadata } Metadata value corresponding to the **HDR_GAINMAP_METADATA** key in
     *     [HdrMetadataKey]{@link @ohos.multimedia.image:image.HdrMetadataKey}.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 12
     */
    type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata;
    /**
     * Creates a PixelMap from existing pixel data. The pixel data will be copied and converted to the specified
     * pixel format to initialize the PixelMap.
     *
     * The following pixel formats are not supported for PixelMap creation:
     * RGBA_1010102, YCBCR_P010, YCRCB_P010, ASTC_4x4.
     *
     * @param { ArrayBuffer } pixels - The pixel data buffer used to initialize the PixelMap.
     *     The format of the pixel data can be specified by InitializationOptions.srcPixelFormat.
     *     The size of the buffer should be: image width * image height * bytes per pixel.
     * @param { InitializationOptions } param - Initialization options for the PixelMap.
     *     If InitializationOptions.pixelFormat is set to ASTC_4x4, it will be reset to the default value RGBA_8888.
     *     If InitializationOptions.srcPixelFormat is set to ASTC_4x4, it will be reset to the default value BGRA_8888.
     * @returns { Promise<PixelMap> } A Promise of the new PixelMap created.
     * @throws { BusinessError } 7600206 - Invalid parameter.
     *     Possible cause: Size of the pixel data buffer does not match InitializationOptions.size.
     * @throws { BusinessError } 7600207 - Unsupported pixel format.
     * @throws { BusinessError } 7600301 - Failed to allocate memory.
     *     Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory.
     * @throws { BusinessError } 7600305 - Failed to create the PixelMap.
     *     Possible causes:
     *     1. Failed to perform pixel format conversion.
     *     2. Internal data is corrupted. Please check the logs for detailed information.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    function createPixelMapFromPixels(pixels: ArrayBuffer, param: InitializationOptions): Promise<PixelMap>;
    /**
     * Creates a PixelMap from existing pixel data. The pixel data will be copied and converted to the specified
     * pixel format to initialize the PixelMap.
     *
     * The following pixel formats are not supported for PixelMap creation:
     * RGBA_1010102, YCBCR_P010, YCRCB_P010, ASTC_4x4.
     *
     * @param { ArrayBuffer } pixels - The pixel data buffer used to initialize the PixelMap.
     *     The format of the pixel data can be specified by InitializationOptions.srcPixelFormat.
     *     The size of the buffer should be: image width * image height * bytes per pixel.
     * @param { InitializationOptions } param - Initialization options for the PixelMap.
     *     If InitializationOptions.pixelFormat is set to ASTC_4x4, it will be reset to the default value RGBA_8888.
     *     If InitializationOptions.srcPixelFormat is set to ASTC_4x4, it will be reset to the default value BGRA_8888.
     * @returns { PixelMap } The new PixelMap created.
     * @throws { BusinessError } 7600206 - Invalid parameter.
     *     Possible cause: Size of the pixel data buffer does not match InitializationOptions.size.
     * @throws { BusinessError } 7600207 - Unsupported pixel format.
     * @throws { BusinessError } 7600301 - Failed to allocate memory.
     *     Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory.
     * @throws { BusinessError } 7600305 - Failed to create the PixelMap.
     *     Possible causes:
     *     1. Failed to perform pixel format conversion.
     *     2. Internal data is corrupted. Please check the logs for detailed information.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    function createPixelMapFromPixelsSync(pixels: ArrayBuffer, param: InitializationOptions): PixelMap;
    /**
     * Create pixelmap by data buffer.
     *
     * @param { ArrayBuffer } colors The image color buffer.
     * @param { InitializationOptions } options Initialization options for pixelmap.
     * @param { AsyncCallback<PixelMap> } callback Callback used to return the PixelMap object.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 8
     */
    /**
     * Create pixelmap by data buffer.
     *
     * Starting from API 26.0.0, it is recommended to use {@link createPixelMapFromPixels} instead for better exception handling capabilities.
     *
     * @param { ArrayBuffer } colors The image color buffer.
     * @param { InitializationOptions } options Initialization options for pixelmap.
     * @param { AsyncCallback<PixelMap> } callback Callback used to return the PixelMap object.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform
     * @since 10
     */
    function createPixelMap(colors: ArrayBuffer, options: InitializationOptions, callback: AsyncCallback<PixelMap>): void;
    /**
     * Create pixelmap by data buffer.
     *
     * @param { ArrayBuffer } colors The image color buffer.
     * @param { InitializationOptions } options Initialization options for pixelmap.
     * @returns { Promise<PixelMap> } A Promise instance used to return the PixelMap object.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 8
     */
    /**
     * Create pixelmap by data buffer.
     *
     * Starting from API 26.0.0, it is recommended to use {@link createPixelMapFromPixels} instead for better exception handling capabilities.
     *
     * @param { ArrayBuffer } colors The image color buffer.
     * @param { InitializationOptions } options Initialization options for pixelmap.
     * @returns { Promise<PixelMap> } A Promise instance used to return the PixelMap object.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform
     * @since 10
     */
    function createPixelMap(colors: ArrayBuffer, options: InitializationOptions): Promise<PixelMap>;
    /**
     * Create pixelmap by data buffer.
     *
     * Starting from API 26.0.0, it is recommended to use {@link createPixelMapFromPixelsSync} instead for better exception handling capabilities.
     *
     * @param { ArrayBuffer } colors The image color buffer.
     * @param { InitializationOptions } options Initialization options for pixelmap.
     * @returns { PixelMap } Returns the instance if the operation is successful;Otherwise, return undefined.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     * 2.Incorrect parameter types. 3.Parameter verification failed.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform
     * @since 12
     */
    function createPixelMapSync(colors: ArrayBuffer, options: InitializationOptions): PixelMap;
    /**
     * Create pixelmap by data buffer based on opts, the memory type used by the PixelMap can be specified
     * by allocatorType. By default, the system selects the memory type based on the image type, image size,
     * platform capability, etc. When processing the PixelMap returned by this interface, please always
     * consider the impact of stride.
     *
     * @param { ArrayBuffer } colors The image color buffer.
     * @param { InitializationOptions } param Initialization options for pixelmap.
     * @param { AllocatorType } [allocatorType] Indicate which memory type will be used by the returned PixelMap.
     * @returns { Promise<PixelMap> } A Promise instance used to return the PixelMap object.
     * @throws { BusinessError } 7600201 - Unsupported operation.
     * @throws { BusinessError } 7600301 - Memory alloc failed.
     * @throws { BusinessError } 7600302 - Memory copy failed.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 20
     */
    function createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): Promise<PixelMap>;
    /**
     * Create pixelmap by data buffer based on opts, the memory type used by the PixelMap can be specified
     * by allocatorType. By default, the system selects the memory type based on the image type, image size,
     * platform capability, etc. When processing the PixelMap returned by this interface, please always
     * consider the impact of stride.
     *
     * @param { ArrayBuffer } colors The image color buffer.
     * @param { InitializationOptions } param Initialization options for pixelmap.
     * @param { AllocatorType } [allocatorType] Indicate which memory type will be used by the returned PixelMap.
     * @returns { PixelMap } Returns the instance if the operation is successful;Otherwise, return undefined.
     * @throws { BusinessError } 7600201 - Unsupported operation.
     * @throws { BusinessError } 7600301 - Memory alloc failed.
     * @throws { BusinessError } 7600302 - Memory copy failed.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 20
     */
    function createPixelMapUsingAllocatorSync(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): PixelMap;
    /**
     * Creates an empty PixelMap.
     *
     * The following pixel format is not supported for PixelMap creation: ASTC_4x4.
     *
     * @param { InitializationOptions } param - Initialization options for the PixelMap.
     *     If InitializationOptions.pixelFormat is set to ASTC_4x4, it will be reset to the default value RGBA_8888.
     * @returns { PixelMap } The new PixelMap created.
     * @throws { BusinessError } 7600206 - Invalid parameter.
     * @throws { BusinessError } 7600301 - Failed to allocate memory.
     *     Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory.
     * @throws { BusinessError } 7600305 - Failed to create the PixelMap.
     *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 26.0.0
     */
    function createEmptyPixelMap(param: InitializationOptions): PixelMap;
    /**
     * Create an empty pixelmap.
     *
     * Starting from API 26.0.0, it is recommended to use {@link createEmptyPixelMap} instead for better exception handling capabilities.
     *
     * @param { InitializationOptions } options Initialization options for pixelmap.
     * @returns { PixelMap } Returns the instance if the operation is successful;Otherwise, return undefined.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     * 2.Incorrect parameter types. 3.Parameter verification failed.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform
     * @since 12
     */
    function createPixelMapSync(options: InitializationOptions): PixelMap;
    /**
     * Create an empty pixelmap by data buffer based on opts, the memory type used by the PixelMap can be specified
     * by allocatorType. By default, the system selects the memory type based on the image type, image size,
     * platform capability, etc. When processing the PixelMap returned by this interface, please always
     * consider the impact of stride.
     *
     * @param { InitializationOptions } param Initialization options for pixelmap.
     * @param { AllocatorType } [allocatorType] Indicate which memory type will be used by the returned PixelMap.
     * @returns { PixelMap } Returns the instance if the operation is successful;Otherwise, return undefined.
     * @throws { BusinessError } 7600201 - Unsupported operation.
     * @throws { BusinessError } 7600301 - Memory alloc failed.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 20
     */
    function createPixelMapUsingAllocatorSync(param: InitializationOptions, allocatorType?: AllocatorType): PixelMap;
    /**
     * Transforms pixelmap from unpremultiplied alpha format to premultiplied alpha format.
     *
     * @param { PixelMap } src The source pixelmap.
     * @param { PixelMap } dst The destination pixelmap.
     * @param { AsyncCallback<void> } callback Callback used to return the operation result.
     * If the operation fails, an error message is returned.
     * @throws { BusinessError } 62980103 - The image data is not supported.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     * 2.Incorrect parameter types. 3.Parameter verification failed.
     * @throws { BusinessError } 62980246 - Failed to read the pixelMap.
     * @throws { BusinessError } 62980248 - Pixelmap not allow modify.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform
     * @since 12
     */
    function createPremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void;
    /**
     * Transforms pixelmap from premultiplied alpha format to unpremultiplied alpha format.
     *
     * @param { PixelMap } src The source pixelMap.
     * @param { PixelMap } dst The destination pixelmap.
     * @returns { Promise<void> } A Promise instance used to return the operation result.
     * If the operation fails, an error message is returned.
     * @throws { BusinessError } 62980103 - The image data is not supported.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     * 2.Incorrect parameter types. 3.Parameter verification failed.
     * @throws { BusinessError } 62980246 - Failed to read the pixelMap.
     * @throws { BusinessError } 62980248 - Pixelmap not allow modify.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform
     * @since 12
     */
    function createPremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>;
    /**
     * Transforms pixelmap from premultiplied alpha format to unpremultiplied alpha format.
     *
     * @param { PixelMap } src The source pixelmap.
     * @param { PixelMap } dst The destination pixelmap.
     * @param { AsyncCallback<void> } callback Callback used to return the operation result.
     * If the operation fails, an error message is returned.
     * @throws { BusinessError } 62980103 - The image data is not supported.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     * 2.Incorrect parameter types. 3.Parameter verification failed.
     * @throws { BusinessError } 62980246 - Failed to read the pixelMap.
     * @throws { BusinessError } 62980248 - Pixelmap not allow modify.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform
     * @since 12
     */
    function createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void;
    /**
     * Transforms pixelmap from premultiplied alpha format to unpremultiplied alpha format.
     *
     * @param { PixelMap } src The source pixelmap.
     * @param { PixelMap } dst The destination pixelmap.
     * @returns { Promise<void> } A Promise instance used to return the operation result.
     * If the operation fails, an error message is returned.
     * @throws { BusinessError } 62980103 - The image data is not supported.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     * 2.Incorrect parameter types. 3.Parameter verification failed.
     * @throws { BusinessError } 62980246 - Failed to read the pixelMap.
     * @throws { BusinessError } 62980248 - Pixelmap not allow modify.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform
     * @since 12
     */
    function createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>;
    /**
     * Creates a PixelMap object based on MessageSequence parameter.
     *
     * @param { rpc.MessageSequence } sequence - rpc.MessageSequence parameter.
     * @returns { PixelMap } Returns the instance if the operation is successful;Otherwise, an exception will be thrown.
     * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
     * 2. Decoding process exception. 3. Insufficient memory.
     * @throws { BusinessError } 62980097 - IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception.
     * 3. Decode process exception. 4. Insufficient memory.
     * @throws { BusinessError } 62980115 - Invalid input parameter.
     * @throws { BusinessError } 62980105 - Failed to get the data.
     * @throws { BusinessError } 62980177 - Abnormal API environment.
     * @throws { BusinessError } 62980178 - Failed to create the PixelMap.
     * @throws { BusinessError } 62980179 - Abnormal buffer size.
     * @throws { BusinessError } 62980180 - FD mapping failed.
     * Possible cause: 1. Size and address does not match. 2. Memory map in memalloc failed.
     * @throws { BusinessError } 62980246 - Failed to read the PixelMap.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 11
     */
    function createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap;
    /**
     * Creates a PixelMap object from surface id.
     *
     * @param { string } surfaceId - surface id.
     * @param { Region } region - The region to surface.
     * @returns { Promise<PixelMap> } Returns the instance if the operation is successful;Otherwise, an exception will be thrown.
     * @throws { BusinessError } 62980115 - If the image parameter invalid.
     * @throws { BusinessError } 62980105 - Failed to get the data.
     * @throws { BusinessError } 62980178 - Failed to create the PixelMap.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 11
     */
    function createPixelMapFromSurface(surfaceId: string, region: Region): Promise<PixelMap>;
    /**
     * Creates a PixelMap object from surface id.
     *
     * @param { string } surfaceId - surface id.
     * @param { Region } region - The region to surface.
     * @returns { PixelMap } Returns the instance if the operation is successful;Otherwise, an exception will be thrown.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types. 3.Parameter verification failed.
     * @throws { BusinessError } 62980105 - Failed to get the data.
     * @throws { BusinessError } 62980178 - Failed to create the PixelMap.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 12
     */
    function createPixelMapFromSurfaceSync(surfaceId: string, region: Region): PixelMap;
    /**
     * Creates a PixelMap object from surface id.
     *
     * @param { string } surfaceId - surface id.
     * @returns { Promise<PixelMap> } Returns the instance if the operation is successful;Otherwise, an exception will be thrown.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types. 3.Parameter verification failed.
     * @throws { BusinessError } 62980105 - Failed to get the data.
     * @throws { BusinessError } 62980178 - Failed to create the PixelMap.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 15
     */
    function createPixelMapFromSurface(surfaceId: string): Promise<PixelMap>;
    /**
     * Creates a PixelMap object from surface id.
     *
     * @param { string } surfaceId - surface id.
     * @returns { PixelMap } Returns the instance if the operation is successful;Otherwise, an exception will be thrown.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types. 3.Parameter verification failed.
     * @throws { BusinessError } 62980105 - Failed to get the data.
     * @throws { BusinessError } 62980178 - Failed to create the PixelMap.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 15
     */
    function createPixelMapFromSurfaceSync(surfaceId: string): PixelMap;
    /**
     * Creates a PixelMap object based on the ID of a Surface with transformation.
     *
     * @param { string } surfaceId - ID of the Surface.
     * @param { boolean } transformEnabled - Whether to inverse transform the PixelMap to cancel out the transformation
     *     from the Surface.
     *     If true, the PixelMap will be transformed by the same amount from the Surface but in a reversed direction;
     *     if false, the PixelMap will not be transformed.
     * @returns { Promise<PixelMap> } A Promise of PixelMap instance if the operation is successful.
     *     Otherwise, an exception will be thrown.
     * @throws { BusinessError } 7600104 - Failed to get the data from Surface.
     * @throws { BusinessError } 7600201 - Unsupported operation, e.g. on cross-platform.
     * @throws { BusinessError } 7600206 - Invalid parameter.
     * @throws { BusinessError } 7600305 - Failed to create the PixelMap.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    function createPixelMapFromSurfaceWithTransformation(surfaceId: string, transformEnabled: boolean): Promise<PixelMap>;
    /**
     * Creates a PixelMap object based on the ID of a Surface with transformation.
     *
     * @param { string } surfaceId - ID of the Surface.
     * @param { boolean } transformEnabled - Whether to inverse transform the PixelMap to cancel out the transformation
     *     from the Surface.
     *     If true, the PixelMap will be transformed by the same amount from the Surface but in a reversed direction;
     *     if false, the PixelMap will not be transformed.
     * @returns { PixelMap } A PixelMap instance if the operation is successful.
     *     Otherwise, an exception will be thrown.
     * @throws { BusinessError } 7600104 - Failed to get the data from Surface.
     * @throws { BusinessError } 7600201 - Unsupported operation, e.g. on cross-platform.
     * @throws { BusinessError } 7600206 - Invalid parameter.
     * @throws { BusinessError } 7600305 - Failed to create the PixelMap.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    function createPixelMapFromSurfaceWithTransformationSync(surfaceId: string, transformEnabled: boolean): PixelMap;
    /**
     * Creates an ImageSource instance based on a given URI.
     *
     * Images occupy a large amount of memory. When you finish using an ImageSource instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageSource.release(callback: AsyncCallback<void>)} to free the memory
     * promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have
     * finished and the instance is no longer needed.
     *
     * @param { string } uri - Image path. Currently, only the application sandbox path is supported.
     *     <br>The following formats are supported: .jpg, .png, .gif, .bmp, .webp, .dng, .heic<sup>12+</sup>
     *     (depending on the hardware), [.svg<sup>10+</sup>]{@link @ohos.multimedia.image:image.Functions#SVG Tags}, and
     *     .ico<sup>11+</sup>.
     * @returns { ImageSource } ImageSource instance. If the operation fails, undefined is returned.
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    function createImageSource(uri: string): ImageSource;
    /**
     * Creates an ImageSource instance based on a given URI.
     *
     * Images occupy a large amount of memory. When you finish using an ImageSource instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageSource.release(callback: AsyncCallback<void>)} to free the memory
     * promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have
     * finished and the instance is no longer needed.
     *
     * @param { string } uri - Image path. Currently, only the application sandbox path is supported.
     *     <br>The following formats are supported: .jpg, .png, .gif, .bmp, .webp, .dng, .heic<sup>12+</sup> (depending on
     *     the hardware), [.svg<sup>10+</sup>]{@link @ohos.multimedia.image:image.Functions#SVG Tags}, and
     *     .ico<sup>11+</sup>.
     * @param { SourceOptions } options - Image properties, including the image pixel density, pixel format, and image
     *     size.
     * @returns { ImageSource } ImageSource instance. If the operation fails, undefined is returned.
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    function createImageSource(uri: string, options: SourceOptions): ImageSource;
    /**
     * Creates an ImageSource instance based on a given file descriptor.
     *
     * Images occupy a large amount of memory. When you finish using an ImageSource instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageSource.release(callback: AsyncCallback<void>)} to free the memory
     * promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have
     * finished and the instance is no longer needed.
     *
     * @param { number } fd - File descriptor.
     * @returns { ImageSource } ImageSource instance. If the operation fails, undefined is returned.
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    function createImageSource(fd: number): ImageSource;
    /**
     * Creates an ImageSource instance based on a given file descriptor.
     *
     * Images occupy a large amount of memory. When you finish using an ImageSource instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageSource.release(callback: AsyncCallback<void>)} to free the memory
     * promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have
     * finished and the instance is no longer needed.
     *
     * @param { number } fd - File descriptor.
     * @param { SourceOptions } options - Image properties, including the image pixel density, pixel format, and image
     *     size.
     * @returns { ImageSource } ImageSource instance. If the operation fails, undefined is returned.
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    function createImageSource(fd: number, options: SourceOptions): ImageSource;
    /**
     * Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the
     * pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call
     * [image.createPixelMapSync]{@link @ohos.multimedia.image:image.ImageSource.createPixelMapSync(options?: DecodingOptions)}
     * .
     * Images occupy a large amount of memory. When you finish using an ImageSource instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageSource.release(callback: AsyncCallback<void>)} to free the memory
     * promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have
     * finished and the instance is no longer needed.
     *
     * @param { ArrayBuffer } buf - Array of image buffers.
     * @returns { ImageSource } ImageSource instance. If the operation fails, undefined is returned.
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    function createImageSource(buf: ArrayBuffer): ImageSource;
    /**
     * Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the
     * pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call
     * [image.createPixelMapSync]{@link @ohos.multimedia.image:image.ImageSource.createPixelMapSync(options?: DecodingOptions)}
     * .
     * Images occupy a large amount of memory. When you finish using an ImageSource instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageSource.release(callback: AsyncCallback<void>)} to free the memory
     * promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have
     * finished and the instance is no longer needed.
     *
     * @param { ArrayBuffer } buf - Array of image buffers.
     * @param { SourceOptions } options - Image properties, including the image pixel density, pixel format, and image
     *     size.
     * @returns { ImageSource } ImageSource instance. If the operation fails, undefined is returned.
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource;
    /**
     * Creates an ImageSource instance based on the raw file descriptor of an image resource file.
     * Images occupy a large amount of memory. When you finish using an ImageSource instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageSource.release(callback: AsyncCallback<void>)} to free the memory
     * promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have
     * finished and the instance is no longer needed.
     *
     * @param { resourceManager.RawFileDescriptor } rawfile - Raw file descriptor of the image resource file.
     * @param { SourceOptions } options - Image properties, including the image pixel density, pixel format, and image
     *     size.
     * @returns { ImageSource } ImageSource instance. If the operation fails, undefined is returned.
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform
     * @atomicservice
     * @since 11
     */
    function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource;
    /**
     * Creates an ImageSource instance in incremental mode based on buffers. Such an instance does not support reading or
     * writing of Exif information.
     *
     * Images occupy a large amount of memory. When you finish using an ImageSource instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageSource.release(callback: AsyncCallback<void>)} to free the memory
     * promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have
     * finished and the instance is no longer needed.
     *
     * The ImageSource instance created in incremental mode supports the following capabilities (applicable to synchronous
     * , callback, and promise modes):
     *
     * - Obtaining image information: Call
     * [getImageInfo]{@link @ohos.multimedia.image:image.ImageSource.getImageInfo(index: number, callback: AsyncCallback<ImageInfo>)}
     * to obtain image information by index, or call
     * [getImageInfo]{@link @ohos.multimedia.image:image.ImageSource.getImageInfo(callback: AsyncCallback<ImageInfo>)} to
     * directly obtain image information.
     * - Obtaining an image property: Call
     * [getImageProperty]{@link @ohos.multimedia.image:image.ImageSource.getImageProperty(key: PropertyKey, options?: ImagePropertyOptions)}
     * to obtain the value of a property with the specified index in an image.
     * - Obtaining image properties: Call
     * [getImageProperties]{@link @ohos.multimedia.image:image.ImageSource.getImageProperties(key: Array<PropertyKey>)} to
     * obtain the values of properties with the given names in an image.
     * - Updating incremental data: Call
     * [updateData]{@link @ohos.multimedia.image:image.ImageSource.updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number)}
     * .
     * - Creating a PixelMap object: Call
     * [createPixelMap]{@link @ohos.multimedia.image:image.ImageSource.createPixelMap(options?: DecodingOptions)} or
     * [createPixelMap]{@link @ohos.multimedia.image:image.ImageSource.createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>)}
     * to create a PixelMap object based on decoding options; call
     * [createPixelMap]{@link @ohos.multimedia.image:image.ImageSource.createPixelMap(callback: AsyncCallback<PixelMap>)}
     * to create a PixelMap object based on default parameters.
     * - Releasing an ImageSource instance: Call
     * [release]{@link @ohos.multimedia.image:image.ImageSource.release(callback: AsyncCallback<void>)}.
     *
     * @param { ArrayBuffer } buf - Incremental data.
     * @returns { ImageSource } ImageSource instance. If the operation fails, undefined is returned.
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @since 9
     */
    function CreateIncrementalSource(buf: ArrayBuffer): ImageSource;
    /**
     * Creates an ImageSource instance in incremental mode based on buffers. Such an instance does not support reading or
     * writing of Exif information.
     *
     * The capabilities supported by the ImageSource instance created by this API are the same as those supported by the
     * instance created by
     * [CreateIncrementalSource(buf: ArrayBuffer): ImageSource]{@link image.CreateIncrementalSource(buf: ArrayBuffer)}.
     * Images occupy a large amount of memory. When you finish using an ImageSource instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageSource.release(callback: AsyncCallback<void>)} to free the memory
     * promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have
     * finished and the instance is no longer needed.
     *
     * @param { ArrayBuffer } buf - Incremental data.
     * @param { SourceOptions } options - Image properties, including the image pixel density, pixel format, and image
     *     size.
     * @returns { ImageSource } ImageSource instance. If the operation fails, undefined is returned.
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @since 9
     */
    function CreateIncrementalSource(buf: ArrayBuffer, options?: SourceOptions): ImageSource;
    /**
     * Creates an ImagePacker instance.
     *
     * Images occupy a large amount of memory. When you finish using an ImagePacker instance, call
     * [release]{@link @ohos.multimedia.image:image.ImagePacker.release(callback: AsyncCallback<void>)} to free the memory
     * promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have
     * finished and the instance is no longer needed.
     *
     * @returns { ImagePacker } ImagePacker instance created.
     * @syscap SystemCapability.Multimedia.Image.ImagePacker
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    function createImagePacker(): ImagePacker;
    /**
     * Creates an ImageReceiver instance by specifying the image width, height, format, and capacity. The ImageReceiver
     * acts as the receiver and consumer of images. Its parameter properties do not actually affect the received images.
     * The configuration of image properties should be done on the sending side (the producer), such as when creating a
     * camera preview stream with
     * [createPreviewOutput]{@link @ohos.multimedia.camera:camera.CameraManager.createPreviewOutput(profile: Profile, surfaceId: string)}
     * .
     * Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageReceiver.release(callback: AsyncCallback<void>)} to free the
     * memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the
     * instance have finished and the instance is no longer needed.
     *
     * @param { number } width - Default image width, in px. This parameter does not affect the width of the received
     *     image. The actual width is determined by the producer, for example, the camera.
     * @param { number } height - Default image height, in px. This parameter does not affect the height of the received
     *     image. The actual height is determined by the producer, for example, the camera.
     * @param { number } format - Image format, which is a constant of
     *     [ImageFormat]{@link @ohos.multimedia.image:image.ImageFormat}. (Currently, only **ImageFormat:JPEG** is
     *     supported. The format actually returned is determined by the producer, for example, camera.)
     * @param { number } capacity - Maximum number of images that can be accessed at the same time. This parameter is used
     *     only as an expected value. The actual capacity is determined by the device hardware.
     * @returns { ImageReceiver } ImageReceiver instance.
     * @syscap SystemCapability.Multimedia.Image.ImageReceiver
     * @since 9
     * @deprecated since 11
     * @useinstead image.createImageReceiver(size: Size, format: ImageFormat, capacity: int)
     */
    function createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver;
    /**
     * Creates an ImageReceiver instance by specifying the image size, format, and capacity. The ImageReceiver acts as the
     * receiver and consumer of images. Its parameter properties do not actually affect the received images. The
     * configuration of image properties should be done on the sending side (the producer), such as when creating a camera
     * preview stream with
     * [createPreviewOutput]{@link @ohos.multimedia.camera:camera.CameraManager.createPreviewOutput(profile: Profile, surfaceId: string)}
     * .
     * Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageReceiver.release(callback: AsyncCallback<void>)} to free the
     * memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the
     * instance have finished and the instance is no longer needed.
     *
     * @param { Size } size - Default size of the image. This parameter does not affect the size of the received image.
     *     The actual returned size is determined by the producer, for example, the camera.
     * @param { ImageFormat } format - Image format, which is a constant of
     *     [ImageFormat]{@link @ohos.multimedia.image:image.ImageFormat}. (Currently, only **ImageFormat:JPEG** is
     *     supported. The format actually returned is determined by the producer, for example, camera.)
     * @param { number } capacity - Maximum number of images that can be accessed at the same time. This parameter is used
     *     only as an expected value. The actual capacity is determined by the device hardware.
     * @returns { ImageReceiver } ImageReceiver instance.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types;
     * @syscap SystemCapability.Multimedia.Image.ImageReceiver
     * @since 11
     */
    function createImageReceiver(size: Size, format: ImageFormat, capacity: number): ImageReceiver;
    /**
     * Creates an ImageReceiver instance.
     *
     * @param { ImageReceiverOptions } [options] Initialization options for the ImageReceiver.
     * @returns { ImageReceiver | undefined } ImageReceiver instance created. If the operation fails, undefined is
     *     returned.
     * @throws { BusinessError } 7900201 - Invalid parameter.
     * @syscap SystemCapability.Multimedia.Image.ImageReceiver
     * @stagemodelonly
     * @since 23
     */
    function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined;
    /**
     * Creates an ImageCreator instance by specifying the image width, height, format, and capacity.
     * Images occupy a large amount of memory. When you finish using an ImageCreator instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageCreator#release} to free the memory promptly. Before releasing the instance, ensure
     * that all asynchronous operations associated with the instance have finished and the instance is no longer needed.
     *
     * @param { number } width - Default image width, in px.
     * @param { number } height - Default image height, in px.
     * @param { number } format - Image format, for example, YCBCR_422_SP or JPEG.
     * @param { number } capacity - Maximum number of images that can be accessed at the same time. This parameter is used
     *     only as an expected value. The actual capacity is determined by the device hardware.
     * @returns { ImageCreator } ImageCreator instance.
     * @syscap SystemCapability.Multimedia.Image.ImageCreator
     * @since 9
     * @deprecated since 11
     * @useinstead image.createImageCreator(size: Size, format: ImageFormat, capacity: int)
     */
    function createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator;
    /**
     * Creates an ImageCreator instance by specifying the image size, format, and capacity.
     * Images occupy a large amount of memory. When you finish using an ImageCreator instance, call
     * [release]{@link @ohos.multimedia.image:image.ImageCreator#release} to free the memory promptly. Before releasing the instance, ensure
     * that all asynchronous operations associated with the instance have finished and the instance is no longer needed.
     *
     * @param { Size } size - Default size of the image.
     * @param { ImageFormat } format - Image format, for example, YCBCR_422_SP or JPEG.
     * @param { number } capacity - Maximum number of images that can be accessed at the same time. This parameter is used
     *     only as an expected value. The actual capacity is determined by the device hardware.
     * @returns { ImageCreator } ImageCreator instance.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types;
     * @syscap SystemCapability.Multimedia.Image.ImageCreator
     * @since 11
     */
    function createImageCreator(size: Size, format: ImageFormat, capacity: number): ImageCreator;
    /**
     * The **PixelMap** class provides APIs to read or write image data and obtain image information. Before calling any
     * API in PixelMap, you must use
     * [image.createPixelMap]{@link @ohos.multimedia.image:image.createPixelMap(colors: ArrayBuffer, options: InitializationOptions)}
     * to create a PixelMap object. Currently, the maximum size of a serialized PixelMap is 128 MB. A larger size will
     * cause a display failure. The size is calculated as follows: Width × Height ×
     * [Bytes per pixel]{@link @ohos.multimedia.image:image.PixelMapFormat}.
     * Since API version 11, PixelMap supports cross-thread calls through [Worker]{@link @ohos.worker}. If a PixelMap
     * object is invoked by another thread through [Worker]{@link @ohos.worker}, all APIs of the PixelMap object cannot be
     * called in the original thread. Otherwise, error 501 is reported, indicating that the server cannot complete the
     * request.
     * Before calling any API in PixelMap, you can use
     * [image.createPixelMap]{@link @ohos.multimedia.image:image.createPixelMap(colors: ArrayBuffer, options: InitializationOptions)}
     * to pass pixel data to create a PixelMap object, or use [ImageSource]{@link @ohos.multimedia.image:image} to decode
     * an image to a PixelMap object.
     * To develop an atomic service, use [ImageSource]{@link @ohos.multimedia.image:image} to create a PixelMap object.
     * Images occupy a large amount of memory. When you finish using a PixelMap instance, call
     * [release]{@link image.PixelMap.release()} to free the memory promptly. Before releasing the instance, ensure that
     * all asynchronous operations associated with the instance have finished and the instance is no longer needed.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 7
     */
    interface PixelMap {
        /**
         * Whether the image pixels are editable. **true** if editable, **false** otherwise. The value **false** provides
         * better image rendering and transmission performance.<br>
         * This API can be used in atomic services since API version 11.<br>
         * This API can be used in ArkTS widgets since API version 12.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        readonly isEditable: boolean;
        /**
         * Reads all the pixel data from the PixelMap and writes the data to a buffer.
         * The resulting data will be in the same pixel format as the PixelMap.
         *
         * @param { ArrayBuffer } dst - The buffer to receive the pixel data from the PixelMap.
         * @returns { Promise<void> } A Promise that resolves when the operation completes.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600206 - Invalid parameter. Possible cause: Size of the buffer is too small.
         * @throws { BusinessError } 7600302 - Failed to copy the memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        readAllPixelsToBuffer(dst: ArrayBuffer): Promise<void>;
        /**
         * Reads all the pixel data from the PixelMap and writes the data to a buffer.
         * The resulting data will be in the same pixel format as the PixelMap.
         *
         * @param { ArrayBuffer } dst - The buffer to receive the pixel data from the PixelMap.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600206 - Invalid parameter. Possible cause: Size of the buffer is too small.
         * @throws { BusinessError } 7600302 - Failed to copy the memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        readAllPixelsToBufferSync(dst: ArrayBuffer): void;
        /**
         * Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer.
         * This API uses a promise to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link readAllPixelsToBuffer} instead for better exception handling capabilities.
         *
         * @param { ArrayBuffer } dst - Buffer to which the pixels will be written. The buffer size is obtained by calling
         *     [getPixelBytesNumber]{@link image.PixelMap.getPixelBytesNumber}.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        readPixelsToBuffer(dst: ArrayBuffer): Promise<void>;
        /**
         * Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer.
         * This API uses an asynchronous callback to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link readAllPixelsToBuffer} instead for better exception handling capabilities.
         *
         * @param { ArrayBuffer } dst - Buffer to which the pixels will be written. The buffer size is obtained by calling
         *     [getPixelBytesNumber]{@link image.PixelMap.getPixelBytesNumber}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void;
        /**
         * Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer.
         * This API returns the result synchronously.
         *
         * Starting from API 26.0.0, it is recommended to use {@link readAllPixelsToBufferSync} instead for better exception handling capabilities.
         *
         * @param { ArrayBuffer } dst - Buffer to which the pixels will be written. The buffer size is obtained by calling
         *     [getPixelBytesNumber]{@link image.PixelMap.getPixelBytesNumber}.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @form
         * @atomicservice
         * @since 12
         */
        readPixelsToBufferSync(dst: ArrayBuffer): void;
        /**
         * Reads pixel data from a certain area of the PixelMap to a buffer. The resulting data will be in BGRA_8888 format.
         *
         * @param { PositionArea } area - Area of the PixelMap to read the data.
         *     Data will be read from the PixelMap and copied into PositionArea.pixels.
         * @returns { Promise<void> } A Promise that resolves when the operation completes.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         *     Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range.
         * @throws { BusinessError } 7600302 - Failed to copy the memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        readPixelsToArea(area: PositionArea): Promise<void>;
        /**
         * Reads pixel data from a certain area of the PixelMap to a buffer. The resulting data will be in BGRA_8888 format.
         *
         * @param { PositionArea } area - Area of the PixelMap to read the data.
         *     Data will be read from the PixelMap and copied into PositionArea.pixels.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         *     Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range.
         * @throws { BusinessError } 7600302 - Failed to copy the memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        readPixelsToAreaSync(area: PositionArea): void;
        /**
         * Reads the pixels in the area specified by [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.region
         * of this PixelMap object in the BGRA_8888 format and writes the data to the
         * [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.pixels buffer. This API uses a promise to return
         * the result.
         * You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.
         * YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U
         * component + 0.25 * V component)
         * RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G
         * component + 1 * B component + 1 * A component)
         *
         * Starting from API 26.0.0, it is recommended to use {@link readPixelsToArea} instead for better exception handling capabilities.
         *
         * @param { PositionArea } area - Area from which the pixels will be read.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        readPixels(area: PositionArea): Promise<void>;
        /**
         * Reads the pixels in the area specified by [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.region
         * of this PixelMap object in the BGRA_8888 format and writes the data to the
         * [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.pixels buffer. This API uses an asynchronous
         * callback to return the result.
         * You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.
         * YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U
         * component + 0.25 * V component)
         * RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G
         * component + 1 * B component + 1 * A component)
         *
         * Starting from API 26.0.0, it is recommended to use {@link readPixelsToArea} instead for better exception handling capabilities.
         *
         * @param { PositionArea } area - Area from which the pixels will be read.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        readPixels(area: PositionArea, callback: AsyncCallback<void>): void;
        /**
         * Reads the pixels in the area specified by [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.region
         * of this PixelMap object in the BGRA_8888 format and writes the data to the
         * [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.pixels buffer. This API returns the result
         * synchronously.
         *
         * Starting from API 26.0.0, it is recommended to use {@link readPixelsToAreaSync} instead for better exception handling capabilities.
         *
         * @param { PositionArea } area - Area from which the pixels will be read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        readPixelsSync(area: PositionArea): void;
        /**
         * Writes data from a buffer to a certain area of the PixelMap. The source data must be in BGRA_8888 format.
         *
         * @param { PositionArea } area - Area of the PixelMap to write the data.
         *     Data will be copied from PositionArea.pixels to the PixelMap.
         * @returns { Promise<void> } A Promise that resolves when the operation completes.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is not editable or is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         *     Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range.
         * @throws { BusinessError } 7600302 - Failed to copy the memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        writePixelsFromArea(area: PositionArea): Promise<void>;
        /**
         * Writes data from a buffer to a certain area of the PixelMap. The source data must be in BGRA_8888 format.
         *
         * @param { PositionArea } area - Area of the PixelMap to write the data.
         *     Data will be copied from PositionArea.pixels to the PixelMap.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is not editable or is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         *     Possible causes: 1. PositionArea.pixels is too small. 2. PositionArea.region is out of range.
         * @throws { BusinessError } 7600302 - Failed to copy the memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        writePixelsFromAreaSync(area: PositionArea): void;
        /**
         * Reads the pixels in the [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.region buffer in the
         * BGRA_8888 format and writes the data to the area specified by
         * [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.pixels in this PixelMap object. This API uses a
         * promise to return the result.
         * You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.
         * YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U
         * component + 0.25 * V component)
         * RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G
         * component + 1 * B component + 1 * A component)
         *
         * Starting from API 26.0.0, it is recommended to use {@link writePixelsFromArea} instead for better exception handling capabilities.
         *
         * @param { PositionArea } area - Area to which the pixels will be written.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        writePixels(area: PositionArea): Promise<void>;
        /**
         * Reads the pixels in the [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.region buffer in the
         * BGRA_8888 format and writes the data to the area specified by
         * [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.pixels in this PixelMap object. This API uses an
         * asynchronous callback to return the result.
         * You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.
         * YUV region calculation formula: region to read (region.size{width * height}) * 1.5 (1 * Y component + 0.25 * U
         * component + 0.25 * V component)
         * RGBA region calculation formula: region to read (region.size{width * height}) * 4 (1 * R component + 1 * G
         * component + 1 * B component + 1 * A component)
         *
         * Starting from API 26.0.0, it is recommended to use {@link writePixelsFromArea} instead for better exception handling capabilities.
         *
         * @param { PositionArea } area - Area to which the pixels will be written.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        writePixels(area: PositionArea, callback: AsyncCallback<void>): void;
        /**
         * Reads the pixels in the [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.region buffer in the
         * BGRA_8888 format and writes the data to the area specified by
         * [PositionArea]{@link @ohos.multimedia.image:image.PositionArea}.pixels in this PixelMap object. This API returns
         * the result synchronously.
         *
         * Starting from API 26.0.0, it is recommended to use {@link writePixelsFromAreaSync} instead for better exception handling capabilities.
         *
         * @param { PositionArea } area - Area to which the pixels will be written.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @form
         * @atomicservice
         * @since 12
         */
        writePixelsSync(area: PositionArea): void;
        /**
         * Reads the pixel data from a buffer and writes the data to the PixelMap.
         * The source data must be in the same pixel format as the PixelMap.
         *
         * @param { ArrayBuffer } src - The buffer that contains pixel data to be written to the PixelMap.
         * @returns { Promise<void> } A Promise that resolves when the operation completes.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is not editable or is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter. Possible cause: Size of the buffer is too small.
         * @throws { BusinessError } 7600302 - Failed to copy the memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        writeAllPixelsFromBuffer(src: ArrayBuffer): Promise<void>;
        /**
         * Reads the pixel data from a buffer and writes the data to the PixelMap.
         * The source data must be in the same pixel format as the PixelMap.
         *
         * @param { ArrayBuffer } src - The buffer that contains pixel data to be written to the PixelMap.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is not editable or is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter. Possible cause: Size of the buffer is too small.
         * @throws { BusinessError } 7600302 - Failed to copy the memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        writeAllPixelsFromBufferSync(src: ArrayBuffer): void;
        /**
         * Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object.
         * This API uses a promise to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link writeAllPixelsFromBuffer} instead for better exception handling capabilities.
         *
         * @param { ArrayBuffer } src - Buffer from which the pixels are read. The buffer size is obtained by calling
         *     [getPixelBytesNumber]{@link image.PixelMap.getPixelBytesNumber}.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        writeBufferToPixels(src: ArrayBuffer): Promise<void>;
        /**
         * Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object.
         * This API uses an asynchronous callback to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link writeAllPixelsFromBuffer} instead for better exception handling capabilities.
         *
         * @param { ArrayBuffer } src - Buffer from which the pixels are read. The buffer size is obtained by calling
         *     [getPixelBytesNumber]{@link image.PixelMap.getPixelBytesNumber}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the pixels in the buffer are
         *     successfully written to the PixelMap, **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void;
        /**
         * Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object.
         * This API returns the result synchronously.
         *
         * Starting from API 26.0.0, it is recommended to use {@link writeAllPixelsFromBufferSync} instead for better exception handling capabilities.
         *
         * @param { ArrayBuffer } src - Buffer from which the pixels are read. The buffer size is obtained by calling
         *     [getPixelBytesNumber]{@link image.PixelMap.getPixelBytesNumber}.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        writeBufferToPixelsSync(src: ArrayBuffer): void;
        /**
         * Convert pixelmap to standard dynamic range.
         *
         * @returns { Promise<void> } A Promise instance used to return the operation result. If the operation fails, an error message is returned.
         * @throws { BusinessError } 62980137 - Invalid image operation.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        toSdr(): Promise<void>;
        /**
         * Obtains the image information of a PixelMap. This API uses a promise to return the result.
         *
         * @returns { Promise<ImageInfo> } Promise used to return the image information.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        getImageInfo(): Promise<ImageInfo>;
        /**
         * Obtains the image information. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<ImageInfo> } callback - Callback used to return the result. If the operation is successful
         *     , **err** is **undefined** and **data** is the image information obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        getImageInfo(callback: AsyncCallback<ImageInfo>): void;
        /**
         * Obtains the image information. This API returns the result synchronously.
         *
         * @returns { ImageInfo } Image information.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @form
         * @atomicservice
         * @since 12
         */
        getImageInfoSync(): ImageInfo;
        /**
         * Obtains the number of bytes per row of this image. Unit: bytes.
         *
         * @returns { number } Number of bytes per row.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        getBytesNumberPerRow(): number;
        /**
         * Obtains the total number of bytes of this image. Unit: bytes.
         *
         * @returns { number } Total number of bytes.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        getPixelBytesNumber(): number;
        /**
         * Obtains the pixel density of this image. Unit: ppi (pixels/inch)
         *
         * @returns { number } Pixel density, in ppi.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        getDensity(): number;
        /**
         * Sets opacity of the PixelMap. Every pixel will be set to the same opacity value.
         *
         * @param { number } value - The target opacity value to be set. Unit: Percentage, Value range: (0,1].
         *     The valid range is (0.0, 1.0] where 1.0 is fully opaque and becoming transparent as it approaches 0.0.
         * @returns { Promise<void> } A Promise that resolves when the operation completes.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter. Possible cause: The specified value is out of range.
         * @throws { BusinessError } 7600207 - Unsupported data format. Possible cause: Alpha type is not supported.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        setOpacity(value: number): Promise<void>;
        /**
         * Sets opacity of the PixelMap. Every pixel will be set to the same opacity value.
         *
         * @param { number } value - The target opacity value to be set. Unit: Percentage, Value range: (0,1].
         *     The valid range is (0.0, 1.0] where 1.0 is fully opaque and becoming transparent as it approaches 0.0.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter. Possible cause: The specified value is out of range.
         * @throws { BusinessError } 7600207 - Unsupported data format. Possible cause: Alpha type is not supported.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        setOpacitySync(value: number): void;
        /**
         * Sets an opacity rate for this image. This API uses an asynchronous callback to return the result. It is invalid
         * for YUV images.
         *
         * Starting from API 26.0.0, it is recommended to use {@link setOpacity} instead for better exception handling capabilities.
         *
         * @param { number } rate - Opacity rate. The value range is (0,1].
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        opacity(rate: number, callback: AsyncCallback<void>): void;
        /**
         * Sets an opacity rate for this image. It is invalid for YUV images. This API uses a promise to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link setOpacity} instead for better exception handling capabilities.
         *
         * @param { number } rate - Opacity rate. The value range is (0,1].
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        opacity(rate: number): Promise<void>;
        /**
         * Sets an opacity rate for this image. This API returns the result synchronously. It is invalid for YUV images.
         *
         * Starting from API 26.0.0, it is recommended to use {@link setOpacitySync} instead for better exception handling capabilities.
         *
         * @param { number } rate - Opacity rate. The value range is (0,1].
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        opacitySync(rate: number): void;
        /**
         * Extracts the alpha channel from the current PixelMap to create a new ALPHA_U8 format PixelMap.
         *
         * @returns { Promise<PixelMap> } A Promise of the new ALPHA_U8 format PixelMap.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The current PixelMap has been released.
         * @throws { BusinessError } 7600106 - The current PixelMap has been passed across threads.
         * @throws { BusinessError } 7600305 - Failed to create the PixelMap.
         *     Possible cause: Current PixelMap data is corrupted.
         * @throws { BusinessError } 7600306 - Failed to convert the data.
         *     Possible causes: 1. Failed to perform pixel format conversion. 2. The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        extractAlphaPixelMap(): Promise<PixelMap>;
        /**
         * Extracts the alpha channel from the current PixelMap to create a new ALPHA_U8 format PixelMap.
         *
         * @returns { PixelMap } A new ALPHA_U8 format PixelMap.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The current PixelMap has been released.
         * @throws { BusinessError } 7600106 - The current PixelMap has been passed across threads.
         * @throws { BusinessError } 7600305 - Failed to create the PixelMap.
         *     Possible cause: Current PixelMap data is corrupted.
         * @throws { BusinessError } 7600306 - Failed to convert the data.
         *     Possible causes: 1. Failed to perform pixel format conversion. 2. The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        extractAlphaPixelMapSync(): PixelMap;
        /**
         * Creates a PixelMap object that contains only the alpha channel information. This object can be used for the
         * shadow effect. It is invalid for YUV images. This API uses a promise to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link extractAlphaPixelMap} instead for better exception handling capabilities.
         *
         * @returns { Promise<PixelMap> } Promise used to return the PixelMap object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        createAlphaPixelmap(): Promise<PixelMap>;
        /**
         * Creates a PixelMap object that contains only the alpha channel information. This object can be used for the
         * shadow effect. It is invalid for YUV images. This API returns the result through a callback.
         *
         * Starting from API 26.0.0, it is recommended to use {@link extractAlphaPixelMap} instead for better exception handling capabilities.
         *
         * @param { AsyncCallback<PixelMap> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void;
        /**
         * Creates a PixelMap object that contains only the alpha channel information. This object can be used for the
         * shadow effect. This API returns the result synchronously. It is invalid for YUV images.
         *
         * Starting from API 26.0.0, it is recommended to use {@link extractAlphaPixelMapSync} instead for better exception handling capabilities.
         *
         * @returns { PixelMap } PixelMap object. If the operation fails, an error is thrown.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        createAlphaPixelmapSync(): PixelMap;
        /**
         * Scales the PixelMap in the horizontal and/or vertical dimensions.
         *
         * @param { number } x - The scale ratio of width. Unit: Percentage.
         * @param { number } y - The scale ratio of height. Unit: Percentage.
         * @param { AntiAliasingLevel } [level] - The anti-aliasing algorithm to be used. Default value: NONE.
         * @returns { Promise<void> } A Promise that resolves when the operation completes.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         * @throws { BusinessError } 7600301 - Failed to allocate memory.
         *     Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        applyScale(x: number, y: number, level?: AntiAliasingLevel): Promise<void>;
        /**
         * Scales the PixelMap in the horizontal and/or vertical dimensions.
         *
         * @param { number } x - The scale ratio of width. Unit: Percentage.
         * @param { number } y - The scale ratio of height. Unit: Percentage.
         * @param { AntiAliasingLevel } [level] - The anti-aliasing algorithm to be used. Default value: NONE.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         * @throws { BusinessError } 7600301 - Failed to allocate memory.
         *     Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        applyScaleSync(x: number, y: number, level?: AntiAliasingLevel): void;
        /**
         * Scales this image based on the scale factors of the width and height. This API uses an asynchronous callback to
         * return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyScale} instead for better exception handling capabilities.
         *
         * @param { number } x - Scale factor of the width.
         * @param { number } y - Scale factor of the height.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        scale(x: number, y: number, callback: AsyncCallback<void>): void;
        /**
         * Scales this image based on the scale factors of the width and height. This API uses a promise to return the
         * result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyScale} instead for better exception handling capabilities.
         *
         * @param { number } x - Scale factor of the width.
         * @param { number } y - Scale factor of the height.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        scale(x: number, y: number): Promise<void>;
        /**
         * Scales this image based on the scale factors of the width and height. This API returns the result synchronously.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyScaleSync} instead for better exception handling capabilities.
         *
         * @param { number } x - Scale factor of the width.
         * @param { number } y - Scale factor of the height.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        scaleSync(x: number, y: number): void;
        /**
         * Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This
         * API uses a promise to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyScale} instead for better exception handling capabilities.
         *
         * @param { number } x - Scale factor of the width.
         * @param { number } y - Scale factor of the height.
         * @param { AntiAliasingLevel } level - Anti-aliasing level.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @form
         * @atomicservice
         * @since 12
         */
        scale(x: number, y: number, level: AntiAliasingLevel): Promise<void>;
        /**
         * Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This
         * API returns the result synchronously.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyScaleSync} instead for better exception handling capabilities.
         *
         * @param { number } x - Scale factor of the width.
         * @param { number } y - Scale factor of the height.
         * @param { AntiAliasingLevel } level - Anti-aliasing level.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        scaleSync(x: number, y: number, level: AntiAliasingLevel): void;
        /**
         * Creates an image that has been resized based on the specified anti-aliasing level and the scale factors of the
         * width and height. This API uses a promise to return the result.
         *
         * @param { number } x - Scale factor of the width.
         * @param { number } y - Scale factor of the height.
         * @param { AntiAliasingLevel } level - Anti-aliasing level. The default value is **AntiAliasingLevel.NONE**.
         * @returns { Promise<PixelMap> } Promise used to return the PixelMap object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 18
         */
        createScaledPixelMap(x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>;
        /**
         * Creates an image that has been resized based on the specified anti-aliasing level and the scale factors of the
         * width and height. This API returns the result synchronously.
         *
         * @param { number } x - Scale factor of the width.
         * @param { number } y - Scale factor of the height.
         * @param { AntiAliasingLevel } level - Anti-aliasing level. The default value is **AntiAliasingLevel.NONE**.
         * @returns { PixelMap } PixelMap object. If the operation fails, an error is thrown.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 18
         */
        createScaledPixelMapSync(x: number, y: number, level?: AntiAliasingLevel): PixelMap;
        /**
         * Repositions the PixelMap in the horizontal and/or vertical directions.
         *
         * @param { number } x - The distance in pixels to move in the horizontal direction. Unit: px.
         * @param { number } y - The distance in pixels to move in the vertical direction. Unit: px.
         * @returns { Promise<void> } A Promise that resolves when the operation completes.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         * @throws { BusinessError } 7600301 - Failed to allocate memory.
         *     Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        applyTranslate(x: number, y: number): Promise<void>;
        /**
         * Repositions the PixelMap in the horizontal and/or vertical directions.
         *
         * @param { number } x - The distance in pixels to move in the horizontal direction. Unit: px.
         * @param { number } y - The distance in pixels to move in the vertical direction. Unit: px.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         * @throws { BusinessError } 7600301 - Failed to allocate memory.
         *     Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        applyTranslateSync(x: number, y: number): void;
        /**
         * Translates this image based on given coordinates. This API uses an asynchronous callback to return the result.
         * The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and
         * height not exceed the width and height of the screen.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyTranslate} instead for better exception handling capabilities.
         *
         * @param { number } x - X coordinate to translate, in px.
         * @param { number } y - Y coordinate to translate, in px.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        translate(x: number, y: number, callback: AsyncCallback<void>): void;
        /**
         * Translates a PixelMap based on given coordinates. This API uses a promise to return the result.
         * The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and
         * height not exceed the width and height of the screen.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyTranslate} instead for better exception handling capabilities.
         *
         * @param { number } x - X coordinate to translate, in px.
         * @param { number } y - Y coordinate to translate, in px.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        translate(x: number, y: number): Promise<void>;
        /**
         * Translates this image based on given coordinates. This API returns the result synchronously.
         * The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and
         * height not exceed the width and height of the screen.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyTranslateSync} instead for better exception handling capabilities.
         *
         * @param { number } x - X coordinate to translate, in px.
         * @param { number } y - Y coordinate to translate, in px.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        translateSync(x: number, y: number): void;
        /**
         * Rotates the PixelMap.
         *
         * Note: YUV format PixelMaps only support rotation angles that are multiples of 90 degrees.
         *
         * @param { number } angle - The rotation angle in degrees. Unit: Degree.
         * @returns { Promise<void> } A Promise that resolves when the operation completes.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         * @throws { BusinessError } 7600301 - Failed to allocate memory.
         *     Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        applyRotate(angle: number): Promise<void>;
        /**
         * Rotates the PixelMap.
         *
         * Note: YUV format PixelMaps only support rotation angles that are multiples of 90 degrees.
         *
         * @param { number } angle - The rotation angle in degrees. Unit: Degree.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         * @throws { BusinessError } 7600301 - Failed to allocate memory.
         *     Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        applyRotateSync(angle: number): void;
        /**
         * Rotates this image based on a given angle. This API uses an asynchronous callback to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyRotate} instead for better exception handling capabilities.
         *
         * @param { number } angle - Angle to rotate. Unit: degrees.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        rotate(angle: number, callback: AsyncCallback<void>): void;
        /**
         * Rotates a PixelMap based on a given angle. This API uses a promise to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyRotate} instead for better exception handling capabilities.
         *
         * @param { number } angle - Angle to rotate. Unit: degrees.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        rotate(angle: number): Promise<void>;
        /**
         * Rotates this image based on a given angle. This API returns the result synchronously.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyRotateSync} instead for better exception handling capabilities.
         *
         * @param { number } angle - Angle to rotate. Unit: degrees.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        rotateSync(angle: number): void;
        /**
         * Flips the PixelMap in the horizontal and/or vertical directions.
         *
         * @param { boolean } horizontal - Whether to flip horizontally.
         * @param { boolean } vertical - Whether to flip vertically.
         * @returns { Promise<void> } A Promise that resolves when the operation completes.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         * @throws { BusinessError } 7600301 - Failed to allocate memory. Possible cause: The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        applyFlip(horizontal: boolean, vertical: boolean): Promise<void>;
        /**
         * Flips the PixelMap in the horizontal and/or vertical directions.
         *
         * @param { boolean } horizontal - Whether to flip horizontally.
         * @param { boolean } vertical - Whether to flip vertically.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         * @throws { BusinessError } 7600301 - Failed to allocate memory. Possible cause: The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        applyFlipSync(horizontal: boolean, vertical: boolean): void;
        /**
         * Flips this image horizontally or vertically, or both. This API uses an asynchronous callback to return the
         * result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyFlip} instead for better exception handling capabilities.
         *
         * @param { boolean } horizontal - Whether to flip the image horizontally. **true** to flip the image horizontally,
         *     **false** otherwise.
         * @param { boolean } vertical - Whether to flip the image vertically. **true** to flip the image vertically,
         *     **false** otherwise.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void;
        /**
         * Flips a PixelMap based on a given angle. This API uses a promise to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyFlip} instead for better exception handling capabilities.
         *
         * @param { boolean } horizontal - Whether to flip the image horizontally. **true** to flip the image horizontally,
         *     **false** otherwise.
         * @param { boolean } vertical - Whether to flip the image vertically. **true** to flip the image vertically,
         *     **false** otherwise.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        flip(horizontal: boolean, vertical: boolean): Promise<void>;
        /**
         * Flips this image horizontally or vertically, or both. This API returns the result synchronously.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyFlipSync} instead for better exception handling capabilities.
         *
         * @param { boolean } horizontal - Whether to flip the image horizontally. **true** to flip the image horizontally,
         *     **false** otherwise.
         * @param { boolean } vertical - Whether to flip the image vertically. **true** to flip the image vertically,
         *     **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        flipSync(horizontal: boolean, vertical: boolean): void;
        /**
         * Crops the PixelMap.
         *
         * @param { Region } region - The region to crop.
         * @returns { Promise<void> } A Promise that resolves when the operation completes.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600204 - The specified region is invalid or out of range.
         * @throws { BusinessError } 7600301 - Failed to allocate memory.
         *     Possible causes: 1. Failed to process pixel data. 2. The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        applyCrop(region: Region): Promise<void>;
        /**
         * Crops the PixelMap.
         *
         * @param { Region } region - The region to crop.
         * @throws { BusinessError } 7600104 - Failed to get image data.
         *     Possible cause: Internal data is corrupted. Please check the logs for detailed information.
         * @throws { BusinessError } 7600105 - The PixelMap has been released.
         * @throws { BusinessError } 7600106 - The PixelMap has been passed to another thread.
         * @throws { BusinessError } 7600201 - Unsupported operation because the PixelMap is locked.
         * @throws { BusinessError } 7600204 - The specified region is invalid or out of range.
         * @throws { BusinessError } 7600301 - Failed to allocate memory.
         *     Possible causes: 1. Failed to process pixel data. 2. The system is out of memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @crossplatform
         * @form
         * @atomicservice
         * @since 26.0.0
         */
        applyCropSync(region: Region): void;
        /**
         * Crops this image based on a given size. This API uses an asynchronous callback to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyCrop} instead for better exception handling capabilities.
         *
         * @param { Region } region - Size of the image after cropping. The value cannot exceed the width or height of the
         *     image.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        crop(region: Region, callback: AsyncCallback<void>): void;
        /**
         * Crops a PixelMap based on a given size. This API uses a promise to return the result.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyCrop} instead for better exception handling capabilities.
         *
         * @param { Region } region - Size of the image after cropping. The value cannot exceed the width or height of the
         *     image.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        crop(region: Region): Promise<void>;
        /**
         * Crops this image based on a given size. This API returns the result synchronously.
         *
         * Starting from API 26.0.0, it is recommended to use {@link applyCropSync} instead for better exception handling capabilities.
         *
         * @param { Region } region - Size of the image after cropping. The value cannot exceed the width or height of the
         *     image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        cropSync(region: Region): void;
        /**
         * Obtains the color space of this image.
         *
         * @returns { colorSpaceManager.ColorSpaceManager } Color space obtained.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980103 - The image data is not supported.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 11]
         * @since 10
         */
        getColorSpace(): colorSpaceManager.ColorSpaceManager;
        /**
         * Marshals this PixelMap object and writes it to a MessageSequence object.
         *
         * @param { rpc.MessageSequence } sequence - MessageSequence object.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @throws { BusinessError } 62980097 - IPC error. Possible cause: 1.IPC communication failed. 2. Image upload
         *     exception.
         *     3. Decode process exception. 4. Insufficient memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        marshalling(sequence: rpc.MessageSequence): void;
        /**
         * Unmarshals a MessageSequence object to obtain a PixelMap object. To create a PixelMap object in synchronous mode,
         * use [createPixelMapFromParcel]{@link @ohos.multimedia.image:image.createPixelMapFromParcel}.
         *
         * @param { rpc.MessageSequence } sequence - MessageSequence object that stores the PixelMap information.
         * @returns { Promise<PixelMap> } Promise used to return the PixelMap object.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @throws { BusinessError } 62980097 - IPC error. Possible cause: 1.IPC communication failed. 2. Image upload
         *     exception.
         *     3. Decode process exception. 4. Insufficient memory.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>;
        /**
         * Set color space of pixel map.
         *
         * This method is only used to set the colorspace property of pixelmap, while all pixel data remains the same after calling this method.
         * If you want to change colorspace for all pixels, use method {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager)} or
         * {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager, AsyncCallback<void>)}.
         *
         * @param { colorSpaceManager.ColorSpaceManager } colorSpace The color space for pixel map.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 10
         */
        /**
         * Set color space of pixel map.
         *
         * This method is only used to set the colorspace property of pixelmap, while all pixel data remains the same after calling this method.
         * If you want to change colorspace for all pixels, use method {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager)} or
         * {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager, AsyncCallback<void>)}.
         *
         * @param { colorSpaceManager.ColorSpaceManager } colorSpace The color space for pixel map.
         * @throws { BusinessError } 62980111 - If the operation invalid.
         * @throws { BusinessError } 62980115 - If the image parameter invalid.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        /**
         * Set color space of pixel map.
         *
         * This method is only used to set the colorspace property of pixelmap, while all pixel data remains the same after calling this method.
         * If you want to change colorspace for all pixels, use method {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager)} or
         * {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager, AsyncCallback<void>)}.
         *
         * @param { colorSpaceManager.ColorSpaceManager } colorSpace The color space for pixel map.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980115 - If the image parameter invalid.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 12
         */
        setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void;
        /**
         * Whether the row data of the image is memory aligned. The value **true** means that the row data is memory-aligned
         * , and there may be blank bytes padded at the end of each row to meet alignment requirements. The value **false**
         * means that the row data is not memory-aligned, and rows are packed contiguously with no padding bytes at the end.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 11
         */
        readonly isStrideAlignment: boolean;
        /**
         * Performs color space conversion (CSC) on the image pixel color based on a given color space. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { colorSpaceManager.ColorSpaceManager } targetColorSpace - Target color space. SRGB, DCI_P3, DISPLAY_P3,
         *     and ADOBE_RGB_1998 are supported.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 62980104 - Failed to initialize the internal object.
         * @throws { BusinessError } 62980108 - Failed to convert the color space.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void;
        /**
         * Performs Color Space Converters (CSC) on the image pixel color based on a given color space. This API uses a
         * promise to return the result.
         *
         * @param { colorSpaceManager.ColorSpaceManager } targetColorSpace - Target color space. SRGB, DCI_P3, DISPLAY_P3,
         *     and ADOBE_RGB_1998 are supported.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 62980104 - Failed to initialize the internal object.
         * @throws { BusinessError } 62980108 - Failed to convert the color space.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform
         * @since 11
         */
        applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>;
        /**
         * The method is used for the transformation of the image formats. Pixel data will be changed by calling this method.
         *
         * @param { PixelMapFormat } targetPixelFormat - The pixel format for pixelmap conversion.
         * @returns { Promise<void> } A Promise instance used to return the operation result. If the operation fails, an error message is returned.
         * @throws { BusinessError } 62980115 - Invalid input parameter.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980274 - The conversion failed.
         * @throws { BusinessError } 62980276 - The type to be converted is an unsupported target pixel format.
         * @throws { BusinessError } 62980178 - Failed to create the pixelmap.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>;
        /**
         * Releases this PixelMap instance. After the release, any attempt to access the internal data of this object will
         * fail. This API uses an asynchronous callback to return the result.
         * Images occupy a large amount of memory. When you finish using a PixelMap instance, call this API to free the
         * memory promptly.
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * > **NOTE**
         * >
         * > Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied
         * > by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this PixelMap instance. After the release, any attempt to access the internal data of this object will
         * fail. This API uses a promise to return the result.
         * Images occupy a large amount of memory. When you finish using a PixelMap instance, call this API to free the
         * memory promptly.
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * > **NOTE**
         * >
         * > Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied
         * > by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        release(): Promise<void>;
        /**
         * Sets whether to detach from the original thread when this PixelMap is transmitted across threads. This API
         * applies to the scenario where the PixelMap needs to be released immediately.
         *
         * @param { boolean } detached - Whether to detach from the original thread. **true** to detach, **false**
         *     otherwise.
         * @throws { BusinessError } 501 - Resource Unavailable.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        setTransferDetached(detached: boolean): void;
        /**
         * Obtains the value of the metadata with a given key in this PixelMap.
         *
         * @param { HdrMetadataKey } key - Key of the HDR metadata.
         * @returns { HdrMetadataValue } Value of the metadata with the given key.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource unavailable.
         * @throws { BusinessError } 62980173 - The DMA memory does not exist.
         * @throws { BusinessError } 62980302 - Memory copy failed. Possibly caused by invalid metadata value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        getMetadata(key: HdrMetadataKey): HdrMetadataValue;
        /**
         * Sets a memory name for this PixelMap.
         *
         * @param { string } name - Memory name, which can be set only for a PixelMap with the DMA or ASHMEM memory format.
         *     The name length for DMA memory settings should be within the range of 1 to 255 bytes. For ASHMEM memory
         *     settings, the name length should be within the range of 1 to 244 bytes.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.The length of the input parameter is too
         *     long.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource unavailable.
         * @throws { BusinessError } 62980286 - Memory format not supported.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        setMemoryNameSync(name: string): void;
        /**
         * Copies this PixelMap object. This API returns the result synchronously.
         *
         * @returns { PixelMap } PixelMap object. If the operation fails, an error is thrown.
         * @throws { BusinessError } 501 - Resource unavailable.
         * @throws { BusinessError } 62980102 - Image malloc abnormal. This status code is thrown when an error occurs
         *     during the process of copying data.
         * @throws { BusinessError } 62980103 - Image YUV And ASTC types are not supported.
         * @throws { BusinessError } 62980104 - Image initialization abnormal.
         *     This status code is thrown when an error occurs during the process of creating empty pixelmap.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 18
         */
        cloneSync(): PixelMap;
        /**
         * Copies this PixelMap object. This API uses a promise to return the result.
         *
         * @returns { Promise<PixelMap> } Promise used to return the PixelMap object.
         * @throws { BusinessError } 501 - Resource unavailable.
         * @throws { BusinessError } 62980102 - Image malloc abnormal. This status code is thrown when an error occurs
         *     during the process of copying data.
         * @throws { BusinessError } 62980103 - Image YUV And ASTC types are not supported.
         * @throws { BusinessError } 62980104 - Image initialization abnormal.
         *     This status code is thrown when an error occurs during the process of creating empty pixelmap.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 18
         */
        clone(): Promise<PixelMap>;
        /**
         * Sets the value for the metadata with a given key in this PixelMap. This API uses a promise to return the result.
         *
         * @param { HdrMetadataKey } key - Key of the HDR metadata.
         * @param { HdrMetadataValue } value - Value of the metadata.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 501 - Resource unavailable.
         * @throws { BusinessError } 62980173 - The DMA memory does not exist.
         * @throws { BusinessError } 62980302 - Memory copy failed. Possibly caused by invalid metadata value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>;
        /**
         * Checks whether this PixelMap object is released. If released, any attempt to access the internal data of this
         * object will fail.
         *
         * > **NOTE**
         * >
         * > Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied
         * > by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.
         *
         * @returns { boolean } Check result for whether the PixelMap object is released. **true** if released; **false**
         *     otherwise.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 22
         */
        isReleased(): boolean;
        /**
         * Obtains the unique ID of this PixelMap.
         *
         * @returns { number } Unique ID. The value is a positive integer.
         * @throws { BusinessError } 7600201 - The PixelMap has been released.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 22
         */
        getUniqueId(): number;
        /**
         * Creates an image that has been cropped and resized based on the specified cropping area, scale factors of the
         * width and height, and anti-aliasing level. This API returns the result synchronously.
         *
         * @param { Region } region - Area to crop. It must be within the original image's dimension (in pixels).
         * @param { number } x - Scale factor of the width. It must not be **0**.
         * @param { number } y - Scale factor of the height. It must not be **0**.
         * @param { AntiAliasingLevel } [level] - Anti-aliasing level. Default value: **NONE**.
         * @returns { PixelMap } PixelMap object. If the operation fails, an error is thrown.
         * @throws { BusinessError } 7600201 - The PixelMap has been released.
         * @throws { BusinessError } 7600204 - Invalid region.
         * @throws { BusinessError } 7600205 - Unsupported memory format or pixel format.
         * @throws { BusinessError } 7600301 - Memory alloc failed.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 22
         */
        createCroppedAndScaledPixelMapSync(region: Region, x: number, y: number, level?: AntiAliasingLevel): PixelMap;
        /**
         * Creates an image that has been cropped and resized based on the specified cropping area, scale factors of the
         * width and height, and anti-aliasing level. This API uses a promise to return the result.
         *
         * @param { Region } region - Area to crop. It must be within the original image's dimension (in pixels).
         * @param { number } x - Scale factor of the width. It must not be **0**.
         * @param { number } y - Scale factor of the height. It must not be **0**.
         * @param { AntiAliasingLevel } [level] - Anti-aliasing level. Default value: **NONE**.
         * @returns { Promise<PixelMap> } Promise used to return the PixelMap object.
         * @throws { BusinessError } 7600201 - The PixelMap has been released.
         * @throws { BusinessError } 7600204 - Invalid region.
         * @throws { BusinessError } 7600205 - Unsupported memory format or pixel format.
         * @throws { BusinessError } 7600301 - Memory alloc failed.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 22
         */
        createCroppedAndScaledPixelMap(region: Region, x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>;
    }
    /**
     * Describes compose parameters.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    interface HdrComposeOptions {
        /**
         * Pixel format used for composite image, RGBA_1010102\YCBCR_P010\YCRCB_P010 are supported.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        desiredPixelFormat?: PixelMapFormat;
    }
    /**
     * An image that contains special information can be decoded into a picture object, which generally contains the main
     * picture, auxiliary picture, and metadata. The main picture contains most information about the image and is mainly
     * used to render the image. The auxiliary picture is used to store data related to but different from the main
     * picture, revealing more comprehensive details. The metadata is generally used to store information about the image
     * file. The picture object class is used to read or write picture objects. Before calling any API in Picture, you
     * must use [image.createPicture]{@link @ohos.multimedia.image:image.createPicture} to create a Picture object.
     *
     * Images occupy a large amount of memory. When you finish using a Picture instance, call
     * [release]{@link image.Picture.release} to free the memory promptly. Before releasing the instance, ensure that all
     * asynchronous operations associated with the instance have finished and the instance is no longer needed.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 13
     */
    interface Picture {
        /**
         * Obtains the PixelMap object of the main picture. This API returns the result synchronously.
         *
         * @returns { PixelMap } PixelMap object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        getMainPixelmap(): PixelMap;
        /**
         * Generates a High Dynamic Range (HDR) image and obtains its PixelMap object. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<PixelMap> } Promise used to return the PixelMap object.
         * @throws { BusinessError } 7600901 - Inner unknown error. Please check the logs for detailed information.
         * @throws { BusinessError } 7600201 - Unsupported operation. e.g.,1. The picture does not has a gainmap.
         *     2. MainPixelMap's allocator type is not DMA.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        getHdrComposedPixelmap(): Promise<PixelMap>;
        /**
         * Composites an HDR image and returns PixelMap of the image. Composition options (such as PixelMapFormat) can be
         * passed. This API uses a promise to return the result.
         *
         * The Picture object that calls this API must contain the main picture, gain map, and metadata.
         *
         * @param { HdrComposeOptions } [options] - Options for HDR composition.
         * @returns { Promise<PixelMap | undefined> } Promise, which returns the PixelMap object or **undefined**.
         * @throws { BusinessError } 7600201 - Unsupported operation.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>;
        /**
         * Obtains the PixelMap object of the gain map.
         *
         * @returns { PixelMap | null } PixelMap object obtained. If there is no PixelMap object, null is returned.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        getGainmapPixelmap(): PixelMap | null;
        /**
         * Sets an auxiliary picture.
         *
         * @param { AuxiliaryPictureType } type - Type of the auxiliary picture.
         * @param { AuxiliaryPicture } auxiliaryPicture - AuxiliaryPicture object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void;
        /**
         * Obtains an auxiliary picture by type.
         *
         * @param { AuxiliaryPictureType } type - Type of the auxiliary picture.
         * @returns { AuxiliaryPicture | null } AuxiliaryPicture object. If there is no AuxiliaryPicture object, null is
         *     returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null;
        /**
         * Sets the metadata for this Picture object. This API uses a promise to return the result.
         *
         * @param { MetadataType } metadataType - Metadata type.
         * @param { Metadata } metadata - Metadata object.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The
         *     metadata type does not match the auxiliary picture type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>;
        /**
         * Obtains the metadata of this Picture object. This API uses a promise to return the result.
         *
         * @param { MetadataType } metadataType - Metadata type.
         * @returns { Promise<Metadata> } Promise used to return the metadata.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The
         *     metadata type does not match the auxiliary picture type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        getMetadata(metadataType: MetadataType): Promise<Metadata>;
        /**
         * Marshals this Picture object and writes it to a MessageSequence object.
         *
         * @param { rpc.MessageSequence } sequence - MessageSequence object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 62980097 - IPC error. Possible cause: 1.IPC communication failed. 2. Image upload
         *     exception.
         *     3. Decode process exception. 4. Insufficient memory.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        marshalling(sequence: rpc.MessageSequence): void;
        /**
         * Releases this Picture object.
         *
         * Images occupy a large amount of memory. When you finish using a Picture instance, call this API to free the
         * memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        release(): void;
        /**
         * Invokes the VPE algorithm to compose the main pixelmap and gainmap. The composed result will replace the
         * main pixelmap of the current picture object.
         *
         * The Picture object that calls this API must contain the main pixelmap, gain map.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7600201 - Unsupported operation. e.g.,1. The picture does not have a gainmap.
         *     2. pixelMap's allocator type is not DMA.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        hdrComposeToMainPixelmap(): Promise<void>;
    }
    /**
     * Creates a Picture object based on a main PixelMap.
     *
     * Images occupy a large amount of memory. When you finish using a Picture instance, call
     * [release]{@link @ohos.multimedia.image:image.Picture.release} to free the memory promptly. Before releasing the
     * instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no
     * longer needed.
     *
     * @param { PixelMap } mainPixelmap - Main PixelMap.
     * @returns { Picture } Picture object.
     * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types; 3.Parameter verification failed.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 13
     */
    function createPicture(mainPixelmap: PixelMap): Picture;
    /**
     * Creates a Picture object from a MessageSequence object.
     *
     * Images occupy a large amount of memory. When you finish using a Picture instance, call
     * [release]{@link @ohos.multimedia.image:image.Picture.release} to free the memory promptly. Before releasing the
     * instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no
     * longer needed.
     *
     * @param { rpc.MessageSequence } sequence - MessageSequence object that stores the Picture information.
     * @returns { Picture } Picture object.
     * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 62980097 - IPC error. Possible cause: 1.IPC communication failed. 2. Image upload
     *     exception.
     *     3. Decode process exception. 4. Insufficient memory.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 13
     */
    function createPictureFromParcel(sequence: rpc.MessageSequence): Picture;
    /**
     * Creates an AuxiliaryPicture instance based on the ArrayBuffer image data, auxiliary picture size, and auxiliary
     * picture type. This API accepts only continuous pixel data in BGRA format and will create an auxiliary picture in
     * RGBA format.
     *
     * Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call
     * [release]{@link @ohos.multimedia.image:image.AuxiliaryPicture.release} to free the memory promptly. Before
     * releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the
     * instance is no longer needed.
     *
     * @param { ArrayBuffer } buffer - Image data stored in the buffer.
     * @param { Size } size - Size of the auxiliary picture, in px.
     * @param { AuxiliaryPictureType } type - Type of the auxiliary picture.
     * @returns { AuxiliaryPicture } AuxiliaryPicture instance.
     * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types; 3.Parameter verification failed.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 13
     */
    function createAuxiliaryPicture(buffer: ArrayBuffer, size: Size, type: AuxiliaryPictureType): AuxiliaryPicture;
    /**
     * Create an <b>AuxiliaryPicture</b> object, the memory type used by the AuxiliaryPicture can be specified by
     * allocatorType {@link IMAGE_ALLOCATOR_TYPE}. By default, the system selects the memory type based on the image type,
     * image size, platform capability, etc. When processing the AuxiliaryPicture returned by this interface, please
     * always consider the impact of stride. The created auxiliary picture is initialized with the input pixels.
     *
     * @param { AuxiliaryPictureInfo } auxiliaryPictureInfo - The basic information of the auxiliary picture.
     * @param { AllocatorType } [allocatorType] - Memory type.
     * @param { ArrayBuffer } [pixels] - Pixel data used to initialize the auxiliary picture.
     * @returns { AuxiliaryPicture } The AuxiliaryPicture object.
     * @throws { BusinessError } 7600205 - Unsupported allocator type, e.g., use shared memory to create a gainmap as
     *     only DMA supported hdr metadata.
     * @throws { BusinessError } 7600206 - Invalid parameter, size.height or size.width is less than or equal to 0.
     * @throws { BusinessError } 7600301 - Alloc memory failed.
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 24
     */
    function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo, allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture;
    /**
     * AuxiliaryPicture instance.
     *
     * @typedef AuxiliaryPicture
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 13
     */
    /**
     * The **AuxiliaryPicture** class is used to read or write auxiliary picture data of an image and obtain auxiliary
     * picture information of an image. The supported types of auxiliary pictures can be found in
     * [AuxiliaryPictureType]{@link @ohos.multimedia.image:image.AuxiliaryPictureType}.
     *
     * Before calling any API in AuxiliaryPicture, you must create an AuxiliaryPicture instance using
     * [image.createAuxiliaryPicture]{@link @ohos.multimedia.image:image.createAuxiliaryPicture} or
     * [getAuxiliaryPicture]{@link @ohos.multimedia.image:image.Picture.getAuxiliaryPicture} in Picture.
     *
     * Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call
     * [release]{@link image.AuxiliaryPicture.release} to free the memory promptly. Before releasing the instance, ensure
     * that all asynchronous operations associated with the instance have finished and the instance is no longer needed.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 13
     */
    interface AuxiliaryPicture {
        /**
         * Reads pixels from an ArrayBuffer and writes the data to this AuxiliaryPicture object. This API uses a promise to
         * return the result.
         *
         * @param { ArrayBuffer } data - Pixels of the auxiliary picture.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        writePixelsFromBuffer(data: ArrayBuffer): Promise<void>;
        /**
         * Reads pixels of this auxiliary picture and writes the data to an ArrayBuffer. This API uses a promise to return
         * the result.
         *
         * @returns { Promise<ArrayBuffer> } Promise used to return the pixels of the auxiliary picture.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        readPixelsToBuffer(): Promise<ArrayBuffer>;
        /**
         * Obtains the type of this auxiliary picture.
         *
         * @returns { AuxiliaryPictureType } Type of the auxiliary picture.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        getType(): AuxiliaryPictureType;
        /**
         * Sets the metadata for this auxiliary picture. This API uses a promise to return the result.
         *
         * @param { MetadataType } metadataType - Metadata type, which is used to set the corresponding metadata.
         * @param { Metadata } metadata - Metadata object.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The
         *     metadata type does not match the auxiliary picture type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>;
        /**
         * Obtains the metadata of this auxiliary picture. This API uses a promise to return the result.
         *
         * @param { MetadataType } metadataType - Metadata type, which is used to obtain metadata of the corresponding type.
         * @returns { Promise<Metadata> } Promise that returns the metadata.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The
         *     metadata type does not match the auxiliary picture type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        getMetadata(metadataType: MetadataType): Promise<Metadata>;
        /**
         * Obtains the auxiliary picture information.
         *
         * @returns { AuxiliaryPictureInfo } Auxiliary picture information.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        getAuxiliaryPictureInfo(): AuxiliaryPictureInfo;
        /**
         * Sets the auxiliary picture information.
         *
         * @param { AuxiliaryPictureInfo } info - Auxiliary picture information.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void;
        /**
         * Releases this AuxiliaryPicture object. No value is returned.
         *
         * Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call this API to free
         * the memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        release(): void;
    }
    /**
     * Enumerates the auxiliary pictures types.
     *
     * Auxiliary pictures do not directly participate in image display, and not all images contain auxiliary pictures.
     *
     * Before obtaining and using a specific auxiliary picture, call
     * [getAuxiliaryPicture]{@link @ohos.multimedia.image:image.Picture.getAuxiliaryPicture} in Picture to obtain the
     * auxiliary picture.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 13
     */
    enum AuxiliaryPictureType {
        /**
         * Gain map.
         *
         * It is used to generate HDR images more accurately.
         *
         * HDR synthesis usually involves using the SDR main image, gain map, and
         * [HDR metadata]{@link @ohos.multimedia.image:image.PixelMap.getMetadata} to calculate the luminance mapping.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        GAINMAP = 1,
        /**
         * Depth map.
         *
         * It is used to store the distance between each pixel and the camera, and provides the 3D structure of the scene.
         *
         * It is useful for tasks like 3D reconstruction, background separation, and scene understanding.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        DEPTH_MAP = 2,
        /**
         * Unrefocus map.
         *
         * It is used to store the pixel content that is not refocused during capture.
         *
         * It is useful for post-processing effects such as portrait blurring, allowing users to select focus areas freely.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        UNREFOCUS_MAP = 3,
        /**
         * Linear map.
         *
         * It records lighting, color, or other visual elements linearly, providing additional data for image processing.
         *
         * It is useful for visual effect enhancement and color post-processing.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        LINEAR_MAP = 4,
        /**
         * Fragment map.
         *
         * It records areas of the original image obscured by watermarks. These areas might be cropped from the original
         * image or filled with placeholder pixel data.
         *
         * It is useful for watermark removal and original image restoration.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        FRAGMENT_MAP = 5,
        /**
         * LHDR gain map.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
        */
        LHDR_GAINMAP = 10
    }
    /**
     * Enumerates image metadata types.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 13
     */
    enum MetadataType {
        /**
         * Exif data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        EXIF_METADATA = 1,
        /**
         * Fragment map metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        FRAGMENT_METADATA = 2,
        /**
         * GIF image metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 20
         */
        GIF_METADATA = 5,
        /**
         * Metadata of a HEIFS image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        HEIFS_METADATA = 15,
        /**
         * Metadata of a DNG image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        DNG_METADATA = 16,
        /**
         * Metadata of a WebP image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        WEBP_METADATA = 17,
        /**
        * Metadata of a PNG image.
        *
        * @syscap SystemCapability.Multimedia.Image.Core
        * @stagemodelonly
        * @since 26.0.0
        */
        PNG_METADATA = 19,
        /**
         * Metadata of a JFIF image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        JFIF_METADATA = 20,
        /**
         * Metadata of a TIFF image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        TIFF_METADATA = 21,
        /**
         * XMP metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        XMP_METADATA = 22,
        /**
         * Metadata of a Avis image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        AVIS_METADATA = 23
    }
    /**
     * The **Metadata** class provides APIs for storing image metadata. For details about the supported metadata types,
     * see [MetadataType]{@link @ohos.multimedia.image:image.MetadataType}.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 13
     */
    interface Metadata {
        /**
         * Obtains the values of properties from the image's metadata. This API uses a promise to return the result.
         * For details about how to query the property values, see
         * [PropertyKey]{@link @ohos.multimedia.image:image.PropertyKey},
         * [FragmentMapPropertyKey]{@link @ohos.multimedia.image:image.FragmentMapPropertyKey},
         * [GifPropertyKey]{@link @ohos.multimedia.image:image.GifPropertyKey}, and
         * [HeifsPropertyKey]{@link @ohos.multimedia.image:image.HeifsPropertyKey}.
         *
         * @param { Array<string> } key - Names of the properties.
         * @returns { Promise<Record<string, string | null>> } Promise used to return the property values. If the operation
         *     fails, an error code is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The
         *     metadata type does not match the auxiliary picture type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        getProperties(key: Array<string>): Promise<Record<string, string | null>>;
        /**
         * Sets the values of properties for the image's metadata. This API uses a promise to return the result.
         *
         * For details about how to query the property values, see
         * [PropertyKey]{@link @ohos.multimedia.image:image.PropertyKey},
         * [FragmentMapPropertyKey]{@link @ohos.multimedia.image:image.FragmentMapPropertyKey},
         * [GifPropertyKey]{@link @ohos.multimedia.image:image.GifPropertyKey}, and
         * [HeifsPropertyKey]{@link @ohos.multimedia.image:image.HeifsPropertyKey}.
         *
         * @param { Record<string, string | null> } records - Array of properties and their values.
         * @returns { Promise<void> } Promise that returns no value. If the operation fails, an error code is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The
         *     metadata type does not match the auxiliary picture type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        setProperties(records: Record<string, string | null>): Promise<void>;
        /**
         * Obtains all properties and values from the image's metadata. This API uses a promise to return the result.
         *
         * For details about how to query the property values, see
         * [PropertyKey]{@link @ohos.multimedia.image:image.PropertyKey},
         * [FragmentMapPropertyKey]{@link @ohos.multimedia.image:image.FragmentMapPropertyKey},
         * [GifPropertyKey]{@link @ohos.multimedia.image:image.GifPropertyKey}, and
         * [HeifsPropertyKey]{@link @ohos.multimedia.image:image.HeifsPropertyKey}.
         *
         * @returns { Promise<Record<string, string | null>> } Promise used to return the values of all properties.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        getAllProperties(): Promise<Record<string, string | null>>;
        /**
         * Clones the metadata. This API uses a promise to return the result.
         *
         * @returns { Promise<Metadata> } Promise used to return the metadata instance.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        clone(): Promise<Metadata>;
        /**
         * Obtains the metadata in binary format. This API uses a promise to return the result.
         *
         * @returns { Promise<ArrayBuffer> } Promise that returns the binary data of the metadata.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getBlob(): Promise<ArrayBuffer>;
        /**
         * Replaces the current metadata with binary data. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } blob - Binary data used to replace the metadata.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7600206 - Invalid parameter. Possible causes: The blob is empty or has a length of 0.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        setBlob(blob: ArrayBuffer): Promise<void>;
    }
    /**
     * Enumerates the fragment map information.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 13
     */
    enum FragmentMapPropertyKey {
        /**
         * X coordinate of the top-left corner of the fragment map in the original image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        X_IN_ORIGINAL = 'XInOriginal',
        /**
         * Y coordinate of the top-left corner of the fragment map in the original image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        Y_IN_ORIGINAL = 'YInOriginal',
        /**
         * Width of the fragment map.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        WIDTH = 'FragmentImageWidth',
        /**
         * Height of the fragment map.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        HEIGHT = 'FragmentImageHeight'
    }
    /**
     * Enumerates the GIF image information.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 20
     */
    enum GifPropertyKey {
        /**
         * Duration for playing each frame of a GIF image, in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 20
         */
        GIF_DELAY_TIME = 'GifDelayTime',
        /**
         * Disposal type of each frame in a GIF image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 20
         */
        GIF_DISPOSAL_TYPE = 'GifDisposalType',
        /**
         * Whether the GIF image has a global color map.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        GIF_HAS_GLOBAL_COLOR_MAP = 'GifHasGlobalColorMap',
        /**
         * Canvas width.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        GIF_CANVAS_WIDTH = 'GifCanvasWidth',
        /**
         * Canvas height.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        GIF_CANVAS_HEIGHT = 'GifCanvasHeight',
        /**
         * Loop count.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        GIF_LOOP_COUNT = 'GifLoopCount',
        /**
         * Unclamped delay of each frame in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        GIF_UNCLAMPED_DELAY_TIME = 'GifUnclampedDelayTime'
    }
    /**
     * Enumerates the properties available for the metadata of a HEIFS image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    enum HeifsPropertyKey {
        /**
         * Playback duration of each frame in an HEIF image sequence, in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        HEIFS_DELAY_TIME = 'HeifsDelayTime',
        /**
         * Unclamped delay of each frame in milliseconds.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        HEIFS_UNCLAMPED_DELAY_TIME = 'HeifsUnclampedDelayTime',
        /**
         * Canvas height.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        HEIFS_CANVAS_HEIGHT = 'HeifsCanvasHeight',
        /**
         * Canvas width.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        HEIFS_CANVAS_WIDTH = 'HeifsCanvasWidth'
    }
    /**
     * Enumerates the properties available for the metadata of a DNG image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 24
     */
    enum DngPropertyKey {
        /**
         * The DNG version.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        DNG_VERSION = 'DNGVersion',
        /**
         * The DNG backward version.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        DNG_BACKWARD_VERSION = 'DNGBackwardVersion',
        /**
         * A unique camera model.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        UNIQUE_CAMERA_MODEL = 'UniqueCameraModel',
        /**
         * A localized camera model.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        LOCALIZED_CAMERA_MODEL = 'LocalizedCameraModel',
        /**
         * The CFA (color filter array) plane color.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CFA_PLANE_COLOR = 'CFAPlaneColor',
        /**
         * The CFA (color filter array) layout.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CFA_LAYOUT = 'CFALayout',
        /**
         * The linearization table.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        LINEARIZATION_TABLE = 'LinearizationTable',
        /**
         * The black level repeat dimension.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        BLACK_LEVEL_REPEAT_DIM = 'BlackLevelRepeatDim',
        /**
         * The zero light encoding level.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        BLACK_LEVEL = 'BlackLevel',
        /**
         * The black level delta H.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        BLACK_LEVEL_DELTA_H = 'BlackLevelDeltaH',
        /**
         * The black level delta V.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        BLACK_LEVEL_DELTA_V = 'BlackLevelDeltaV',
        /**
         * The white level.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        WHITE_LEVEL = 'WhiteLevel',
        /**
         * The default scale.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        DEFAULT_SCALE = 'DefaultScale',
        /**
         * The default crop origin.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        DEFAULT_CROP_ORIGIN = 'DefaultCropOrigin',
        /**
         * The default crop size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        DEFAULT_CROP_SIZE = 'DefaultCropSize',
        /**
         * A transformation matrix under the first calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        COLOR_MATRIX1 = 'ColorMatrix1',
        /**
         * A transformation matrix under the second calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        COLOR_MATRIX2 = 'ColorMatrix2',
        /**
         * A calibration matrix under the first calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CAMERA_CALIBRATION1 = 'CameraCalibration1',
        /**
         * A calibration matrix under the second calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CAMERA_CALIBRATION2 = 'CameraCalibration2',
        /**
         * A dimensionality reduction matrix under the first calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        REDUCTION_MATRIX1 = 'ReductionMatrix1',
        /**
         * A dimensionality reduction matrix under the second calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        REDUCTION_MATRIX2 = 'ReductionMatrix2',
        /**
         * The analog balance.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        ANALOG_BALANCE = 'AnalogBalance',
        /**
         * The as-shot neutral.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        AS_SHOT_NEUTRAL = 'AsShotNeutral',
        /**
         * The as-shot white, encoded as X‑Y chromaticity coordinates.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        AS_SHOT_WHITEXY = 'AsShotWhiteXY',
        /**
         * The baseline exposure.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        BASELINE_EXPOSURE = 'BaselineExposure',
        /**
         * The baseline noise.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        BASELINE_NOISE = 'BaselineNoise',
        /**
         * The baseline sharpness.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        BASELINE_SHARPNESS = 'BaselineSharpness',
        /**
         * The Bayer green split.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        BAYER_GREEN_SPLIT = 'BayerGreenSplit',
        /**
         * The linear response limit.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        LINEAR_RESPONSE_LIMIT = 'LinearResponseLimit',
        /**
         * The serial number of the camera.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CAMERA_SERIAL_NUMBER = 'CameraSerialNumber',
        /**
         * Information about the lens.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        LENS_INFO = 'LensInfo',
        /**
         * The chroma blur radius.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CHROMA_BLUR_RADIUS = 'ChromaBlurRadius',
        /**
         * The anti-alias strength.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        ANTI_ALIAS_STRENGTH = 'AntiAliasStrength',
        /**
         * The shadow scale.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        SHADOW_SCALE = 'ShadowScale',
        /**
         * The private data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        DNG_PRIVATE_DATA = 'DNGPrivateData',
        /**
         * Whether the EXIF MakerNote tag is safe.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        MAKER_NOTE_SAFETY = 'MakerNoteSafety',
        /**
         * The first calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CALIBRATION_ILLUMINANT1 = 'CalibrationIlluminant1',
        /**
         * The second calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CALIBRATION_ILLUMINANT2 = 'CalibrationIlluminant2',
        /**
         * The best quality scale.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        BEST_QUALITY_SCALE = 'BestQualityScale',
        /**
         * The unique identifier of raw image data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        RAW_DATA_UNIQUE_ID = 'RawDataUniqueID',
        /**
         * The original raw file name.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        ORIGINAL_RAW_FILE_NAME = 'OriginalRawFileName',
        /**
         * The original raw file data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        ORIGINAL_RAW_FILE_DATA = 'OriginalRawFileData',
        /**
         * The active area.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        ACTIVE_AREA = 'ActiveArea',
        /**
         * The masked areas.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        MASKED_AREAS = 'MaskedAreas',
        /**
         * An ICC profile.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        AS_SHOT_ICC_PROFILE = 'AsShotICCProfile',
        /**
         * The as-shot pre-profile matrix.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        AS_SHOT_PRE_PROFILE_MATRIX = 'AsShotPreProfileMatrix',
        /**
         * The current ICC profile.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CURRENT_ICC_PROFILE = 'CurrentICCProfile',
        /**
         * The current pre-profile matrix.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CURRENT_PRE_PROFILE_MATRIX = 'CurrentPreProfileMatrix',
        /**
         * The colorimetric reference.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        COLORIMETRIC_REFERENCE = 'ColorimetricReference',
        /**
         * The camera calibration signature.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CAMERA_CALIBRATION_SIGNATURE = 'CameraCalibrationSignature',
        /**
         * The profile calibration signature.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_CALIBRATION_SIGNATURE = 'ProfileCalibrationSignature',
        /**
         * The extra camera profiles.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        EXTRA_CAMERA_PROFILES = 'ExtraCameraProfiles',
        /**
         * The "as-shot" camera profile.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        AS_SHOT_PROFILE_NAME = 'AsShotProfileName',
        /**
         * The applied noise reduction.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        NOISE_REDUCTION_APPLIED = 'NoiseReductionApplied',
        /**
         * The profile name.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_NAME = 'ProfileName',
        /**
         * The profile hue/saturation map dimensions.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_HUE_SAT_MAP_DIMS = 'ProfileHueSatMapDims',
        /**
         * The first hue/saturation mapping table data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_HUE_SAT_MAP_DATA1 = 'ProfileHueSatMapData1',
        /**
         * The second hue/saturation mapping table data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_HUE_SAT_MAP_DATA2 = 'ProfileHueSatMapData2',
        /**
         * The profile tone curve.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_TONE_CURVE = 'ProfileToneCurve',
        /**
         * The profile embed policy.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_EMBED_POLICY = 'ProfileEmbedPolicy',
        /**
         * The profile copyright.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_COPYRIGHT = 'ProfileCopyright',
        /**
         * The first forward matrix.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        FORWARD_MATRIX1 = 'ForwardMatrix1',
        /**
         * The second forward matrix.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        FORWARD_MATRIX2 = 'ForwardMatrix2',
        /**
         * The preview application name.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PREVIEW_APPLICATION_NAME = 'PreviewApplicationName',
        /**
         * The preview application version.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PREVIEW_APPLICATION_VERSION = 'PreviewApplicationVersion',
        /**
         * The preview settings name.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PREVIEW_SETTINGS_NAME = 'PreviewSettingsName',
        /**
         * The preview settings digest.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PREVIEW_SETTINGS_DIGEST = 'PreviewSettingsDigest',
        /**
         * The preview color space.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PREVIEW_COLOR_SPACE = 'PreviewColorSpace',
        /**
         * The preview date time.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PREVIEW_DATE_TIME = 'PreviewDateTime',
        /**
         * An MD5 digest of the raw image data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        RAW_IMAGE_DIGEST = 'RawImageDigest',
        /**
         * An MD5 digest of the data stored in the OriginalRawFileData.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        ORIGINAL_RAW_FILE_DIGEST = 'OriginalRawFileDigest',
        /**
         * The sub‑tile block size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        SUB_TILE_BLOCK_SIZE = 'SubTileBlockSize',
        /**
         * The row interleave factor.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        ROW_INTERLEAVE_FACTOR = 'RowInterleaveFactor',
        /**
         * The profile look table dimensions.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_LOOK_TABLE_DIMS = 'ProfileLookTableDims',
        /**
         * The profile look table data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_LOOK_TABLE_DATA = 'ProfileLookTableData',
        /**
         * The first opcode list.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        OPCODE_LIST1 = 'OpcodeList1',
        /**
         * The second opcode list.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        OPCODE_LIST2 = 'OpcodeList2',
        /**
         * The third opcode list.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        OPCODE_LIST3 = 'OpcodeList3',
        /**
         * The noise profile.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        NOISE_PROFILE = 'NoiseProfile',
        /**
         * The original default final size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        ORIGINAL_DEFAULT_FINAL_SIZE = 'OriginalDefaultFinalSize',
        /**
         * The original best quality final size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        ORIGINAL_BEST_QUALITY_FINAL_SIZE = 'OriginalBestQualityFinalSize',
        /**
         * The original default crop size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        ORIGINAL_DEFAULT_CROP_SIZE = 'OriginalDefaultCropSize',
        /**
         * The profile hue/saturation map encoding.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_HUE_SAT_MAP_ENCODING = 'ProfileHueSatMapEncoding',
        /**
         * The profile look table encoding.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        PROFILE_LOOK_TABLE_ENCODING = 'ProfileLookTableEncoding',
        /**
         * The baseline exposure offset.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        BASELINE_EXPOSURE_OFFSET = 'BaselineExposureOffset',
        /**
         * The default black render.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        DEFAULT_BLACK_RENDER = 'DefaultBlackRender',
        /**
         * A modified MD5 digest of the raw image data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        NEW_RAW_IMAGE_DIGEST = 'NewRawImageDigest',
        /**
         * The gain between the main raw IFD and the preview IFD.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        RAW_TO_PREVIEW_GAIN = 'RawToPreviewGain',
        /**
         * The default user crop.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        DEFAULT_USER_CROP = 'DefaultUserCrop'
    }
    /**
     * Enumerates the properties available for the metadata of a TIFF image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum TiffPropertyKey {
        /**
         * Compression scheme used for image data (e.g., None, LZW, JPEG, Deflate).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        COMPRESSION = 'TiffCompression',
        /**
         * Defines how pixel colors are interpreted (e.g., RGB, grayscale).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        PHOTOMETRIC_INTERPRETATION = 'TiffPhotometricInterpretation',
        /**
         * Tone transfer curve mapping pixel values to output intensity.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        TRANSFER_FUNCTION = 'TiffTransferFunction',
        /**
         * Indicates image orientation for correct display rotation/flip.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        ORIENTATION = 'TiffOrientation',
        /**
         * Horizontal resolution (pixels per resolution unit).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        X_RESOLUTION = 'TiffXResolution',
        /**
         * Vertical resolution (pixels per resolution unit).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        Y_RESOLUTION = 'TiffYResolution',
        /**
         * Unit for X/Y resolution.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        RESOLUTION_UNIT = 'TiffResolutionUnit',
        /**
         * Chromaticity coordinates of the reference white point.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        WHITE_POINT = 'TiffWhitePoint',
        /**
         * Chromaticity coordinates of the RGB primaries.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        PRIMARY_CHROMATICITIES = 'TiffPrimaryChromaticities',
        /**
         * Height of each image tile in pixels.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        TILE_LENGTH = 'TiffTileLength',
        /**
         * Width of each image tile in pixels.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        TILE_WIDTH = 'TiffTileWidth',
        /**
         * Name of the document or image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        DOCUMENT_NAME = 'TiffDocumentName',
        /**
         * Description of the image content.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        IMAGE_DESCRIPTION = 'TiffImageDescription',
        /**
         * Name of the image creator or artist.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        ARTIST = 'TiffArtist',
        /**
         * Copyright notice for the image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        COPYRIGHT = 'TiffCopyright',
        /**
         * Date and time associated with the image (typically last modification).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        DATE_TIME = 'TiffDateTime',
        /**
         * Manufacturer of the capture device.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        MAKE = 'TiffMake',
        /**
         * Model name/number of the capture device.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        MODEL = 'TiffModel',
        /**
         * Software used to create or process the image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        SOFTWARE = 'TiffSoftware',
        /**
         * Host computer/system used for image processing.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        HOST_COMPUTER = 'TiffHostComputer'
    }
    /**
     * Enumerates the properties available for the metadata of a JFIF image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum JfifPropertyKey {
        /**
         * JFIF x density.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        X_DENSITY = 'JfifXDensity',
        /**
         * JFIF y density.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        Y_DENSITY = 'JfifYDensity',
        /**
         * JFIF density unit.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        DENSITY_UNIT = 'JfifDensityUnit',
        /**
         * JFIF version.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        VERSION = 'JfifVersion',
        /**
         * whether the JFIF image is progressive.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        IS_PROGRESSIVE = 'JfifIsProgressive'
    }
    /**
     * Enumerates the properties available for the metadata of a PNG image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum PngPropertyKey {
        /**
         * PNG x pixels per meter.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        X_PIXELS_PER_METER = 'PngXPixelsPerMeter',
        /**
         * PNG y pixels per meter.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        Y_PIXELS_PER_METER = 'PngYPixelsPerMeter',
        /**
         * PNG gamma.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        GAMMA = 'PngGamma',
        /**
         * PNG interlacing mode.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        INTERLACE_TYPE = 'PngInterlaceType',
        /**
         * PNG sRGB rendering intent.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        SRGB_INTENT = 'PngSRGBIntent',
        /**
         * PNG color primary/white-point coordinates.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        CHROMATICITIES = 'PngChromaticities',
        /**
         * PNG title.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        TITLE = 'PngTitle',
        /**
         * PNG description.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        DESCRIPTION = 'PngDescription',
        /**
         * PNG comment.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        COMMENT = 'PngComment',
        /**
         * PNG disclaimer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        DISCLAIMER = 'PngDisclaimer',
        /**
         * PNG warning.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        WARNING = 'PngWarning',
        /**
         * PNG author.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        AUTHOR = 'PngAuthor',
        /**
         * PNG copyright.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        COPYRIGHT = 'PngCopyright',
        /**
         * PNG creation time.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        CREATION_TIME = 'PngCreationTime',
        /**
         * PNG modification time.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        MODIFICATION_TIME = 'PngModificationTime',
        /**
         * PNG software.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        SOFTWARE = 'PngSoftware'
    }
    /**
     * HeifsMetadata implements Metadata
     *
     * HEIF image sequence metadata.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    class HeifsMetadata implements Metadata {
        /**
         * Playback duration of each frame in an HEIF image sequence, in ms.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        readonly heifsDelayTime?: number;
        /**
         * Canvas height.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly heifsCanvasHeight?: number;
        /**
         * Canvas width.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly heifsCanvasWidth?: number;
        /**
         * Unclamped delay of each frame in ms.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly heifsUnclampedDelayTime?: number;
        /**
         * Creates an empty [HeifsMetadata]{@link @ohos.multimedia.image:image.HeifsMetadata} instance.
         *
         * @returns { HeifsMetadata } Empty **HeifsMetadata** instance.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        static createInstance(): HeifsMetadata;
        /**
         * Obtains the property values of image metadata. This API returns the result asynchronously through a promise.
         *
         * @param { Array<string> } key - Names of the properties to query.
         * @returns { Promise<Record<string, string | null>> } Promise used to return the property values. If the operation
         *     fails, an error code is returned.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: unsupported metadata type
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getProperties(key: Array<string>): Promise<Record<string, string | null>>;
        /**
         * Sets the values of specified properties in image metadata in batches. This API returns the result asynchronously
         * through a promise.
         *
         * For details about the properties, see
         * [HeifsPropertyKey]{@link @ohos.multimedia.image:image.HeifsPropertyKey}.
         *
         * @param { Record<string, string | null> } records - Set of key-value pairs representing the **HeifsMetadata**
         *     properties and corresponding values.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: unsupported metadata type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        setProperties(records: Record<string, string | null>): Promise<void>;
        /**
         * Obtains all properties and their values from the image metadata. This API returns the result asynchronously
         * through a promise.
         *
         * For details about the properties, see
         * [HeifsPropertyKey]{@link @ohos.multimedia.image:image.HeifsPropertyKey}.
         *
         * @returns { Promise<Record<string, string | null>> } Promise used to return the values of all properties.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getAllProperties(): Promise<Record<string, string | null>>;
        /**
         * Clones the HEIFS metadata. This API returns the result asynchronously through a promise.
         *
         * @returns { Promise<HeifsMetadata> } Promise used to return the HEIFS metadata instance.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        clone(): Promise<HeifsMetadata>;
        /**
         * Obtains the metadata in binary format. This API uses a promise to return the result.
         *
         * @returns { Promise<ArrayBuffer> } Promise that returns the binary data of the metadata.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getBlob(): Promise<ArrayBuffer>;
        /**
         * Replaces the current metadata with binary data. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } blob - Binary data used to replace the metadata.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7600206 - Invalid parameter. Possible causes: The blob is empty or has a length of 0.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        setBlob(blob: ArrayBuffer): Promise<void>;
    }
    /**
     * JFIF metadata.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    class JfifMetadata {
        /**
         * JFIF x density.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly xDensity?: number;
        /**
         * JFIF y density.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly yDensity?: number;
        /**
         * JFIF density unit.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly densityUnit?: number;
        /**
         * JFIF version.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly version?: number[];
        /**
         * whether the JFIF image is progressive.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly isProgressive?: boolean;
    }
    /**
     * Gif metadata.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    class GifMetadata {
        /**
         * Delay of each frame in milliseconds.
         * Unit: ms, The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly delayTime?: number;
        /**
         * Unclamped delay of each frame in milliseconds.
         * Unit: ms, The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly unclampedDelayTime?: number;
        /**
         * whether the GIF image has a global color map.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly hasGlobalColorMap?: boolean;
        /**
         * Loop count.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly loopCount?: number;
        /**
         * Disposal type of each frame in the image.
         * 0 - No disposal specified.
         * 1 - Do not dispose.
         * 2 - Restore to background color.
         * 3 - Restore to previous.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly disposalType?: number;
        /**
         * Canvas height.
         * Unit: px, The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly canvasHeight?: number;
        /**
         * Canvas width.
         * Unit: px, The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly canvasWidth?: number;
    }
    /**
     * TIFF metadata.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    class TiffMetadata {
        /**
         * Compression scheme used for image data (e.g., None, LZW, JPEG, Deflate).
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly compression?: number;
        /**
         * Defines how pixel colors are interpreted (e.g., RGB, grayscale).
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly photometricInterpretation?: number;
        /**
         * Tone transfer curve mapping pixel values to output intensity.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly transferFunction?: string;
        /**
         * Indicates image orientation for correct display rotation/flip.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly orientation?: Orientation;
        /**
         * Horizontal resolution (pixels per resolution unit).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly xResolution?: number;
        /**
         * Vertical resolution (pixels per resolution unit).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly yResolution?: number;
        /**
         * Unit for X/Y resolution.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly resolutionUnit?: number;
        /**
         * Chromaticity coordinates of the reference white point.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly whitePoint?: number[];
        /**
         * Chromaticity coordinates of the RGB primaries.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly primaryChromaticities?: number[];
        /**
         * Height of each image tile in pixels.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly tileLength?: number;
        /**
         * Width of each image tile in pixels.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly tileWidth?: number;
        /**
         * Name of the document or image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly documentName?: string;
        /**
         * Description of the image content.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly imageDescription?: string;
        /**
         * Name of the image creator or artist.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly artist?: string;
        /**
         * Copyright notice for the image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly copyright?: string;
        /**
         * Date and time associated with the image (typically last modification).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly dateTime?: string;
        /**
         * Manufacturer of the capture device.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly make?: string;
        /**
         * Model name/number of the capture device.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly model?: string;
        /**
         * Software used to create or process the image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly software?: string;
        /**
         * Host computer/system used for image processing.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly hostComputer?: string;
    }
    /**
     * Png metadata.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    class PngMetadata {
        /**
         * PNG x pixels per meter.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly xPixelsPerMeter?: number;
        /**
         * PNG y pixels per meter.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly yPixelsPerMeter?: number;
        /**
         * PNG gamma.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly gamma?: number;
        /**
         * PNG interlacing mode.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly interlaceType?: number;
        /**
         * PNG sRGB rendering intent.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly sRGBIntent?: number;
        /**
         * PNG color primary/white-point coordinates.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly chromaticities?: number[];
        /**
         * PNG title.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly title?: string;
        /**
         * PNG description.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly description?: string;
        /**
         * PNG comment.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly comment?: string;
        /**
         * PNG disclaimer.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly disclaimer?: string;
        /**
         * PNG warning.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly warning?: string;
        /**
         * PNG author.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly author?: string;
        /**
         * PNG copyright.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly copyright?: string;
        /**
         * PNG creation time.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly creationTime?: string;
        /**
         * PNG modification time.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly modificationTime?: string;
        /**
         * PNG software.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly software?: string;
    }
    /**
     * Enumerates image orientation.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    enum Orientation {
        /**
         * The image is not rotated.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        TOP_LEFT = 1,
        /**
         * The image is mirrored horizontally.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        TOP_RIGHT = 2,
        /**
         * The image is rotated 180 degrees.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        BOTTOM_RIGHT = 3,
        /**
         * The image is mirrored vertically.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        BOTTOM_LEFT = 4,
        /**
         * The image is mirrored horizontally, then rotated 270 degrees clockwise.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        LEFT_TOP = 5,
        /**
         * The image is rotated 90 degrees clockwise.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        RIGHT_TOP = 6,
        /**
         * The image is mirrored horizontally, then rotated 90 degrees clockwise.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        RIGHT_BOTTOM = 7,
        /**
         * The image is rotated 270 degrees clockwise.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        LEFT_BOTTOM = 8
    }
    /**
     * ExifMetadata implements Metadata
     *
     * Exchangeable Image File Format (Exif) metadata.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    class ExifMetadata implements Metadata {
        /**
         * Data type of a subfile (for example, basic types such as text or image, rather than specific storage formats).
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        newSubfileType?: number;
        /**
         * Data type of a subfile. It has been deprecated. Use **newSubfileType** instead.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        subfileType?: number;
        /**
         * Image width. The unit is px.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        imageWidth?: number;
        /**
         * Image length. The unit is px.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        imageLength?: number;
        /**
         * Number of bits for each pixel component. For example, RGB has 3 components with a format of 8,8,8.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        bitsPerSample?: number[];
        /**
         * Algorithm standard for image compression.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        compression?: number;
        /**
         * Pixel composition, such as RGB (Red, Green, Blue) and YCbCr (Luma, Blue-difference Chroma, Red-difference Chroma)
         * .
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        photometricInterpretation?: number;
        /**
         * Image description.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        imageDescription?: string;
        /**
         * Manufacturer name of the capture device.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        make?: string;
        /**
         * Camera model.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        model?: string;
        /**
         * Strip storage offset of the image data, in bytes.
         * To improve the efficiency of large image access, the original pixel data is divided into multiple contiguous
         * blocks (called strips).
         * This property stores the starting offset of each strip in the file sequentially.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        stripOffsets?: number[];
        /**
         * Image orientation.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        orientation?: Orientation;
        /**
         * Number of color components per pixel, applicable to RGB and YCbCr color models.
         * Since both the models are three-component models (three color channels, or one luminance component plus two
         * chroma components), the standard value for this property is 3.
         * For JPEG-compressed images, this property will be replaced by the corresponding JPEG marker.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        samplesPerPixel?: number;
        /**
         * Number of rows per image strip.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        rowsPerStrip?: number;
        /**
         * Number of bytes in each strip after compression.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        stripByteCounts?: number[];
        /**
         * Image resolution in the width direction.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        xResolution?: number;
        /**
         * Image resolution in the height direction.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        yResolution?: number;
        /**
         * Whether the pixel components are recorded in chunked or planar format.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        planarConfiguration?: number;
        /**
         * Unit of the image resolution in the width and height directions.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        resolutionUnit?: number;
        /**
         * Transfer function for the image, which is usually used for color correction.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        transferFunction?: string;
        /**
         * Name and version number of the software used to create the image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        software?: string;
        /**
         * Date and time when the image is created.
         * In this standard, it refers to the file date and time. The value format is *YYYY:MM:DD HH:MM:SS* (24-hour clock).
         * For example, 2025:12:15 18:44:59.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        dateTime?: string;
        /**
         * Name of the person who creates the image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        artist?: string;
        /**
         * Chromaticity of the image white point.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        whitePoint?: number[];
        /**
         * Chromaticity of the image primaries.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        primaryChromaticities?: number[];
        /**
         * Image mode.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        photoMode?: number;
        /**
         * Start of Image (SOI) marker of the JPEG bitstream in interchange format.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        jpegInterchangeFormat?: number;
        /**
         * Number of bytes in the JPEG stream.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        jpegInterchangeFormatLength?: number;
        /**
         * Transformation matrix coefficients for converting RGB image data to YCbCr image data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        yCbCrCoefficients?: number[];
        /**
         * Sampling ratios of the chroma components and luminance component.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        yCbCrSubSampling?: number[];
        /**
         * Position of chroma components relative to the luminance component.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        yCbCrPositioning?: number;
        /**
         * Reference black point value and white point value.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        referenceBlackWhite?: number[];
        /**
         * Copyright notice of the image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        copyright?: string;
        /**
         * Exposure time.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        exposureTime?: number;
        /**
         * F number, for example, f/1.8.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        fNumber?: number;
        /**
         * Class used for exposure setting when the camera captures a photo.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        exposureProgram?: number;
        /**
         * Spectral sensitivity of each channel of the camera.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        spectralSensitivity?: string;
        /**
         * GPS information format version identifier.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsVersionID?: number[];
        /**
         * GPS latitude reference. For example, **N** indicates north latitude, and **S** indicates south latitude.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsLatitudeRef?: string;
        /**
         * GPS latitude.
         * The latitude is represented by three RATIONAL values (numeric values stored in fractional form), corresponding to
         * degrees, minutes, and seconds, in the **dd/1, mm/1, ss/1** format.
         * When using degrees and minutes, the minutes are stored with up to two decimal places, in the
         * **dd/1, mmmm/100, 0/1** format.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsLatitude?: number[];
        /**
         * GPS longitude reference. For example, **E** indicates east longitude, and **W** indicates west longitude.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsLongitudeRef?: string;
        /**
         * GPS longitude.
         * The longitude is represented by three RATIONAL values (numeric values stored in fractional form), corresponding
         * to degrees, minutes, and seconds, in the **dd/1, mm/1, ss/1** format.
         * When using degrees and minutes, the minutes are stored with up to two decimal places, in the
         * **dd/1, mmmm/100, 0/1** format.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsLongitude?: number[];
        /**
         * GPS altitude reference.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsAltitudeRef?: number;
        /**
         * GPS altitude based on **GPSAltitudeRef**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsAltitude?: number;
        /**
         * GPS timestamp.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsTimestamp?: number[];
        /**
         * GPS satellite used for measurement. Generally, the value is the GPS satellite's pseudo-random noise (PRN) number.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsSatellites?: string;
        /**
         * Status of the GPS receiver when the image is recorded.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsStatus?: string;
        /**
         * GPS measurement mode.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsMeasureMode?: string;
        /**
         * Dilution of Precision (DOP) of the GPS data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDop?: number;
        /**
         * Speed unit of the GPS receiver.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsSpeedRef?: string;
        /**
         * Speed of the GPS receiver.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsSpeed?: number;
        /**
         * Reference for the GPS receiver movement direction.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsTrackRef?: string;
        /**
         * Movement direction of the GPS receiver.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsTrack?: number;
        /**
         * Reference of the image orientation.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsImgDirectionRef?: string;
        /**
         * Image orientation at the time of capture.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsImgDirection?: number;
        /**
         * Geodetic data used by the GPS receiver.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsMapDatum?: string;
        /**
         * Latitude reference of the destination.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDestLatitudeRef?: string;
        /**
         * Latitude of the destination.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDestLatitude?: number[];
        /**
         * Longitude reference of the destination.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDestLongitudeRef?: string;
        /**
         * Longitude of the destination.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDestLongitude?: number[];
        /**
         * Bearing reference to the destination.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDestBearingRef?: string;
        /**
         * Bearing to the destination.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDestBearing?: number;
        /**
         * Unit used to express the distance to the destination.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDestDistanceRef?: string;
        /**
         * Distance to the destination.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDestDistance?: number;
        /**
         * Name of the positioning method.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsProcessingMethod?: string;
        /**
         * String of the GPS area name.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsAreaInformation?: string;
        /**
         * GPS date stamp.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDateStamp?: string;
        /**
         * Whether differential correction has been applied to the GPS data, which is crucial for precise positioning
         * accuracy.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsDifferential?: number;
        /**
         * Horizontal positioning error, in meters.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gpsHPositioningError?: number;
        /**
         * ISO speed and latitude of the camera or input device, which are specified in ISO 12232.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        isoSpeedRatings?: number;
        /**
         * Sensitivity of the camera or input device during image capture.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        photographicSensitivity?: number[];
        /**
         * Opto-Electric Conversion Function (OECF) specified in ISO 14524.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        oecf?: ArrayBuffer;
        /**
         * Sensitivity type.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sensitivityType?: number;
        /**
         * Standard output sensitivity.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        standardOutputSensitivity?: number;
        /**
         * GPS measurement mode.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        recommendedExposureIndex?: number;
        /**
         * Maximum dynamic range recordable by the camera sensor in a single exposure. The unit is EV.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        isoSpeedLatitudeyyy?: number;
        /**
         * Highlight retention capacity of the camera sensor in overexposure. The unit is EV.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        isoSpeedLatitudezzz?: number;
        /**
         * Version of the supported Exif standard.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        exifVersion?: string;
        /**
         * Date and time when the original image data is generated.
         * For a digital still camera (DSC), the date and time when a photo is taken are recorded. The value format is *YYYY
         * :MM:DD HH:MM:SS* (24-hour clock).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        dateTimeOriginal?: string;
        /**
         * Date and time when the image is stored as digital data.
         * For example, if a DSC captures an image and records the file at the same time, the values of **DateTimeOriginal**
         * and **DateTimeDigitized** are the same. The value format is *YYYY:MM:DD HH:MM:SS* (24-hour clock).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        dateTimeDigitized?: string;
        /**
         * Geographical time zone of the device.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        offsetTime?: string;
        /**
         * Geographical time zone of the device.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        offsetTimeOriginal?: string;
        /**
         * Coordinated Universal Time (UTC) offset at the time of image digitization, which helps to precisely adjust the
         * timestamp.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        offsetTimeDigitized?: string;
        /**
         * Information about the compressed data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        componentsConfiguration?: string;
        /**
         * Image compression scheme. The unit is bit/pixel.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        compressedBitsPerPixel?: number;
        /**
         * Shutter speed, expressed as an Additive System of Photographic Exposure (APEX) value.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        shutterSpeedValue?: number;
        /**
         * Lens aperture. The unit is APEX.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        apertureValue?: number;
        /**
         * Image brightness. The unit is APEX.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        brightnessValue?: number;
        /**
         * Exposure bias.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        exposureBiasValue?: number;
        /**
         * Minimum aperture value of the lens.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        maxApertureValue?: number;
        /**
         * Distance from the capture device to the photographed object, in meters.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        subjectDistance?: number;
        /**
         * Metering mode.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        meteringMode?: number;
        /**
         * Light source.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        lightSource?: number;
        /**
         * Flash.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        flash?: number;
        /**
         * Focal length of the lens, in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        focalLength?: number;
        /**
         * Location and area of the main object in the entire scene.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        subjectArea?: number[];
        /**
         * Information required by the Exif/Design rule for Camera File system (DCF) writer manufacturer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        makerNote?: ArrayBuffer;
        /**
         * User comments.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        userComment?: string;
        /**
         * Second fraction of **DateTime**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        subsecTime?: string;
        /**
         * Second of **DateTimeOriginal**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        subsecTimeOriginal?: string;
        /**
         * Second of **DateTimeDigitized**.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        subsecTimeDigitized?: string;
        /**
         * FlashPix format version supported by the FlashPix Extension Resource (FPXR), which is used to enhance device
         * compatibility.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        flashpixVersion?: string;
        /**
         * Color space information, which is usually recorded as a color space descriptor.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        colorSpace?: number;
        /**
         * Image size on the X axis (horizontal axis in a two-dimensional coordinate system).
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        pixelXDimension?: number;
        /**
         * Image size on the Y axis (vertical axis in a two-dimensional coordinate system).
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        pixelYDimension?: number;
        /**
         * Name of the audio file related to the image data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        relatedSoundFile?: string;
        /**
         * Flash energy at the time the image is captured. The unit is beam candlepower seconds (BCPS).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        flashEnergy?: number;
        /**
         * Spatial frequency table of the camera or input device.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        spatialFrequencyResponse?: ArrayBuffer;
        /**
         * Number of pixels per unit physical length in the X-axis of the sensor's physical plane.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        focalPlaneXResolution?: number;
        /**
         * Number of pixels per unit physical length in the Y-axis of the sensor's physical plane.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        focalPlaneYResolution?: number;
        /**
         * Measurement unit of **FocalPlaneXResolution** and **FocalPlaneYResolution**.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        focalPlaneResolutionUnit?: number;
        /**
         * Pixel coordinates of the primary object in the image (based on the origin in the upper left corner).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        subjectLocation?: number[];
        /**
         * Exposure index selected at the time the image is captured.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        exposureIndex?: number;
        /**
         * Type of the image sensor on the camera.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sensingMethod?: number;
        /**
         * Image source.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        fileSource?: ArrayBuffer;
        /**
         * Scene type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneType?: ArrayBuffer;
        /**
         * Color filter array (CFA) geometric pattern of the image sensor.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        cfaPattern?: ArrayBuffer;
        /**
         * Special processing of image data, such as HDR composition and AI scene enhancement.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        customRendered?: number;
        /**
         * Exposure mode.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        exposureMode?: number;
        /**
         * White balance.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        whiteBalance?: number;
        /**
         * Digital zoom ratio used when the image is captured.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        digitalZoomRatio?: number;
        /**
         * Focal length of the 35 mm film.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        focalLengthIn35mmFilm?: number;
        /**
         * Type of the scene that is captured.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneCaptureType?: number;
        /**
         * Degree of overall image gain adjustment.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gainControl?: number;
        /**
         * Contrast optimization policy applied by the camera. For example, standard processing and contrast reduction.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        contrast?: number;
        /**
         * Color saturation adjustment policy applied by the camera. For example, standard processing and saturation
         * reduction.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        saturation?: number;
        /**
         * Edge enhancement processing method applied by the camera. For example, weak sharpening and standard sharpening.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sharpness?: number;
        /**
         * Capture condition information of a specific camera model.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        deviceSettingDescription?: ArrayBuffer;
        /**
         * Distance range to the object.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        subjectDistanceRange?: number;
        /**
         * Unique ID assigned to each image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        imageUniqueId?: string;
        /**
         * Name of the camera owner.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        cameraOwnerName?: string;
        /**
         * Serial number of the camera body.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        bodySerialNumber?: string;
        /**
         * Specifications of the lens.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        lensSpecification?: number[];
        /**
         * Manufacturer of the lens.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        lensMake?: string;
        /**
         * Model of the lens.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        lensModel?: string;
        /**
         * Serial number of the lens.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        lensSerialNumber?: string;
        /**
         * Whether the image is a composite image.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        compositeImage?: number;
        /**
         * Number of source images of the composite image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sourceImageNumberOfCompositeImage?: number[];
        /**
         * Exposure time of source images for the composite image, for example, 1/33 s.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sourceExposureTimesOfCompositeImage?: ArrayBuffer;
        /**
         * Gamma value of each component.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        gamma?: number;
        /**
         * Creates an empty [ExifMetadata]{@link @ohos.multimedia.image:image.ExifMetadata} instance.
         *
         * @returns { ExifMetadata } Empty **ExifMetadata** instance.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        static createInstance(): ExifMetadata;
        /**
         * Obtains the property values from image metadata. This API returns the result asynchronously through a promise.
         *
         * For details about the properties, see [PropertyKey]{@link @ohos.multimedia.image:image.PropertyKey}.
         *
         * @param { Array<string> } key - Names of the properties to query.
         * @returns { Promise<Record<string, string | null>> } Promise used to return the obtained image metadata property
         *     values.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: unsupported metadata type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getProperties(key: Array<string>): Promise<Record<string, string | null>>;
        /**
         * Sets the values of specified properties in image metadata in batches. This API returns the result asynchronously
         * through a promise.
         *
         * For details about the properties, see [PropertyKey]{@link @ohos.multimedia.image:image.PropertyKey}.
         *
         * @param { Record<string, string | null> } records - Set of key-value pairs representing properties and
         *     corresponding values of the **ExifMetadata** object.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: unsupported metadata type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        setProperties(records: Record<string, string | null>): Promise<void>;
        /**
         * Obtains all properties and their values from the image metadata. This API returns the result asynchronously
         * through a promise.
         *
         * @returns { Promise<Record<string, string | null>> } Promise used to return the values of all properties.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getAllProperties(): Promise<Record<string, string | null>>;
        /**
         * Clones the Exif metadata. This API returns the result asynchronously through a promise.
         *
         * @returns { Promise<ExifMetadata> } Promise used to return the Exif metadata instance if the operation is
         *     successful.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        clone(): Promise<ExifMetadata>;
        /**
         * Obtains the metadata in binary format. This API uses a promise to return the result.
         *
         * @returns { Promise<ArrayBuffer> } Promise that returns the binary data of the metadata.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getBlob(): Promise<ArrayBuffer>;
        /**
         * Replaces the current metadata with binary data. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } blob - Binary data used to replace the metadata.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7600206 - Invalid parameter. Possible causes: The blob is empty or has a length of 0.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        setBlob(blob: ArrayBuffer): Promise<void>;
    }
    /**
     * The XMAGE watermark is at the bottom of the photo.The value is 9.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const XMAGE_WATERMARK_MODE_AT_THE_BOTTOM: number;
    /**
     * The XMAGE watermark is around the edges of the photo.The value is 10.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const XMAGE_WATERMARK_MODE_BORDER: number;
    /**
     * Capture mode: professional.The value is 2.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_PROFESSIONAL: number;
    /**
     * Capture mode: night view with front lens.The value is 7.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_FRONT_LENS_NIGHT_VIEW: number;
    /**
     * Capture mode: panorama.The value is 8.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_PANORAMA: number;
    /**
     * Capture mode: tail light.The value is 9.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_TAIL_LIGHT: number;
    /**
     * Capture mode: light graffiti.The value is 10.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_LIGHT_GRAFFITI: number;
    /**
     * Capture mode: silky water.The value is 11.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_SILKY_WATER: number;
    /**
     * Capture mode: star track.The value is 12.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_STAR_TRACK: number;
    /**
     * Capture mode: wide aperture.The value is 19.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_WIDEAPERTURE: number;
    /**
     * Capture mode: moving photos.The value is 20.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_MOVING_PHOTO: number;
    /**
     * Capture mode: portrait.The value is 23.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_PORTRAIT: number;
    /**
     * Capture mode: night view with rear lens.The value is 42.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_REAR_LENS_NIGHT_VIEW: number;
    /**
     * Capture mode: super macro.The value is 47.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_SUPER_MACRO: number;
    /**
     * Capture mode: snap shot.The value is 62.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    const CAPTURE_MODE_SNAP_SHOT: number;
    /**
     * Enumerates the focus modes.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    enum FocusMode {
        /**
         * Intelligent autofocus.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        AF_A = 0,
        /**
         * Single autofocus.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        AF_S = 1,
        /**
         * Continuous auto focus.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        AF_C = 2,
        /**
         * Manual focus.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        MF = 3
    }
    /**
     * Enumerates the XMAGE color modes.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    enum XmageColorMode {
        /**
         * Original.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        NORMAL = 0,
        /**
         * Bright.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        BRIGHT = 1,
        /**
         * Vivid.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        SOFT = 2,
        /**
         * Mono.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        MONO = 3
    }
    /**
     * MakerNoteHuaweiMetadata implements Metadata
     *
     * Photo metadata from Huawei cameras.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    class MakerNoteHuaweiMetadata implements Metadata {
        /**
         * Whether XMAGE is supported. **true** indicates yes; **false** indicates no.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        isXmageSupported?: boolean;
        /**
         * XMAGE watermark mode. For details, see [Constants]{@link @ohos.multimedia.image:image.Constants}.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        xmageWatermarkMode?: number;
        /**
         * Horizontal coordinate of the left boundary of the effective content area (excluding the watermark coverage area)
         * on the original image, relative to the top-left origin of the image. The unit is px.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        xmageLeft?: number;
        /**
         * Vertical coordinate of the top boundary of the effective content area (excluding the watermark coverage area) on
         * the original image, relative to the top-left origin of the image. The unit is px.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        xmageTop?: number;
        /**
         * Horizontal coordinate of the right boundary of the effective content area (excluding the watermark coverage area)
         * on the original image, relative to the top-left origin of the image. The unit is px.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        xmageRight?: number;
        /**
         * Vertical coordinate of the bottom boundary of the effective content area (excluding the watermark coverage area)
         * on the original image, relative to the top-left origin of the image. The unit is px.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        xmageBottom?: number;
        /**
         * XMAGE color mode.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        xmageColorMode?: XmageColorMode;
        /**
         * Whether the image has been cloud-enhanced. **true** indicates yes; **false** indicates no.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        isCloudEnhanced?: boolean;
        /**
         * Cloud enhancement label.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        cloudLabel?: string;
        /**
         * Whether the wind snapshot mode is used. **true** indicates yes; **false** indicates no.
         * This mode is a specialized photography mode designed for capturing fast-moving subjects or scenes prone to
         * blurring, such as in windy conditions or when photographing moving objects.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        isWindSnapshot?: boolean;
        /**
         * Version number of the scene recognition algorithm.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneVersion?: number;
        /**
         * Capture scene: food confidence.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneFoodConfidence?: number;
        /**
         * Capture scene: stage performance confidence.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneStageConfidence?: number;
        /**
         * Capture scene: blue sky confidence.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneBlueSkyConfidence?: number;
        /**
         * Capture scene: green plant confidence.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneGreenPlantConfidence?: number;
        /**
         * Capture scene: beach confidence.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneBeachConfidence?: number;
        /**
         * Capture scene: snow confidence.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneSnowConfidence?: number;
        /**
         * Capture scene: sunset confidence.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneSunsetConfidence?: number;
        /**
         * Capture scene: flower confidence.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneFlowersConfidence?: number;
        /**
         * Capture scene: night scene confidence.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneNightConfidence?: number;
        /**
         * Capture scene: text confidence.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        sceneTextConfidence?: number;
        /**
         * Number of faces.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        faceCount?: number;
        /**
         * Confidences of a specified number of faces.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        faceConfidences?: number[];
        /**
         * Smile scores of a specified number of faces.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        faceSmileScores?: number[];
        /**
         * Capture mode.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        captureMode?: number;
        /**
         * Number of burst shots.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        burstNumber?: number;
        /**
         * Whether to use the front camera. **true** indicates yes; **false** indicates no.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        isFrontCamera?: boolean;
        /**
         * Horizontal pan angle.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        rollAngle?: number;
        /**
         * Pitch angle.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        pitchAngle?: number;
        /**
         * Physical aperture, in fNumber.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        physicalAperture?: number;
        /**
         * Lens focus control policy, which determines how the camera adjusts the focal length.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        focusMode?: FocusMode;
        /**
         * Returns an empty [MakerNoteHuaweiMetadata]{@link @ohos.multimedia.image:image.MakerNoteHuaweiMetadata} instance.
         *
         * @returns { MakerNoteHuaweiMetadata } Empty **MakerNoteHuaweiMetadata** instance.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        static createInstance(): MakerNoteHuaweiMetadata;
        /**
         * Obtains the property values from image metadata. This API returns the result asynchronously through a promise.
         *
         * @param { Array<string> } key - Names of the properties to query.
         * @returns { Promise<Record<string, string | null>> } Promise used to return the obtained image metadata property
         *     values.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: unsupported metadata type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getProperties(key: Array<string>): Promise<Record<string, string | null>>;
        /**
         * Sets the values of specified properties in image metadata in batches. This API returns the result asynchronously
         * through a promise.
         *
         * For details about the properties, see [PropertyKey]{@link @ohos.multimedia.image:image.PropertyKey}.
         *
         * @param { Record<string, string | null> } records - Array containing key-value pairs representing properties and
         *     their corresponding values of the **MakerNoteHuaweiMetadata** object to be modified.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7600202 - Unsupported metadata. Possible causes: unsupported metadata type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        setProperties(records: Record<string, string | null>): Promise<void>;
        /**
         * Obtains all properties and their values from the image metadata. This API returns the result asynchronously
         * through a promise.
         *
         * @returns { Promise<Record<string, string | null>> } Promise used to return the values of all properties.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getAllProperties(): Promise<Record<string, string | null>>;
        /**
         * Clones [MakerNoteHuaweiMetadata]{@link @ohos.multimedia.image:image.MakerNoteHuaweiMetadata} metadata. This API returns the result
         * asynchronously through a promise.
         *
         * @returns { Promise<MakerNoteHuaweiMetadata> } Promise used to return the **MakerNoteHuaweiMetadata** metadata
         *     instance if metadata is successfully obtained.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        clone(): Promise<MakerNoteHuaweiMetadata>;
        /**
         * Obtains the metadata in binary format. This API uses a promise to return the result.
         *
         * @returns { Promise<ArrayBuffer> } Promise that returns the binary data of the metadata.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getBlob(): Promise<ArrayBuffer>;
        /**
         * Replaces the current metadata with binary data. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } blob - Binary data used to replace the metadata.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7600206 - Invalid parameter. Possible causes: The blob is empty or has a length of 0.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        setBlob(blob: ArrayBuffer): Promise<void>;
    }
    /**
     * DNG metadata.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 24
     */
    class DngMetadata {
        /**
         * The DNG version.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly dngVersion?: number[];
        /**
         * The DNG backward compatibility version.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly dngBackwardVersion?: number[];
        /**
         * A unique camera model.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly uniqueCameraModel?: string;
        /**
         * A localized camera model.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly localizedCameraModel?: string;
        /**
         * The CFA (color filter array) plane color.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly cfaPlaneColor?: number[];
        /**
         * The CFA (color filter array) layout.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly cfaLayout?: number;
        /**
         * The linearization table.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly linearizationTable?: number[];
        /**
         * The black level repeat dimension.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly blackLevelRepeatDim?: number[];
        /**
         * The zero-light encoding level.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly blackLevel?: number[];
        /**
         * The black level delta H.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly blackLevelDeltaH?: number[];
        /**
         * The black level delta V.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly blackLevelDeltaV?: number[];
        /**
         * The white level.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly whiteLevel?: number[];
        /**
         * The default scale.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly defaultScale?: number[];
        /**
         * The default crop origin.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly defaultCropOrigin?: number[];
        /**
         * The default crop size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly defaultCropSize?: number[];
        /**
         * A transformation matrix under the first calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly colorMatrix1?: number[];
        /**
         * A transformation matrix under the second calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly colorMatrix2?: number[];
        /**
         * A calibration matrix under the first calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly cameraCalibration1?: number[];
        /**
         * A calibration matrix under the second calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly cameraCalibration2?: number[];
        /**
         * A dimensionality reduction matrix under the first calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly reductionMatrix1?: number[];
        /**
         * A dimensionality reduction matrix under the second calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly reductionMatrix2?: number[];
        /**
         * The analog balance.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly analogBalance?: number[];
        /**
         * The as-shot neutral.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly asShotNeutral?: number[];
        /**
         * The as-shot white, encoded as x-y chromaticity coordinates.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly asShotWhiteXY?: number[];
        /**
         * The baseline exposure.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly baselineExposure?: number;
        /**
         * The baseline noise.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly baselineNoise?: number;
        /**
         * The baseline sharpness.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly baselineSharpness?: number;
        /**
         * The Bayer green split.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly bayerGreenSplit?: number;
        /**
         * The linear response limit.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly linearResponseLimit?: number;
        /**
         * The serial number of the camera.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly cameraSerialNumber?: string;
        /**
         * Information about the lens.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly lensInfo?: number[];
        /**
         * The chroma blur radius.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly chromaBlurRadius?: number;
        /**
         * The anti-alias strength.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly antiAliasStrength?: number;
        /**
         * The shadow scale.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly shadowScale?: number;
        /**
         * The private data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly dngPrivateData?: ArrayBuffer;
        /**
         * Whether the EXIF MakerNote tag is safe.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly makerNoteSafety?: boolean;
        /**
         * The first calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly calibrationIlluminant1?: number;
        /**
         * The second calibration illuminant.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly calibrationIlluminant2?: number;
        /**
         * The best quality scale.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly bestQualityScale?: number;
        /**
         * The unique identifier of raw image data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly rawDataUniqueID?: string;
        /**
         * The original raw file name.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly originalRawFileName?: string;
        /**
         * The original raw file data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly originalRawFileData?: ArrayBuffer;
        /**
         * The active area.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly activeArea?: number[];
        /**
         * The masked areas.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly maskedAreas?: number[];
        /**
         * An ICC profile.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly asShotICCProfile?: ArrayBuffer;
        /**
         * The as-shot pre-profile matrix.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly asShotPreProfileMatrix?: number[];
        /**
         * The current ICC profile.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly currentICCProfile?: ArrayBuffer;
        /**
         * The current pre-profile matrix.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly currentPreProfileMatrix?: number[];
        /**
         * The colorimetric reference.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly colorimetricReference?: number;
        /**
         * The camera calibration signature.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly cameraCalibrationSignature?: string;
        /**
         * The profile calibration signature.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileCalibrationSignature?: string;
        /**
         * The extra camera profiles.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly extraCameraProfiles?: number[];
        /**
         * The as-shot camera profile.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly asShotProfileName?: string;
        /**
         * The applied noise reduction.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly noiseReductionApplied?: number;
        /**
         * The profile name.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileName?: string;
        /**
         * The profile hue/saturation map dims.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileHueSatMapDims?: number[];
        /**
         * The first hue/saturation mapping table data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileHueSatMapData1?: number[];
        /**
         * The second hue/saturation mapping table data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileHueSatMapData2?: number[];
        /**
         * The profile tone curve.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileToneCurve?: number[];
        /**
         * The profile embed policy.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileEmbedPolicy?: number;
        /**
         * The profile copyright.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileCopyright?: string;
        /**
         * The first forward matrix.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly forwardMatrix1?: number[];
        /**
         * The second forward matrix.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly forwardMatrix2?: number[];
        /**
         * The preview application name.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly previewApplicationName?: string;
        /**
         * The preview application version.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly previewApplicationVersion?: string;
        /**
         * The preview settings name.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly previewSettingsName?: string;
        /**
         * The preview settings digest.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly previewSettingsDigest?: string;
        /**
         * The preview color space.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly previewColorSpace?: number;
        /**
         * The preview date time.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly previewDateTime?: string;
        /**
         * An MD5 digest of the raw image data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly rawImageDigest?: string;
        /**
         * An MD5 digest of the data stored in the OriginalRawFileData.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly originalRawFileDigest?: string;
        /**
         * The sub‑tile block size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly subTileBlockSize?: number[];
        /**
         * The row interleave factor.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly rowInterleaveFactor?: number;
        /**
         * The profile lookup table dimensions.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileLookTableDims?: number[];
        /**
         * The profile lookup table data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileLookTableData?: number[];
        /**
         * The first opcode list.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly opcodeList1?: ArrayBuffer;
        /**
         * The second opcode list.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly opcodeList2?: ArrayBuffer;
        /**
         * The third opcode list.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly opcodeList3?: ArrayBuffer;
        /**
         * The noise profile.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly noiseProfile?: number[];
        /**
         * The original default final size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly originalDefaultFinalSize?: number[];
        /**
         * The original best quality final size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly originalBestQualityFinalSize?: number[];
        /**
         * The original default crop size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly originalDefaultCropSize?: number[];
        /**
         * The profile hue/saturation map encoding.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileHueSatMapEncoding?: number;
        /**
         * The profile lookup table encoding.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly profileLookTableEncoding?: number;
        /**
         * The baseline exposure offset.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly baselineExposureOffset?: number;
        /**
         * The default black render.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly defaultBlackRender?: number;
        /**
         * A modified MD5 digest of the raw image data.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly newRawImageDigest?: string;
        /**
         * The gain between the main raw IFD and the preview IFD.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly rawToPreviewGain?: number;
        /**
         * The default user crop.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly defaultUserCrop?: number[];
    }
    /**
     * Enumerates the properties available for the metadata of a WebP image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 24
     */
    enum WebPPropertyKey {
        /**
         * Canvas Width.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CANVAS_WIDTH = 'WebPCanvasWidth',
        /**
         * Canvas Height.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        CANVAS_HEIGHT = 'WebPCanvasHeight',
        /**
         * Delay of each frame in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        DELAY_TIME = 'WebPDelayTime',
        /**
         * Unclamped delay of each frame in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        UNCLAMPED_DELAY_TIME = 'WebPUnclampedDelayTime',
        /**
         * Loop count.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        LOOP_COUNT = 'WebPLoopCount'
    }
    /**
     * WebP metadata.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 24
     */
    class WebPMetadata {
        /**
         * Canvas Width.
         * Unit: px, The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly canvasWidth?: number;
        /**
         * Canvas Height.
         * Unit: px, The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly canvasHeight?: number;
        /**
         * Delay of each frame.
         * Unit: ms, The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly delayTime?: number;
        /**
         * Unclamped delay of each frame.
         * Unit: ms, The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly unclampedDelayTime?: number;
        /**
         * Loop count.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        readonly loopCount?: number;
    }
    /**
     * Enumerates XMP tag type.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum XMPTagType {
        /**
         * Unknown XMP tag type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        UNKNOWN = 0,
        /**
         * String XMP tag type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        STRING = 1,
        /**
         * Unordered array XMP tag type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        UNORDERED_ARRAY = 2,
        /**
         * Ordered array XMP tag type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        ORDERED_ARRAY = 3,
        /**
         * Alternate array XMP tag type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        ALTERNATE_ARRAY = 4,
        /**
         * Alternate text XMP tag type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        ALTERNATE_TEXT = 5,
        /**
         * Structure XMP tag type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        STRUCTURE = 6
    }
    /**
     * Describes XMP namespace parameters.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface XMPNamespace {
        /**
         * The uri of XMP namespace.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        uri: string;
        /**
         * The prefix of XMP namespace.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        prefix: string;
    }
    /**
     * XMP namespace: XMP basic.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    const XMP_BASIC: XMPNamespace;
    /**
     * XMP namespace: XMP rights.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    const XMP_RIGHTS: XMPNamespace;
    /**
     * XMP namespace: exif.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    const EXIF: XMPNamespace;
    /**
     * XMP namespace: dublin core.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    const DUBLIN_CORE: XMPNamespace;
    /**
     * XMP namespace: tiff.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    const TIFF: XMPNamespace;
    /**
     * Describes XMP Tag parameters.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface XMPTag {
        /**
         * The namespace of XMP tag.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        xmpNamespace: XMPNamespace;
        /**
         * The name of XMP tag.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        name: string;
        /**
         * The type of XMP tag.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        type: XMPTagType;
        /**
         * The value of XMP tag.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        value?: string;
    }
    /**
     * Describes XMP enumerate option parameters.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface XMPEnumerateOptions {
        /**
         * The option that controls recursive enabling.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        isRecursive?: boolean;
        /**
         * Whether to return only qualifier data.
         * <br>Default value:false.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        onlyQualifier?: boolean;
    }
    /**
     * XMPMetadata instance.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    class XMPMetadata {
        /**
         * Register a new namespace according to the xml namespace and prefix.
         *
         * @param { XMPNamespace } xmpNamespace - The xmp namespace.
         * @returns { Promise<void> } A Promise instance used to return the operation result. If the operation fails, an
         * error message is returned.
         * @throws { BusinessError } 7600206 - Invalid argument. Possible causes: 1. Invalid namespace format.
         *     2. The uri is already registered. 3. The prefix is already registered.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        public registerXMPNamespace(xmpNamespace: XMPNamespace): Promise<void>;
        /**
         * Set the XMP type and value of the XMP tag in the specified path.
         *
         * @param { string } path - The specified path of the target XMP tag.(e.g., "dc:title").
         * @param { XMPTagType } type - The specified XMP tag type.
         * @param { string } [value] - The specified value. If this parameter is not specified, the default value is empty.
         * @returns { Promise<void> } A Promise instance used to return the operation result. If the operation fails, an
         * error message is returned.
         * @throws { BusinessError } 7600206 - Invalid argument. Possible causes: 1. Namespace is not registered.
         *     2. The path syntax is invalid. 3. The path does not match the type. 4. The value is invalid for the type.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        public setValue(path: string, type: XMPTagType, value?: string): Promise<void>;
        /**
         * Get a single XMP tag from specified path.
         *
         * @param { string } path - The specified path of the target XMP tag.(e.g., "dc:title").
         * @returns { Promise<XMPTag | null> } Promise used to return the XMP tag.
         * @throws { BusinessError } 7600206 - Invalid argument. Possible causes: 1. Namespace is not registered.
         *     2. The path syntax is invalid.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        public getTag(path: string): Promise<XMPTag | null>;
        /**
         * Remove the XMP tag from specified path.
         *
         * @param { string } path - The specified path of the target XMP tag.(e.g., "dc:title").
         * @returns { Promise<void> } A Promise instance used to return the operation result. If the operation fails, an
         * error message is returned.
         * @throws { BusinessError } 7600206 - Invalid argument. Possible causes: 1. Namespace is not registered.
         *     2. The path syntax is invalid.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        public removeTag(path: string): Promise<void>;
        /**
         * Enumerate the XMP tags from specified path and uses a callback to return the result.
         *
         * @param { function } callback - Callback used to return the XMP node and the corresponding XMPTag.
         *     The callback receives a path argument that follows the XMP namespace:path format.
         * @param { string } [rootPath] - Enumerate root path. If this parameter is not specified, the default value is root
         *     path.
         * @param { XMPEnumerateOptions } [options] - XMP enumerate option.
         * @throws { BusinessError } 7600206 - Invalid argument. Possible causes: 1. Namespace is not registered.
         *     2. The rootPath syntax is invalid.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        public enumerateTags(callback: (path: string, tag: XMPTag) => boolean, rootPath?: string, options?: XMPEnumerateOptions): void;
        /**
         * Get all XMP tags from specified path.
         *
         * @param { string } [rootPath] - The specified path. If this parameter is not specified, the default value is root
         *     path.
         * @param { XMPEnumerateOptions } [options] - XMP enumerate option.
         * @returns { Promise<Record<string, XMPTag>> } A Promise instance used to return all XMP tags.
         * @throws { BusinessError } 7600206 - Invalid argument. Possible causes: 1. Namespace is not registered.
         *     2. The rootPath syntax is invalid.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        public getTags(rootPath?: string, options?: XMPEnumerateOptions): Promise<Record<string, XMPTag>>;
        /**
         * Set a blob into the XMP metadata.
         *
         * @param { ArrayBuffer } buffer - blob data.
         * @returns { Promise<void> } A Promise instance used to return the operation result. If the operation fails, an
         * error message is returned.
         * @throws { BusinessError } 7600206 - Invalid argument. Possible causes: 1. The buffer is empty or invalid.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        public setBlob(buffer: ArrayBuffer): Promise<void>;
        /**
         * Obtains the XMP metadata as a blob.
         *
         * @returns { Promise<ArrayBuffer> } A Promise instance used to return the ArrayBuffer of blob.
         * @throws { BusinessError } 7600301 - Memory alloc failed.
         * @throws { BusinessError } 7600302 - Memory copy failed.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        public getBlob(): Promise<ArrayBuffer>;
    }
    /**
     * Enumerates the properties available for the metadata of a Avis image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum AvisPropertyKey {
        /**
         * Delay of each frame in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        DELAY_TIME = 'AvisDelayTime'
    }
    /**
     * Avis metadata.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    class AvisMetadata {
        /**
         * Delay of each frame.
         * Unit: ms, The value should be an integer.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly delayTime?: number;
    }
    /**
     * Metadata set of an image.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @stagemodelonly
     * @since 23
     */
    interface ImageMetadata {
        /**
         * Exif metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        exifMetadata?: ExifMetadata;
        /**
         * Huawei Camera metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        makerNoteHuaweiMetadata?: MakerNoteHuaweiMetadata;
        /**
         * Heifs metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        heifsMetadata?: HeifsMetadata;
        /**
         * Dng metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        dngMetadata?: DngMetadata;
        /**
         * WebP metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 24
         */
        webPMetadata?: WebPMetadata;
        /**
         * Gif metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        gifMetadata?: GifMetadata;
        /**
         * Tiff metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        tiffMetadata?: TiffMetadata;
        /**
         * Jfif metadata.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        jfifMetadata?: JfifMetadata;
        /**
         * Png metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        pngMetadata?: PngMetadata;
        /**
         * XMP metadata.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        xmpMetadata?: XMPMetadata;
        /**
         * Avis metadata.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        avisMetadata?: AvisMetadata;
    }
    /**
     * Describes the image decoding options.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @since 13
     */
    interface DecodingOptionsForPicture {
        /**
         * Auxiliary picture type. If no auxiliary picture type is specified or an empty array is passed, the system decodes
         * all available auxiliary picture types.
         *
         * To exclude all auxiliary picture, you can decode the auxiliary picture to a PixelMap and use the PixelMap to
         * create a Picture that contains only the main picture.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @since 13
         */
        desiredAuxiliaryPictures: Array<AuxiliaryPictureType>;
        /**
         * Desired size of the main pixel map. The value (0, 0) indicates that the pixels are decoded
         * based on the original image size.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 24
         */
        desiredSizeForMainPixelMap?: Size;
        /**
         * Desired Pixel format, RGBA_8888\BGRA_8888\RGB_565\NV12\NV21 are supported.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 24
         */
        desiredPixelFormat?: PixelMapFormat;
    }
    /**
     * Describes thumbnail decoding parameters.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @stagemodelonly
     * @since 26.0.0
     */
    interface DecodingOptionsForThumbnail {
        /**
         * Flag to specify whether the thumbnail should be generated, if the image does not have a thumbnail.
         *
         * <br>Default value: true.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 26.0.0
         */
        generateThumbnailIfAbsent?: boolean;
        /**
         * This parameter is valid only when generateThumbnailIfAbsent is set to true. The width and height of the image
         *     cannot exceed the value of this parameter.
         * The value should be an integer.
         * <br>Unit:px.
         * <br>Default value:512.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 26.0.0
         */
        maxGeneratedPixelDimension?: number;
    }
    /**
    * Describes the auxiliary picture information.
    *
    * @syscap SystemCapability.Multimedia.Image.Core
    * @since 13
    */
    interface AuxiliaryPictureInfo {
        /**
         * Auxiliary picture type.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        auxiliaryPictureType: AuxiliaryPictureType;
        /**
         * Image size.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        size: Size;
        /**
         * Row stride.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 13
         */
        rowStride: number;
        /**
          * Pixel format.
          *
          * @syscap SystemCapability.Multimedia.Image.Core
          * @since 13
          */
        pixelFormat: PixelMapFormat;
        /**
          * Color space.
          *
          * @syscap SystemCapability.Multimedia.Image.Core
          * @since 13
          */
        colorSpace: colorSpaceManager.ColorSpaceManager;
    }
    /**
     * Describes raw data in an image.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @stagemodelonly
     * @since 24
     */
    interface ImageRawData {
        /**
         * Binary data of the raw image.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 24
         */
        buffer: ArrayBuffer;
        /**
         * Number of bits that each pixel actually occupies in the buffer data.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 24
         */
        bitsPerPixel: number;
    }
    /**
     * The **ImageSource** class provides APIs to obtain image information.
     *
     * Before calling any API in ImageSource, you must use
     * [image.createImageSource]{@link @ohos.multimedia.image:image.createImageSource(uri: string)} to create an
     * ImageSource instance.
     *
     * All APIs in ImageSource cannot be called concurrently.
     *
     * Images occupy a large amount of memory. When you finish using an ImageSource instance, call
     * [release]{@link image.ImageSource.release(callback: AsyncCallback<void>)} to free the memory promptly. Before
     * releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the
     * instance is no longer needed.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 6
     */
    interface ImageSource {
        /**
         * Obtains the image information with the specified index. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { number } index - Index of the image source. The default value is **0**, indicating the first image. If this
         *     parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For
         *     multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1).
         * @param { AsyncCallback<ImageInfo> } callback - Callback used to return the result. If the operation is successful
         *     , **err** is **undefined** and **data** is the image information obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 6
         */
        getImageInfo(index: number, callback: AsyncCallback<ImageInfo>): void;
        /**
         * Obtains the image information. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<ImageInfo> } callback - Callback used to return the result. If the operation is successful
         *     , **err** is **undefined** and **data** is the image information obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 6
         */
        getImageInfo(callback: AsyncCallback<ImageInfo>): void;
        /**
         * Obtains the image information. This API uses a promise to return the result.
         *
         * @param { number } index - Index of the image source. The default value is **0**, indicating the first image. If this
         *     parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For
         *     multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1).
         * @returns { Promise<ImageInfo> } Promise used to return the image information.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 6
         */
        getImageInfo(index?: number): Promise<ImageInfo>;
        /**
         * Obtains the image information with the specified index. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > This API operates synchronously and will block the current thread during execution. It should not be invoked
         * > from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For
         * > details, see
         * > [Overview of Concurrency in Time-Consuming Tasks](docroot://arkts-utils/time-consuming-task-overview.md).
         *
         * @param { number } index - Index of the image source. The default value is **0**, indicating the first image. If this
         *     parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For
         *     multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1).
         * @returns { ImageInfo } Image information.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 12
         */
        getImageInfoSync(index?: number): ImageInfo;
        /**
         * Creates a PixelMap object based on decoding options. This API uses a promise to return the result. This API uses
         * a promise to return the result.
         *
         * Starting from API version 15, you are advised to use
         * [createPixelMapUsingAllocator]{@link image.ImageSource.createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType)}
         * . This API can be used to specify the memory type
         * [AllocatorType]{@link @ohos.multimedia.image:image.AllocatorType} of the output PixelMap. For details, see
         * [Optimizing Memory for Image Decoding (ArkTS)](docroot://media/image/image-allocator-type.md).
         *
         * > **NOTE**
         * >
         * > - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
         * >
         * > - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
         * > [release]{@link @ohos.multimedia.image:image.PixelMap.release()} to free the memory promptly.
         * >
         * > - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
         * > finished and the instance is no longer needed.
         *
         * @param { DecodingOptions } options - Decoding options.
         * @returns { Promise<PixelMap> } Promise used to return the PixelMap object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        createPixelMap(options?: DecodingOptions): Promise<PixelMap>;
        /**
         * Creates a PixelMap object based on the default parameters. This API uses an asynchronous callback to return the
         * result.
         *
         * Starting from API version 15, you are advised to use
         * [createPixelMapUsingAllocator]{@link image.ImageSource.createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType)}
         * . This API can be used to specify the memory type
         * [AllocatorType]{@link @ohos.multimedia.image:image.AllocatorType} of the output PixelMap. For details, see
         * [Optimizing Memory for Image Decoding (ArkTS)](docroot://media/image/image-allocator-type.md).
         *
         * > **NOTE**
         * >
         * > - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
         * >
         * > - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
         * > [release]{@link @ohos.multimedia.image:image.PixelMap.release()} to free the memory promptly.
         * >
         * > - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
         * > finished and the instance is no longer needed.
         *
         * @param { AsyncCallback<PixelMap> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        createPixelMap(callback: AsyncCallback<PixelMap>): void;
        /**
         * Creates a PixelMap object based on decoding options. This API uses a promise to return the result. This API uses
         * an asynchronous callback to return the result.
         *
         * Starting from API version 15, you are advised to use
         * [createPixelMapUsingAllocator]{@link image.ImageSource.createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType)}
         * . This API can be used to specify the memory type
         * [AllocatorType]{@link @ohos.multimedia.image:image.AllocatorType} of the output PixelMap. For details, see
         * [Optimizing Memory for Image Decoding (ArkTS)](docroot://media/image/image-allocator-type.md).
         *
         * > **NOTE**
         * >
         * > - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
         * >
         * > - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
         * > [release]{@link @ohos.multimedia.image:image.PixelMap.release()} to free the memory promptly.
         * >
         * > - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
         * > finished and the instance is no longer needed.
         *
         * @param { DecodingOptions } options - Decoding options.
         * @param { AsyncCallback<PixelMap> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void;
        /**
         * Creates a PixelMap object based on decoding options and memory type. This API uses a promise to return the
         * result. For details, see
         * [Optimizing Memory for Image Decoding (ArkTS)](docroot://media/image/image-allocator-type.md).
         *
         * > **NOTE**
         * >
         * > - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
         * >
         * > - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
         * > [release]{@link @ohos.multimedia.image:image.PixelMap.release()} to free the memory promptly.
         * >
         * > - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
         * > finished and the instance is no longer needed.
         *
         * @param { DecodingOptions } options - Decoding options.
         * @param { AllocatorType } allocatorType - Type of the memory. The default value is **AllocatorType.AUTO**.
         * @returns { Promise<PixelMap> } Promise used to return the PixelMap object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 7700101 - Bad source. e.g.,1. Image has invalid width or height. 2. Image source
         *     incomplete.
         *     3. Read image data failed. 4. Codec create failed.
         * @throws { BusinessError } 7700102 - Unsupported mimetype.
         * @throws { BusinessError } 7700103 - Image too large. This status code is thrown when an error occurs during the
         *     process of
         *     checking size.
         * @throws { BusinessError } 7700201 - Unsupported allocator type, e.g., use share memory to decode a HDR image as
         *     only DMA supported hdr metadata.
         * @throws { BusinessError } 7700203 - Unsupported options, e.g, cannot convert image into desired pixel format.
         * @throws { BusinessError } 7700301 - Failed to decode image.
         * @throws { BusinessError } 7700302 - Failed to allocate memory.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @since 15
         */
        createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>;
        /**
         * Creates a PixelMap object based on decoding options. This API returns the result synchronously.
         *
         * Images occupy a large amount of memory. When you finish using a PixelMap instance, call
         * [release]{@link @ohos.multimedia.image:image.PixelMap.release()} to free the memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * Starting from API version 15, you are advised to use
         * [createPixelMapUsingAllocatorSync]{@link image.ImageSource.createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType)}
         * . This API can be used to specify the memory type
         * [AllocatorType]{@link @ohos.multimedia.image:image.AllocatorType} of the output PixelMap. For details, see
         * [Optimizing Memory for Image Decoding (ArkTS)](docroot://media/image/image-allocator-type.md).
         *
         * > **NOTE**
         * >
         * > This API operates synchronously and will block the current thread during execution. It should not be invoked
         * > from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For
         * > details, see
         * > [Overview of Concurrency in Time-Consuming Tasks](docroot://arkts-utils/time-consuming-task-overview.md).
         *
         * @param { DecodingOptions } options - Decoding options.
         * @returns { PixelMap } PixelMap object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 12
         */
        createPixelMapSync(options?: DecodingOptions): PixelMap;
        /**
         * Creates a PixelMap object based on decoding options and memory type. This API returns the result synchronously.
         * For details, see [Optimizing Memory for Image Decoding (ArkTS)](docroot://media/image/image-allocator-type.md).
         *
         * Images occupy a large amount of memory. When you finish using a PixelMap instance, call
         * [release]{@link @ohos.multimedia.image:image.PixelMap.release()} to free the memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * > **NOTE**
         * >
         * > This API operates synchronously and will block the current thread during execution. It should not be invoked
         * > from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For
         * > details, see
         * > [Overview of Concurrency in Time-Consuming Tasks](docroot://arkts-utils/time-consuming-task-overview.md).
         *
         * @param { DecodingOptions } options - Decoding options.
         * @param { AllocatorType } allocatorType - Type of the memory. The default value is **AllocatorType.AUTO**.
         * @returns { PixelMap } PixelMap object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 7700101 - Bad source. e.g.,1. Image has invalid width or height. 2. Image source
         *     incomplete.
         *     3. Read image data failed. 4. Codec create failed.
         * @throws { BusinessError } 7700102 - Unsupported mimetype.
         * @throws { BusinessError } 7700103 - Image too large. This status code is thrown when an error occurs during the
         *     process of
         *     checking size.
         * @throws { BusinessError } 7700201 - Unsupported allocator type, e.g., use share memory to decode a HDR image as
         *     only DMA supported hdr metadata.
         * @throws { BusinessError } 7700203 - Unsupported options, e.g, cannot convert image into desired pixel format.
         * @throws { BusinessError } 7700301 - Failed to decode image.
         * @throws { BusinessError } 7700302 - Failed to allocate memory.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @since 15
         */
        createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap;
        /**
         * Creates an array of PixelMap objects based on decoding options. This API uses a promise to return the result.
         *
         * For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static
         * images, this API returns the data of the unique frame of the image.
         *
         * > **NOTE**
         * >
         * > - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
         * >
         * > - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
         * > [release]{@link @ohos.multimedia.image:image.PixelMap.release()} to free the memory promptly.
         * >
         * > - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
         * > finished and the instance is no longer needed.
         * >
         * > - This function decodes all frames at once. If the number of frames is high or the size of individual frames is
         * > large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component
         * > for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this
         * > function.
         *
         * @param { DecodingOptions } options - Decoding options.
         * @returns { Promise<Array<PixelMap>> } Promise used to return an array of PixelMap objects.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980099 - The shared memory data is abnormal.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980103 - The image data is not supported.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @throws { BusinessError } 62980109 - Failed to crop the image.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @throws { BusinessError } 62980116 - Failed to decode the image.
         * @throws { BusinessError } 62980118 - Failed to create the image plugin.
         * @throws { BusinessError } 62980137 - Invalid media operation.
         * @throws { BusinessError } 62980173 - The DMA memory does not exist.
         * @throws { BusinessError } 62980174 - The DMA memory data is abnormal.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 10
         */
        createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>;
        /**
         * Creates an array of PixelMap objects based on the default parameters. This API uses an asynchronous callback to
         * return the result.
         *
         * For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static
         * images, this API returns the data of the unique frame of the image.
         *
         * > **NOTE**
         * >
         * > - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
         * >
         * > - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
         * > [release]{@link @ohos.multimedia.image:image.PixelMap.release()} to free the memory promptly.
         * >
         * > - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
         * > finished and the instance is no longer needed.
         * >
         * > - This function decodes all frames at once. If the number of frames is high or the size of individual frames is
         * > large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component
         * > for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this
         * > function.
         *
         * @param { AsyncCallback<Array<PixelMap>> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is undefined and **data** is the array of PixelMap objects obtained; otherwise, **err**
         *     is an error object.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980099 - The shared memory data is abnormal.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980103 - The image data is not supported.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @throws { BusinessError } 62980109 - Failed to crop the image.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @throws { BusinessError } 62980116 - Failed to decode the image.
         * @throws { BusinessError } 62980118 - Failed to create the image plugin.
         * @throws { BusinessError } 62980137 - Invalid media operation.
         * @throws { BusinessError } 62980173 - The DMA memory does not exist.
         * @throws { BusinessError } 62980174 - The DMA memory data is abnormal.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 10
         */
        createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void;
        /**
         * Creates an array of PixelMap objects based on decoding options. This API uses an asynchronous callback to return
         * the result.
         *
         * For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static
         * images, this API returns the data of the unique frame of the image.
         *
         * > **NOTE**
         * >
         * > - This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
         * >
         * > - Images occupy a large amount of memory. When you finish using a PixelMap instance, call
         * > [release]{@link @ohos.multimedia.image:image.PixelMap.release()} to free the memory promptly.
         * >
         * > - Before releasing the instance, ensure that all asynchronous operations associated with the instance have
         * > finished and the instance is no longer needed.
         * >
         * > - This function decodes all frames at once. If the number of frames is high or the size of individual frames is
         * > large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component
         * > for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this
         * > function.
         *
         * @param { DecodingOptions } options - Decoding options.
         * @param { AsyncCallback<Array<PixelMap>> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is undefined and **data** is the array of PixelMap objects obtained; otherwise, **err**
         *     is an error object.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980099 - The shared memory data is abnormal.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980103 - The image data is not supported.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @throws { BusinessError } 62980109 - Failed to crop the image.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @throws { BusinessError } 62980116 - Failed to decode the image.
         * @throws { BusinessError } 62980118 - Failed to create the image plugin.
         * @throws { BusinessError } 62980137 - Invalid media operation.
         * @throws { BusinessError } 62980173 - The DMA memory does not exist.
         * @throws { BusinessError } 62980174 - The DMA memory data is abnormal.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 10
         */
        createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void;
        /**
         * Obtains an array of delay times. This API uses a promise to return the result. This API applies only to images in
         * GIF or WebP format.
         *
         * @returns { Promise<Array<number>> } Promise used to return an array of delay times.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980110 - The image source data is incorrect.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @throws { BusinessError } 62980116 - Failed to decode the image.
         * @throws { BusinessError } 62980118 - Failed to create the image plugin.
         * @throws { BusinessError } 62980122 - Failed to decode the image header.
         * @throws { BusinessError } 62980149 - Invalid MIME type for the image source.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 10
         */
        getDelayTimeList(): Promise<Array<number>>;
        /**
         * Obtains an array of delay times. This API uses an asynchronous callback to return the result. This API applies
         * only to images in GIF or WebP format.
         *
         * @param { AsyncCallback<Array<number>> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the array of delay times obtained; otherwise, **err** is
         *     an error object.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980110 - The image source data is incorrect.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @throws { BusinessError } 62980116 - Failed to decode the image.
         * @throws { BusinessError } 62980118 - Failed to create the image plugin.
         * @throws { BusinessError } 62980122 - Failed to decode the image header.
         * @throws { BusinessError } 62980149 - Invalid MIME type for the image source.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 10
         */
        getDelayTimeList(callback: AsyncCallback<Array<number>>): void;
        /**
         * Obtains the list of disposal types. This API uses a promise to return the result. It is used only for GIF images.
         *
         * @returns { Promise<Array<number>> } Promise used to return an array of disposal types.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980137 - Invalid media operation.
         * @throws { BusinessError } 62980149 - Invalid MIME type for the image source.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 12
         */
        getDisposalTypeList(): Promise<Array<number>>;
        /**
         * Obtains the number of frames. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the number of frames.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980112 - The image format does not match.
         * @throws { BusinessError } 62980113 - Unknown image format.
         *     The image data provided is not in a recognized or supported format, or it may be corrupted.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @throws { BusinessError } 62980116 - Failed to decode the image.
         * @throws { BusinessError } 62980118 - Failed to create the image plugin.
         * @throws { BusinessError } 62980122 - Failed to decode the image header.
         * @throws { BusinessError } 62980137 - Invalid media operation.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 10
         */
        getFrameCount(): Promise<number>;
        /**
         * Obtains the number of frames. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the number of frames obtained; otherwise, **err** is an error
         *     object.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980112 - The image format does not match.
         * @throws { BusinessError } 62980113 - Unknown image format.
         *     The image data provided is not in a recognized or supported format, or it may be corrupted.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @throws { BusinessError } 62980116 - Failed to decode the image.
         * @throws { BusinessError } 62980118 - Failed to create the image plugin.
         * @throws { BusinessError } 62980122 - Failed to decode the image header.
         * @throws { BusinessError } 62980137 - Invalid media operation.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 10
         */
        getFrameCount(callback: AsyncCallback<number>): void;
        /**
         * Obtains the value of a property with the specified index in this image. This API uses a promise to return the
         * result.
         *
         * This API applies only to images that are in JPEG, PNG, HEIF<sup>12+</sup>, WEBP<sup>23+</sup>, or DNG<sup>23+</
         * sup> format and contain Exif information. (The supported formats may vary depending on the hardware.)
         *
         * @param { PropertyKey } key - Name of the property.
         * @param { ImagePropertyOptions } options - Image properties, including the image index and default property value.
         * @returns { Promise<string> } Promise used to return the property value. If the operation fails, the default value
         *     is returned.
         * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2
         *     .Incorrect parameter types;3.Parameter verification failed;
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980103 - The image data is not supported.
         * @throws { BusinessError } 62980110 - The image source data is incorrect.
         * @throws { BusinessError } 62980111 - The image source data is incomplete.
         * @throws { BusinessError } 62980112 - The image format does not match.
         * @throws { BusinessError } 62980113 - Unknown image format.
         *     The image data provided is not in a recognized or supported format, or it may be corrupted.
         * @throws { BusinessError } 62980115 - Invalid image parameter.
         * @throws { BusinessError } 62980118 - Failed to create the image plugin.
         * @throws { BusinessError } 62980122 - Failed to decode the image header.
         * @throws { BusinessError } 62980123 - The image does not support EXIF decoding.
         * @throws { BusinessError } 62980135 - The EXIF value is invalid.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 11
         */
        getImageProperty(key: PropertyKey, options?: ImagePropertyOptions): Promise<string>;
        /**
         * Obtains the value of a property with the specified index in this image. This API uses a promise to return the
         * result.
         *
         * This API applies only to images that are in JPEG, PNG, HEIF<sup>12+</sup>, or WEBP<sup>23+</sup> format and
         * contain the Exif information. (The supported formats may vary depending on the hardware.)
         *
         * @param { string } key - Name of the property.
         * @param { GetImagePropertyOptions } options - Image properties, including the image index and default property
         *     value.
         * @returns { Promise<string> } Promise used to return the property value. If the operation fails, the default value
         *     is returned.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 7
         * @deprecated since 11
         * @useinstead image.ImageSource.getImageProperty(key: PropertyKey, options?: ImagePropertyOptions)
         */
        getImageProperty(key: string, options?: GetImagePropertyOptions): Promise<string>;
        /**
         * Obtains the value of a property with the specified index in this image. This API uses an asynchronous callback to
         * return the result.
         *
         * This API applies only to images that are in JPEG, PNG, HEIF<sup>12+</sup>, or WEBP<sup>23+</sup> format and
         * contain the Exif information. (The supported formats may vary depending on the hardware.)
         *
         * @param { string } key - Name of the property.
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the property value obtained; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 7
         * @deprecated since 11
         * @useinstead image.ImageSource.getImageProperty(key: PropertyKey, options?: ImagePropertyOptions)
         */
        getImageProperty(key: string, callback: AsyncCallback<string>): void;
        /**
         * Obtains the value of a property in this image. This API uses an asynchronous callback to return the result.
         * This API applies only to images that are in JPEG, PNG, HEIF<sup>12+</sup>, or WEBP<sup>23+</sup> format and
         * contain the Exif information. (The supported formats may vary depending on the hardware.)
         *
         * @param { string } key - Name of the property.
         * @param { GetImagePropertyOptions } options - Image properties, including the image index and default property
         *     value.
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the property value obtained; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 7
         * @deprecated since 11
         * @useinstead image.ImageSource.getImageProperty(key: PropertyKey, options?: ImagePropertyOptions)
         */
        getImageProperty(key: string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void;
        /**
         * Obtains the values of properties with the given names in this image. This API uses a promise to return the
         * result.
         *
         * This API applies only to images that are in JPEG, PNG, HEIF, WEBP<sup>23+</sup>, or DNG<sup>23+</sup>format and
         * contain Exif information. (The supported formats may vary depending on the hardware.)
         *
         * @param { Array<PropertyKey> } key - Array of properties names.
         * @returns { Promise<Record<PropertyKey, string|null>> } Promise used to return the property values. If the
         *     operation fails, **null** is returned.
         * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2
         *     .Incorrect parameter types; 3.Parameter verification failed;
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980110 - The image source data is incorrect.
         * @throws { BusinessError } 62980113 - Unknown image format.
         *     The image data provided is not in a recognized or supported format, or it may be corrupted.
         * @throws { BusinessError } 62980116 - Failed to decode the image.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 12
         */
        getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string | null>>;
        /**
         * Obtains the value of a specified Exif property. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > - This API applies only to images that are in JPEG, PNG, HEIF, WEBP<sup>23+</sup>, or DNG<sup>23+</sup>format
         * > and contain Exif information. (The supported formats may vary depending on the hardware.)
         * >
         * > - Exif information is metadata of the image, including shooting time, camera model, aperture, focal length, and
         * > ISO.
         * >
         * > - This API operates synchronously and will block the current thread during execution. It should not be invoked
         * > from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For
         * > details, see
         * > [Overview of Concurrency in Time-Consuming Tasks](docroot://arkts-utils/time-consuming-task-overview.md).
         *
         * @param { PropertyKey } key - Name of the property.
         * @returns { string } Value of the specified Exif property. If retrieval fails, the default value of the property
         *     is returned. For details about the meaning of each data value, see
         *     [PropertyKey]{@link @ohos.multimedia.image:image.PropertyKey}.
         * @throws { BusinessError } 7700101  - Bad source. e.g.,1. Image has invalid width or height. 2. Image
         *     source incomplete. 3. Read image data failed. 4. Codec create failed.
         * @throws { BusinessError } 7700102 - Unsupported MIME type.
         * @throws { BusinessError } 7700202 - Unsupported metadata. For example, key is not supported.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @since 20
         */
        getImagePropertySync(key: PropertyKey): string;
        /**
         * Modifies the value of a property in this image. This API uses a promise to return the result.
         *
         * This API applies only to images that are in JPEG, PNG, HEIF<sup>12+</sup>, or WEBP<sup>23+</sup> format and
         * contain the Exif information. (The supported formats may vary depending on the hardware.)
         *
         * > **NOTE**
         * >
         * > The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a
         * > property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path
         * > , but not an ImageSource instance created based on buffers.
         *
         * @param { PropertyKey } key - Name of the property.
         * @param { string } value - New value of the property.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2
         *     .Incorrect parameter types;
         * @throws { BusinessError } 62980123 - The image does not support EXIF decoding.
         * @throws { BusinessError } 62980133 - The EXIF data is out of range.
         * @throws { BusinessError } 62980135 - The EXIF value is invalid.
         * @throws { BusinessError } 62980146 - The EXIF data failed to be written to the file.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 11
         */
        modifyImageProperty(key: PropertyKey, value: string): Promise<void>;
        /**
         * Modifies the value of a property in this image. This API uses a promise to return the result.
         *
         * This API applies only to images that are in JPEG, PNG, HEIF<sup>12+</sup>, or WEBP<sup>23+</sup> format and
         * contain the Exif information. (The supported formats may vary depending on the hardware.)
         *
         * > **NOTE**
         * >
         * > - The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a
         * > property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path
         * > , but not an ImageSource instance created based on buffers.
         *
         * @param { string } key - Name of the property.
         * @param { string } value - New value of the property.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 9
         * @deprecated since 11
         * @useinstead image.ImageSource.modifyImageProperty(key: PropertyKey, value: string)
         */
        modifyImageProperty(key: string, value: string): Promise<void>;
        /**
         * Modifies the value of a property in this image. This API uses an asynchronous callback to return the result.
         *
         * This API applies only to images that are in JPEG, PNG, HEIF<sup>12+</sup>, or WEBP<sup>23+</sup> format and
         * contain the Exif information. (The supported formats may vary depending on the hardware.)
         *
         * > **NOTE**
         * >
         * > - The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a
         * > property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path
         * > , but not an ImageSource instance created based on buffers.
         *
         * @param { string } key - Name of the property.
         * @param { string } value - New value of the property.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 9
         * @deprecated since 11
         * @useinstead image.ImageSource.modifyImageProperty(key: PropertyKey, value: string)
         */
        modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void;
        /**
         * Modifies the values of properties in this image. This API uses a promise to return the result.
         *
         * This API applies only to images that are in JPEG, PNG, HEIF, or WEBP<sup>23+</sup> format and contain the Exif
         * information. (The supported formats may vary depending on the hardware.)
         *
         * > **NOTE**
         * >
         * > The property byte length is changed when the **modifyImageProperties** API is called to modify the values of
         * > properties. Currently, you can call the API in an ImageSource instance created based on a file descriptor or
         * > path, but not an ImageSource instance created based on buffers.
         *
         * @param { Record<PropertyKey, string|null> } records - Array of property names and property values.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2
         *     .Incorrect parameter types; 3.Parameter verification failed;
         * @throws { BusinessError } 62980123 - The image does not support EXIF decoding.
         * @throws { BusinessError } 62980135 - The EXIF value is invalid.
         * @throws { BusinessError } 62980146 - The EXIF data failed to be written to the file.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform
         * @since 12
         */
        modifyImageProperties(records: Record<PropertyKey, string | null>): Promise<void>;
        /**
         * Modifies image properties in batches. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - Calling this API to modify properties alters the property byte length. You are advised to create an
         * > [image.createImageSource]{@link @ohos.multimedia.image:image.createImageSource(fd: number)} instance by passing a
         * > file descriptor or an
         * > [image.createImageSource]{@link @ohos.multimedia.image:image.createImageSource(uri: string)} instance by
         * > passing a URI.
         * >
         * > - This API modifies batch data in memory and writes the data to the file in a single operation. It is more
         * > efficient than
         * > [modifyImageProperties]{@link image.ImageSource.modifyImageProperties(records: Record<PropertyKey, string|null>)}
         * > .
         * >
         * > - This API applies only to images that are in JPEG, PNG, HEIF, or WEBP format and contain the Exif information.
         *
         * @param { Record<string, string|null> } records - Key-value pairs of image property names and property values.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7700102 - Unsupported MIME type.
         * @throws { BusinessError } 7700202 - Unsupported metadata. For example, the property key is not supported,
         *     or the property value is invalid.
         * @throws { BusinessError } 7700304 - Failed to write image properties to the file.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @since 22
         */
        modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>;
        /**
         * Updates incremental data. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } buf - Buffer for storing the incremental data.
         * @param { boolean } isFinished - Whether data update is complete. The value **true** means that the data update is
         *     complete and the last segment of data is stored in the buffer. The value **false** means that the data update
         *     is still in progress.
         * @param { number } offset - Offset of the data in the buffer, measured from the start of the entire image file, in
         *     bytes. [since 11]
         * @param { number } length - Length of the buffer, in bytes.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 9
         */
        updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number): Promise<void>;
        /**
         * Updates incremental data. This API uses an asynchronous callback to return the result.
         *
         * @param { ArrayBuffer } buf - Buffer for storing the incremental data.
         * @param { boolean } isFinished - Whether data update is complete. The value **true** means that the data update is
         *     complete and the last segment of data is stored in the buffer. The value **false** means that the data update
         *     is still in progress.
         * @param { number } offset - Offset of the data in the buffer, measured from the start of the entire image file, in
         *     bytes. [since 11]
         * @param { number } length - Length of the buffer, in bytes.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 9
         */
        updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number, callback: AsyncCallback<void>): void;
        /**
         * Releases this ImageSource instance. This API uses an asynchronous callback to return the result.
         *
         * Images occupy a large amount of memory. When you finish using an ImageSource instance, call this API to free the
         * memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 6
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this ImageSource instance. This API uses a promise to return the result.
         *
         * Images occupy a large amount of memory. When you finish using an ImageSource instance, call this API to free the
         * memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 6
         */
        release(): Promise<void>;
        /**
         * Creates a Picture object based on decoding options. This API uses a promise to return the result.
         *
         * Images occupy a large amount of memory. When you finish using a Picture instance, call
         * [release]{@link @ohos.multimedia.image:image.Picture.release} to free the memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @param { DecodingOptionsForPicture } options - Decoding options.
         * @returns { Promise<Picture> } Promise used to return the Picture object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 7700301 - Decode failed.
         * @throws { BusinessError } 7700203 - Unsupported options. For example, unsupported desiredPixelFormat causes
         *     a failure in converting an image into the desired pixel format. [since 24]
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @since 13
         */
        createPicture(options?: DecodingOptionsForPicture): Promise<Picture>;
        /**
         * Creates a **Picture** object using a specified image (only GIF and HEIF<sup>23+</sup> images currently). This API
         * uses a promise to return the result.
         *
         * Images occupy a large amount of memory. When you finish using a Picture instance, call
         * [release]{@link @ohos.multimedia.image:image.Picture.release} to free the memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @param { number } index - Index of the image. The value range is [0, Number of frames – 1].
         * @returns { Promise<Picture> } Promise used to return the Picture object.
         * @throws { BusinessError } 7700101 - Bad source.
         * @throws { BusinessError } 7700102 - Unsupported MIME type.
         * @throws { BusinessError } 7700103 - Image too large.
         * @throws { BusinessError } 7700203 - Unsupported options. For example, index is invalid.
         * @throws { BusinessError } 7700301 - Decoding failed.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @since 20
         */
        createPictureAtIndex(index: number): Promise<Picture>;
        /**
         * Supported image formats, include PNG, JPEG, BMP, GIF, WEBP, DNG, HEIC<sup>12+</sup>, WBMP<sup>23+</sup>, HEIFS<
         * sup>23+</sup>, and TIFF<sup>23+</sup>. Decoding support for certain formats depends on the specific device
         * hardware. You are advised to use the
         * [image.getImageSourceSupportedFormats<sup>20+</sup>]{@link @ohos.multimedia.image:image.getImageSourceSupportedFormats}
         * API before calling this API to dynamically query the decoding capabilities of the current device.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @crossplatform [since 10]
         * @since 6
         */
        readonly supportedFormats: Array<string>;
        /**
         * Reads image metadata. You can use **propertyKeys** to specify the keys of metadata. This API uses a promise to
         * return the result.
         *
         * This API applies only to images that are in JPEG, PNG, HEIF, WEBP, or DNG format and contain Exif information. (
         * The supported formats may vary depending on the hardware.)
         *
         * > **NOTE**
         * >
         * > When reading a DNG image, this API applies special handling to some **propertyKeys**. For details about the
         * > values of the following properties, see [PropertyKey]{@link @ohos.multimedia.image:image.PropertyKey}:
         * >
         * > - **NewSubfileType**, **ImageWidth**, **ImageLength**, **DefaultCropSize**, **Orientation**, **Compression**,
         * > **PhotometricInterpretation**, **PlanarConfiguration**, **RowsPerStrip**, **StripOffsets**, **StripByteCounts**
         * > , **SamplesPerPixel**, **BitsPerSample**, **YCbCrCoefficients**, **YCbCrSubSampling**, **YCbCrPositioning**,
         * > **ReferenceBlackWhite**, **XResolution**, **YResolution**, and **ResolutionUnit**: For these properties, values
         * > related to the main image are returned.
         * >
         * > - **ImageUniqueID**: The value is verified based on the specifications. If the value fails to comply with the
         * > specifications, an empty string is returned.
         * >
         * > - **ExifVersion**, **FlashpixVersion**, and **ColorSpace**: If the image does not contain these properties, an
         * > error code is returned.
         * >
         * > - **DNGVersion**: If the value is earlier than **1.0.0.0**, **1.0.0.0** is returned.
         * >
         * > - **GPSVersionID**: If there is no valid GPS data, the GPS version number is cleared and **0** is returned.
         * >
         * > - **GPSAltitudeRef**: If **GPSAltitude** is not set, this property is set to **0xFFFFFFFF**.
         * >
         * > - **ISOSpeedRatings**: If its value is **0** or **65535**, the recommended exposure index is used first. If the
         * > recommended exposure index does not exist, the standard output sensitivity, ISO speed, and exposure index are
         * > used in sequence.
         *
         * @param { string[] } [propertyKeys] - Array of properties names. If **propertyKeys** is not specified, all
         *     supported metadata is returned.
         * @param { number } [index] - Index of the property to be obtained. The default value is **0**.
         * @returns { Promise<ImageMetadata> } Promise used to return the **ImageMetadata** object, which contains the
         *     metadata object corresponding to the image property name. You can obtain the image property values through
         *     this metadata object.
         * @throws { BusinessError } 7700102 - Unsupported MIME type.
         * @throws { BusinessError } 7700202 - Unsupported metadata.
         * @throws { BusinessError } 7700204 - Invalid parameter. Possible causes: 1. The index is negative.
         *     2. The index is greater than or equal to the number of frames in the image.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 23
         */
        readImageMetadata(propertyKeys?: string[], index?: number): Promise<ImageMetadata>;
        /**
         * Modifies image properties in batches. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - Calling this API to modify properties alters the property byte length. You are advised to create an
         * > [image.createImageSource]{@link @ohos.multimedia.image:image.createImageSource(fd: number)} instance by passing a
         * > file descriptor or an
         * > [image.createImageSource]{@link @ohos.multimedia.image:image.createImageSource(uri: string)} instance by
         * > passing a URI.
         * >
         * > - This API modifies batch data in memory and writes the data to the file in a single operation. It is more
         * > efficient than
         * > [modifyImageProperties]{@link image.ImageSource.modifyImageProperties(records: Record<PropertyKey, string|null>)}
         * > .
         * >
         * > - This API applies only to images that are in JPEG, PNG, or HEIF format and contain the Exif information.
         * > Before modifying properties, use the **supportedFormats** property to check whether the device supports Exif
         * > information read/write in HEIF format.
         *
         * @param { ImageMetadata } imageMetadata - Image metadata set. If all property values in **imageMetadata** are
         *     empty, all Exif metadata is cleared.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7700102 - Unsupported MIME type.
         * @throws { BusinessError } 7700202 - Unsupported metadata.
         * @throws { BusinessError } 7700204 - Invalid parameter. Possible causes: The imageSource object is released.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 23
         */
        writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>;
        /**
         * Reads the metadata of an image source. You can use **metadataTypes** to specify the metadata types. If
         * **metadataTypes** is not specified, all supported metadata is returned. This API uses a promise to return the
         * result.
         *
         * This API applies only to images that are in JPEG, PNG, HEIF, WEBP, DNG, or HEIFS format. (The supported formats
         * may vary depending on the hardware.)
         *
         * > **NOTE**
         * >
         * > - **EXIF_METADATA** applies to JPEG, PNG, HEIF, WEBP, and DNG images.
         * >
         * > - **HEIFS_METADATA** applies to HEIFS images.
         * >
         * > - If the input **MetadataType** does not match the image format, error code **7700102** will be returned.
         *
         * @param { MetadataType[] } [metadataTypes] - Metadata type array. If this parameter is left empty, all supported
         *     metadata is obtained.
         * @param { number }[index] - Image frame number for metadata retrieval. The default value is **0**.
         *     <br>- For single-frame images, the value can only be 0.
         *     <br>- For multi-frame images such as animations, the value ranges from
         *     0 to (Number of frames – 1).
         * @returns { Promise<ImageMetadata> } Promise used to return the **ImageMetadata** object, which contains the
         *     corresponding metadata object. You can obtain the image property values through this metadata object.
         * @throws { BusinessError } 7700102 - Unsupported MIME type.
         * @throws { BusinessError } 7700202 - Unsupported metadata.
         * @throws { BusinessError } 7700204 - Invalid parameter. Possible causes: 1.The index is negative.
         *     2. The index is greater than or equal to the number of frames in the image.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 24
         */
        readImageMetadataByType(metadataTypes?: MetadataType[], index?: number): Promise<ImageMetadata>;
        /**
         * Obtains raw data from an image.
         *
         * @returns { Promise<ImageRawData> } A Promise instance used to return image raw data.
         * @throws { BusinessError } 7700101 - Bad source.
         * @throws { BusinessError } 7700102 - Unsupported MIME type.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 24
         */
        createImageRawData(): Promise<ImageRawData>;
        /**
         * Creates a thumbnail image based on image decoding parameters.
         * This method uses a promise to return the PixelMap object, which represents the thumbnail.
         *
         * @param { DecodingOptionsForThumbnail } [options] - Image decoding parameters for creating the thumbnail.
         * @returns { Promise<PixelMap | undefined> } A Promise instance used to return the PixelMap object representing
         *     the thumbnail.
         * @throws { BusinessError } 7700102 - Unsupported mimetype.
         * @throws { BusinessError } 7700103 - Image too large.
         * @throws { BusinessError } 7700204 - Invalid parameter, e.g, invalid generate size.
         * @throws { BusinessError } 7700301 - Decode failed.
         * @throws { BusinessError } 7700303 - Image does not carry thumbnail data.
         * @throws { BusinessError } 7700305 - Thumbnail generation failed.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 26.0.0
         */
        createThumbnail(options?: DecodingOptionsForThumbnail): Promise<PixelMap | undefined>;
        /**
         * Synchronously creates a thumbnail image based on image decoding parameters.
         * This method returns a `PixelMap` object, which represents the generated thumbnail.
         *
         * @param { DecodingOptionsForThumbnail } [options] - Image decoding parameters for creating the thumbnail.
         * @returns { PixelMap | undefined } The PixelMap object representing the generated thumbnail.
         * @throws { BusinessError } 7700102 - Unsupported mimetype.
         * @throws { BusinessError } 7700103 - Image too large.
         * @throws { BusinessError } 7700204 - Invalid parameter, e.g, invalid generate size.
         * @throws { BusinessError } 7700301 - Decode failed.
         * @throws { BusinessError } 7700303 - Image does not carry thumbnail data.
         * @throws { BusinessError } 7700305 - Thumbnail generation failed.
         * @syscap SystemCapability.Multimedia.Image.ImageSource
         * @stagemodelonly
         * @since 26.0.0
         */
        createThumbnailSync(options?: DecodingOptionsForThumbnail): PixelMap | undefined;
    }
    /**
     * Describes binary buffer info.
     *
     * @syscap SystemCapability.Multimedia.Image.ImagePacker
     * @stagemodelonly
     * @since 26.0.0
     */
    interface BinaryBufferInfo {
        /**
         * Describes binary buffer size.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        size: Size;
        /**
         * Describes binary buffer.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        data: ArrayBuffer;
        /**
         * Bytes per row.If it is not specified, it will be calculated as (width + 7) / 8.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        bytesPerRow?: number;
    }
    /**
     * The **ImagePacker** class provides APIs to compress and encode images.
     *
     * Before calling any API in ImagePacker, you must use
     * [image.createImagePacker]{@link @ohos.multimedia.image:image.createImagePacker} to create an ImagePacker instance.
     * During encoding, do not modify or release the ImageSource, PixelMap, or Picture object that is being used as the
     * input. Otherwise, a crash or other undefined behavior may occur.
     *
     * Images occupy a large amount of memory. When you finish using an ImagePacker instance, call
     * [release]{@link image.ImagePacker.release(callback: AsyncCallback<void>)} to free the memory promptly. Before
     * releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the
     * instance is no longer needed.
     *
     * Currently, the following formats are supported: jpeg, webp, png, heic<sup>12+</sup>, and gif<sup>18+</sup>. (The
     * supported formats may vary depending on the hardware. You can refer to the **supportedFormats** property of
     * ImagePacker to see which ones are supported.)
     *
     * @syscap SystemCapability.Multimedia.Image.ImagePacker
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    interface ImagePacker {
        /**
         * Compresses or re-encodes an image. This API uses an asynchronous callback to return the result.
         *
         * @param { ImageSource } source - Image source to compress or re-encode.
         * @param { PackingOption } option - Encoding parameters.
         * @param { AsyncCallback<ArrayBuffer> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the compressed or encoded image data; otherwise, **err**
         *     is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         * @deprecated since 13
         * @useinstead image.ImagePacker#packToData
         */
        packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void;
        /**
         * Compresses or re-encodes an image. This API uses a promise to return the result.
         *
         * @param { ImageSource } source - Image source to compress or re-encode.
         * @param { PackingOption } option - Encoding parameters.
         * @returns { Promise<ArrayBuffer> } Promise used to return the compressed or encoded image data.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         * @deprecated since 13
         * @useinstead image.ImagePacker#packToData
         */
        packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>;
        /**
         * Compresses or re-encodes an image. This API uses a promise to return the result.
         *
         * @param { ImageSource } source - Image source to compress or re-encode.
         * @param { PackingOption } options - Encoding parameters.
         * @returns { Promise<ArrayBuffer> } Promise used to return the compressed or encoded image data.
         * @throws { BusinessError } 401 - If the parameter is invalid.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @throws { BusinessError } 62980113 - Unknown image format.
         *     The image data provided is not in a recognized or supported format, or it may be corrupted.
         * @throws { BusinessError } 62980119 - Failed to encode the image.
         * @throws { BusinessError } 62980120 - Add pixelmap out of range.
         * @throws { BusinessError } 62980172 - Failed to encode icc.
         * @throws { BusinessError } 62980252 - Failed to create surface.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform
         * @atomicservice
         * @since 13
         */
        packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>;
        /**
         * Compresses or re-encodes an image. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > If the message "PixelMap mismatch" is returned, the parameters are abnormal. The possible cause is that the
         * > PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is
         * > released after this API is called.
         *
         * @param { PixelMap } source - PixelMap to compress or re-encode.
         * @param { PackingOption } option - Encoding parameters.
         * @param { AsyncCallback<ArrayBuffer> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the compressed or encoded image data; otherwise, **err**
         *     is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         * @deprecated since 13
         * @useinstead image.ImagePacker#packToData
         */
        packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void;
        /**
         * Compresses or re-encodes an image. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > If the message "PixelMap mismatch" is returned, the parameters are abnormal. The possible cause is that the
         * > PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is
         * > released after this API is called.
         *
         * @param { PixelMap } source - PixelMap to compress or re-encode.
         * @param { PackingOption } option - Encoding parameters.
         * @returns { Promise<ArrayBuffer> } Promise used to return the compressed or encoded image data.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         * @deprecated since 13
         * @useinstead image.ImagePacker#packToData
         */
        packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>;
        /**
         * Compresses or re-encodes an image. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > If error code 401 is returned, the parameters are abnormal. The possible cause is that the PixelMap object is
         * > released in advance. You need to check the code and ensure that the PixelMap object is released after this API
         * > is called.
         *
         * @param { PixelMap } source - PixelMap to compress or re-encode.
         * @param { PackingOption } options - Encoding parameters.
         * @returns { Promise<ArrayBuffer> } Promise used to return the compressed or encoded image data.
         * @throws { BusinessError } 401 - If the parameter is invalid.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @throws { BusinessError } 62980113 - Unknown image format.
         *     The image data provided is not in a recognized or supported format, or it may be corrupted.
         * @throws { BusinessError } 62980119 - Failed to encode the image.
         * @throws { BusinessError } 62980120 - Add pixelmap out of range.
         * @throws { BusinessError } 62980172 - Failed to encode icc.
         * @throws { BusinessError } 62980252 - Failed to create surface.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform
         * @atomicservice
         * @since 13
         */
        packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>;
        /**
         * Encodes multiple PixelMap objects into GIF data. This API uses a promise to return the result.
         *
         * @param { Array<PixelMap> } pixelmapSequence - PixelMaps to encode.
         * @param { PackingOptionsForSequence } options - Options for encoding animated images.
         * @returns { Promise<ArrayBuffer> } Promise used to return the encoded data.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types;3.Parameter verification failed.
         * @throws { BusinessError } 7800301 - Failed to encode image.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @since 18
         */
        packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>;
        /**
         * Encodes the image source into a file based on the specified encoding parameters. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { ImageSource } source - Image source to encode.
         * @param { number } fd - File descriptor.
         * @param { PackingOption } options - Encoding parameters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @throws { BusinessError } 62980113 - Unknown image format.
         *     The image data provided is not in a recognized or supported format, or it may be corrupted.
         * @throws { BusinessError } 62980115 - Invalid input parameter.
         * @throws { BusinessError } 62980119 - Failed to encode the image.
         * @throws { BusinessError } 62980120 - Add pixelmap out of range.
         * @throws { BusinessError } 62980172 - Failed to encode icc.
         * @throws { BusinessError } 62980252 - Failed to create surface.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform
         * @since 11
         */
        packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback<void>): void;
        /**
         * Encodes the image source into a file based on the specified encoding parameters. This API uses a promise to
         * return the result.
         *
         * @param { ImageSource } source - Image source to encode.
         * @param { number } fd - File descriptor.
         * @param { PackingOption } options - Encoding parameters.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @throws { BusinessError } 62980113 - Unknown image format.
         *     The image data provided is not in a recognized or supported format, or it may be corrupted.
         * @throws { BusinessError } 62980115 - Invalid input parameter.
         * @throws { BusinessError } 62980119 - Failed to encode the image.
         * @throws { BusinessError } 62980120 - Add pixelmap out of range.
         * @throws { BusinessError } 62980172 - Failed to encode icc.
         * @throws { BusinessError } 62980252 - Failed to create surface.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform
         * @since 11
         */
        packToFile(source: ImageSource, fd: number, options: PackingOption): Promise<void>;
        /**
         * Encodes the PixelMap into a file based on the specified encoding parameters. This API uses an asynchronous
         * callback to return the result.
         *
         * > **NOTE**
         * >
         * > If error code 62980115 is returned, the parameters are abnormal. The possible cause is that the PixelMap
         * > object is released in advance. You need to check the code and ensure that the PixelMap object is released after
         * > this API is called.
         *
         * @param { PixelMap } source - PixelMap to encode.
         * @param { number } fd - File descriptor.
         * @param { PackingOption } options - Encoding parameters.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @throws { BusinessError } 62980113 - Unknown image format.
         *     The image data provided is not in a recognized or supported format, or it may be corrupted.
         * @throws { BusinessError } 62980115 - Invalid input parameter.
         * @throws { BusinessError } 62980119 - Failed to encode the image.
         * @throws { BusinessError } 62980120 - Add pixelmap out of range.
         * @throws { BusinessError } 62980172 - Failed to encode icc.
         * @throws { BusinessError } 62980252 - Failed to create surface.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform
         * @since 11
         */
        packToFile(source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback<void>): void;
        /**
         * Encodes the PixelMap into a file based on the specified encoding parameters. This API uses a promise to return
         * the result.
         *
         * > **NOTE**
         * >
         * > If error code 62980115 is returned, the parameters are abnormal. The possible cause is that the PixelMap
         * > object is released in advance. You need to check the code and ensure that the PixelMap object is released after
         * > this API is called.
         *
         * @param { PixelMap } source - PixelMap to encode.
         * @param { number } fd - File descriptor.
         * @param { PackingOption } options - Encoding parameters.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 62980096 - The operation failed. Possible cause: 1.Image upload exception.
         *     2. Decoding process exception. 3. Insufficient memory.
         * @throws { BusinessError } 62980101 - The image data is abnormal.
         * @throws { BusinessError } 62980106 - The image data is too large. This status code is thrown when an error occurs
         *     during the process of checking size.
         * @throws { BusinessError } 62980113 - Unknown image format.
         *     The image data provided is not in a recognized or supported format, or it may be corrupted.
         * @throws { BusinessError } 62980115 - Invalid input parameter.
         * @throws { BusinessError } 62980119 - Failed to encode the image.
         * @throws { BusinessError } 62980120 - Add pixelmap out of range.
         * @throws { BusinessError } 62980172 - Failed to encode icc.
         * @throws { BusinessError } 62980252 - Failed to create surface.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform
         * @since 11
         */
        packToFile(source: PixelMap, fd: number, options: PackingOption): Promise<void>;
        /**
         * Encodes multiple PixelMaps into a GIF file. This API uses a promise to return the result.
         *
         * @param { Array<PixelMap> } pixelmapSequence - PixelMaps to encode.
         * @param { number } fd - File descriptor.
         * @param { PackingOptionsForSequence } options - Options for encoding animated images.
         * @returns { Promise<void> } that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types;3.Parameter verification failed.
         * @throws { BusinessError } 7800301 - Failed to encode image.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @since 18
         */
        packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>;
        /**
        * Releases this ImagePacker instance. This API uses an asynchronous callback to return the result.
        *
        * Images occupy a large amount of memory. When you finish using an ImagePacker instance, call this API to free the
        * memory promptly.
        *
        * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
        * and the instance is no longer needed.
        *
        * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
        *     **err** is **undefined**; otherwise, **err** is an error object.
        * @syscap SystemCapability.Multimedia.Image.ImagePacker
        * @crossplatform [since 10]
        * @since 6
        */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this ImagePacker instance. This API uses a promise to return the result.
         *
         * Images occupy a large amount of memory. When you finish using an ImagePacker instance, call this API to free the
         * memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform [since 10]
         * @since 6
         */
        release(): Promise<void>;
        /**
         * Compresses or re-encodes an image. This API uses a promise to return the result.
         *
         * @param { Picture } picture - Picture to compress or re-encode.
         * @param { PackingOption } options - Encoding parameters.
         * @returns { Promise<ArrayBuffer> } Promise used to return the compressed or encoded image data.
         * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 7800301 - Encode failed.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @since 13
         */
        packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>;
        /**
         * Encodes the Picture into a file based on the specified encoding parameters. This API uses a promise to return the
         * result.
         *
         * @param { Picture } picture - Picture to encode.
         * @param { number } fd - File descriptor.
         * @param { PackingOption } options - Encoding parameters.
         * @returns { Promise<void> } that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 7800301 - Encode failed.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @since 13
         */
        packToFile(picture: Picture, fd: number, options: PackingOption): Promise<void>;
        /**
         * Compresses or packs an image into a file and uses a promise to return the result.
         *
         * @param { BinaryBufferInfo } bufferInfo - image buffer info.
         * @param { number } fd - ID of a file descriptor
         *     <br>The value must be a positive integer.
         * @param { PackingOptionsForTiff } [options] - Options for tiff image packing.
         * @returns { Promise<void> } A Promise instance used to return the operation result.
         * @throws { BusinessError } 7800202 - Invalid parameter. Possible causes: 1. Invalid FD; 2. Compression algorithm
         *     mismatch.
         * @throws { BusinessError } 7800301 - Encode failed.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: number, options?: PackingOptionsForTiff): Promise<void>;
        /**
         * Compresses or packs an image into a file and uses a promise to return the result.
         *
         * @param { BinaryBufferInfo } bufferInfo - image buffer info.
         * @param { PackingOptionsForTiff } [options] - Options for tiff image packing.
         * @returns { Promise<ArrayBuffer> } A Promise instance used to return the compressed or packed data.
         * @throws { BusinessError } 7800202 - Invalid parameter. Possible causes: 1. Invalid FD; 2. Compression algorithm
         *     mismatch.
         * @throws { BusinessError } 7800301 - Encode failed.
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @stagemodelonly
         * @since 26.0.0
         */
        packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>;
        /**
         * Supported formats for image encoding, including jpeg, webp, png, heic<sup>12+</sup>, and gif<sup>18+</sup>. (The
         * supported formats may vary depending on the hardware.)
         *
         * @syscap SystemCapability.Multimedia.Image.ImagePacker
         * @crossplatform [since 10]
         * @since 6
         */
        readonly supportedFormats: Array<string>;
    }
    /**
     * The **Image** class is used to obtain image content.
     *
     * An Image instance is returned when
     * [readNextImage]{@link @ohos.multimedia.image:image.ImageReceiver.readNextImage(callback: AsyncCallback<Image>)} and
     * [readLatestImage]{@link @ohos.multimedia.image:image.ImageReceiver.readLatestImage(callback: AsyncCallback<Image>)}
     * are called.
     *
     * Image properties are initialized only during image creation and cannot be changed later. These properties do not
     * affect the actual image content. You should always rely on the properties written by the image producer, that is,
     * the content actually sent to the [ImageReceiver]{@link @ohos.multimedia.image:image.ImageReceiver} by the data source.
     * Images occupy a large amount of memory. When you finish using an Image instance, call
     * [release]{@link image.Image.release(callback: AsyncCallback<void>)} to free the memory promptly. Before releasing
     * the instance, ensure that all asynchronous operations associated with the instance have finished and the instance
     * is no longer needed.
     *
     * @syscap SystemCapability.Multimedia.Image.Core
     * @since 9
     */
    interface Image {
        /**
         * Image area to be cropped.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        clipRect: Region;
        /**
         * Image size.
         *
         * If the Image object stores camera preview stream data (YUV image data), the width and height in **size**
         * reflect the dimensions of the YUV image.
         *
         * If the Image object stores camera capture stream data (JPEG image data), given that it is an encoded file,
         * the width in **size** is the size of the JPEG file, while the height is set to **1**.
         *
         * The type of data stored in the Image object depends on whether the application passes the surface ID in the
         * receiver to a previewOutput or captureOutput object of the camera.
         *
         * For details about the best practices of camera preview and photo capture, see
         * [Dual-Channel Preview (ArkTS)](docroot://media/camera/camera-dual-channel-preview.md) and
         * [Photo Capture Sample (ArkTS)](docroot://media/camera/camera-shooting-case.md).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        readonly size: Size;
        /**
         * Image format. For details, see
         * [OH_NativeBuffer_Format](docroot://reference/apis-arkgraphics2d/c-apis/capi-buffer-common-h.md#oh_nativebuffer_format).
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        readonly format: number;
        /**
         * Image timestamp. Timestamps, measured in nanoseconds, are usually monotonically increasing. The specific meaning
         * and baseline of these timestamps are determined by the image producer, which is the camera in the camera preview
         * and photo scenarios. As a result, images from different producers may carry timestamps with distinct meanings and
         * baselines, making direct comparison between them infeasible. To obtain the generation time of a photo, you can
         * use
         * [getImageProperty]{@link @ohos.multimedia.image:image.ImageSource.getImageProperty(key: PropertyKey, options?: ImagePropertyOptions)}
         * to read the related Exif information.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 12
         */
        readonly timestamp: number;
        /**
         * Color space of the image.
         *
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        readonly colorSpace: colorSpaceManager.ColorSpace;
        /**
         * Obtains the component buffer from the Image instance based on the color component type. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { ComponentType } componentType - Component type. (Currently, only **ComponentType:JPEG** is supported.
         *     The actual format is determined by the producer, for example, camera.)
         * @param { AsyncCallback<Component> } callback - Callback used to return the result. If the operation is successful
         *     , **err** is **undefined** and **data** is the component buffer obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        getComponent(componentType: ComponentType, callback: AsyncCallback<Component>): void;
        /**
         * Obtains the component buffer from the Image instance based on the color component type. This API uses a promise
         * to return the result.
         *
         * @param { ComponentType } componentType - Component type. (Currently, only **ComponentType:JPEG** is supported.
         *     The actual format is determined by the producer, for example, camera.)
         * @returns { Promise<Component> } Promise used to return the component buffer.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        getComponent(componentType: ComponentType): Promise<Component>;
        /**
         * Releases this Image instance. This API uses an asynchronous callback to return the result.
         *
         * The corresponding resources must be released before another image arrives.
         *
         * Images occupy a large amount of memory. When you finish using an Image instance, call this API to free the memory
         * promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this Image instance. This API uses a promise to return the result.
         *
         * The corresponding resources must be released before another image arrives.
         *
         * Images occupy a large amount of memory. When you finish using an Image instance, call this API to free the memory
         * promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @since 9
         */
        release(): Promise<void>;
        /**
         * Obtains ImageBufferData from an image.
         *
         * > **NOTE**
         * >
         * > **byteBuffer** in **ImageBufferData** is a shallow copy of the internal buffer. When the lifecycle of an image
         * > ends, do not perform any operations on **byteBuffer**, as this may lead to undefined behavior.
         *
         * @returns { ImageBufferData | null } Struct that encapsulates the image data buffer. If no struct is obtained,
         *     **null** is returned.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getBufferData(): ImageBufferData | null;
        /**
         * Obtains the HDR metadata from an image based on the HDR metadata type.
         *
         * @param { HdrMetadataKey } key - HDR metadata key.
         * @returns { HdrMetadataValue | null } Value of the HDR metadata key. If the image does not have HDR metadata,
         *     **null** is returned.
         * @throws { BusinessError } 7600206 - Invalid parameter.
         * @throws { BusinessError } 7600302 - Memory copy failed.
         * @syscap SystemCapability.Multimedia.Image.Core
         * @stagemodelonly
         * @since 23
         */
        getMetadata(key: HdrMetadataKey): HdrMetadataValue | null;
    }
    /**
     * The **ImageReceiver** class provides APIs to obtain the surface ID of a component, read the latest image, read the
     * next image, and release the ImageReceiver instance. The ImageReceiver acts as the receiver and consumer of images.
     * Its parameter properties do not actually affect the received images. The configuration of image properties should
     * be done on the sending side (the producer), such as when creating a camera preview stream with
     * [createPreviewOutput]{@link @ohos.multimedia.camera:camera.CameraManager.createPreviewOutput(profile: Profile, surfaceId: string)}
     * .
     * Before calling any APIs in ImageReceiver, you must use
     * [image.createImageReceiver]{@link @ohos.multimedia.image:image.createImageReceiver(size: Size, format: ImageFormat, capacity: number)}
     * to create an ImageReceiver instance.
     * Since API version 23, you are advised to use
     * [image.createImageReceiver]{@link @ohos.multimedia.image:image.createImageReceiver(size: Size, format: ImageFormat, capacity: number)} to
     * create an **ImageReceiver** instance based on the passed
     * [ImageReceiverOptions]{@link  @ohos.multimedia.image:image.ImageReceiverOptions}.
     * Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call
     * [release]{@link image.ImageReceiver.release(callback: AsyncCallback<void>)} to free the memory promptly. Before
     * releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the
     * instance is no longer needed.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageReceiver
     * @since 9
     */
    interface ImageReceiver {
        /**
         * Image size. This parameter does not affect the size of the received image. The actual returned size is determined
         * by the producer, for example, the camera.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        readonly size: Size;
        /**
         * Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value.
         * The actual capacity is determined by the device hardware.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        readonly capacity: number;
        /**
         * Image format. The value is an enum value of [ImageFormat]{@link @ohos.multimedia.image:image.ImageFormat}. (
         * Currently, only **ImageFormat:JPEG** is supported. The format actually returned depends on the producer, for
         * example, camera.)
         *
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        readonly format: ImageFormat;
        /**
         * Obtains a surface ID for the camera or other components. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the surface ID obtained. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        getReceivingSurfaceId(callback: AsyncCallback<string>): void;
        /**
         * Obtains a surface ID for the camera or other components. This API uses a promise to return the result.
         *
         * @returns { Promise<string> } Promise used to return the surface ID.
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        getReceivingSurfaceId(): Promise<string>;
        /**
         * Reads the latest image from the ImageReceiver instance. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API can be called to receive data only after the
         * > [on]{@link image.ImageReceiver.on(type: 'imageArrival', callback: AsyncCallback<void>)} callback is triggered.
         * > When the [Image]{@link @ohos.multimedia.image:image.Image} object returned by this API is no longer needed, call
         * > [release]{@link @ohos.multimedia.image:image.Image.release(callback: AsyncCallback<void>)} to release the
         * > object. New data can be received only after the release.
         *
         * @param { AsyncCallback<Image> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the latest image obtained; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        readLatestImage(callback: AsyncCallback<Image>): void;
        /**
         * Reads the latest image from the ImageReceiver instance. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called to receive data only after the
         * > [on]{@link image.ImageReceiver.on(type: 'imageArrival', callback: AsyncCallback<void>)} callback is triggered.
         * > When the [Image]{@link @ohos.multimedia.image:image.Image} object returned by this API is no longer needed, call
         * > [release]{@link @ohos.multimedia.image:image.Image.release(callback: AsyncCallback<void>)} to release the
         * > object. New data can be received only after the release.
         *
         * @returns { Promise<Image> } Promise used to return the latest image.
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        readLatestImage(): Promise<Image>;
        /**
         * Reads the next image from the ImageReceiver instance. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API can be called to receive data only after the
         * > [on]{@link image.ImageReceiver.on(type: 'imageArrival', callback: AsyncCallback<void>)} callback is triggered.
         * > When the [Image]{@link @ohos.multimedia.image:image.Image} object returned by this API is no longer needed, call
         * > [release]{@link @ohos.multimedia.image:image.Image.release(callback: AsyncCallback<void>)} to release the
         * > object. New data can be received only after the release.
         *
         * @param { AsyncCallback<Image> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the next image obtained. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        readNextImage(callback: AsyncCallback<Image>): void;
        /**
         * Reads the next image from the ImageReceiver instance. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called to receive data only after the
         * > [on]{@link image.ImageReceiver.on(type: 'imageArrival', callback: AsyncCallback<void>)} callback is triggered.
         * > When the [Image]{@link @ohos.multimedia.image:image.Image} object returned by this API is no longer needed, call
         * > [release]{@link @ohos.multimedia.image:image.Image.release(callback: AsyncCallback<void>)} to release the
         * > object. New data can be received only after the release.
         *
         * @returns { Promise<Image> } Promise used to return the next image.
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        readNextImage(): Promise<Image>;
        /**
         * Listens for image arrival events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'imageArrival' } type - Type of event to listen for. The value is fixed at **'imageArrival'**, which is
         *     triggered when an image is received.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        on(type: 'imageArrival', callback: AsyncCallback<void>): void;
        /**
         * Unregisters the callback function that is triggered when the buffer is released. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'imageArrival' } type - Type of event, which is **'imageArrival'**.
         * @param { AsyncCallback<void> } callback - Callback to unregister.
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 13
         */
        off(type: 'imageArrival', callback?: AsyncCallback<void>): void;
        /**
         * Releases this ImageReceiver instance. This API uses an asynchronous callback to return the result.
         *
         * Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call this API to free
         * the memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this ImageReceiver instance. This API uses a promise to return the result.
         *
         * Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call this API to free
         * the memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.ImageReceiver
         * @since 9
         */
        release(): Promise<void>;
    }
    /**
     * The ImageCreator class provides APIs for applications to request an image data area and compile image data.
     *
     * Before calling any APIs in ImageCreator, you must use
     * [image.createImageCreator]{@link @ohos.multimedia.image:image.createImageCreator(size: Size, format: ImageFormat, capacity: number)}
     * to create an ImageCreator instance. ImageCreator does not support multiple threads.
     *
     * Images occupy a large amount of memory. When you finish using an ImageCreator instance, call
     * [release]{@link image.ImageCreator.release(callback: AsyncCallback<void>)} to free the memory promptly. Before
     * releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the
     * instance is no longer needed.
     *
     * @syscap SystemCapability.Multimedia.Image.ImageCreator
     * @since 9
     */
    interface ImageCreator {
        /**
         * Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value.
         * The actual capacity is determined by the device hardware.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageCreator
         * @since 9
         */
        readonly capacity: number;
        /**
         * Image format.
         *
         * @syscap SystemCapability.Multimedia.Image.ImageCreator
         * @since 9
         */
        readonly format: ImageFormat;
        /**
         * Obtains an image buffer from the idle queue and writes image data into it. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { AsyncCallback<Image> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the latest image obtained; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageCreator
         * @since 9
         */
        dequeueImage(callback: AsyncCallback<Image>): void;
        /**
         * Obtains an image buffer from the idle queue and writes image data into it. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<Image> } Promise used to return the latest image.
         * @syscap SystemCapability.Multimedia.Image.ImageCreator
         * @since 9
         */
        dequeueImage(): Promise<Image>;
        /**
         * Places the drawn image in the queue. This API uses an asynchronous callback to return the result.
         *
         * @param { Image } image - Drawn image.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageCreator
         * @since 9
         */
        queueImage(image: Image, callback: AsyncCallback<void>): void;
        /**
         * Places the drawn image in the queue. This API uses a promise to return the result.
         *
         * @param { Image } image - Drawn image.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.ImageCreator
         * @since 9
         */
        queueImage(image: Image): Promise<void>;
        /**
         * Listens for image release events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'imageRelease' } type - Type of event, which is **'imageRelease'**.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageCreator
         * @since 9
         */
        on(type: 'imageRelease', callback: AsyncCallback<void>): void;
        /**
         * Unregisters the callback function that is triggered when the buffer is released. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'imageRelease' } type - Type of event, which is **'imageRelease'**.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is null; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageCreator
         * @since 13
         */
        off(type: 'imageRelease', callback?: AsyncCallback<void>): void;
        /**
         * Releases this ImageCreator instance. This API uses an asynchronous callback to return the result.
         *
         * Images occupy a large amount of memory. When you finish using an ImageCreator instance, call this API to free the
         * memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Image.ImageCreator
         * @since 9
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this ImageCreator instance. This API uses a promise to return the result.
         *
         * Images occupy a large amount of memory. When you finish using an ImageCreator instance, call this API to free the
         * memory promptly.
         *
         * Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished
         * and the instance is no longer needed.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Image.ImageCreator
         * @since 9
         */
        release(): Promise<void>;
    }
    /**
     * Obtains the supported decoding formats, represented by MIME types.
     *
     * @returns { string[] } List of supported decoding formats (MIME types).
     * @syscap SystemCapability.Multimedia.Image.ImageSource
     * @since 20
     */
    function getImageSourceSupportedFormats(): string[];
    /**
     * Obtains the supported encoding formats, represented by MIME types.
     *
     * @returns { string[] } List of supported encoding formats (MIME types).
     * @syscap SystemCapability.Multimedia.Image.ImagePacker
     * @since 20
     */
    function getImagePackerSupportedFormats(): string[];
}
export default image;

```
