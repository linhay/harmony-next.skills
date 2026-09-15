# @ohos.data.intelligence.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * Provides methods for intelligent data processing.
 *
 * @namespace intelligence
 * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
 * @since 15
 */
declare namespace intelligence {
    /**
     * Obtains a text embedding model.
     *
     * @param { ModelConfig } config - The configuration of the embedding model.
     * @returns { Promise<TextEmbedding> } The promise returned by the function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     * <br>2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 31300000 - Inner error.
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @since 15
     */
    function getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding>;
    /**
     * Obtains an image embedding model.
     *
     * @param { ModelConfig } config - The configuration of the embedding model.
     * @returns { Promise<ImageEmbedding> } The promise returned by the function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     * <br>2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 31300000 - Inner error.
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @since 15
     */
    function getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>;
    /**
     * Indicates cloud embedding model information.
     *
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface CloudModelInfo {
        /**
         * Indicates cloud embedding model type.
         *
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        modelType: string;
        /**
         * Indicates cloud embedding model version.
         *
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        modelVersionCode?: string;
    }
    /**
     * Indicates network policy.
     *
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum NetworkPolicy {
        /**
         * Using WiFi.
         *
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        WIFI_ONLY = 0,
        /**
         * Using WiFi and Cellular.
         *
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        WIFI_AND_CELLULAR = 1
    }
    /**
     * Manages configurations of the embedding model.
     *
     * @interface ModelConfig
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @since 15
     */
    interface ModelConfig {
        /**
         * Version of the model.
         * The outputs of text or image embedding models with the same version are in the same vector space.
         *
         * @type { ModelVersion }
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        version: ModelVersion;
        /**
         * Indicates whether NPU is used.
         *
         * @type { boolean }
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        isNpuAvailable: boolean;
        /**
         * If NPU is used for accelerating, a local path is required for model caching.
         *
         * @type { ?string }
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        cachePath?: string;
        /**
         * Indicates cloud embedding model information.
         *
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        modelInfo?: CloudModelInfo;
        /**
         * Indicates cloud embedding model network policy.
         *
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        networkPolicy?: NetworkPolicy;
    }
    /**
     * Version of the model.
     *
     * @enum { number }
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @since 15
     */
    enum ModelVersion {
        /**
         * The basic embedding model.
         *
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        BASIC_MODEL = 0
    }
    /**
     * Describes the text embedding functions of the multi-modal embedding model.
     * Chinese and English are supported.
     *
     * @interface TextEmbedding
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @since 15
     */
    interface TextEmbedding {
        /**
         * Loads this text embedding model. If the loading fails, an error code is returned.
         *
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 31300000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        loadModel(): Promise<void>;
        /**
         * Releases this text embedding model. If the releasing fails, an error code is returned.
         *
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 31300000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        releaseModel(): Promise<void>;
        /**
         * Obtains the embedding vector of the given text.
         * The model can process up to 512 characters of text per inference, supporting both Chinese and English.
         *
         * @param { string } text - The input text of the embedding model.
         * @returns { Promise<Array<number>> } The promise used to return the embedding result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         * <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 31300000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        getEmbedding(text: string): Promise<Array<number>>;
        /**
         * Obtains the embedding vector of a given batch of text.
         * The model can process up to 512 characters of text per inference, supporting both Chinese and English.
         *
         * @param { Array<string> } batchTexts - The input batch of texts of the embedding model.
         * @returns { Promise<Array<Array<number>>> } The promise used to return the embedding result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         * <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 31300000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        getEmbedding(batchTexts: Array<string>): Promise<Array<Array<number>>>;
    }
    /**
     * Describes the image embedding functions of the multi-modal embedding model.
     *
     * @interface ImageEmbedding
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @since 15
     */
    interface ImageEmbedding {
        /**
         * Loads this image embedding model. If the loading fails, an error code is returned.
         *
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 31300000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        loadModel(): Promise<void>;
        /**
         * Releases this image embedding model. If the releasing fails, an error code is returned.
         *
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 31300000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        releaseModel(): Promise<void>;
        /**
         * Obtains the embedding vector of the given image.
         * The model can handle images below 20 MB in size in a single inference.
         *
         * @param { Image } image - The input image of the embedding model.
         * @returns { Promise<Array<number>> } The promise used to return the embedding result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         * <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 31300000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        getEmbedding(image: Image): Promise<Array<number>>;
    }
    /**
     * The type of the image can be its URI.
     *
     * @typedef { string } Image
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 15
     */
    type Image = string;
    /**
     * Splits text.
     *
     * @param { string } text - Text for chunking. The length of the text is no longer then 100k tokens.
     * @param { SplitConfig } config - Configurations of text chunking.
     * @returns { Promise<Array<string>> } The promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     * <br>2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 31300000 - Inner error.
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @since 15
     */
    function splitText(text: string, config: SplitConfig): Promise<Array<string>>;
    /**
     * Obtains the supported cloud embedding models.
     *
     * @returns { Promise<Array<CloudModelInfo>> } The promise returned by the function.
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function getSupportedCloudModel(): Promise<Array<CloudModelInfo>>;
    /**
     * Manages text chunk process configurations.
     *
     * @interface SplitConfig
     * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
     * @since 15
     */
    interface SplitConfig {
        /**
         * The maximun size of chunks.
         *
         * @type { number }
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        size: number;
        /**
         * The ratio of overlap between adjacent chunks.
         *
         * @type { number }
         * @syscap SystemCapability.DistributedDataManager.DataIntelligence.Core
         * @since 15
         */
        overlapRatio: number;
    }
}
export default intelligence;

```
