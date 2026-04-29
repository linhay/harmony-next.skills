# udmf_meta.h

**概述**

声明统一类型数据信息。

引用文件： <database/udmf/udmf_meta.h>

库： libudmf.so

系统能力： SystemCapability.DistributedDataManager.UDMF.Core

起始版本： 12

相关模块： [UDMF](UDMF.md)

**汇总**

**宏定义**

| 名称 | 描述 |
| --- | --- |
| UDMF_META_ENTITY "general.entity" | 所有表示物理存储类型的基类型，用于描述类型的物理属性，无归属类型。 起始版本： 12 |
| UDMF_META_OBJECT "general.object" | 所有表示逻辑内容类型的基类型，用于描述类型的功能性特征，无归属类型。 起始版本： 12 |
| UDMF_META_COMPOSITE_OBJECT "general.composite-object" | 所有组合内容类型（例如PDF文件类型混合了文本和图片类数据）的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_TEXT "general.text" | 所有文本的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_PLAIN_TEXT "general.plain-text" | 未指定编码的文本类型，没有标识符，归属类型为TEXT。  起始版本： 12 |
| UDMF_META_HTML "general.html" | HTML文本类型，归属类型为TEXT。 起始版本： 12 |
| UDMF_META_HYPERLINK "general.hyperlink" | 超链接类型，归属类型为TEXT。 起始版本： 12 |
| UDMF_META_XML "general.xml" | XML文本类型，归属类型为TEXT。 起始版本： 12 |
| UDMF_META_SOURCE_CODE "general.source-code" | 所有源代码的基类型，归属类型为PLAIN_TEXT。 起始版本： 12 |
| UDMF_META_SCRIPT "general.script" | 所有脚本语言源代码的基类型，归属类型为SOURCE_CODE。 起始版本： 12 |
| UDMF_META_SHELL_SCRIPT "general.shell-script" | Shell脚本类型，归属类型为SCRIPT。 起始版本： 12 |
| UDMF_META_CSH_SCRIPT "general.csh-script" | C-shell脚本类型，归属类型为SHELL_SCRIPT。 起始版本： 12 |
| UDMF_META_PERL_SCRIPT "general.perl-script" | Perl脚本类型，归属类型为SHELL_SCRIPT。 起始版本： 12 |
| UDMF_META_PHP_SCRIPT "general.php-script" | PHP脚本类型，归属类型为SHELL_SCRIPT。 起始版本： 12 |
| UDMF_META_PYTHON_SCRIPT "general.python-script" | Python脚本类型，归属类型为SHELL_SCRIPT。 起始版本： 12 |
| UDMF_META_RUBY_SCRIPT "general.ruby-script" | Ruby脚本类型，归属类型为SHELL_SCRIPT。 起始版本： 12 |
| UDMF_META_TYPE_SCRIPT "general.type-script" | TypeScript源代码类型，归属类型为SCRIPT。 起始版本： 12 |
| UDMF_META_JAVA_SCRIPT "general.java-script" | JavaScript源代码类型，归属类型为SCRIPT。  起始版本： 12 |
| UDMF_META_C_HEADER "general.c-header" | C头文件类型，归属类型为SOURCE_CODE。 起始版本： 12 |
| UDMF_META_C_SOURCE "general.c-source" | C源代码类型，归属类型为SOURCE_CODE。 起始版本： 12 |
| UDMF_META_C_PLUS_PLUS_HEADER "general.c-plus-plus-header" | C++头文件类型，归属类型为SOURCE_CODE。 起始版本： 12 |
| UDMF_META_C_PLUS_PLUS_SOURCE "general.c-plus-plus-source" | C++源代码类型，归属类型为SOURCE_CODE。 起始版本： 12 |
| UDMF_META_JAVA_SOURCE "general.java-source" | Java源代码类型，归属类型为SOURCE_CODE。 起始版本： 12 |
| UDMF_META_EBOOK "general.ebook" | 所有电子书文件格式的基类型，归属类型为COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_EPUB "general.epub" | 电子出版物（EPUB）文件格式类型，归属类型为EBOOK。 起始版本： 12 |
| UDMF_META_AZW "com.amazon.azw" | AZW电子书文件格式类型，归属类型为EBOOK。 起始版本： 12 |
| UDMF_META_AZW3 "com.amazon.azw3" | AZW3电子书文件格式类型，归属类型为EBOOK。 起始版本： 12 |
| UDMF_META_KFX "com.amazon.kfx" | KFX电子书文件格式类型，归属类型为EBOOK。 起始版本： 12 |
| UDMF_META_MOBI "com.amazon.mobi" | MOBI电子书文件格式类型，归属类型为EBOOK。 起始版本： 12 |
| UDMF_META_MEDIA "general.media" | 所有媒体的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_IMAGE "general.image" | 所有图片的基类型，归属类型为MEDIA。 起始版本： 12 |
| UDMF_META_JPEG "general.jpeg" | JPEG图片类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_PNG "general.png" | PNG图片类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_RAW_IMAGE "general.raw-image" | 所有原始图像格式的基类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_TIFF "general.tiff" | TIFF图片类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_BMP "com.microsoft.bmp" | WINDOWS位图图像类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_ICO "com.microsoft.ico" | WINDOWS图标图像类型，归属类型为IMAGE。  起始版本： 12 |
| UDMF_META_PHOTOSHOP_IMAGE "com.adobe.photoshop-image" | Adobe Photoshop图片类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_AI_IMAGE "com.adobe.illustrator.ai-image" | Adobe Illustrator图片类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_WORD_DOC "com.microsoft.word.doc" | Microsoft Word数据类型，归属类型为COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_EXCEL "com.microsoft.excel.xls" | Microsoft Excel数据类型，归属类型为COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_PPT "com.microsoft.powerpoint.ppt" | Microsoft PowerPoint演示文稿类型，归属类型为COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_PDF "com.adobe.pdf" | PDF数据类型，归属类型为COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_POSTSCRIPT "com.adobe.postscript" | PostScript数据类型，归属类型为COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_ENCAPSULATED_POSTSCRIPT "com.adobe.encapsulated-postscript" | Encapsulated PostScript类型，归属类型为POSTSCRIPT。 起始版本： 12 |
| UDMF_META_VIDEO "general.video" | 所有视频的基类型，归属类型为MEDIA。 起始版本： 12 |
| UDMF_META_AVI "general.avi" | AVI视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_MPEG "general.mpeg" | MPEG-1或MPEG-2视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_MPEG4 "general.mpeg-4" | MPEG-4视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_VIDEO_3GPP "general.3gpp" | 3GPP视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_VIDEO_3GPP2 "general.3gpp2" | 3GPP2视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_WINDOWS_MEDIA_WM "com.microsoft.windows-media-wm" | WINDOWS WM视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_WINDOWS_MEDIA_WMV "com.microsoft.windows-media-wmv" | WINDOWS WMV视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_WINDOWS_MEDIA_WMP "com.microsoft.windows-media-wmp" | WINDOWS WMP视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_AUDIO "general.audio" | 所有音频的基类型，归属类型为MEDIA。 起始版本： 12 |
| UDMF_META_AAC "general.aac" | AAC音频类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_AIFF "general.aiff" | AIFF音频类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_ALAC "general.alac" | ALAC音频类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_FLAC "general.flac" | FLAC音频类型，归属类型为AUDIO。  起始版本： 12 |
| UDMF_META_MP3 "general.mp3" | MP3音频类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_OGG "general.ogg" | OGG音频类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_PCM "general.pcm" | PCM音频类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_WINDOWS_MEDIA_WMA "com.microsoft.windows-media-wma" | WINDOWS WMA音频类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_WAVEFORM_AUDIO "com.microsoft.waveform-audio" | WINDOWS波形音频类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_WINDOWS_MEDIA_WMX "com.microsoft.windows-media-wmx" | WINDOWS WMX视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_WINDOWS_MEDIA_WVX "com.microsoft.windows-media-wvx" | WINDOWS WVX视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_WINDOWS_MEDIA_WAX "com.microsoft.windows-media-wax" | WINDOWS WAX音频类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_GENERAL_FILE "general.file" | 所有文件的基类型，归属类型为ENTITY。 起始版本： 12 |
| UDMF_META_DIRECTORY "general.directory" | 所有目录的基类型，归属类型为ENTITY。 起始版本： 12 |
| UDMF_META_FOLDER "general.folder" | 所有文件夹的基类型，归属类型为DIRECTORY。 起始版本： 12 |
| UDMF_META_SYMLINK "general.symlink" | 所有符号链接的基类型，归属类型为ENTITY。 起始版本： 12 |
| UDMF_META_ARCHIVE "general.archive" | 所有文件和目录存档文件的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_BZ2_ARCHIVE "general.bz2-archive" | BZ2存档文件类型，归属类型为ARCHIVE。 起始版本： 12 |
| UDMF_META_DISK_IMAGE "general.disk-image" | 所有可作为卷装载项的文件类型的基类型，归属类型为ARCHIVE。 起始版本： 12 |
| UDMF_META_TAR_ARCHIVE "general.tar-archive" | TAR存档文件类型，归属类型为ARCHIVE。 起始版本： 12 |
| UDMF_META_ZIP_ARCHIVE "general.zip-archive" | ZIP存档文件类型，归属类型为ARCHIVE。 起始版本： 12 |
| UDMF_META_JAVA_ARCHIVE "com.sun.java-archive" | JAVA存档文件类型，归属类型为ARCHIVE和EXECUTABLE。 起始版本： 12 |
| UDMF_META_GNU_TAR_ARCHIVE "org.gnu.gnu-tar-archive" | GUN存档文件类型，归属类型为ARCHIVE。 起始版本： 12 |
| UDMF_META_GNU_ZIP_ARCHIVE "org.gnu.gnu-zip-archive" | GZIP存档文件类型，归属类型为ARCHIVE。 起始版本： 12 |
| UDMF_META_GNU_ZIP_TAR_ARCHIVE "org.gnu.gnu-zip-tar-archive" | GZIP TAR存档文件类型，归属类型为ARCHIVE。 起始版本： 12 |
| UDMF_META_CALENDAR "general.calendar" | 所有日程类数据的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_CONTACT "general.contact" | 所有联系人类数据的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_DATABASE "general.database" | 所有数据库文件的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_MESSAGE "general.message" | 所有消息类数据的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_VCARD "general.vcard" | 所有电子名片类数据的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_NAVIGATION "general.navigation" | 所有导航类数据的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_LOCATION "general.location" | 导航定位类型，归属类型为NAVIGATION。 起始版本： 12 |
| UDMF_META_OPENHARMONY_FORM "openharmony.form" | 系统定义的卡片类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_OPENHARMONY_APP_ITEM "openharmony.app-item" | 系统定义的桌面图标类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_OPENHARMONY_PIXEL_MAP "openharmony.pixel-map" | 系统定义的像素图类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_OPENHARMONY_ATOMIC_SERVICE "openharmony.atomic-service" | 系统定义的元服务类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_OPENHARMONY_PACKAGE "openharmony.package" | 系统定义的包（即目录的打包文件），归属类型为DIRECTORY。 起始版本： 12 |
| UDMF_META_OPENHARMONY_HAP "openharmony.hap" | 系统定义的能力包，归属类型为OPENHARMONY_PACKAGE。 起始版本： 12 |
| UDMF_META_SMIL "com.real.smil" | 同步多媒体集成语言类型，归属类型为XML文本类型。 起始版本： 12 |
| UDMF_META_MARKDOWN "general.markdown" | 标记语言文本类型，归属类型为PLAIN_TEXT。 起始版本： 12 |
| UDMF_META_FAX "general.fax" | 传真图像的基本类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_JFX_FAX "com.j2.jfx-fax" | J2 jConnect传真文件类型，归属类型为FAX。 起始版本： 12 |
| UDMF_META_EFX_FAX "com.js.efx-fax" | 电子传真文件类型，归属类型为FAX。 起始版本： 12 |
| UDMF_META_XBITMAP_IMAGE "general.xbitmap-image" | X Window系统（X11）中使用的位图图像格式，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_TGA_IMAGE "com.truevision.tga-image" | 标签图形（TaggedGraphics）图像类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_SGI_IMAGE "com.sgi.sgi-image" | 硅图（Silicon Graphics）图像类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_OPENEXR_IMAGE "com.ilm.openexr-image" | 开放标准的高动态范围图像格式类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_FLASHPIX_IMAGE "com.kodak.flashpix.image" | FlashPix图像文件类型，归属类型为IMAGE。 起始版本： 12 |
| UDMF_META_REALMEDIA "com.real.realmedia" | 流媒体视频类型，归属类型为VIDEO。 起始版本： 12 |
| UDMF_META_AU_AUDIO "general.au-audio" | Au数据格式，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_AIFC_AUDIO "general.aifc-audio" | 音频交换数据类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_SD2_AUDIO "com.digidesign.sd2-audio" | 单声道/立体声音频类型（Digidesign Sound Designer II），归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_REALAUDIO "com.real.realaudio" | RealMedia音频类型，归属类型为AUDIO。 起始版本： 12 |
| UDMF_META_OPENXML "org.openxmlformats.openxml" | 开源XML基类型，归属类型为ARCHIVE。 起始版本： 12 |
| UDMF_META_WORDPROCESSINGML_DOCUMENT "org.openxmlformats.wordprocessingml.document" | 开源XML文档类型，归属类型为OPENXML和COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_SPREADSHEETML_SHEET "org.openxmlformats.spreadsheetml.sheet" | 开源XML电子表格类型，归属类型为OPENXML和COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_PRESENTATIONML_PRESENTATION "org.openxmlformats.presentationml.presentation" | 开源XML演示文稿类型，归属类型为OPENXML和COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_OPENDOCUMENT "org.oasis.opendocument" | Office应用程序的开源文档类型，归属类型为ARCHIVE。 起始版本： 12 |
| UDMF_META_OPENDOCUMENT_TEXT "org.oasis.opendocument.text" | 开源文档类型，归属类型为OPENDOCUMENT和COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_OPENDOCUMENT_SPREADSHEET "org.oasis.opendocument.spreadsheet" | 开源文档电子表格类型，归属类型为OPENDOCUMENT和COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_OPENDOCUMENT_PRESENTATION "org.oasis.opendocument.presentation" | 开源文档演示类型，归属类型为OPENDOCUMENT和COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_OPENDOCUMENT_GRAPHICS "org.oasis.opendocument.graphics" | 开源文档图形类型，归属类型为OPENDOCUMENT和COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_OPENDOCUMENT_FORMULA "org.oasis.opendocument.formula" | 开源文档公式集类型，归属类型为OPENDOCUMENT。 起始版本： 12 |
| UDMF_META_STUFFIT_ARCHIVE "com.allume.stuffit-archive" | Stuffit压缩格式类型（Stuffit archive），归属类型为ARCHIVE。 起始版本： 12 |
| UDMF_META_VCS "general.vcs" | VCalendar日历数据类型，归属类型为CALENDAR和TEXT。 起始版本： 12 |
| UDMF_META_ICS "general.ics" | ICalendar日历数据类型，归属类型为CALENDAR和TEXT。 起始版本： 12 |
| UDMF_META_EXECUTABLE "general.executable" | 所有可执行文件的基类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_PORTABLE_EXECUTABLE "com.microsoft.portable-executable" | Microsoft Windows应用程序类型，归属类型为EXECUTABLE。 起始版本： 12 |
| UDMF_META_SUN_JAVA_CLASS "com.sun.java-class" | Java类文件类型，归属类型为EXECUTABLE。 起始版本： 12 |
| UDMF_META_FONT "general.font" | 所有字体数据类型的基础类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_TRUETYPE_FONT "general.truetype-font" | TrueType字体类型，归属类型为FONT。 起始版本： 12 |
| UDMF_META_TRUETYPE_COLLECTION_FONT "general.truetype-collection-font" | TrueType collection字体类型，归属类型为FONT。 起始版本： 12 |
| UDMF_META_OPENTYPE_FONT "general.opentype-font" | OpenType字体类型，归属类型为FONT。 起始版本： 12 |
| UDMF_META_POSTSCRIPT_FONT "com.adobe.postscript-font" | PostScript字体类型，归属类型为FONT。 起始版本： 12 |
| UDMF_META_POSTSCRIPT_PFB_FONT "com.adobe.postscript-pfb-font" | PostScript Font Binary字体类型，归属类型为FONT。 起始版本： 12 |
| UDMF_META_POSTSCRIPT_PFA_FONT "com.adobe.postscript-pfa-font" | Adobe Type 1 字体类型，归属类型为FONT。 起始版本： 12 |
| UDMF_META_OPENHARMONY_HDOC "openharmony.hdoc" | 系统定义的备忘录数据类型，归属类型为COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_OPENHARMONY_HINOTE "openharmony.hinote" | 系统定义的笔记数据类型，归属类型为COMPOSITE_OBJECT。 |
| UDMF_META_OPENHARMONY_STYLED_STRING "openharmony.styled-string" | 系统定义的样式字符串类型，归属类型为COMPOSITE_OBJECT。 起始版本： 12 |
| UDMF_META_OPENHARMONY_WANT "openharmony.want" | 系统定义的Want类型，归属类型为OBJECT。 起始版本： 12 |
| UDMF_META_GENERAL_FILE_URI "general.file-uri" | 文件地址类型，归属类型为TEXT。 起始版本： 13 |
| UDMF_METE_GENERAL_CONTENT_FORM "general.content-form" | 内容卡片类型，归属类型为OBJECT。 起始版本： 14 |