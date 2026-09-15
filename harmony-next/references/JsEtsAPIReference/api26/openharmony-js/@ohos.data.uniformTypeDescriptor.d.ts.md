# @ohos.data.uniformTypeDescriptor.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2026 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @file
 * @kit ArkData
 */
/**
 * The **uniformTypeDescriptor** module abstracts and defines uniform data types.
 *
 * @syscap SystemCapability.DistributedDataManager.UDMF.Core
 * @stagemodelonly
 * @crossplatform [since 14]
 * @atomicservice [since 11]
 * @since 10
 */
declare namespace uniformTypeDescriptor {
    /**
     * Enumerates the uniform data types. Some data types are related. For example, the JPEG type belongs to the IMAGE
     * type. For more preset data types, see [Preset UTD List].
     *
     * The following table lists the common uniform data types.
     *
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @crossplatform [since 14]
     * @atomicservice [since 11]
     * @since 10
     */
    enum UniformDataType {
        /**
         * Generic physical storage type.
         *
         * This type is uncategorized.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        ENTITY = 'general.entity',
        /**
         * Generic logical content type.
         *
         * This type is uncategorized.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        OBJECT = 'general.object',
        /**
         * Generic composite content type. For example, a PDF file that contains text and image.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        COMPOSITE_OBJECT = 'general.composite-object',
        /**
         * Generic text type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 14]
         * @atomicservice [since 11]
         * @since 10
         */
        TEXT = 'general.text',
        /**
         * Text without specific encoding or identifier.
         *
         * This type belongs to **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 14]
         * @atomicservice [since 11]
         * @since 10
         */
        PLAIN_TEXT = 'general.plain-text',
        /**
         * HTML.
         *
         * This type belongs to **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 14]
         * @atomicservice [since 11]
         * @since 10
         */
        HTML = 'general.html',
        /**
         * Hyperlink.
         *
         * This type belongs to **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 14]
         * @atomicservice [since 11]
         * @since 10
         */
        HYPERLINK = 'general.hyperlink',
        /**
         * XML.
         *
         * This type belongs to **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        XML = 'general.xml',
        /**
         * XHTML.
         *
         * This type belongs to **XML**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        XHTML = 'general.xhtml',
        /**
         * RSS.
         *
         * This type belongs to **XML**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        RSS = 'general.rss',
        /**
         * Synchronized Multimedia Integration Language (SMIL).
         *
         * This type belongs to **XML**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        SMIL = 'com.real.smil',
        /**
         * Generic source code type.
         *
         * This type belongs to **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        SOURCE_CODE = 'general.source-code',
        /**
         * Source code in any scripting language.
         *
         * This type belongs to **SOURCE_CODE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        SCRIPT = 'general.script',
        /**
         * Shell script.
         *
         * This type belongs to **SCRIPT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        SHELL_SCRIPT = 'general.shell-script',
        /**
         * C shell script.
         *
         * This type belongs to **SHELL_SCRIPT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        CSH_SCRIPT = 'general.csh-script',
        /**
         * Perl script.
         *
         * This type belongs to **SHELL_SCRIPT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        PERL_SCRIPT = 'general.perl-script',
        /**
         * PHP script.
         *
         * This type belongs to **SHELL_SCRIPT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        PHP_SCRIPT = 'general.php-script',
        /**
         * Python script.
         *
         * This type belongs to **SHELL_SCRIPT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        PYTHON_SCRIPT = 'general.python-script',
        /**
         * Ruby script.
         *
         * This type belongs to **SHELL_SCRIPT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        RUBY_SCRIPT = 'general.ruby-script',
        /**
         * TypeScript source code.
         *
         * This type belongs to **SOURCE_CODE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        TYPE_SCRIPT = 'general.type-script',
        /**
         * JavaScript source code.
         *
         * This type belongs to **SOURCE_CODE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        JAVA_SCRIPT = 'general.java-script',
        /**
         * CSS.
         *
         * This type belongs to **SCRIPT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        CSS = 'general.css',
        /**
         * Header file in C.
         *
         * This type belongs to **SOURCE_CODE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        C_HEADER = 'general.c-header',
        /**
         * Source code in C.
         *
         * This type belongs to **SOURCE_CODE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        C_SOURCE = 'general.c-source',
        /**
         * Header file in C++.
         *
         * This type belongs to **SOURCE_CODE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        C_PLUS_PLUS_HEADER = 'general.c-plus-plus-header',
        /**
         * Source code in C++.
         *
         * This type belongs to **SOURCE_CODE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        C_PLUS_PLUS_SOURCE = 'general.c-plus-plus-source',
        /**
         * Source code in Java.
         *
         * This type belongs to **SOURCE_CODE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        JAVA_SOURCE = 'general.java-source',
        /**
         * Source code in TEX format.
         *
         * This type belongs to **SOURCE_CODE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        TEX = 'general.tex',
        /**
         * Markdown.
         *
         * This type belongs to **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        MARKDOWN = 'general.markdown',
        /**
         * ASCII.
         *
         * This type belongs to **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        ASC_TEXT = 'general.asc-text',
        /**
         * Rich text.
         *
         * This type belongs to **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        RICH_TEXT = 'general.rich-text',
        /**
         * Generic type of all delimited value texts.
         *
         * This type belongs to **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        DELIMITED_VALUES_TEXT = 'general.delimited-values-text',
        /**
         * Comma-separated values (CSV).
         *
         * This type belongs to **DELIMITED_VALUES_TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        COMMA_SEPARATED_VALUES_TEXT = 'general.comma-separated-values-text',
        /**
         * Tab-separated values (TSV).
         *
         * This type belongs to **DELIMITED_VALUES_TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        TAB_SEPARATED_VALUES_TEXT = 'general.tab-separated-values-text',
        /**
         * Generic eBook file format type.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        EBOOK = 'general.ebook',
        /**
         * Electronic publication (EPUB).
         *
         * This type belongs to **EBOOK**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        EPUB = 'general.epub',
        /**
         * AZW.
         *
         * This type belongs to **EBOOK**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        AZW = 'com.amazon.azw',
        /**
         * AZW3.
         *
         * This type belongs to **EBOOK**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        AZW3 = 'com.amazon.azw3',
        /**
         * KFX.
         *
         * This type belongs to **EBOOK**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        KFX = 'com.amazon.kfx',
        /**
         * MOBI.
         *
         * This type belongs to **EBOOK**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        MOBI = 'com.amazon.mobi',
        /**
         * Generic media type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        MEDIA = 'general.media',
        /**
         * Image.
         *
         * This type belongs to **MEDIA**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 14]
         * @atomicservice [since 11]
         * @since 10
         */
        IMAGE = 'general.image',
        /**
         * JPEG.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        JPEG = 'general.jpeg',
        /**
         * PNG.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        PNG = 'general.png',
        /**
         * Raw image.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        RAW_IMAGE = 'general.raw-image',
        /**
         * TIFF.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        TIFF = 'general.tiff',
        /**
         * BMP.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        BMP = 'com.microsoft.bmp',
        /**
         * Windows icon.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        ICO = 'com.microsoft.ico',
        /**
         * Adobe Photoshop image.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        PHOTOSHOP_IMAGE = 'com.adobe.photoshop-image',
        /**
         * Adobe Illustrator image (.ai).
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        AI_IMAGE = 'com.adobe.illustrator.ai-image',
        /**
         * Generic type of the fax.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        FAX = 'general.fax',
        /**
         * J2 jConnect fax file format.
         *
         * This type belongs to **FAX**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        JFX_FAX = 'com.j2.jfx-fax',
        /**
         * EFX file format.
         *
         * This type belongs to **FAX**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        EFX_FAX = 'com.js.efx-fax',
        /**
         * X BitMAP (XBM) used in the X Window system (X11).
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        XBITMAP_IMAGE = 'general.xbitmap-image',
        /**
         * GIF.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        GIF = 'general.gif',
        /**
         * Tagged Graphics (TGA) format.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        TGA_IMAGE = 'com.truevision.tga-image',
        /**
         * Silicon Graphics image (SGI) format.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        SGI_IMAGE = 'com.sgi.sgi-image',
        /**
         * OpenXR image format.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENEXR_IMAGE = 'com.ilm.openexr-image',
        /**
         * FlashPix image format.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        FLASHPIX_IMAGE = 'com.kodak.flashpix.image',
        /**
         * Microsoft Word.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        WORD_DOC = 'com.microsoft.word.doc',
        /**
         * Microsoft Excel.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        EXCEL = 'com.microsoft.excel.xls',
        /**
         * Microsoft PowerPoint presentation format.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        PPT = 'com.microsoft.powerpoint.ppt',
        /**
         * Microsoft Word template.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        WORD_DOT = 'com.microsoft.word.dot',
        /**
         * Microsoft PowerPoint slide show format.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        POWERPOINT_PPS = 'com.microsoft.powerpoint.pps',
        /**
         * Microsoft PowerPoint template.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        POWERPOINT_POT = 'com.microsoft.powerpoint.pot',
        /**
         * Microsoft Excel template.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        EXCEL_XLT = 'com.microsoft.excel.xlt',
        /**
         * Microsoft Visio.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        VISIO_VSD = 'com.microsoft.visio.vsd',
        /**
         * PDF.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        PDF = 'com.adobe.pdf',
        /**
         * PostScript.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        POSTSCRIPT = 'com.adobe.postscript',
        /**
         * Encapsulated PostScript.
         *
         * This type belongs to **POSTSCRIPT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        ENCAPSULATED_POSTSCRIPT = 'com.adobe.encapsulated-postscript',
        /**
         * Generic video type.
         *
         * This type belongs to **MEDIA**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 14]
         * @atomicservice [since 11]
         * @since 10
         */
        VIDEO = 'general.video',
        /**
         * AVI.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        AVI = 'general.avi',
        /**
         * MPEG-1 or MPEG-2.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        MPEG = 'general.mpeg',
        /**
         * MPEG-4.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        MPEG4 = 'general.mpeg-4',
        /**
         * 3GP (3GPP file format).
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        VIDEO_3GPP = 'general.3gpp',
        /**
         * 3G2 (3GPP2 file format).
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        VIDEO_3GPP2 = 'general.3gpp2',
        /**
         * MPEG-TS.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        TS = 'general.ts',
        /**
         * MPEG video playlist format.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        MPEGURL_VIDEO = 'general.mpegurl-video',
        /**
         * Windows WM format.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        WINDOWS_MEDIA_WM = 'com.microsoft.windows-media-wm',
        /**
         * Windows WMV format.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        WINDOWS_MEDIA_WMV = 'com.microsoft.windows-media-wmv',
        /**
         * Windows WMP format.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        WINDOWS_MEDIA_WMP = 'com.microsoft.windows-media-wmp',
        /**
         * Windows WVX format.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        WINDOWS_MEDIA_WVX = 'com.microsoft.windows-media-wvx',
        /**
         * Windows WMX format.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        WINDOWS_MEDIA_WMX = 'com.microsoft.windows-media-wmx',
        /**
         * RealMedia format.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        REALMEDIA = 'com.real.realmedia',
        /**
         * MKV.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        MATROSKA_VIDEO = 'org.matroska.mkv',
        /**
         * Flash.
         *
         * This type belongs to **VIDEO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        FLASH = 'com.adobe.flash',
        /**
         * Generic audio type.
         *
         * This type belongs to **MEDIA**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 14]
         * @atomicservice [since 11]
         * @since 10
         */
        AUDIO = 'general.audio',
        /**
         * AAC.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        AAC = 'general.aac',
        /**
         * AIFF.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        AIFF = 'general.aiff',
        /**
         * ALAC.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        ALAC = 'general.alac',
        /**
         * FLAC.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        FLAC = 'general.flac',
        /**
         * MP3.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        MP3 = 'general.mp3',
        /**
         * OGG.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        OGG = 'general.ogg',
        /**
         * PCM.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        PCM = 'general.pcm',
        /**
         * Windows WMA.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        WINDOWS_MEDIA_WMA = 'com.microsoft.windows-media-wma',
        /**
         * Windows Waveform.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        WAVEFORM_AUDIO = 'com.microsoft.waveform-audio',
        /**
         * Windows WAX.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        WINDOWS_MEDIA_WAX = 'com.microsoft.windows-media-wax',
        /**
         * AU format.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        AU_AUDIO = 'general.au-audio',
        /**
         * AIFC.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        AIFC_AUDIO = 'general.aifc-audio',
        /**
         * MPEG audio playlist format.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        MPEGURL_AUDIO = 'general.mpegurl-audio',
        /**
         * MPEG-4.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        MPEG_4_AUDIO = 'general.mpeg-4-audio',
        /**
         * MP2.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        MP2 = 'general.mp2',
        /**
         * MPEG audio format.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        MPEG_AUDIO = 'general.mpeg-audio',
        /**
         * ULAW.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        ULAW_AUDIO = 'general.ulaw-audio',
        /**
         * Digidesign Sound Designer II (SDII).
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        SD2_AUDIO = 'com.digidesign.sd2-audio',
        /**
         * RealAudio.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        REALAUDIO = 'com.real.realaudio',
        /**
         * MKA.
         *
         * This type belongs to **AUDIO**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        MATROSKA_AUDIO = 'org.matroska.mka',
        /**
         * Generic file type.
         *
         * This type belongs to **ENTITY**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 14]
         * @atomicservice [since 11]
         * @since 10
         */
        FILE = 'general.file',
        /**
         * Generic directory type.
         *
         * This type belongs to **ENTITY**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        DIRECTORY = 'general.directory',
        /**
         * Generic folder type.
         *
         * This type belongs to **DIRECTORY**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 14]
         * @atomicservice [since 11]
         * @since 10
         */
        FOLDER = 'general.folder',
        /**
         * Generic symbolic type.
         *
         * This type belongs to **ENTITY**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        SYMLINK = 'general.symlink',
        /**
         * Generic archive file type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        ARCHIVE = 'general.archive',
        /**
         * BZ2.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        BZ2_ARCHIVE = 'general.bz2-archive',
        /**
         * OPG.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPG = 'general.opg',
        /**
         * TAR.
         *
         * This type belongs to **TAR_ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        TAZ_ARCHIVE = 'general.taz-archive',
        /**
         * MHTML format for web page archiving.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        WEB_ARCHIVE = 'general.web-archive',
        /**
         * Generic type of any file that can be mounted as a volume.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        DISK_IMAGE = 'general.disk-image',
        /**
         * ISO image (optical disk image) format.
         *
         * This type belongs to **DISK_IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        ISO = 'general.iso',
        /**
         * TAR.
         *
         * This type belongs to ARCHIVE.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        TAR_ARCHIVE = 'general.tar-archive',
        /**
         * ZIP.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        ZIP_ARCHIVE = 'general.zip-archive',
        /**
         * JAR (Java archive).
         *
         * This type belongs to **ARCHIVE** and **EXECUTABLE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        JAVA_ARCHIVE = 'com.sun.java-archive',
        /**
         * GNU.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        GNU_TAR_ARCHIVE = 'org.gnu.gnu-tar-archive',
        /**
         * GZIP archive.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        GNU_ZIP_ARCHIVE = 'org.gnu.gnu-zip-archive',
        /**
         * GZIP TAR.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        GNU_ZIP_TAR_ARCHIVE = 'org.gnu.gnu-zip-tar-archive',
        /**
         * OpenXML base type.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENXML = 'org.openxmlformats.openxml',
        /**
         * WordProcessingML format.
         *
         * This type belongs to **OPENXML** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        WORDPROCESSINGML_DOCUMENT = 'org.openxmlformats.wordprocessingml.document',
        /**
         * SpreadsheetML format.
         *
         * This type belongs to **OPENXML** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        SPREADSHEETML_SHEET = 'org.openxmlformats.spreadsheetml.sheet',
        /**
         * PresentationML format.
         *
         * This type belongs to **OPENXML** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        PRESENTATIONML_PRESENTATION = 'org.openxmlformats.presentationml.presentation',
        /**
         * DrawingML file format of Office Open XML (OOXML).
         *
         * This type belongs to **OPENXML** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        DRAWINGML_VISIO = 'org.openxmlformats.drawingml.visio',
        /**
         * DrawingML template format of OOXML.
         *
         * This type belongs to **OPENXML** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        DRAWINGML_TEMPLATE = 'org.openxmlformats.drawingml.template',
        /**
         * WordProcessingML template format of OOXML.
         *
         * This type belongs to **OPENXML** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        WORDPROCESSINGML_TEMPLATE = 'org.openxmlformats.wordprocessingml.template',
        /**
         * PresentationML template format of OOXML.
         *
         * This type belongs to **OPENXML** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        PRESENTATIONML_TEMPLATE = 'org.openxmlformats.presentationml.template',
        /**
         * PresentationML slide show format of OOXML.
         *
         * This type belongs to **OPENXML** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        PRESENTATIONML_SLIDESHOW = 'org.openxmlformats.presentationml.slideshow',
        /**
         * SpreadsheetML template format of OOXML.
         *
         * This type belongs to **OPENXML** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        SPREADSHEETML_TEMPLATE = 'org.openxmlformats.spreadsheetml.template',
        /**
         * OpenDocument format for Office applications.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENDOCUMENT = 'org.oasis.opendocument',
        /**
         * OpenDocument format for word processing (text) documents.
         *
         * This type belongs to **OPENDOCUMENT** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENDOCUMENT_TEXT = 'org.oasis.opendocument.text',
        /**
         * OpenDocument format for spreadsheets.
         *
         * This type belongs to **OPENDOCUMENT** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENDOCUMENT_SPREADSHEET = 'org.oasis.opendocument.spreadsheet',
        /**
         * OpenDocument format for presentations.
         *
         * This type belongs to **OPENDOCUMENT** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENDOCUMENT_PRESENTATION = 'org.oasis.opendocument.presentation',
        /**
         * OpenDocument format for graphics.
         *
         * This type belongs to **OPENDOCUMENT** and **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENDOCUMENT_GRAPHICS = 'org.oasis.opendocument.graphics',
        /**
         * OpenDocument format for formula.
         *
         * This type belongs to **OPENDOCUMENT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENDOCUMENT_FORMULA = 'org.oasis.opendocument.formula',
        /**
         * Stuffit compression format (stuffit archive).
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        STUFFIT_ARCHIVE = 'com.allume.stuffit-archive',
        /**
         * WinRAR.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        RAR_ARCHIVE = 'com.rarlab.rar-archive',
        /**
         * 7-Zip.
         *
         * This type belongs to **ARCHIVE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        SEVEN_ZIP_ARCHIVE = 'org.7-zip.7-zip-archive',
        /**
         * Generic calendar type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        CALENDAR = 'general.calendar',
        /**
         * VCalendar (VCS) format.
         *
         * This type belongs to **CALENDAR** and **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        VCS = 'general.vcs',
        /**
         * Internet Calendaring and Scheduling (ICS) format.
         *
         * This type belongs to **CALENDAR** and **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        ICS = 'general.ics',
        /**
         * Generic contact type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        CONTACT = 'general.contact',
        /**
         * Generic database file type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        DATABASE = 'general.database',
        /**
         * Generic message type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        MESSAGE = 'general.message',
        /**
         * Generic type of all executable files.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        EXECUTABLE = 'general.executable',
        /**
         * Microsoft Windows portable executable format.
         *
         * This type belongs to **EXECUTABLE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        PORTABLE_EXECUTABLE = 'com.microsoft.portable-executable',
        /**
         * Java class file format.
         *
         * This type belongs to **EXECUTABLE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        SUN_JAVA_CLASS = 'com.sun.java-class',
        /**
         * Generic electronic business card type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        VCARD = 'general.vcard',
        /**
         * Generic navigation data type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        NAVIGATION = 'general.navigation',
        /**
         * Location data.
         *
         * This type belongs to **NAVIGATION**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        LOCATION = 'general.location',
        /**
         * Basic type of fonts.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        FONT = 'general.font',
        /**
         * TrueType font format.
         *
         * This type belongs to **FONT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        TRUETYPE_FONT = 'general.truetype-font',
        /**
         * TrueType Collection font format.
         *
         * This type belongs to **FONT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        TRUETYPE_COLLECTION_FONT = 'general.truetype-collection-font',
        /**
         * OpenType font format.
         *
         * This type belongs to **FONT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENTYPE_FONT = 'general.opentype-font',
        /**
         * PostScript font format.
         *
         * This type belongs to **FONT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        POSTSCRIPT_FONT = 'com.adobe.postscript-font',
        /**
         * PostScript Font Binary font format.
         *
         * This type belongs to **FONT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        POSTSCRIPT_PFB_FONT = 'com.adobe.postscript-pfb-font',
        /**
         * Adobe Type 1 font format.
         *
         * This type belongs to **FONT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        POSTSCRIPT_PFA_FONT = 'com.adobe.postscript-pfa-font',
        /**
         * Widget defined for the system.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @atomicservice [since 11]
         * @since 10
         */
        OPENHARMONY_FORM = 'openharmony.form',
        /**
         * Home screen icon defined for the system.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @atomicservice [since 11]
         * @since 10
         */
        OPENHARMONY_APP_ITEM = 'openharmony.app-item',
        /**
         * Pixel map defined for the system.
         *
         * This type belongs to **IMAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 14]
         * @atomicservice [since 11]
         * @since 10
         */
        OPENHARMONY_PIXEL_MAP = 'openharmony.pixel-map',
        /**
         * Atomic service type defined for the system.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        OPENHARMONY_ATOMIC_SERVICE = 'openharmony.atomic-service',
        /**
         * Package (compressed folder) defined for the system.
         *
         * This type belongs to **DIRECTORY**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        OPENHARMONY_PACKAGE = 'openharmony.package',
        /**
         * Ability package defined for the system.
         *
         * This type belongs to **OPENHARMONY_PACKAGE**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 11
         */
        OPENHARMONY_HAP = 'openharmony.hap',
        /**
         * Memo format defined for the system.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENHARMONY_HDOC = 'openharmony.hdoc',
        /**
         * Note format defined for the system.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENHARMONY_HINOTE = 'openharmony.hinote',
        /**
         * Style string type defined for the system.
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENHARMONY_STYLED_STRING = 'openharmony.styled-string',
        /**
         * Want defined for the system.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OPENHARMONY_WANT = 'openharmony.want',
        /**
         * Open Fixed-layout Document (OFD).
         *
         * This type belongs to **COMPOSITE_OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OFD = 'general.ofd',
        /**
         * Generic type of all computer-aided design types.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        CAD = 'general.cad',
        /**
         * Any binary data type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        OCTET_STREAM = 'general.octet-stream',
        /**
         * File address type.
         *
         * This type belongs to **TEXT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        FILE_URI = 'general.file-uri',
        /**
         * Content widget type.
         *
         * This type belongs to **OBJECT**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        CONTENT_FORM = 'general.content-form'
    }
    /**
     * Represents a class for defining a uniform data type. It provides properties and methods for describing a uniform
     * data type and its relationship with other uniform data types.
     *
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @crossplatform [since 20]
     * @since 11
     */
    class TypeDescriptor {
        /**
         * Type ID of the uniform data type, which corresponds to the enum string in the {@code UniformDataType}.
         *
         * @type { string } [since 11 - 22]
         * @returns { string } Type ID of the uniform data type. [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        get typeId(): string;
        /**
         * Type ID of the uniform data type, which corresponds to the enum string in the {@code UniformDataType}.
         *
         * @type { string } [since 11 - 22]
         * @param { string } value - Type ID of the uniform data type. [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        set typeId(value: string);
        /**
         * Uniform data type IDs that the uniform data type belongs to.
         *
         * @type { Array<string> } [since 11 - 22]
         * @returns { Array<string> } Uniform data type IDs [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        get belongingToTypes(): Array<string>;
        /**
         * Uniform data type IDs that the uniform data type belongs to.
         *
         * @type { Array<string> } [since 11 - 22]
         * @param { Array<string> } value - Uniform data type IDs [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        set belongingToTypes(value: Array<string>);
        /**
         * A textual description for the uniform data type.
         *
         * @type { string } [since 11 - 22]
         * @returns { string } A textual description [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        get description(): string;
        /**
         * A textual description for the uniform data type.
         *
         * @type { string } [since 11 - 22]
         * @param { string } value - A textual description [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        set description(value: string);
        /**
         * Reference URL for the uniform data type, which describes the detail information of the type.
         *
         * @type { string } [since 11 - 22]
         * @returns { string } Reference URL [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        get referenceURL(): string;
        /**
         * Reference URL for the uniform data type, which describes the detail information of the type.
         *
         * @type { string } [since 11 - 22]
         * @param { string } value - Reference URL [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        set referenceURL(value: string);
        /**
         * Default icon file path for the uniform data type.
         *
         * @type { string } Default icon file path [since 11 - 22]
         * @returns { string } Default icon file path [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        get iconFile(): string;
        /**
         * Default icon file path for the uniform data type.
         *
         * @type { string } [since 11 - 22]
         * @param { string } value - Default icon file path [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        set iconFile(value: string);
        /**
         * File name extensions for the uniform data type.
         *
         * @type { Array<string> } [since 12 - 22]
         * @returns { Array<string> } File name extensions [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 12
         */
        get filenameExtensions(): Array<string>;
        /**
         * File name extensions for the uniform data type.
         *
         * @type { Array<string> } [since 12 - 22]
         * @param { Array<string> } value - File name extensions [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 12
         */
        set filenameExtensions(value: Array<string>);
        /**
         * MIMETypes of the uniform data type.
         *
         * @type { Array<string> } [since 12 - 22]
         * @returns { Array<string> } MIMETypes [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 12
         */
        get mimeTypes(): Array<string>;
        /**
         * MIMETypes of the uniform data type.
         *
         * @type { Array<string> } [since 12 - 22]
         * @param { Array<string> } value - MIMETypes [since 23]
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 12
         */
        set mimeTypes(value: Array<string>);
        /**
         * Checks whether this data type belongs to the specified uniform data type.
         *
         * @param { string } type - Uniform data type specified, which is a value of
         *     [UniformDataType]{@link uniformTypeDescriptor.UniformDataType}.
         * @returns { boolean } Returns **true** if the data type belongs to or is the same as the specified uniform data
         *     type; returns **false** if they are not related.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        belongsTo(type: string): boolean;
        /**
         * Checks whether this data type is a lower-level type of the specified uniform data type. For example,
         * **TYPE_SCRIPT** is a lower-level type of **SOURCE_CODE**, and **TYPE_SCRIPT** and **SOURCE_CODE** are lower-level
         * types of **TEXT**.
         *
         * @param { string } type - Uniform data type specified, which is a value of
         *     [UniformDataType]{@link uniformTypeDescriptor.UniformDataType}.
         * @returns { boolean } Returns **true** if the data type is a lower-level type of the specified uniform data type;
         *     returns **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        isLowerLevelType(type: string): boolean;
        /**
         * Checks whether this data type is a higher-level type of the specified uniform data type. For example,
         * **SOURCE_CODE** is a higher-level type of **TYPE_SCRIPT**, and **TEXT** is a higher-level type of **SOURCE_CODE**
         * and **TYPE_SCRIPT**.
         *
         * @param { string } type - Uniform data type specified, which is a value of
         *     [UniformDataType]{@link uniformTypeDescriptor.UniformDataType}.
         * @returns { boolean } Returns **true** if the data type is a higher-level type of the specified uniform data type;
         *     returns **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        isHigherLevelType(type: string): boolean;
        /**
         * Checks whether this data type is the same as the specified uniform data type. That is, compares **typeId**s of
         * two [TypeDescriptor]{@link uniformTypeDescriptor.TypeDescriptor} objects.
         *
         * @param { TypeDescriptor } typeDescriptor - Uniform data type to compare.
         * @returns { boolean } Returns **true** if the type IDs are the same; returns **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @crossplatform [since 20]
         * @since 11
         */
        equals(typeDescriptor: TypeDescriptor): boolean;
    }
    /**
     * Obtains the **TypeDescriptor** object based on the uniform data type ID.
     *
     * @param { string } typeId - [Uniform data type ID].
     * @returns { TypeDescriptor } **TypeDescriptor** object obtained. If the uniform data type does not exist, **null**
     *     is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
     *     <br>2.Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @crossplatform [since 20]
     * @since 11
     */
    function getTypeDescriptor(typeId: string): TypeDescriptor;
    /**
     * Obtains the uniform data type ID based on the given file name extension and data type. If there are multiple
     * uniform data type IDs matching the conditions, the first one is returned.
     *
     * @param { string } filenameExtension - File name extension.
     * @param { string } [belongsTo] - ID of the uniform data type, to which the data type to be obtained belongs. This
     *     parameter has no default value. If it is not specified, the
     *     [uniform data type ID] is queried based on the file name
     *     extension.
     * @returns { string } ID of the uniform data type that matches the specified file name extension and **belongsTo** (
     *     if specified). If no match is found, the data type dynamically generated based on the rules specified by the
     *     input parameters is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
     *     <br>2.Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @crossplatform [since 20]
     * @since 11
     */
    function getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string;
    /**
     * Obtains the uniform data type ID based on the given MIME type and data type. If there are multiple uniform data
     * type IDs matching the conditions, the first one is returned.
     *
     * @param { string } mimeType - MIME type.
     * @param { string } [belongsTo] - ID of the uniform data type, to which the data type to be obtained belongs. This
     *     parameter has no default value. If it is not specified, the
     *     [uniform data type ID] is queried based on the MIME name.
     * @returns { string } ID of the uniform data type that matches the specified MIME type and **belongsTo** (if
     *     specified). If no match is found, the data type dynamically generated based on the rules specified by the input
     *     parameters is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
     *     <br>2.Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @crossplatform [since 20]
     * @since 11
     */
    function getUniformDataTypeByMIMEType(mimeType: string, belongsTo?: string): string;
    /**
     * Obtains the uniform data type IDs based on the given file name extension and data type.
     *
     * @param { string } filenameExtension - File name extension.
     * @param { string } [belongsTo] - ID of the uniform data type, to which the data type to be obtained belongs. This
     *     parameter has no default value. If it is not specified, the
     *     [uniform data type ID] is queried based on the file name
     *     extension.
     * @returns { Array<string> } Uniform data type IDs that match the specified file name extension and **belongsTo** (if
     *     specified). If no match is found, the data types dynamically generated based on the rules specified by the
     *     input parameters are returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
     *     <br>2.Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @crossplatform [since 20]
     * @since 13
     */
    function getUniformDataTypesByFilenameExtension(filenameExtension: string, belongsTo?: string): Array<string>;
    /**
     * Obtains the uniform data type IDs based on the given MIME type and data type.
     *
     * @param { string } mimeType - MIME type.
     * @param { string } [belongsTo] - ID of the uniform data type, to which the data type to be obtained belongs. This
     *     parameter has no default value. If it is not specified, the
     *     [uniform data type ID] is queried based on the MIME name.
     * @returns { Array<string> } Uniform data type IDs that match the specified MIME type and **belongsTo** (if specified
     *     ). If no match is found, the data types dynamically generated based on the rules specified by the input
     *     parameters are returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
     *     <br>2.Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @crossplatform [since 20]
     * @since 13
     */
    function getUniformDataTypesByMIMEType(mimeType: string, belongsTo?: string): Array<string>;
}
export default uniformTypeDescriptor;

```
