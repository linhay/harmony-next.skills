# Constants

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| XMAGE_WATERMARK_MODE_AT_THE_BOTTOM | number | 9 | XMAGE水印固定位于图像底部中央。 |
| XMAGE_WATERMARK_MODE_BORDER | number | 10 | XMAGE水印会自动调整到边界位置，系统根据图像内容选择最适合的边界区域。 |
| CAPTURE_MODE_PROFESSIONAL | number | 2 | 拍摄模式：专业模式。 |
| CAPTURE_MODE_FRONT_LENS_NIGHT_VIEW | number | 7 | 拍摄模式：前置摄像头夜景模式。 |
| CAPTURE_MODE_PANORAMA | number | 8 | 拍摄模式：全景模式。 |
| CAPTURE_MODE_TAIL_LIGHT | number | 9 | 拍摄模式：尾灯模式。 |
| CAPTURE_MODE_LIGHT_GRAFFITI | number | 10 | 拍摄模式：轻涂鸦模式。 |
| CAPTURE_MODE_SILKY_WATER | number | 11 | 拍摄模式：缎面感水流模式。 |
| CAPTURE_MODE_STAR_TRACK | number | 12 | 拍摄模式：星轨模式。 |
| CAPTURE_MODE_WIDEAPERTURE | number | 19 | 拍摄模式：广角模式。 |
| CAPTURE_MODE_MOVING_PHOTO | number | 20 | 拍摄模式：动态照片模式。 |
| CAPTURE_MODE_PORTRAIT | number | 23 | 拍摄模式：人像模式。 |
| CAPTURE_MODE_REAR_LENS_NIGHT_VIEW | number | 42 | 拍摄模式：后镜头夜景模式。 |
| CAPTURE_MODE_SUPER_MACRO | number | 47 | 拍摄模式：超微距模式。 |
| CAPTURE_MODE_SNAP_SHOT | number | 62 | 拍摄模式：抓拍模式。 |

示例：

```ets
import { image } from '@kit.ImageKit';

const defaultXmageWaterMarkModeAtTheBottom = image.XMAGE_WATERMARK_MODE_AT_THE_BOTTOM;
const defaultXmageWaterMarkModeBorder = image.XMAGE_WATERMARK_MODE_BORDER;
const defaultCaptureModeProfessional = image.CAPTURE_MODE_PROFESSIONAL;
const defaultCaptureModeFrontLensNightView = image.CAPTURE_MODE_FRONT_LENS_NIGHT_VIEW;
const defaultCaptureModePanorama = image.CAPTURE_MODE_PANORAMA;
const defaultCaptureModeTailLight = image.CAPTURE_MODE_TAIL_LIGHT;
const defaultCaptureModeLightGraffiti = image.CAPTURE_MODE_LIGHT_GRAFFITI;
const defaultCaptureModeSilkyWater = image.CAPTURE_MODE_SILKY_WATER;
const defaultCaptureModeStarTrack = image.CAPTURE_MODE_STAR_TRACK;
const defaultCaptureModeWideAperture = image.CAPTURE_MODE_WIDEAPERTURE;
const defaultCaptureModeMovingPhoto = image.CAPTURE_MODE_MOVING_PHOTO;
const defaultCaptureModePortrait = image.CAPTURE_MODE_PORTRAIT;
const defaultCaptureModeRearLensNightView = image.CAPTURE_MODE_REAR_LENS_NIGHT_VIEW;
const defaultCaptureModeSuperMacro = image.CAPTURE_MODE_SUPER_MACRO;
const defaultCaptureModeSnapShot = image.CAPTURE_MODE_SNAP_SHOT;
```