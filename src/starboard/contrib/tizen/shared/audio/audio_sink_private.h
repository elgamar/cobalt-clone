// Copyright (c) 2016 The Cobalt Authors Co., Ltd All Rights Reserved
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef STARBOARD_CONTRIB_TIZEN_SHARED_AUDIO_AUDIO_SINK_PRIVATE_H_
#define STARBOARD_CONTRIB_TIZEN_SHARED_AUDIO_AUDIO_SINK_PRIVATE_H_

#include <audio_io.h>

#include "starboard/audio_sink.h"
#include "starboard/mutex.h"
#include "starboard/thread.h"
#include "starboard/time.h"

// starboard object
struct SbAudioSinkPrivate {
 public:
  SbAudioSinkPrivate(
      int channels,
      int sampling_frequency_hz,
      SbMediaAudioSampleType audio_sample_type,
      SbMediaAudioFrameStorageType audio_frame_storage_type,
      SbAudioSinkFrameBuffers frame_buffers,
      int frames_per_channel,
      SbAudioSinkUpdateSourceStatusFunc update_source_status_func,
      SbAudioSinkConsumeFramesFunc consume_frames_func,
      void* context);
  virtual ~SbAudioSinkPrivate();

  bool IsValid();

  // callbacks
  static void* AudioSinkThreadProc_CB(void* context);

 private:
  const char* GetCAPIErrorString(int capi_ret);

  void* AudioSinkThreadProc();
  void ResetWaitPlay();
  void WaitPlay(int consumed_frames);

  // setting of creation
  int channels_;
  int sampling_frequency_hz_;
  SbMediaAudioSampleType audio_sample_type_;
  SbMediaAudioFrameStorageType audio_frame_storage_type_;
  SbAudioSinkFrameBuffers frame_buffers_;
  int frames_per_channel_;
  SbAudioSinkUpdateSourceStatusFunc update_source_status_func_;
  SbAudioSinkConsumeFramesFunc consume_frames_func_;
  void* context_;

  // thread related
  ::starboard::Mutex mutex_;
  bool destroying_;
  SbThread audio_out_thread_;
  int send_frames_;
  SbTimeMonotonic send_start_;

  // capi related
  audio_out_h capi_audio_out_;
  bool is_paused_;
};

#endif  // STARBOARD_CONTRIB_TIZEN_SHARED_AUDIO_AUDIO_SINK_PRIVATE_H_
