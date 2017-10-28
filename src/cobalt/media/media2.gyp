# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'media2',
      'type': '<(component)',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/ui/ui.gyp:ui',
      ],
      'cflags_cc': [
        '-Wno-conversion',
        '-Wno-unused-parameter',
        '-Wno-unused-variable',
      ],
      'defines': [
        'MEDIA_IMPLEMENTATION',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'decoder_buffer_allocator.cc',
        'decoder_buffer_allocator.h',
        'fetcher_buffered_data_source.cc',
        'fetcher_buffered_data_source.h',
        'media_module.cc',
        'media_module.h',
        'media_module_starboard.cc',

        'base/audio_codecs.cc',
        'base/audio_codecs.h',
        'base/audio_decoder_config.cc',
        'base/audio_decoder_config.h',
        'base/audio_timestamp_helper.cc',
        'base/audio_timestamp_helper.h',
        'base/bit_reader.cc',
        'base/bit_reader.h',
        'base/bit_reader_core.cc',
        'base/bit_reader_core.h',
        'base/byte_queue.cc',
        'base/byte_queue.h',
        'base/channel_layout.cc',
        'base/channel_layout.h',
        'base/color_space.cc',
        'base/color_space.h',
        'base/data_source.cc',
        'base/data_source.h',
        'base/decoder_buffer.cc',
        'base/decoder_buffer.h',
        'base/decoder_buffer_cache.cc',
        'base/decoder_buffer_cache.h',
        'base/decrypt_config.cc',
        'base/decrypt_config.h',
        'base/demuxer.cc',
        'base/demuxer.h',
        'base/demuxer_stream.cc',
        'base/demuxer_stream.h',
        'base/demuxer_stream_provider.cc',
        'base/demuxer_stream_provider.h',
        'base/drm_system.cc',
        'base/drm_system.h',
        'base/encryption_scheme.cc',
        'base/encryption_scheme.h',
        'base/hdr_metadata.cc',
        'base/hdr_metadata.h',
        'base/media_log.cc',
        'base/media_log.h',
        'base/media_track.cc',
        'base/media_track.h',
        'base/media_tracks.cc',
        'base/media_tracks.h',
        'base/media_util.cc',
        'base/media_util.h',
        'base/mime_util.cc',
        'base/mime_util.h',
        'base/mime_util_internal.cc',
        'base/mime_util_internal.h',
        'base/ranges.cc',
        'base/ranges.h',
        'base/sample_format.cc',
        'base/sample_format.h',
        'base/sbplayer_pipeline.cc',
        'base/sbplayer_set_bounds_helper.cc',
        'base/sbplayer_set_bounds_helper.h',
        'base/shell_audio_bus.cc',
        'base/shell_audio_bus.h',
        'base/shell_data_source_reader.cc',
        'base/shell_data_source_reader.h',
        'base/shell_media_platform.cc',
        'base/shell_media_platform.h',
        'base/starboard_player.cc',
        'base/starboard_player.h',
        'base/starboard_utils.cc',
        'base/starboard_utils.h',
        'base/stream_parser.cc',
        'base/stream_parser.h',
        'base/stream_parser_buffer.cc',
        'base/stream_parser_buffer.h',
        'base/text_track_config.cc',
        'base/text_track_config.h',
        'base/video_codecs.cc',
        'base/video_codecs.h',
        'base/video_decoder_config.cc',
        'base/video_decoder_config.h',
        'base/video_util.cc',
        'base/video_util.h',
        'filters/chunk_demuxer.cc',
        'filters/chunk_demuxer.h',
        'filters/frame_processor.cc',
        'filters/frame_processor.h',
        'filters/h264_bit_reader.cc',
        'filters/h264_bit_reader.h',
        'filters/h264_bitstream_buffer.cc',
        'filters/h264_bitstream_buffer.h',
        'filters/h264_parser.cc',
        'filters/h264_parser.h',
        'filters/h264_to_annex_b_bitstream_converter.cc',
        'filters/h264_to_annex_b_bitstream_converter.h',
        'filters/h265_parser.cc',
        'filters/h265_parser.h',
        'filters/shell_au.cc',
        'filters/shell_au.h',
        'filters/shell_avc_parser.cc',
        'filters/shell_avc_parser.h',
        'filters/shell_demuxer.cc',
        'filters/shell_demuxer.h',
        'filters/shell_mp4_map.cc',
        'filters/shell_mp4_map.h',
        'filters/shell_mp4_parser.cc',
        'filters/shell_mp4_parser.h',
        'filters/shell_parser.cc',
        'filters/shell_parser.h',
        'filters/shell_rbsp_stream.cc',
        'filters/shell_rbsp_stream.h',
        'filters/source_buffer_range.cc',
        'filters/source_buffer_range.h',
        'filters/source_buffer_state.cc',
        'filters/source_buffer_state.h',
        'filters/source_buffer_stream.cc',
        'filters/source_buffer_stream.h',
        'filters/stream_parser_factory.cc',
        'filters/stream_parser_factory.h',
        'formats/common/offset_byte_queue.cc',
        'formats/common/offset_byte_queue.h',
        'formats/mp4/aac.cc',
        'formats/mp4/aac.h',
        'formats/mp4/avc.cc',
        'formats/mp4/avc.h',
        'formats/mp4/bitstream_converter.cc',
        'formats/mp4/bitstream_converter.h',
        'formats/mp4/box_definitions.cc',
        'formats/mp4/box_definitions.h',
        'formats/mp4/box_reader.cc',
        'formats/mp4/box_reader.h',
        'formats/mp4/es_descriptor.cc',
        'formats/mp4/es_descriptor.h',
        'formats/mp4/fourccs.h',
        'formats/mp4/hevc.cc',
        'formats/mp4/hevc.h',
        'formats/mp4/mp4_stream_parser.cc',
        'formats/mp4/mp4_stream_parser.h',
        'formats/mp4/rcheck.h',
        'formats/mp4/sample_to_group_iterator.cc',
        'formats/mp4/sample_to_group_iterator.h',
        'formats/mp4/track_run_iterator.cc',
        'formats/mp4/track_run_iterator.h',
        'formats/mpeg/adts_constants.cc',
        'formats/mpeg/adts_constants.h',
        'formats/mpeg/adts_stream_parser.cc',
        'formats/mpeg/adts_stream_parser.h',
        'formats/mpeg/mpeg1_audio_stream_parser.cc',
        'formats/mpeg/mpeg1_audio_stream_parser.h',
        'formats/mpeg/mpeg_audio_stream_parser_base.cc',
        'formats/mpeg/mpeg_audio_stream_parser_base.h',
        'formats/webm/cluster_builder.cc',
        'formats/webm/cluster_builder.h',
        'formats/webm/opus_packet_builder.cc',
        'formats/webm/opus_packet_builder.h',
        'formats/webm/tracks_builder.cc',
        'formats/webm/tracks_builder.h',
        'formats/webm/webm_audio_client.cc',
        'formats/webm/webm_audio_client.h',
        'formats/webm/webm_cluster_parser.cc',
        'formats/webm/webm_cluster_parser.h',
        'formats/webm/webm_colour_parser.cc',
        'formats/webm/webm_colour_parser.h',
        'formats/webm/webm_constants.cc',
        'formats/webm/webm_constants.h',
        'formats/webm/webm_content_encodings.cc',
        'formats/webm/webm_content_encodings.h',
        'formats/webm/webm_content_encodings_client.cc',
        'formats/webm/webm_content_encodings_client.h',
        'formats/webm/webm_crypto_helpers.cc',
        'formats/webm/webm_crypto_helpers.h',
        'formats/webm/webm_info_parser.cc',
        'formats/webm/webm_info_parser.h',
        'formats/webm/webm_parser.cc',
        'formats/webm/webm_parser.h',
        'formats/webm/webm_stream_parser.cc',
        'formats/webm/webm_stream_parser.h',
        'formats/webm/webm_tracks_parser.cc',
        'formats/webm/webm_tracks_parser.h',
        'formats/webm/webm_video_client.cc',
        'formats/webm/webm_video_client.h',
        'formats/webm/webm_webvtt_parser.cc',
        'formats/webm/webm_webvtt_parser.h',
        'player/buffered_data_source.h',
        'player/web_media_player_impl.cc',
        'player/web_media_player_impl.h',
        'player/web_media_player_proxy.cc',
        'player/web_media_player_proxy.h',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '..',
        ],
      },
      'dependencies': [
        '<(DEPTH)/googleurl/googleurl.gyp:googleurl',
        '<(DEPTH)/nb/nb.gyp:nb',
        '<(DEPTH)/starboard/starboard.gyp:starboard',
      ],
    },
    {
      # Rename 'media2_unittests' to 'media_unittests' once the original media
      # is removed.
      'target_name': 'media2_unittests',
      'type': '<(gtest_target_type)',
      'dependencies': [
        'media2',
        'media_test_support',
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/base/base.gyp:base_i18n',
        '<(DEPTH)/base/base.gyp:test_support_base',
        '<(DEPTH)/testing/gmock.gyp:gmock',
        '<(DEPTH)/testing/gtest.gyp:gtest',
        '<(DEPTH)/ui/ui.gyp:ui',
      ],
      'sources': [
        'base/audio_bus_unittest.cc',
        'base/audio_converter_unittest.cc',
        'base/audio_fifo_unittest.cc',
        'base/audio_pull_fifo_unittest.cc',
        'base/audio_renderer_mixer_input_unittest.cc',
        'base/audio_renderer_mixer_unittest.cc',
        'base/audio_splicer_unittest.cc',
        'base/audio_timestamp_helper_unittest.cc',
        'base/bit_reader_unittest.cc',
        'base/bind_to_loop_unittest.cc',
        'base/buffers_unittest.cc',
        'base/channel_mixer_unittest.cc',
        'base/clock_unittest.cc',
        'base/data_buffer_unittest.cc',
        'base/decoder_buffer_unittest.cc',
        'base/djb2_unittest.cc',
        'base/filter_collection_unittest.cc',
        'base/gmock_callback_support_unittest.cc',
        'base/pipeline_impl_unittest.cc',
        'base/ranges_unittest.cc',
        'base/run_all_unittests.cc',
        'base/seekable_buffer_unittest.cc',
        'base/shell_audio_bus_test.cc',
        'base/test_data_util.cc',
        'base/test_data_util.h',
        'base/vector_math_testing.h',
        'base/vector_math_unittest.cc',
        'base/video_frame_unittest.cc',
        'base/video_util_unittest.cc',
        'base/yuv_convert_unittest.cc',
        'filters/audio_decoder_selector_unittest.cc',
        'filters/audio_file_reader_unittest.cc',
        'filters/audio_renderer_algorithm_unittest.cc',
        'filters/audio_renderer_impl_unittest.cc',
        'filters/blocking_url_protocol_unittest.cc',
        'filters/chunk_demuxer_unittest.cc',
        'filters/decrypting_audio_decoder_unittest.cc',
        'filters/decrypting_demuxer_stream_unittest.cc',
        'filters/decrypting_video_decoder_unittest.cc',
        'filters/ffmpeg_audio_decoder_unittest.cc',
        'filters/ffmpeg_demuxer_unittest.cc',
        'filters/ffmpeg_glue_unittest.cc',
        'filters/ffmpeg_h264_to_annex_b_bitstream_converter_unittest.cc',
        'filters/ffmpeg_video_decoder_unittest.cc',
        'filters/file_data_source_unittest.cc',
        'filters/h264_to_annex_b_bitstream_converter_unittest.cc',
        'filters/pipeline_integration_test.cc',
        'filters/pipeline_integration_test_base.cc',
        'filters/skcanvas_video_renderer_unittest.cc',
        'filters/source_buffer_stream_unittest.cc',
        'filters/video_decoder_selector_unittest.cc',
        'filters/video_renderer_base_unittest.cc',
        'mp4/aac_unittest.cc',
        'mp4/avc_unittest.cc',
        'mp4/box_reader_unittest.cc',
        'mp4/es_descriptor_unittest.cc',
        'mp4/mp4_stream_parser_unittest.cc',
        'mp4/offset_byte_queue_unittest.cc',
        'mp4/track_run_iterator_unittest.cc',
        'video/capture/video_capture_device_unittest.cc',
        'webm/cluster_builder.cc',
        'webm/cluster_builder.h',
        'webm/webm_cluster_parser_unittest.cc',
        'webm/webm_content_encodings_client_unittest.cc',
        'webm/webm_parser_unittest.cc',
      ],
      'conditions': [
        ['OS == "lb_shell" or OS=="starboard"', {
          'sources': [
            'base/mock_shell_data_source_reader.h',
            'base/shell_buffer_factory_unittest.cc',
            'filters/shell_mp4_map_unittest.cc',
            'filters/shell_rbsp_stream_unittest.cc',
          ],
        }],
      ],
    },
    {
      'target_name': 'media_test_support',
      'type': 'static_library',
      'dependencies': [
        'media2',
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/testing/gmock.gyp:gmock',
        '<(DEPTH)/testing/gtest.gyp:gtest',
      ],
      'sources': [
        'base/gmock_callback_support.h',
        'base/mock_demuxer_host.cc',
        'base/mock_demuxer_host.h',
        'base/mock_filters.cc',
        'base/mock_filters.h',
        'base/test_helpers.cc',
        'base/test_helpers.h',
      ],
    },
    {
      # Rename 'media2_qt_faststart' to 'qt_faststart' once the original media
      # is removed.
      'target_name': 'media2_qt_faststart',
      'type': 'executable',
      'sources': [
        'tools/qt_faststart/qt_faststart.c'
      ],
    },
    {
      # Rename 'media2_seek_tester' to 'seek_tester' once the original media is
      # removed.
      'target_name': 'media2_seek_tester',
      'type': 'executable',
      'dependencies': [
        'media2',
        '<(DEPTH)/base/base.gyp:base',
      ],
      'sources': [
        'tools/seek_tester/seek_tester.cc',
      ],
    },
    {
      # Rename 'media2_demuxer_bench' to 'demuxer_bench' once the original media
      # is removed.
      'target_name': 'media2_demuxer_bench',
      'type': 'executable',
      'dependencies': [
        'media2',
        '<(DEPTH)/base/base.gyp:base',
      ],
      'sources': [
        'tools/demuxer_bench/demuxer_bench.cc',
      ],
    },
  ],
}
