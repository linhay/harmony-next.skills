# voipCall (应用内通话管理)

本模块提供应用内通话管理功能，包括向系统上报来电、上报去电、上报通话状态以及获取用户点击事件等。

获取用户点击事件需使用[voipCall.on](#section7587131203319)在业务流程开始时提前订阅voipCallUiEvent事件，可于业务流程结束后使用[voipCall.off](#section84793361325)结束订阅。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { voipCall } from '@kit.CallServiceKit';
```

#### VoipCallType

表示通话类型的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

名称

值

说明

VOIP_CALL_VOICE

0

语音通话。

VOIP_CALL_VIDEO

1

视频通话。

#### VoipCallState

表示通话状态的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

名称

值

说明

VOIP_CALL_STATE_IDLE

0

呼叫状态空闲。

VOIP_CALL_STATE_RINGING

1

呼叫传入状态。

VOIP_CALL_STATE_ACTIVE

2

激活呼叫状态。

VOIP_CALL_STATE_HOLDING

3

保持呼叫状态。

VOIP_CALL_STATE_DISCONNECTED

4

呼叫状态已断开。

VOIP_CALL_STATE_DIALING

5

拨号中。

**起始版本**: 5.0.0(12)

VOIP_CALL_STATE_ANSWERED

6

正在接听。

**起始版本**: 5.0.0(12)

VOIP_CALL_STATE_DISCONNECTING

7

正在断开。

**起始版本**: 5.0.0(12)

#### VoipCallUiEvent

表示通话事件的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

名称

值

说明

VOIP_CALL_EVENT_NONE

0

无任何事件。

VOIP_CALL_EVENT_VOICE_ANSWER

1

通话语音接听事件。

VOIP_CALL_EVENT_VIDEO_ANSWER

2

通话视频接听事件。

VOIP_CALL_EVENT_REJECT

3

通话拒接事件。

VOIP_CALL_EVENT_HANGUP

4

通话挂断事件。

VOIP_CALL_EVENT_MUTED

5

静音事件。

**起始版本**: 5.0.0(12)

VOIP_CALL_EVENT_UNMUTED

6

取消静音事件。

**起始版本**: 5.0.0(12)

VOIP_CALL_EVENT_SPEAKER_ON

7

开启扬声器事件。

**起始版本**: 5.0.0(12)

（预留事件，暂未支持）

VOIP_CALL_EVENT_SPEAKER_OFF

8

关闭扬声器事件。

**起始版本**: 5.0.0(12)

（预留事件，暂未支持）

VOIP_CALL_EVENT_MUTE_RINGTONE

9

用户按键静音铃声事件。

**起始版本**: 6.0.2(22)

#### ErrorReason

表示错误码类型的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

名称

值

说明

ERROR_NONE

0

无错误出现。

CELLULAR_CALL_EXISTS

1

当前已存在蜂窝通话。

VOIP_CALL_EXISTS

2

当前已存在其他应用内通话。

INVALID_CALL

3

通话无效，比如传入的callId未通过校验等。

USER_ANSWER_CELLULAR_FIRST

4

用户选择接听蜂窝。

#### VoipCallUiEventInfo

通话事件详细信息。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

callId

string

否

否

应用内通话唯一ID。

voipCallUiEvent

[VoipCallUiEvent](#section26961727970)

否

否

应用内通话事件。

errorReason

[ErrorReason](#section15252018876)

否

否

应用内通话错误码。

#### VoipCallFailureCause

表示来电消息建立失败原因的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

名称

值

说明

OTHER

0

其他失败原因。

ROUTE_BUSY

1

应用线路忙。

CONNECTION_FAILED

2

通话连接建立失败。

#### VoipCallAttribute

通话属性选项。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

callId

string

否

否

应用内通话唯一ID。

voipCallType

[VoipCallType](#section0933646875)

否

否

应用内通话类型。

userName

string

否

否

应用内通话用户昵称。

userProfile

image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

否

否

用户头像图片，需导入图像处理模块，详情见[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)。

支持传入的最大图片大小为 221 x 221 像素，推荐传入的图片大小为 112 x 112 像素。通过 [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)的[getPixelBytesNumber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#getpixelbytesnumber7)接口获取到的图片大小要小于196608。

abilityName

string

否

否

接听后需加载的应用界面ability名称。

voipCallState

[VoipCallState](#section24523814719)

否

否

应用内通话状态。

showBannerForIncomingCall

boolean

否

是

支持应用上报来电/去电是否显示横幅通知。

true：应用设置来电显示横幅通知。

false：应用设置来电不显示横幅通知。

默认值为true。

**起始版本**: 5.0.0(12)

isConferenceCall

boolean

否

是

通话是否为会议。

true：来电是会议。

false：来电不是会议。

默认值为false。

**起始版本**: 5.0.0(12)

isVoiceAnswerSupported

boolean

否

是

视频来电/去电是否支持语音接听。

true：支持。

false：不支持。

默认值为true。

**起始版本**: 5.0.0(12)

isUserMuteRingToneAllowed

boolean

否

是

是否支持用户按键静音来电铃声。

true：支持。

false：不支持。

默认值为false。

**起始版本**: 6.0.2(22)

isDialingAllowedDuringCarrierCall

boolean

否

是

是否允许运营商通话中发起VoIP主叫。

true：支持。

false：不支持。

默认值为false。

**起始版本**: 6.0.2(22)

#### CallAudioEvent

表示静音、扬声器事件的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**5.0.0(12)

名称

值

说明

AUDIO_EVENT_MUTED

0

静音。

AUDIO_EVENT_UNMUTED

1

取消静音。

AUDIO_EVENT_SPEAKER_ON

2

开启扬声器。

AUDIO_EVENT_SPEAKER_OFF

3

关闭扬声器。

#### voipCall.on('voipCallUiEvent')

on(type: 'voipCallUiEvent', callback: Callback<VoipCallUiEventInfo>): void

订阅voipCallUiEvent事件。使用Callback的方式获取订阅voipCallUiEvent事件的结果。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

type

string

是

通话事件类型，参数固定为“voipCallUiEvent”。

callback

Callback<[VoipCallUiEventInfo](#section1178710819715)>

是

回调函数，返回通话事件详细信息对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1007200001

Invalid parameter value.

1007200002

Operation failed. Cannot connect to service.

1007200003

System internal error.

1007200999

Unknown error code.

**示例：**

```ets
import { voipCall } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

voipCall.on('voipCallUiEvent', (data: voipCall.VoipCallUiEventInfo) => {
  hilog.info(0x0000, 'testTag', `Succeeded in reading callback. CallId: ${data.callId}, voipCallUiEvent: ${data.voipCallUiEvent}`);
});
```

#### voipCall.off('voipCallUiEvent')

off(type: 'voipCallUiEvent', callback?: Callback<VoipCallUiEventInfo>): void

取消订阅voipCallUiEvent事件。使用Callback的方式获取取消订阅voipCallUiEvent事件的结果。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

type

string

是

通话事件类型，参数固定为“voipCallUiEvent”。

callback

Callback<[VoipCallUiEventInfo](#section1178710819715)>

否

需要取消监听的回调函数，返回通话事件详细信息对象。若不填，则取消当前应用监听该事件的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1007200001

Invalid parameter value.

1007200002

Operation failed. Cannot connect to service.

1007200003

System internal error.

1007200999

Unknown error code.

**示例：**

```ets
import { voipCall } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

voipCall.off('voipCallUiEvent', (data: voipCall.VoipCallUiEventInfo) => {
  hilog.info(0x0000, 'testTag', `Succeeded in reading callback. CallId: ${data.callId}, voipCallUiEvent: ${data.voipCallUiEvent}`);
});
```

#### voipCall.reportIncomingCall

reportIncomingCall(voipCallAttribute: VoipCallAttribute): Promise<ErrorReason>

通知来电消息，如果应用来电消息建立失败，需调用[reportIncomingCallError](#section155796451716)通知来电建立失败。需设置通话详细信息，见[VoipCallAttribute](#section4221135015444)。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

voipCallAttribute

[VoipCallAttribute](#section4221135015444)

是

应用内通话详细信息如用户头像、用户昵称、通话唯一标识等，详情请参见[VoipCallAttribute](#section4221135015444)。（应用上报去电时，VoipCallAttribute中的voipCallState属性必须为VOIP_CALL_STATE_DIALING。）

**返回值：**

类型

说明

Promise<[ErrorReason](#section15252018876)>

Promise对象，返回错误码类型。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1007200001

Invalid parameter value.

1007200002

Operation failed. Cannot connect to service.

1007200003

System internal error.

1007200999

Unknown error code.

**示例：**

```ets
import { image } from '@kit.ImageKit';
import { voipCall } from '@kit.CallServiceKit';
import { resourceManager } from '@kit.LocalizationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIAbility } from '@kit.AbilityKit';
import { pushService } from '@kit.PushKit';

interface Content {
  data: string;
  callId: string;
}

export default class VoipAbility extends UIAbility {
  onCreate(): void {
    hilog.info(0x0000, 'testTag', 'VoipExtAbility onCreate.');
    pushService.receiveMessage('VoIP', this, async (data) => {
      let content: Content = JSON.parse(data.data);
      let callId: string = content.callId;

      hilog.info(0x0000, 'testTag', 'Get voip message successfully: %{public}s', callId);

      // 此处为用户头像，需要创建PixelMap类型
      const resourceMgr : resourceManager.ResourceManager = this.context.resourceManager;
      const fileData : Uint8Array = await resourceMgr.getRawFileContent('example.png');
      const buffer = fileData.buffer;
      const imageSource : image.ImageSource = image.createImageSource(buffer);
      const pixelMap : image.PixelMap = await imageSource.createPixelMap();
      if (pixelMap) {
        pixelMap.getImageInfo((err, imageInfo) => {
          if (imageInfo) {
            hilog.info(0x0000, 'testTag', `DemoPushMessageAbility imageInfo: ${imageInfo.size.width} * ${imageInfo.size.height}.`);
          }
        });
      }

      // 构建通话详细信息的对象
      let callInfo: voipCall.VoipCallAttribute = {
        callId: callId,
        voipCallType: voipCall.VoipCallType.VOIP_CALL_VOICE,
        userName: "name",
        userProfile: pixelMap,
        abilityName: 'ability',
        voipCallState: voipCall.VoipCallState.VOIP_CALL_STATE_RINGING
      };

      // 通知来电消息
      let error = await voipCall.reportIncomingCall(callInfo);
      if (error != voipCall.ErrorReason.ERROR_NONE) {
        hilog.error(0x0000, 'testTag', 'Failed to report incoming call: %{public}d', error);
        return;
      }

      hilog.info(0x0000, 'testTag', 'Get voip message end.');
    });
    hilog.info(0x0000, 'testTag', 'Succeeded in registering VoIP.');
  }
}
```

#### voipCall.reportOutgoingCall

reportOutgoingCall(voipCallAttribute: VoipCallAttribute): Promise<ErrorReason>

应用上报去电。需设置通话详细信息，见[VoipCallAttribute](#section4221135015444)。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

voipCallAttribute

[VoipCallAttribute](#section4221135015444)

是

应用内通话详细信息如用户头像、用户昵称、通话唯一标识等，详情请参见[VoipCallAttribute](#section4221135015444)。

**返回值：**

类型

说明

Promise<[ErrorReason](#section15252018876)>

Promise对象，返回错误码类型。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1007200001

Invalid parameter value.

1007200002

Operation failed. Cannot connect to service.

1007200003

System internal error.

1007200999

Unknown error code.

**示例：**

```ets
import { image } from '@kit.ImageKit';
import { voipCall } from '@kit.CallServiceKit';
import { resourceManager } from '@kit.LocalizationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIAbility } from '@kit.AbilityKit';
import { pushService } from '@kit.PushKit';

interface Content {
  data: string;
  callId: string;
}

export default class VoipExtAbility extends UIAbility {
  onCreate(): void {
    hilog.info(0x0000, 'testTag', 'VoipExtAbility onCreate.');
    pushService.receiveMessage('VoIP', this, async (data) => {
      let content: Content = JSON.parse(data.data);
      let callId: string = content.callId;

      hilog.info(0x0000, 'testTag', 'Get voip message successfully: %{public}s', callId);

      // 此处为用户头像，需要创建PixelMap类型
      const resourceMgr : resourceManager.ResourceManager = this.context.resourceManager;
      const fileData : Uint8Array = await resourceMgr.getRawFileContent('example.png');
      const buffer = fileData.buffer;
      const imageSource : image.ImageSource = image.createImageSource(buffer);
      const pixelMap : image.PixelMap = await imageSource.createPixelMap();
      if (pixelMap) {
        pixelMap.getImageInfo((err, imageInfo) => {
          if (imageInfo) {
            hilog.info(0x0000, 'testTag', `DemoPushMessageAbility imageInfo: ${imageInfo.size.width} * ${imageInfo.size.height}.`);
          }
        });
      }

      // 构建通话详细信息的对象
      let callInfo: voipCall.VoipCallAttribute = {
        callId: callId,
        voipCallType: voipCall.VoipCallType.VOIP_CALL_VOICE,
        userName: "name",
        userProfile: pixelMap,
        abilityName: 'ability',
        voipCallState: voipCall.VoipCallState.VOIP_CALL_STATE_DIALING
      };

      // 通知去电消息
      let error = await voipCall.reportOutgoingCall(callInfo);
      if (error != voipCall.ErrorReason.ERROR_NONE) {
        hilog.error(0x0000, 'testTag', 'Failed to report outgoing call: %{public}d', error);
        return;
      }
      hilog.info(0x0000, 'testTag', 'Get voip message end.');
    });
    hilog.info(0x0000, 'testTag', 'Succeeded in registering VoIP.');
  }
}
```

#### voipCall.reportCallAudioEventChange

reportCallAudioEventChange(callId: string, callAudioEvent: CallAudioEvent): Promise<void>

应用上报通话中的静音、扬声器事件。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

callId

string

是

应用内通话唯一ID。

callAudioEvent

[CallAudioEvent](#section312217120409)

是

VoIP开/关静音、扬声器事件，详情请参见[CallAudioEvent](#section312217120409)。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1007200001

Invalid parameter value.

1007200002

Operation failed. Cannot connect to service.

1007200003

System internal error.

1007200999

Unknown error code.

**示例：**

```ets
import { voipCall } from '@kit.CallServiceKit';
import { UIAbility } from '@kit.AbilityKit';
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

interface Content {
  data: string;
  callId: string;
}

export default class VoipExtAbility extends UIAbility {
  onCreate(): void {
    hilog.info(0x0000, 'testTag', 'VoipExtAbility onCreate.');
    pushService.receiveMessage('VoIP', this, async (data) => {
      let content: Content = JSON.parse(data.data);
      let callId: string = content.callId;

      let callAudioEvent : voipCall.CallAudioEvent = voipCall.CallAudioEvent.AUDIO_EVENT_MUTED;

      // 上报通话中静音、扬声器事件
      voipCall.reportCallAudioEventChange(callId, callAudioEvent).then(() => {
        hilog.info(0x0000, 'testTag', `Succeeded in reporting call audio event change.`);
      });
    });
    hilog.info(0x0000, 'testTag', 'Succeeded in registering VoIP.');
  }
}
```

#### voipCall.reportCallStateChange

reportCallStateChange(callId: string, callState: VoipCallState): Promise<void>

通知应用内通话状态变化，使用Promise异步回调。

该接口不能改变通话类型，例如，语音通话不能升级为视频通话，视频通话也不能降级为语音通话，如需上述升降级操作，请调用[voipCall.reportCallStateChange](#section5360122718341)。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

callId

string

是

呼叫ID。

callState

[VoipCallState](#section24523814719)

是

通话状态，参考[VoipCallState](#section24523814719)。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1007200001

Invalid parameter value.

1007200002

Operation failed. Cannot connect to service.

1007200003

System internal error.

1007200999

Unknown error code.

**示例：**

```ets
import { voipCall } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

voipCall.reportCallStateChange("callId123", voipCall.VoipCallState.VOIP_CALL_STATE_ACTIVE).then(() => {
  hilog.info(0x0000, 'testTag', `Succeeded in reporting call state change.`);
});
```

#### voipCall.reportCallStateChange

reportCallStateChange(callId: string, callState: VoipCallState, callType: VoipCallType): Promise<void>

通知应用内通话状态变化，并指定通话类型，使用Promise异步回调。

对于视频来电语音接听、通话中视频降语音或者语音升视频，需要调用该接口，并传入正确的callType。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

callId

string

是

呼叫ID。

callState

[VoipCallState](#section24523814719)

是

通话状态，参考[VoipCallState](#section24523814719)。

callType

[VoipCallType](#section0933646875)

是

通话类型，参考[VoipCallType](#section0933646875)。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1007200001

Invalid parameter value.

1007200002

Operation failed. Cannot connect to service.

1007200003

System internal error.

1007200999

Unknown error code.

**示例：**

```ets
import { voipCall } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

voipCall.reportCallStateChange("callId123", voipCall.VoipCallState.VOIP_CALL_STATE_ACTIVE, voipCall.VoipCallType.VOIP_CALL_VOICE).then(() => {
  hilog.info(0x0000, 'testTag', `Succeeded in reporting call state change.`);
});
```

#### voipCall.reportIncomingCallError

reportIncomingCallError(callId: string, voipCallFailureCause: VoipCallFailureCause): Promise<void>

通知来电消息建立失败的原因，使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

callId

string

是

应用内通话唯一ID。

voipCallFailureCause

[VoipCallFailureCause](#section157617591167)

是

来电消息建立失败原因。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error.

1007200001

Invalid parameter value.

1007200002

Operation failed. Cannot connect to service.

1007200003

System internal error.

1007200999

Unknown error code.

**示例：**

```ets
import { voipCall } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

voipCall.reportIncomingCallError("callId123", voipCall.VoipCallFailureCause.OTHER).then(() => {
  hilog.info(0x0000, 'testTag', `Succeeded in reporting incoming call error.`);
});
```