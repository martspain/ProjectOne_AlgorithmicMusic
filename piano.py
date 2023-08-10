from music import *

# Funcion para exportar la parte (instrumento) que nos toca
def getDrumPart():

  # TODO This is only for testing instrument individually. Delete after finishing part.
  score = Score("Drum Machine Pattern #1", 145.0)

  drumsPart = Part("Piano", 0, 1)
  bassDrumPhrase = Phrase(0.0) # Create phrase at beat 0.0

  bassDrumPhrase.setInstrument(OVERDRIVEN_GUITAR)
  bassDrumPhrase.setTempo(123)

  # Intro 20 4
  bassPitches   = [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST]
  bassDurations = [QN, EN, EN, HN, QN, EN, EN, EN, DHN] # 20 WN

  # Verse1 16 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2 # 16 wn

  # Coro 16 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2

  # Bridge PT1 8 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2

  # Bridge PT2 16 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2

  # Break 8 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2

  # Chorus 16 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2

  # Bridge PT1 8 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2

  # Bridge PT2 16 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2

  # Chorus 16 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2

  # Final Chorus 9 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2

  # Silence 2 4
  bassPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  bassDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2
  

  bassDrumPhrase.addNoteList(bassPitches, bassDurations)
  drumsPart.addPhrase(bassDrumPhrase)

  # TODO This is only for testing instrument individually. Delete after finishing part.
  score.addPart(drumsPart)
  Play.midi(score)

  return drumsPart