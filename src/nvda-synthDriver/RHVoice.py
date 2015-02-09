# -*- coding: utf-8 -*-
# Copyright (C) 2010, 2011, 2012, 2013  Olga Yakovleva <yakovleva.o.v@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

from ctypes import CFUNCTYPE, POINTER, Structure, c_char_p, c_double
from ctypes import c_int, c_uint, c_short, c_void_p


# --- bindings ---

class RHVoice_tts_engine_struct(Structure):
    pass
RHVoice_tts_engine=POINTER(RHVoice_tts_engine_struct)

class RHVoice_message_struct(Structure):
    pass
RHVoice_message=POINTER(RHVoice_message_struct)


class RHVoice_callback_types:
    play_speech=CFUNCTYPE(c_int,POINTER(c_short),c_uint,c_void_p)
    process_mark=CFUNCTYPE(c_int,c_char_p,c_void_p)
    word_starts=CFUNCTYPE(c_int,c_uint,c_uint,c_void_p)
    word_ends=CFUNCTYPE(c_int,c_uint,c_uint,c_void_p)
    sentence_starts=CFUNCTYPE(c_int,c_uint,c_uint,c_void_p)
    sentence_ends=CFUNCTYPE(c_int,c_uint,c_uint,c_void_p)
    play_audio=CFUNCTYPE(c_int,c_char_p,c_void_p)

class RHVoice_callbacks(Structure):
    _fields_=[("play_speech",RHVoice_callback_types.play_speech),
              ("process_mark",RHVoice_callback_types.process_mark),
              ("word_starts",RHVoice_callback_types.word_starts),
              ("word_ends",RHVoice_callback_types.word_ends),
              ("sentence_starts",RHVoice_callback_types.sentence_starts),
              ("sentence_ends",RHVoice_callback_types.sentence_ends),
              ("play_audio",RHVoice_callback_types.play_audio)]

class RHVoice_init_params(Structure):
    _fields_=[("data_path",c_char_p),
              ("config_path",c_char_p),
              ("resource_paths",POINTER(c_char_p)),
              ("callbacks",RHVoice_callbacks),
              ("options",c_uint)]


class RHVoice_voice_info(Structure):
    _fields_=[("language",c_char_p),
              ("name",c_char_p),
              ("gender",c_int)]

class RHVoice_synth_params(Structure):
    _fields_=[("voice_profile",c_char_p),
              ("absolute_rate",c_double),
              ("absolute_pitch",c_double),
              ("absolute_volume",c_double),
              ("relative_rate",c_double),
              ("relative_pitch",c_double),
              ("relative_volume",c_double),
              ("punctuation_mode",c_int),
              ("punctuation_list",c_char_p),
              ("capitals_mode",c_int)]

# --- main code ---

module_dir=os.path.dirname(__file__.decode(sys.getfilesystemencoding()))
RHVoice_lib_path=os.path.join(module_dir,"RHVoice.dll")
