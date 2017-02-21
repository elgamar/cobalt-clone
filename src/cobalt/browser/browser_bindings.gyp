# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'includes': [
    '../bindings/bindings.gypi',
  ],
  'variables': {
    # Base directory into which generated sources and intermediate files should
    # be generated.
    'bindings_output_dir': '<(SHARED_INTERMEDIATE_DIR)/bindings/browser',

    'bindings_dependencies': [
      '../h5vcc/h5vcc.gyp:h5vcc',
      '../webdriver/webdriver.gyp:webdriver',
    ],

    # Bindings for the interfaces in this list will be generated, and there must
    # be an implementation declared in a header that lives in the same
    # directory of each IDL.
    'source_idl_files': [
        '../audio/AudioBuffer.idl',
        '../audio/AudioBufferSourceNode.idl',
        '../audio/AudioContext.idl',
        '../audio/AudioDestinationNode.idl',
        '../audio/AudioNode.idl',

        '../cssom/CSS.idl',
        '../cssom/CSSConditionRule.idl',
        '../cssom/CSSGroupingRule.idl',
        '../cssom/CSSFontFaceRule.idl',
        '../cssom/CSSMediaRule.idl',
        '../cssom/CSSKeyframeRule.idl',
        '../cssom/CSSKeyframesRule.idl',
        '../cssom/CSSRule.idl',
        '../cssom/CSSRuleList.idl',
        '../cssom/CSSStyleDeclaration.idl',
        '../cssom/CSSStyleRule.idl',
        '../cssom/CSSStyleSheet.idl',
        '../cssom/MediaList.idl',
        '../cssom/StyleSheet.idl',
        '../cssom/StyleSheetList.idl',

        '../debug/DebugHub.idl',
        '../debug/Debugger.idl',
        '../debug/DebuggerEventTarget.idl',
        '../debug/DebugScriptRunner.idl',

        '../dom/AnimationEvent.idl',
        '../dom/ArrayBuffer.idl',
        '../dom/ArrayBufferView.idl',
        '../dom/Attr.idl',
        '../dom/Blob.idl',
        '../dom/CDATASection.idl',
        '../dom/CharacterData.idl',
        '../dom/Comment.idl',
        '../dom/Console.idl',
        '../dom/Crypto.idl',
        '../dom/DataView.idl',
        '../dom/Document.idl',
        '../dom/DocumentTimeline.idl',
        '../dom/DocumentType.idl',
        '../dom/DOMException.idl',
        '../dom/DOMImplementation.idl',
        '../dom/DOMParser.idl',
        '../dom/DOMRect.idl',
        '../dom/DOMRectList.idl',
        '../dom/DOMRectReadOnly.idl',
        '../dom/DOMStringMap.idl',
        '../dom/DOMTokenList.idl',
        '../dom/Element.idl',
        '../dom/Event.idl',
        '../dom/EventListener.idl',
        '../dom/EventTarget.idl',
        '../dom/Float32Array.idl',
        '../dom/Float64Array.idl',
        '../dom/FocusEvent.idl',
        '../dom/History.idl',
        '../dom/HTMLAnchorElement.idl',
        '../dom/HTMLBodyElement.idl',
        '../dom/HTMLBRElement.idl',
        '../dom/HTMLCollection.idl',
        '../dom/HTMLDivElement.idl',
        '../dom/HTMLElement.idl',
        '../dom/HTMLHeadElement.idl',
        '../dom/HTMLHeadingElement.idl',
        '../dom/HTMLHtmlElement.idl',
        '../dom/HTMLImageElement.idl',
        '../dom/HTMLLinkElement.idl',
        '../dom/HTMLMediaElement.idl',
        '../dom/HTMLMetaElement.idl',
        '../dom/HTMLParagraphElement.idl',
        '../dom/HTMLScriptElement.idl',
        '../dom/HTMLSpanElement.idl',
        '../dom/HTMLStyleElement.idl',
        '../dom/HTMLTitleElement.idl',
        '../dom/HTMLUnknownElement.idl',
        '../dom/HTMLVideoElement.idl',
        '../dom/KeyboardEvent.idl',
        '../dom/Location.idl',
        '../dom/MediaError.idl',
        '../dom/MediaKeyCompleteEvent.idl',
        '../dom/MediaKeyError.idl',
        '../dom/MediaKeyErrorEvent.idl',
        '../dom/MediaKeyMessageEvent.idl',
        '../dom/MediaKeyNeededEvent.idl',
        '../dom/MediaQueryList.idl',
        '../dom/MediaSource.idl',
        '../dom/MemoryInfo.idl',
        '../dom/MimeTypeArray.idl',
        '../dom/NamedNodeMap.idl',
        '../dom/Navigator.idl',
        '../dom/Node.idl',
        '../dom/NodeList.idl',
        '../dom/Performance.idl',
        '../dom/PerformanceTiming.idl',
        '../dom/PluginArray.idl',
        '../dom/ProgressEvent.idl',
        '../dom/Screen.idl',
        '../dom/SecurityPolicyViolationEvent.idl',
        '../dom/SourceBuffer.idl',
        '../dom/SourceBufferList.idl',
        '../dom/Storage.idl',
        '../dom/StorageEvent.idl',
        '../dom/TestRunner.idl',
        '../dom/Text.idl',
        '../dom/TimeRanges.idl',
        '../dom/TransitionEvent.idl',
        '../dom/UIEvent.idl',
        '../dom/Uint16Array.idl',
        '../dom/Uint32Array.idl',
        '../dom/Uint8Array.idl',
        '../dom/URL.idl',
        '../dom/VideoPlaybackQuality.idl',
        '../dom/Window.idl',
        '../dom/XMLDocument.idl',
        '../dom/XMLSerializer.idl',

        '../h5vcc/dial/DialHttpRequest.idl',
        '../h5vcc/dial/DialHttpResponse.idl',
        '../h5vcc/dial/DialServer.idl',
        '../h5vcc/H5vcc.idl',
        '../h5vcc/H5vccAccountInfo.idl',
        '../h5vcc/H5vccAccountManager.idl',
        '../h5vcc/H5vccAudioConfig.idl',
        '../h5vcc/H5vccAudioConfigArray.idl',
        '../h5vcc/H5vccCVal.idl',
        '../h5vcc/H5vccCValKeyList.idl',
        '../h5vcc/H5vccDeepLinkEventTarget.idl',
        '../h5vcc/H5vccRuntime.idl',
        '../h5vcc/H5vccRuntimeEventTarget.idl',
        '../h5vcc/H5vccSettings.idl',
        '../h5vcc/H5vccStorage.idl',
        '../h5vcc/H5vccSystem.idl',
        '../h5vcc/H5vccTraceEvent.idl',

        '../speech/SpeechRecognition.idl',
        '../speech/SpeechRecognitionAlternative.idl',
        '../speech/SpeechRecognitionError.idl',
        '../speech/SpeechRecognitionEvent.idl',
        '../speech/SpeechRecognitionResult.idl',
        '../speech/SpeechRecognitionResultList.idl',

        '../web_animations/Animatable.idl',
        '../web_animations/Animation.idl',
        '../web_animations/AnimationEffectReadOnly.idl',
        '../web_animations/AnimationEffectTimingReadOnly.idl',
        '../web_animations/AnimationTimeline.idl',
        '../web_animations/Keyframe.idl',
        '../web_animations/KeyframeEffectReadOnly.idl',

        '../webdriver/ScriptExecutor.idl',
        '../webdriver/ScriptExecutorParams.idl',
        '../webdriver/ScriptExecutorResult.idl',

        '../websocket/WebSocket.idl',

        '../xhr/XMLHttpRequest.idl',
        '../xhr/XMLHttpRequestEventTarget.idl',
        '../xhr/XMLHttpRequestUpload.idl',
    ],

    # Partial interfaces and the right-side of "implements". Also includes
    # callback interfaces.
    # Code will not get generated for these interfaces; they are used to add
    # functionality to other interfaces.
    'dependency_idl_files': [
        '../cssom/LinkStyle.idl',

        '../dom/Document_CSSOM.idl',
        '../dom/Document_HTML5.idl',
        '../dom/Document_WebAnimationsAPI.idl',
        '../dom/Element_CSSOMView.idl',
        '../dom/Element_DOMParsingAndSerialization.idl',
        '../dom/ElementCSSInlineStyle.idl',
        '../dom/GlobalCrypto.idl',
        '../dom/GlobalEventHandlers.idl',
        '../dom/HTMLElement_CSSOMView.idl',
        '../dom/NavigatorID.idl',
        '../dom/NavigatorLanguage.idl',
        '../dom/NavigatorPlugins.idl',
        '../dom/NavigatorStorageUtils.idl',
        '../dom/NonDocumentTypeChildNode.idl',
        '../dom/NonElementParentNode.idl',
        '../dom/ParentNode.idl',
        '../dom/Performance_HighResolutionTime.idl',
        '../dom/URLUtils.idl',
        '../dom/Window_AnimationTiming.idl',
        '../dom/Window_CSSOM.idl',
        '../dom/Window_CSSOMView.idl',
        '../dom/Window_Performance.idl',
        '../dom/WindowEventHandlers.idl',
        '../dom/WindowLocalStorage.idl',
        '../dom/WindowSessionStorage.idl',
        '../dom/WindowTimers.idl',
    ],
  },
}
