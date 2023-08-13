from music import *

# Funcion para exportar la parte (instrumento) que nos toca
def getDrumPart():

  # TODO This is only for testing instrument individually. Delete after finishing part.
  score = Score("Drum Machine Pattern #1", 123.0)
  # -------------------------------------------------------------------------------- #

  drumsPart = Part("Drums", 0, 9)
  stickDrumPhrase = Phrase(0.0) # Create phrase at beat 0.0
  snareDrumPhrase = Phrase(0.0)
  cymbalDrumPhrase = Phrase(0.0)
  bassDrumPhrase = Phrase(0.0)

  # Intro 12 4
  stickPitches   = [LMT] * 96
  stickDurations = [EN] * 96 # 12 WN
  
  snarePitches = [REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, SNR] * 6
  snareDurations = [QN, QN, QN, EN, EN, QN, QN, EN, EN, EN, EN] * 6

  cymbalPitches = ([CC1] + [REST] * 3 + [REST] * 3) * 3
  cymbalDurations = ([QN] + [WN] * 3 + [QN] * 3) * 3

  bassPitches = [BDR] * 48
  bassDurations = [QN] * 48

  # Verse1 16 4
  stickPitches   += [LMT] * 128
  stickDurations += [EN] * 128 # 16 wn
  
  snarePitches += [REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, SNR] * 4
  snareDurations += [QN, QN, QN, EN, EN, QN, QN, QN, EN, EN, QN, QN, QN, EN, EN, QN, QN, EN, EN, EN, EN] * 4

  cymbalPitches += ([CC1] + [REST] * 7 + [REST] * 3) * 2
  cymbalDurations += ([QN] + [WN] * 7 + [QN] * 3) * 2

  bassPitches += [BDR] * 64
  bassDurations += [QN] * 64

  # Coro 16 4
  stickPitches   += [LMT] * 128
  stickDurations += [EN] * 128

  snarePitches += [REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, SNR] * 4 + [REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, SNR] * 2
  snareDurations += [QN, QN, QN, EN, EN, QN, QN, EN, EN, EN, EN] * 4 + [QN, QN, QN, EN, EN, QN, QN, QN, EN, EN, QN, QN, QN, EN, EN, QN, QN, EN, EN, EN, EN] * 2

  cymbalPitches += ([CC1] + [REST] * 3 + [REST] * 3) * 2 + ([CC1] + [REST] * 7 + [REST] * 3)
  cymbalDurations += ([QN] + [WN] * 3 + [QN] * 3) * 2 + ([QN] + [WN] * 7 + [QN] * 3)

  bassPitches += [BDR] * 64
  bassDurations += [QN] * 64

  # Bridge PT1 8 4
  stickPitches   += [CHH, SNR] + [CC1, CHH, CHH, CHH] * 7 + [CHH, SNR, CC1]
  stickDurations += [EN, EN] + [QN, QN, QN, QN] * 7 + [QN, QN, QN]
  
  snarePitches += [SNR, SNR] + [SNR] * 31
  snareDurations += [EN, EN] + [QN] * 31

  cymbalPitches += [REST] * 8
  cymbalDurations += [WN] * 8

  bassPitches += [REST] + [BDR] * 30 + [REST]
  bassDurations += [DQN] + [QN] * 30 + [EN]

  # Bridge PT2 16 4
  stickPitches   += [CHH] * 63 + [RBL] + [LMT] * 64
  stickDurations += [EN] * 63 + [EN] + [EN] * 64

  snarePitches += [REST] * 8 + [SNR] * 64
  snareDurations += [WN] * 8 + [EN] * 64

  cymbalPitches += [REST] * 16
  cymbalDurations += [WN] * 16
  
  bassPitches += [REST] * 16
  bassDurations += [WN] * 16

  # Break 4 4
  stickPitches   += [LMT] * 32
  stickDurations += [EN] * 32
  
  snarePitches += [REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, SNR] * 2
  snareDurations += [QN, QN, QN, EN, EN, QN, QN, EN, EN, EN, EN] * 2

  cymbalPitches += ([CC1] + [REST] * 3 + [REST] * 3) * 1
  cymbalDurations += ([QN] + [WN] * 3 + [QN] * 3) * 1

  bassPitches += [BDR] * 16
  bassDurations += [QN] * 16

  # Chorus 16 4
  stickPitches   += [LMT] * 128
  stickDurations += [EN] * 128

  snarePitches += [REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, SNR] * 4 + [REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, SNR] * 2
  snareDurations += [QN, QN, QN, EN, EN, QN, QN, EN, EN, EN, EN] * 4 + [QN, QN, QN, EN, EN, QN, QN, QN, EN, EN, QN, QN, QN, EN, EN, QN, QN, EN, EN, EN, EN] * 2

  cymbalPitches += ([CC1] + [REST] * 3 + [REST] * 3) * 2 + ([CC1] + [REST] * 7 + [REST] * 3)
  cymbalDurations += ([QN] + [WN] * 3 + [QN] * 3) * 2 + ([QN] + [WN] * 7 + [QN] * 3)

  bassPitches += [BDR] * 64
  bassDurations += [QN] * 64

  # Bridge PT1 8 4
  stickPitches   += [CHH, SNR] + [CC1, CHH, CHH, CHH] * 7 + [CHH, SNR, CC1]
  stickDurations += [EN, EN] + [QN, QN, QN, QN] * 7 + [QN, QN, QN]
  
  snarePitches += [SNR, SNR] + [SNR] * 31
  snareDurations += [EN, EN] + [QN] * 31

  cymbalPitches += [REST] * 8
  cymbalDurations += [WN] * 8

  bassPitches += [REST] + [BDR] * 30 + [REST]
  bassDurations += [DQN] + [QN] * 30 + [EN]

  # Bridge PT2 16 4
  stickPitches   += [CHH, SNR] + [CC1, CHH, CHH, CHH] * 6 + [CHH, SNR, CC1] + [REST] + [REST] * 15 + [REST, CHH, CHH, CC1]
  stickDurations += [EN, EN] + [QN, QN, QN, QN] * 6 + [QN, QN, QN] + [WN] + [HN] * 15 + [EN, EN, EN, EN]
  
  snarePitches += [SNR, SNR] + [SNR] * 27 + [SNR] * 16 + [CC2, REST, SNR] + [REST, SNR] * 7 + [REST, CC2] + [REST, SNR] * 6 + [REST, SNR, SNR, SNR]
  snareDurations += [EN, EN] + [QN] * 27 + [SN] * 16 + [EN, QN, EN] + [DQN, EN] * 7 + [DQN, EN] + [DQN, EN] * 6 + [EN, EN, EN, EN]

  cymbalPitches += [REST] * 8 + [CC1] + [CC1] * 28 + [REST, REST]
  cymbalDurations += [WN] * 8 + [EN] + [QN] * 28 + [DQN, HN]

  bassPitches += [REST] + [BDR] * 26 + [REST] + [REST] + [BDR, BDR, BDR, REST] * 16
  bassDurations += [DQN] + [QN] * 26 + [EN] + [WN] + [EN, EN, EN, EN] * 16

  # Chorus 8 4
  stickPitches   += [LMT] * 62 + [CC2]
  stickDurations += [EN] * 62 + [QN]

  snarePitches += [REST, SNR, REST, SNR, SNR, REST, SNR, REST, SNR, SNR, SNR] * 4
  snareDurations += [QN, QN, QN, EN, EN, QN, QN, EN, EN, EN, EN] * 4

  cymbalPitches += ([CC1] + [REST] * 3 + [REST] * 3) + [CC1] + [REST] * 3 + [REST] * 2 + [CC1]
  cymbalDurations += ([QN] + [WN] * 3 + [QN] * 3) + [QN] + [WN] * 3 + [QN] * 2 + [QN]

  bassPitches += [BDR] * 32
  bassDurations += [QN] * 32

  # # Final Chorus 9 4
  # stickPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  # stickDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2

  # # Silence 2 4
  # stickPitches   += [CLP, CLP, CLP, REST, REST, CLP, CLP, CLP, REST] * 2
  # stickDurations += [QN, EN, EN, HN, QN, EN, EN, EN, DHN] * 2
  

  stickDrumPhrase.addNoteList(stickPitches, stickDurations)
  Mod.crescendo(stickDrumPhrase, 240, 272, 10, 100)
  drumsPart.addPhrase(stickDrumPhrase)
  
  snareDrumPhrase.addNoteList(snarePitches, snareDurations)
  Mod.crescendo(snareDrumPhrase, 240, 272, 10, 100)
  drumsPart.addPhrase(snareDrumPhrase)
  
  cymbalDrumPhrase.addNoteList(cymbalPitches, cymbalDurations)
  drumsPart.addPhrase(cymbalDrumPhrase)

  bassDrumPhrase.addNoteList(bassPitches, bassDurations)
  drumsPart.addPhrase(bassDrumPhrase)

  # TODO This is only for testing instrument individually. Delete after finishing part.
  score.addPart(drumsPart)
  Write.midi(score, "Drum.mid")
  Play.midi(score)
  # -------------------------------------------------------------------------------- #

  return drumsPart

getDrumPart()