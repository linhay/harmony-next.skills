# @ohos.data.uniformTypeDescriptor (标准化数据定义与描述)

本模块对标准化数据类型进行了抽象定义与描述。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { uniformTypeDescriptor } from '@kit.ArkData';
```

#### UniformDataType

标准化数据类型之间存在归属关系，例如JPEG图片类型归属于IMAGE类型。更多预置数据类型参考[UTD预置列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-list)。

下表以枚举形式，列举了常用的标准化数据类型定义。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

名称值说明ENTITY11+'general.entity'所有表示物理存储类型的基类型，无归属类型。OBJECT11+'general.object'所有表示逻辑内容类型的基类型，无归属类型。COMPOSITE_OBJECT11+'general.composite-object'所有组合内容类型（例如PDF文件类型混合了文本和图片类数据）的基类型，归属类型为OBJECT。TEXT'general.text'

所有文本的基类型，归属类型为OBJECT。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

PLAIN_TEXT'general.plain-text'

未指定编码的文本类型，没有标识符，归属类型为TEXT。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

HTML'general.html'

HTML文本类型，归属类型为TEXT。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

HYPERLINK'general.hyperlink'

超链接类型，归属类型为TEXT。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

XML11+'general.xml'XML文本类型，归属类型为TEXT。XHTML12+'general.xhtml'XHTML文本类型，归属类型为XML。RSS12+'general.rss'RSS文本类型，归属类型为XML。SMIL12+'com.real.smil'同步多媒体集成语言类型，归属类型为XML文本类型。SOURCE_CODE11+'general.source-code'所有源代码的基类型，归属类型为TEXT。SCRIPT11+'general.script'所有脚本语言源代码的基类型，归属类型为SOURCE_CODE。SHELL_SCRIPT11+'general.shell-script'shell脚本类型，归属类型为SCRIPT。CSH_SCRIPT11+'general.csh-script'C-shell脚本类型，归属类型为SHELL_SCRIPT。PERL_SCRIPT11+'general.perl-script'Perl脚本类型，归属类型为SHELL_SCRIPT。PHP_SCRIPT11+'general.php-script'PHP脚本类型，归属类型为SHELL_SCRIPT。PYTHON_SCRIPT11+'general.python-script'Python脚本类型，归属类型为SHELL_SCRIPT。RUBY_SCRIPT11+'general.ruby-script'Ruby脚本类型，归属类型为SHELL_SCRIPT。TYPE_SCRIPT11+'general.type-script'TypeScript源代码类型，归属类型为SOURCE_CODE。JAVA_SCRIPT11+'general.java-script'JavaScript源代码类型，归属类型为SOURCE_CODE。CSS12+'general.css'CSS样式表类型，归属类型为SCRIPT。C_HEADER11+'general.c-header'C头文件类型，归属类型为SOURCE_CODE。C_SOURCE11+'general.c-source'C源代码类型，归属类型为SOURCE_CODE。C_PLUS_PLUS_HEADER11+'general.c-plus-plus-header'C++头文件类型，归属类型为SOURCE_CODE。C_PLUS_PLUS_SOURCE11+'general.c-plus-plus-source'C++源代码类型，归属类型为SOURCE_CODE。JAVA_SOURCE11+'general.java-source'Java源代码类型，归属类型为SOURCE_CODE。TEX12+'general.tex'TEX源代码类型，归属类型为SOURCE_CODE。MARKDOWN12+'general.markdown'标记语言文本类型，归属类型为TEXT。ASC_TEXT12+'general.asc-text'ASCII文本类型，归属类型为TEXT。RICH_TEXT12+'general.rich-text'富文本类型，归属类型为TEXT。DELIMITED_VALUES_TEXT12+'general.delimited-values-text'所有分隔值文本的基类型，归属类型为TEXT。COMMA_SEPARATED_VALUES_TEXT12+'general.comma-separated-values-text'CSV文本类型，归属类型为DELIMITED_VALUES_TEXT。TAB_SEPARATED_VALUES_TEXT12+'general.tab-separated-values-text'TSV文本类型，归属类型为DELIMITED_VALUES_TEXT。EBOOK11+'general.ebook'所有电子书文件格式的基类型，归属类型为COMPOSITE_OBJECT。EPUB11+'general.epub'电子出版物（EPUB）文件格式类型，归属类型为EBOOK。AZW11+'com.amazon.azw'AZW电子书文件格式类型，归属类型为EBOOK。AZW311+'com.amazon.azw3'AZW3电子书文件格式类型，归属类型为EBOOK。KFX11+'com.amazon.kfx'KFX电子书文件格式类型，归属类型为EBOOK。MOBI11+'com.amazon.mobi'MOBI电子书文件格式类型，归属类型为EBOOK。MEDIA11+'general.media'所有媒体的基类型，归属类型为OBJECT。IMAGE'general.image'

所有图片的基类型，归属类型为MEDIA。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

JPEG11+'general.jpeg'JPEG图片类型，归属类型为IMAGE。PNG11+'general.png'PNG图片类型，归属类型为IMAGE。RAW_IMAGE11+'general.raw-image'所有原始图像格式的基类型，归属类型为IMAGE。TIFF11+'general.tiff'TIFF图片类型，归属类型为IMAGE。BMP11+'com.microsoft.bmp'WINDOWS位图图像类型，归属类型为IMAGE。ICO11+'com.microsoft.ico'WINDOWS图标图像类型，归属类型为IMAGE。PHOTOSHOP_IMAGE11+'com.adobe.photoshop-image'Adobe Photoshop图片类型，归属类型为IMAGE。AI_IMAGE11+'com.adobe.illustrator.ai-image'Adobe Illustrator图片类型，归属类型为IMAGE。FAX12+'general.fax'传真图像的基本类型，归属类型为IMAGE。JFX_FAX12+'com.j2.jfx-fax'J2 jConnect传真文件类型，归属类型为FAX。EFX_FAX12+'com.js.efx-fax'电子传真文件类型，归属类型为FAX。XBITMAP_IMAGE12+'general.xbitmap-image'X Window系统（X11）中使用的位图图像格式，归属类型为IMAGE。GIF12+'general.gif'GIF图像类型，归属类型为IMAGE。TGA_IMAGE12+'com.truevision.tga-image'标签图形（TaggedGraphics）图像类型，归属类型为IMAGE。SGI_IMAGE12+'com.sgi.sgi-image'硅图（Silicon Graphics）图像类型，归属类型为IMAGE。OPENEXR_IMAGE12+'com.ilm.openexr-image'开放标准的高动态范围图像格式类型，归属类型为IMAGE。FLASHPIX_IMAGE12+'com.kodak.flashpix.image'FlashPix 图像文件类型，归属类型为IMAGE。WORD_DOC11+'com.microsoft.word.doc'Microsoft Word数据类型，归属类型为COMPOSITE_OBJECT。EXCEL11+'com.microsoft.excel.xls'Microsoft Excel数据类型，归属类型为COMPOSITE_OBJECT。PPT11+'com.microsoft.powerpoint.ppt'Microsoft PowerPoint演示文稿类型，归属类型为COMPOSITE_OBJECT。WORD_DOT12+'com.microsoft.word.dot'Microsoft Word模板类型，归属类型为COMPOSITE_OBJECT。POWERPOINT_PPS12+'com.microsoft.powerpoint.pps'Microsoft PowerPoint演示文稿幻灯片放映类型，归属类型为COMPOSITE_OBJECT。POWERPOINT_POT12+'com.microsoft.powerpoint.pot'Microsoft PowerPoint演示文稿模板类型，归属类型为COMPOSITE_OBJECT。EXCEL_XLT12+'com.microsoft.excel.xlt'Microsoft Excel模板类型，归属类型为COMPOSITE_OBJECT。VISIO_VSD12+'com.microsoft.visio.vsd'Microsoft Visio数据类型，归属类型为COMPOSITE_OBJECT。PDF11+'com.adobe.pdf'PDF数据类型，归属类型为COMPOSITE_OBJECT。POSTSCRIPT11+'com.adobe.postscript'PostScript数据类型，归属类型为COMPOSITE_OBJECT。ENCAPSULATED_POSTSCRIPT11+'com.adobe.encapsulated-postscript'Encapsulated PostScript类型，归属类型为POSTSCRIPT。VIDEO'general.video'

所有视频的基类型，归属类型为MEDIA。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

AVI11+'general.avi'AVI视频类型，归属类型为VIDEO。MPEG11+'general.mpeg'MPEG-1或MPEG-2视频类型，归属类型为VIDEO。MPEG411+'general.mpeg-4'MPEG-4视频类型，归属类型为VIDEO。VIDEO_3GPP11+'general.3gpp'3GPP视频类型，归属类型为VIDEO。VIDEO_3GPP211+'general.3gpp2'3GPP2视频类型，归属类型为VIDEO。TS12+'general.ts'MPEG-TS类型，归属类型为VIDEO。MPEGURL_VIDEO12+'general.mpegurl-video'MPEG视频播放列表文件类型，归属类型为VIDEO。WINDOWS_MEDIA_WM11+'com.microsoft.windows-media-wm'WINDOWS WM视频类型，归属类型为VIDEO。WINDOWS_MEDIA_WMV11+'com.microsoft.windows-media-wmv'WINDOWS WMV视频类型，归属类型为VIDEO。WINDOWS_MEDIA_WMP11+'com.microsoft.windows-media-wmp'WINDOWS WMP视频类型，归属类型为VIDEO。WINDOWS_MEDIA_WVX11+'com.microsoft.windows-media-wvx'WINDOWS WVX视频类型，归属类型为VIDEO。WINDOWS_MEDIA_WMX11+'com.microsoft.windows-media-wmx'WINDOWS WMX视频类型，归属类型为VIDEO。REALMEDIA12+'com.real.realmedia'流媒体视频类型，归属类型为VIDEO。MATROSKA_VIDEO12+'org.matroska.mkv'MKV视频类型，归属类型为VIDEO。FLASH12+'com.adobe.flash'FLASH视频类型，归属类型为VIDEO。AUDIO'general.audio'

所有音频的基类型，归属类型为MEDIA。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

AAC11+'general.aac'AAC音频类型，归属类型为AUDIO。AIFF11+'general.aiff'AIFF音频类型，归属类型为AUDIO。ALAC11+'general.alac'ALAC音频类型，归属类型为AUDIO。FLAC11+'general.flac'FLAC音频类型，归属类型为AUDIO。MP311+'general.mp3'MP3音频类型，归属类型为AUDIO。OGG11+'general.ogg'OGG音频类型，归属类型为AUDIO。PCM11+'general.pcm'PCM音频类型，归属类型为AUDIO。WINDOWS_MEDIA_WMA11+'com.microsoft.windows-media-wma'WINDOWS WMA音频类型，归属类型为AUDIO。WAVEFORM_AUDIO11+'com.microsoft.waveform-audio'WINDOWS波形音频类型，归属类型为AUDIO。WINDOWS_MEDIA_WAX11+'com.microsoft.windows-media-wax'WINDOWS WAX音频类型，归属类型为AUDIO。AU_AUDIO12+'general.au-audio'Au数据格式，归属类型为AUDIO。AIFC_AUDIO12+'general.aifc-audio'音频交换数据类型，归属类型为AUDIO。MPEGURL_AUDIO12+'general.mpegurl-audio'MPEG音频播放列表文件类型，归属类型为AUDIO。MPEG_4_AUDIO12+'general.mpeg-4-audio'MPEG-4音频类型，归属类型为AUDIO。MP212+'general.mp2'MP2音频类型，归属类型为AUDIO。MPEG_AUDIO12+'general.mpeg-audio'MPEG音频类型，归属类型为AUDIO。ULAW_AUDIO12+'general.ulaw-audio'ULAW音频类型，归属类型为AUDIO。SD2_AUDIO12+'com.digidesign.sd2-audio'单声道/立体声音频类型（Digidesign Sound Designer II），归属类型为AUDIO。REALAUDIO12+'com.real.realaudio'RealMedia音频类型，归属类型为AUDIO。MATROSKA_AUDIO12+'org.matroska.mka'MKA音频类型，归属类型为AUDIO。FILE'general.file'

所有文件的基类型，归属类型为ENTITY。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

DIRECTORY11+'general.directory'所有目录的基类型，归属类型为ENTITY。FOLDER'general.folder'

所有文件夹的基类型，归属类型为DIRECTORY。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

SYMLINK11+'general.symlink'所有符号链接的基类型，归属类型为ENTITY。ARCHIVE11+'general.archive'所有文件和目录存档文件的基类型，归属类型为OBJECT。BZ2_ARCHIVE11+'general.bz2-archive'BZ2存档文件类型，归属类型为ARCHIVE。OPG12+'general.opg'OPG存档文件类型，归属类型为ARCHIVE。TAZ_ARCHIVE12+'general.taz-archive'TAR压缩文件类型，归属类型为TAR_ARCHIVE。WEB_ARCHIVE12+'general.web-archive'MHTML网页归档文件类型，归属类型为ARCHIVE。DISK_IMAGE11+'general.disk-image'所有可作为卷装载项的文件类型的基类型，归属类型为ARCHIVE。ISO12+'general.iso'光盘映像文件类型，归属类型为DISK_IMAGE。TAR_ARCHIVE11+'general.tar-archive'TAR存档文件类型，归属类型为ARCHIVE。ZIP_ARCHIVE11+'general.zip-archive'ZIP存档文件类型，归属类型为ARCHIVE。JAVA_ARCHIVE11+'com.sun.java-archive'JAVA存档文件类型，归属类型为ARCHIVE和EXECUTABLE。GNU_TAR_ARCHIVE11+'org.gnu.gnu-tar-archive'GNU存档文件类型，归属类型为ARCHIVE。GNU_ZIP_ARCHIVE11+'org.gnu.gnu-zip-archive'GZIP存档文件类型，归属类型为ARCHIVE。GNU_ZIP_TAR_ARCHIVE11+'org.gnu.gnu-zip-tar-archive'GZIP TAR存档文件类型，归属类型为ARCHIVE。OPENXML12+'org.openxmlformats.openxml'开源XML基类型，归属类型为ARCHIVE。WORDPROCESSINGML_DOCUMENT12+'org.openxmlformats.wordprocessingml.document'开源XML文档类型，归属类型为OPENXML和COMPOSITE_OBJECT。SPREADSHEETML_SHEET12+'org.openxmlformats.spreadsheetml.sheet'开源XML电子表格类型，归属类型为OPENXML和COMPOSITE_OBJECT。PRESENTATIONML_PRESENTATION12+'org.openxmlformats.presentationml.presentation'开源XML演示文稿类型，归属类型为OPENXML和COMPOSITE_OBJECT。DRAWINGML_VISIO12+'org.openxmlformats.drawingml.visio'开源XML绘图文件类型，归属类型为OPENXML和COMPOSITE_OBJECT。DRAWINGML_TEMPLATE12+'org.openxmlformats.drawingml.template'开源XML绘图模板类型，归属类型为OPENXML和COMPOSITE_OBJECT。WORDPROCESSINGML_TEMPLATE12+'org.openxmlformats.wordprocessingml.template'开源XML文档模板类型，归属类型为OPENXML和COMPOSITE_OBJECT。PRESENTATIONML_TEMPLATE12+'org.openxmlformats.presentationml.template'开源XML演示文稿模板类型，归属类型为OPENXML和COMPOSITE_OBJECT。PRESENTATIONML_SLIDESHOW12+'org.openxmlformats.presentationml.slideshow'开源XML演示文稿幻灯片放映类型，归属类型为OPENXML和COMPOSITE_OBJECT。SPREADSHEETML_TEMPLATE12+'org.openxmlformats.spreadsheetml.template'开源XML电子表格模板类型，归属类型为OPENXML和COMPOSITE_OBJECT。OPENDOCUMENT12+'org.oasis.opendocument'Office应用程序的开源文档类型，归属类型为ARCHIVE。OPENDOCUMENT_TEXT12+'org.oasis.opendocument.text'开源文档类型，归属类型为OPENDOCUMENT和COMPOSITE_OBJECT。OPENDOCUMENT_SPREADSHEET12+'org.oasis.opendocument.spreadsheet'开源文档电子表格类型，归属类型为OPENDOCUMENT和COMPOSITE_OBJECT。OPENDOCUMENT_PRESENTATION12+'org.oasis.opendocument.presentation'开源文档演示类型，归属类型为OPENDOCUMENT和COMPOSITE_OBJECT。OPENDOCUMENT_GRAPHICS12+'org.oasis.opendocument.graphics'开源文档图形类型，归属类型为OPENDOCUMENT和COMPOSITE_OBJECT。OPENDOCUMENT_FORMULA12+'org.oasis.opendocument.formula'开源文档公式集类型，归属类型为OPENDOCUMENT。STUFFIT_ARCHIVE12+'com.allume.stuffit-archive'Stuffit压缩格式类型（Stuffit archive），归属类型为ARCHIVE。RAR_ARCHIVE12+'com.rarlab.rar-archive'WinRAR压缩格式类型，归属类型为ARCHIVE。SEVEN_ZIP_ARCHIVE12+'org.7-zip.7-zip-archive'7-zip压缩格式类型，归属类型为ARCHIVE。CALENDAR11+'general.calendar'所有日程类数据的基类型，归属类型为OBJECT。VCS12+'general.vcs'VCalendar日历数据类型，归属类型为CALENDAR和TEXT。ICS12+'general.ics'ICalendar日历数据类型，归属类型为CALENDAR和TEXT。CONTACT11+'general.contact'所有联系人类数据的基类型，归属类型为OBJECT。DATABASE11+'general.database'所有数据库文件的基类型，归属类型为OBJECT。MESSAGE11+'general.message'所有消息类数据的基类型，归属类型为OBJECT。EXECUTABLE12+'general.executable'所有可执行文件的基类型，归属类型为OBJECT。PORTABLE_EXECUTABLE12+'com.microsoft.portable-executable'Microsoft Windows应用程序类型，归属类型为EXECUTABLE。SUN_JAVA_CLASS12+'com.sun.java-class'Java类文件类型，归属类型为EXECUTABLE。VCARD11+'general.vcard'所有电子名片类数据的基类型，归属类型为OBJECT。NAVIGATION11+'general.navigation'所有导航类数据的基类型，归属类型为OBJECT。LOCATION11+'general.location'导航定位类型，归属类型为NAVIGATION。FONT12+'general.font'所有字体数据类型的基础类型，归属类型为OBJECT。TRUETYPE_FONT12+'general.truetype-font'TrueType字体类型，归属类型为FONT。TRUETYPE_COLLECTION_FONT12+'general.truetype-collection-font'TrueType collection字体类型，归属类型为FONT。OPENTYPE_FONT12+'general.opentype-font'OpenType 字体类型，归属类型为FONT。POSTSCRIPT_FONT12+'com.adobe.postscript-font'PostScript 字体类型，归属类型为FONT。POSTSCRIPT_PFB_FONT12+'com.adobe.postscript-pfb-font'PostScript Font Binary字体类型，归属类型为FONT。POSTSCRIPT_PFA_FONT12+'com.adobe.postscript-pfa-font'Adobe Type 1 字体类型，归属类型为FONT。OPENHARMONY_FORM'openharmony.form'

系统定义的卡片类型，归属类型为OBJECT。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

OPENHARMONY_APP_ITEM'openharmony.app-item'

系统定义的桌面图标类型，归属类型为OBJECT。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

OPENHARMONY_PIXEL_MAP'openharmony.pixel-map'

系统定义的像素图类型，归属类型为IMAGE。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

OPENHARMONY_ATOMIC_SERVICE11+'openharmony.atomic-service'系统定义的元服务类型，归属类型为OBJECT。OPENHARMONY_PACKAGE11+'openharmony.package'系统定义的包（即目录的打包文件），归属类型为DIRECTORY。OPENHARMONY_HAP11+'openharmony.hap'系统定义的能力包，归属类型为OPENHARMONY_PACKAGE。OPENHARMONY_HDOC12+'openharmony.hdoc'系统定义的备忘录数据类型，归属类型为COMPOSITE_OBJECT。OPENHARMONY_HINOTE12+'HarmonyOS.hinote'系统定义的笔记数据类型，归属类型为COMPOSITE_OBJECT。OPENHARMONY_STYLED_STRING12+'openharmony.styled-string'系统定义的样式字符串类型，归属类型为COMPOSITE_OBJECT。OPENHARMONY_WANT12+'openharmony.want'系统定义的Want类型，归属类型为OBJECT。OFD12+'general.ofd'开放版式文档类型，归属类型为COMPOSITE_OBJECT。CAD12+'general.cad'所有计算机辅助设计类型的基类型，归属类型为OBJECT。OCTET_STREAM12+'general.octet-stream'任意二进制数据类型，归属类型为OBJECT。FILE_URI15+'general.file-uri'文件地址类型，归属类型为TEXT。CONTENT_FORM15+'general.content-form'内容卡片类型，归属类型为OBJECT。

#### TypeDescriptor11+

标准化数据类型的描述类，它包含了一些属性和方法用于描述标准化数据类型自身以及和其他标准化数据类型之间的归属与层级关系。

#### 属性

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

名称类型只读可选说明typeId11+string否否标准化数据类型的ID（即[UTD列表](#ZH-CN_TOPIC_0000002497444710__uniformdatatype)中对应的枚举值），也可以是自定义UTD。belongingToTypes11+Array<string>否否标准化数据类型所归属的类型typeId列表。description11+string否否标准化数据类型的简要说明。referenceURL11+string否否标准化数据类型的参考链接URL，用于描述类型的详细信息。iconFile11+string否否标准化数据类型的默认图标文件路径，可能为空字符串（即没有默认图标），应用可以自行决定是否使用该默认图标。filenameExtensions12+Array<string>否否标准化数据类型所关联的文件名后缀列表。mimeTypes12+Array<string>否否标准化数据类型所关联的多用途互联网邮件扩展类型列表。

#### belongsTo11+

belongsTo(type: string): boolean

判断当前标准化数据类型是否归属于指定的标准化数据类型。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

参数名类型必填说明typestring是所指定的标准化数据类型（即[UniformDataType](#ZH-CN_TOPIC_0000002497444710__uniformdatatype)中对应的枚举值）。

**返回值：**

类型说明boolean返回true表示当前的标准化数据类型归属于所指定的标准化数据类型，包括所指定类型与当前类型相同的情况；返回false则表示无归属关系。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.type-script');
    let ret = typeObj.belongsTo('general.source-code');
    if(ret) {
        console.info('type general.type-script belongs to type general.source-code');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`belongsTo throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### isLowerLevelType11+

