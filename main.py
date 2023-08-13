from music import *
from piano import *

# BPM 123 4/4

score = Score("Drum Machine Pattern #1", 123.0)

drumsPart = Part("Drums", 0, 9)

bassDrumPhrase = Phrase(0.0)

bassPitches   = [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2 + [CLP, REST, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, CLP, REST, REST, REST]
bassDurations = [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2 + [QN, QN, HN, HN, HN, HN, QN, QN, QN, QN, EN, EN, EN, EN, SN, SN, SN, SN, SN, SN, SN, SN, WN, WN, WN]
bassDrumPhrase.addNoteList(bassPitches, bassDurations)

drumsPart.addPhrase(bassDrumPhrase)

score.addPart(drumsPart)

Play.midi(score)