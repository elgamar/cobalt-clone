// Copyright 2015 Google Inc. All Rights Reserved.
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

#ifndef COBALT_DOM_MEDIA_KEY_MESSAGE_EVENT_H_
#define COBALT_DOM_MEDIA_KEY_MESSAGE_EVENT_H_

#include <string>

#include "base/memory/ref_counted.h"
#include "cobalt/dom/event.h"
#include "cobalt/script/typed_arrays.h"
#include "cobalt/script/wrappable.h"

namespace cobalt {
namespace dom {

// The MediaKeyMessageEvent indicates that a message has been generated (and
// likely needs to be sent to a key server).
//   https://dvcs.w3.org/hg/html-media/raw-file/eme-v0.1b/encrypted-media/encrypted-media.html#dom-mediakeymessageevent
class MediaKeyMessageEvent : public Event {
 public:
  MediaKeyMessageEvent(const std::string& key_system,
                       const std::string& session_id,
                       const script::Handle<script::Uint8Array>& message,
                       const std::string& default_url);

  const std::string& key_system() const { return key_system_; }
  const std::string& session_id() const { return session_id_; }
  const script::Handle<script::Uint8Array> message() const {
    return script::Handle<script::Uint8Array>(message_reference_);
  }
  const std::string& default_url() const { return default_url_; }

  DEFINE_WRAPPABLE_TYPE(MediaKeyMessageEvent);

 private:
  std::string key_system_;
  std::string session_id_;
  std::string default_url_;
  script::ScriptValue<script::Uint8Array>::Reference message_reference_;
};

}  // namespace dom
}  // namespace cobalt

#endif  // COBALT_DOM_MEDIA_KEY_MESSAGE_EVENT_H_