isLowerLevelType(type: string): boolean

判断当前标准化数据类型是否是指定标准化数据类型的低层级类型。例如TYPE_SCRIPT为SOURCE_CODE的低层级类型，TYPE_SCRIPT和SOURCE_CODE为TEXT的低层级类型。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

参数名类型必填说明typestring是所指定的标准化数据类型（即[UniformDataType](#ZH-CN_TOPIC_0000002497444710__uniformdatatype)中对应的枚举值）。

**返回值：**

类型说明boolean返回true表示当前的标准化数据类型是所指定标准化数据类型的低层级类型，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.type-script');
    let ret = typeObj.isLowerLevelType('general.source-code');
    if(ret) {
        console.info('type general.type-script is lower level type of type general.source-code');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`isLowerLevelType throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### isHigherLevelType11+

isHigherLevelType(type: string): boolean

判断当前标准化数据类型是否是指定标准化数据类型的高层级类型。例如SOURCE_CODE为TYPE_SCRIPT的高层级类型，TEXT为SOURCE_CODE和TYPE_SCRIPT的高层级类型。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

参数名类型必填说明typestring是所指定的标准化数据类型（即[UniformDataType](#ZH-CN_TOPIC_0000002497444710__uniformdatatype)中对应的枚举值）。

**返回值：**

类型说明boolean返回true表示当前的标准化数据类型是所指定标准化数据类型的高层级类型，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.source-code');
    let ret = typeObj.isHigherLevelType('general.type-script');
    if(ret) {
        console.info('type general.source-code is higher level type of type general.type-script');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`isHigherLevelType throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### equals11+

equals(typeDescriptor: TypeDescriptor): boolean

判断指定的标准化数据类型描述类对象的类型ID和当前标准化数据类型描述类对象的类型ID是否相同，即[TypeDescriptor](#ZH-CN_TOPIC_0000002497444710__typedescriptor11)对象的typeId。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

参数名类型必填说明typeDescriptor[TypeDescriptor](#ZH-CN_TOPIC_0000002497444710__typedescriptor11)是待比较的标准化数据类型描述类对象。

**返回值：**

类型说明boolean返回true表示所比较的标准化数据类型相同；返回false则表示不同。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeA : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.type-script');
    let typeB : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.python-script');
    if(!typeA.equals(typeB)) {
      console.info('typeA is not equal to typeB');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### uniformTypeDescriptor.getTypeDescriptor11+

getTypeDescriptor(typeId: string): TypeDescriptor

按给定的标准化数据类型ID查询并返回对应的标准化数据类型描述类对象。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

参数名类型必填说明typeIdstring是[标准化数据类型ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-list#基础类型)。

**返回值：**

类型说明[TypeDescriptor](#ZH-CN_TOPIC_0000002497444710__typedescriptor11)返回标准化数据类型描述类对象，如果要查询的标准化数据类型不存在则返回null。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('com.adobe.photoshop-image');
    if (typeObj) {
        let typeId = typeObj.typeId;
        let belongingToTypes = typeObj.belongingToTypes;
        let description = typeObj.description;
        let referenceURL = typeObj.referenceURL;
        let iconFile = typeObj.iconFile;
        let filenameExtensions = typeObj.filenameExtensions;
        let mimeTypes = typeObj.mimeTypes;
        console.info(`typeId: ${typeId}, belongingToTypes: ${belongingToTypes}, description: ${description}, referenceURL: ${referenceURL}, iconFile: ${iconFile}, filenameExtensions: ${filenameExtensions}, mimeTypes: ${mimeTypes}`);
    } else {
        console.info('type com.adobe.photoshop-image does not exist');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`getTypeDescriptor throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### uniformTypeDescriptor.getUniformDataTypeByFilenameExtension11+

getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string

根据给定的文件后缀名和所归属的标准化数据类型查询标准化数据类型ID，若有多个符合条件的标准化数据类型ID，则返回第一个。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

参数名类型必填说明filenameExtensionstring是文件后缀名称。belongsTostring否要查询的标准化数据类型所归属类型ID，无默认值，若不传入此参数则只按照文件后缀名称查询[标准化数据类型ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-list#基础类型)。

**返回值：**

类型说明string返回与给定文件后缀名以及归属类型ID（如果设置了belongsTo参数）匹配的标准化数据类型ID，如果要查询的标准化数据类型不存在则返回根据入参按指定规则生成的动态类型。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeId = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension('.ts', 'general.source-code');
    if(typeId) {
        console.info('typeId is general.type-script');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`getUniformDataTypeByFilenameExtension throws an exception. code is ${error.code}, message is ${error.message} `);
}

// 根据“.myts”，“general.plain-text”查不到预置数据类型则按返回根据入参信息生成的动态类型。
try {
    let typeId = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension('.myts', 'general.plain-text');
    if(typeId) {
        console.info('typeId is flex.************');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`getUniformDataTypeByFilenameExtension throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### uniformTypeDescriptor.getUniformDataTypeByMIMEType11+

getUniformDataTypeByMIMEType(mimeType: string, belongsTo?: string): string

根据给定的MIME类型和所归属的标准化数据类型查询标准化数据类型ID，若有多个符合条件的标准化数据类型ID，则返回第一个。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

参数名类型必填说明mimeTypestring是MIME类型名称。belongsTostring否要查询的标准化数据类型所归属类型ID。无默认值，若不传入此参数则只按照MIME类型名称查询[标准化数据类型ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-list#基础类型)。

**返回值：**

类型说明string返回与MIME类型名称以及归属类型ID（如果设置了belongsTo参数）匹配的标准化数据类型ID，如果要查询的标准化数据类型不存在则返回根据入参按指定规则生成的动态类型。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeId = uniformTypeDescriptor.getUniformDataTypeByMIMEType('image/jpeg', 'general.image');
    if(typeId) {
        console.info('typeId is general.jpeg');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`getUniformDataTypeByMIMEType throws an exception. code is ${error.code}, message is ${error.message} `);
}

// 根据“image/myimage”, “general.image”查不到预置数据类型则按返回根据入参信息生成的动态类型。
try {
    let typeId = uniformTypeDescriptor.getUniformDataTypeByMIMEType('image/myimage', 'general.image');
    if(typeId) {
        console.info('typeId is flex.************');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`getUniformDataTypeByMIMEType throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### uniformTypeDescriptor.getUniformDataTypesByFilenameExtension13+

getUniformDataTypesByFilenameExtension(filenameExtension: string, belongsTo?: string): Array<string>

根据给定的文件后缀名和所归属的标准化数据类型查询标准化数据类型ID列表。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

参数名类型必填说明filenameExtensionstring是文件后缀名称。belongsTostring否要查询的标准化数据类型所归属类型ID，无默认值，若不传入此参数则只按照文件后缀名称查询[标准化数据类型ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-list#基础类型)。

**返回值：**

类型说明Array<string>返回与给定文件后缀名以及归属类型ID（如果设置了belongsTo参数）匹配的标准化数据类型ID列表，如果要查询的标准化数据类型不存在则返回根据入参按指定规则生成的动态类型列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeIds = uniformTypeDescriptor.getUniformDataTypesByFilenameExtension('.ts', 'general.source-code');
    for (let typeId of typeIds) {
        console.info(`typeId is ${typeId}`);
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`getUniformDataTypesByFilenameExtension throws an exception. code is ${error.code}, message is ${error.message} `);
}

// 根据“.myts”，“general.plain-text”查不到预置数据类型则按返回根据入参信息生成的动态类型列表。
try {
    let flexTypeIds = uniformTypeDescriptor.getUniformDataTypesByFilenameExtension('.myts', 'general.plain-text');
    for (let flexTypeId of flexTypeIds) {
        console.info(`typeId is flex type, flex typeId is ${flexTypeId}`);
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`getUniformDataTypesByFilenameExtension throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

#### uniformTypeDescriptor.getUniformDataTypesByMIMEType13+

getUniformDataTypesByMIMEType(mimeType: string, belongsTo?: string): Array<string>

根据给定的MIME类型和所归属的标准化数据类型查询标准化数据类型ID列表。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

参数名类型必填说明mimeTypestring是MIME类型名称。belongsTostring否要查询的标准化数据类型所归属类型ID。无默认值，若不传入此参数则只按照MIME类型名称查询[标准化数据类型ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-list#基础类型)。

**返回值：**

类型说明Array<string>返回与MIME类型名称以及归属类型ID（如果设置了belongsTo参数）匹配的标准化数据类型ID列表，如果要查询的标准化数据类型不存在则返回根据入参按指定规则生成的动态类型列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.

**示例：**

```ets
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeIds = uniformTypeDescriptor.getUniformDataTypesByMIMEType('text/plain', 'general.text');
    for (let typeId of typeIds) {
        console.info(`typeId is ${typeId}`);
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`getUniformDataTypesByMIMEType throws an exception. code is ${error.code}, message is ${error.message} `);
}

// 根据“image/myimage”, “general.image”查不到预置数据类型则按返回根据入参信息生成的动态类型列表。
try {
    let flexTypeIds = uniformTypeDescriptor.getUniformDataTypesByMIMEType('image/myimage', 'general.image');
    for (let flexTypeId of flexTypeIds) {
        console.info(`typeId is flex type, flex typeId is ${flexTypeId}`);
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`getUniformDataTypesByMIMEType throws an exception. code is ${error.code}, message is ${error.message} `);
}
```