from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
try:
    from mycroft.skills.audioservice import AudioService
except:
    from mycroft.util import play_mp3
    AudioService = None
from bs4 import BeautifulSoup
import requests


__author__ = 'domcross'

LOGGER = getLogger(__name__)


EINSLIVE_URL = 'http://wdr-1live-live.icecast.wdr.de/wdr/1live/live/mp3/128/stream.mp3'
EINSLIVE_DIGGI_URL = 'http://wdr-1live-diggi.icecast.wdr.de/wdr/1live/diggi/mp3/128/stream.mp3'
EINSLIVE_PLAN_B_URL = 'http://wdr-1live-planb.icecast.wdr.de/wdr/1live/planb/mp3/128/stream.mp3'
EINSLIVE_DJ_SESSION_URL = 'http://wdr-1live-djsession.icecast.wdr.de/wdr/1live/djsession/mp3/128/stream.mp3'
EINSLIVE_NEU_URL = 'http://wdr-1live-neufuerdensektor.icecast.wdr.de/wdr/1live/neufuerdensektor/mp3/128/stream.mp3'
EINSLIVE_SPECIAL_URL = 'http://wdr-1live-specials.icecast.wdr.de/wdr/1live/specials/mp3/128/stream.mp3'
EINSLIVE_HIPHOP_URL = 'http://wdr-1live-hiphop.icecast.wdr.de/wdr/1live/hiphop/mp3/128/stream.mp3'

class EinsliveSkill(MycroftSkill):
    def __init__(self):
        super(EinsliveSkill, self).__init__(name="EinsliveSkill")
        self.audioservice = None

    def initialize(self):
        if AudioService:
            self.audioservice = AudioService(self.emitter)

        whatson_einslive_intent = IntentBuilder("WhatsonEinsliveIntent").\
                         require("WhatsonKeyword").\
                         require("EinsliveKeyword").build()
        self.register_intent(whatson_einslive_intent, self.handle_whatson_einslive_intent)

        einslive_intent = IntentBuilder("EinsliveIntent").\
                     require("EinsliveKeyword").require("PlayKeyword").build()
        self.register_intent(einslive_intent, self.handle_einslive_intent)

        einslive_diggi_intent = IntentBuilder("EinsliveDiggiIntent").\
                     require("EinsliveDiggiKeyword").require("PlayKeyword").build()
        self.register_intent(einslive_diggi_intent, self.handle_einslive_diggi_intent)

        einslive_planb_intent = IntentBuilder("EinslivePlanbIntent").\
                     require("EinslivePlanbKeyword").require("PlayKeyword").build()
        self.register_intent(einslive_planb_intent, self.handle_einslive_planb_intent)

        einslive_dj_intent = IntentBuilder("EinsliveDjIntent").\
                     require("EinsliveDjKeyword").require("PlayDjKeyword").build()
        self.register_intent(einslive_dj_intent, self.handle_einslive_dj_intent)

        einslive_neu_intent = IntentBuilder("EinsliveNeuIntent").\
                     require("EinsliveNeuKeyword").require("PlayKeyword").build()
        self.register_intent(einslive_neu_intent, self.handle_einslive_neu_intent)

        einslive_special_intent = IntentBuilder("EinsliveSpecialIntent").\
                     require("EinsliveSpecialKeyword").require("PlayKeyword").build()
        self.register_intent(einslive_special_intent, self.handle_einslive_special_intent)

        einslive_hiphop_intent = IntentBuilder("EinsliveHiphopIntent").\
                     require("EinsliveHiphopKeyword").require("PlayKeyword").build()
        self.register_intent(einslive_hiphop_intent, self.handle_einslive_hiphop_intent)

    def handle_whatson_einslive_intent(self, message):
        r = requests.get('http://www1.wdr.de/radio/1live/index.html')
        soup = BeautifulSoup(r.text)
        for el in soup.find_all(span='wdrCurrentShowTitleTitle'):
                self.speak_dialog("currently",
                                  { "station": "einslive", "title": el.string})

    def handle_einslive_intent(self, message):
        if self.audioservice:
            self.audioservice.play(EINSLIVE_URL, message.data['utterance'])
        else:
            self.process = play_mp3(EINSLIVE_URL)

    def handle_einslive_diggi_intent(self, message):
        if self.audioservice:
            self.audioservice.play(EINSLIVE_DIGGI_URL, message.data['utterance'])
        else:
            self.process = play_mp3(EINSLIVE_DIGGI_URL)

    def handle_einslive_planb_intent(self, message):
        if self.audioservice:
            self.audioservice.play(EINSLIVE_PLAN_B_URL, message.data['utterance'])
        else:
            self.process = play_mp3(EINSLIVE_PLAN_B_URL)

    def handle_einslive_dj_intent(self, message):
        if self.audioservice:
            self.audioservice.play(EINSLIVE_DJ_SESSION_URL, message.data['utterance'])
        else:
            self.process = play_mp3(EINSLIVE_DJ_SESSION_URL)

    def handle_einslive_neu_intent(self, message):
        if self.audioservice:
            self.audioservice.play(EINSLIVE_NEU_URL, message.data['utterance'])
        else:
            self.process = play_mp3(EINSLIVE_NEU_URL)

    def handle_einslive_special_intent(self, message):
        if self.audioservice:
            self.audioservice.play(EINSLIVE_SPECIAL_URL, message.data['utterance'])
        else:
            self.process = play_mp3(EINSLIVE_SPECIAL_URL)

    def handle_einslive_hiphop_intent(self, message):
        if self.audioservice:
            self.audioservice.play(EINSLIVE_HIPHOP_URL, message.data['utterance'])
        else:
            self.process = play_mp3(EINSLIVE_HIPHOP_URL)


    def stop(self):
        pass


def create_skill():
    return EinsliveSkill()
