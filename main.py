__author__ = 'bmartins'
# -*- coding: utf-8 -*-

import ispeech_api
import sys

from subprocess import call

f = open("input_text")
input_text = f.read()

input_text = unicode(input_text, "utf-8")
audio_file = ispeech_api.fetch_audio_for_text(input_text, "ukenglishfemale")

if sys.platform == 'linux2':
    call(["xdg-open", audio_file])
elif sys.platform == 'darwin':
    call(["afplay", audio_file])