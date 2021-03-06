# Copyright 2014 The Cobalt Authors. All Rights Reserved.
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
  'variables': {
    # This platform uses a compositor to present the rendering output, so
    # set the swap interval to update the buffer immediately. That buffer
    # will then be presented by the compositor on its own time.
    'cobalt_egl_swap_interval': 0,

    # Hook into the swap buffers call to facilitate synchronization of the
    # OpenGL output with the punch-through video layer.
    'linker_flags': [
      '-Wl,--wrap=eglSwapBuffers',
    ],

    'platform_libraries': [
      '-lEGL',
      '-lGLESv2',
      '-lX11',
      '-lXcomposite',
      '-lXext',
      '-lXrender',
    ],
  },
}
