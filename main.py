from music import *
# from piano import 
# from drumset import getDrumPart
# from overdrivenGuitar import getOverdrivenGuitarPart
# from fuzzBass import getBassPart

# BPM 123 4/4

def getDrumPart():

  # TODO This is only for testing instrument individually. Delete after finishing part.
  # score = Score("Drum Machine Pattern #1", 123.0)
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
  # score.addPart(drumsPart)
  # Write.midi(score, "Drum.mid")
  # Play.midi(score)
  # -------------------------------------------------------------------------------- #

  return drumsPart

def getBassPart():

  # TODO This is only for testing instrument individually. Delete after finishing part.
  # score = Score("Drum Machine Pattern #1", 145.0)

  bassPart = Part("Bass", 0, 3)
  bassDrumPhrase = Phrase(0.0) # Create phrase at beat 0.0
  
  bassDrumPhrase.setInstrument(BASS)
  bassDrumPhrase.setTempo(123)

  # Intro 20 4
  bassP1 = [B2, B2, B2, B2, B2, B2, B2, B2]
  bassD1 = [EN, EN, EN, EN, EN, EN, EN, EN]
  bassP2 = [B2, B2, B2, B2, B2, B2, B2, C3]
  bassP3 = [C3, C3, C3, C3, C3, B2, C3, F3]
  bassP4 = [G3, G3, G3, G3, G3, G3, G3, E3]
  bassP5 = [E3, E3, E3, E3, E3, D3, E3, F3]

  # Verse1 16 4
  # Conformada también por P4, P1 y P2 
  bassP6 = [C3, C3, C3, C3, C3, C3, C3, C3]
  bassP7 = [E3, E3, E3, E3, E3, E3, E3, E3]

  # Coro 16 4
  # Conformada también por P2, p6, p4, p7 

  # Bridge PT1 8 4
  bassP8 = [C3, C3, C3, C3, C3, C3, C3, F2]
  bassP9 = [F2, F2, F2, F2, F2, F2, F2, F2]
  bassP10= [D3, D3, D3, D3, D3, D3, D3, G2]
  bassP11= [G2, G2, G2, G2, G2, G2, G2, G2]
  bassP12= [A2, A2, A2, A2, A2, A2, A2, E2]
  bassP13= [E2, E2, E2, E2, E2, E2, E2, E2]
  bassP14= [A2, A2, A2, A2, A2, A2, A2, D3]
  bassP15= [D3, D3, D3, D3, D3, D3, D3, D3]

  # Bridge PT2 16 4
  # utiliza P11, P15, P7 
  bassP16= [B2, B2, B2, B2, A2, A2, A2, A2]
  
  # Intro 12 4
  bassDrumPhrase.addNoteList(bassP1, bassD1)
  bassDrumPhrase.addNoteList(bassP1, bassD1)
  bassDrumPhrase.addNoteList(bassP1, bassD1)
  bassDrumPhrase.addNoteList(bassP1, bassD1)
  bassDrumPhrase.addNoteList(bassP2, bassD1)
  bassDrumPhrase.addNoteList(bassP3, bassD1)
  bassDrumPhrase.addNoteList(bassP4, bassD1)
  bassDrumPhrase.addNoteList(bassP5, bassD1)
  bassDrumPhrase.addNoteList(bassP2, bassD1)
  bassDrumPhrase.addNoteList(bassP3, bassD1)
  bassDrumPhrase.addNoteList(bassP4, bassD1)
  bassDrumPhrase.addNoteList(bassP5, bassD1)

  # Verse1 16 4
  bassDrumPhrase.addNoteList(bassP2, bassD1)
  bassDrumPhrase.addNoteList(bassP6, bassD1)
  bassDrumPhrase.addNoteList(bassP4, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)
  bassDrumPhrase.addNoteList(bassP1, bassD1)
  bassDrumPhrase.addNoteList(bassP6, bassD1)
  bassDrumPhrase.addNoteList(bassP4, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)
  bassDrumPhrase.addNoteList(bassP2, bassD1)
  bassDrumPhrase.addNoteList(bassP6, bassD1)
  bassDrumPhrase.addNoteList(bassP4, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)
  bassDrumPhrase.addNoteList(bassP2, bassD1)
  bassDrumPhrase.addNoteList(bassP6, bassD1)
  bassDrumPhrase.addNoteList(bassP4, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)

  # Chorus 16 4
  bassDrumPhrase.addNoteList(bassP2, bassD1)
  bassDrumPhrase.addNoteList(bassP6, bassD1)
  bassDrumPhrase.addNoteList(bassP4, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)
  bassDrumPhrase.addNoteList(bassP2, bassD1)
  bassDrumPhrase.addNoteList(bassP6, bassD1)
  bassDrumPhrase.addNoteList(bassP4, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)
  bassDrumPhrase.addNoteList(bassP2, bassD1)
  bassDrumPhrase.addNoteList(bassP6, bassD1)
  bassDrumPhrase.addNoteList(bassP4, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)
  bassDrumPhrase.addNoteList(bassP2, bassD1)
  bassDrumPhrase.addNoteList(bassP6, bassD1)
  bassDrumPhrase.addNoteList(bassP4, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)

  # Bridge PT1 8 4
  bassDrumPhrase.addNoteList(bassP8, bassD1)
  bassDrumPhrase.addNoteList(bassP9, bassD1)
  bassDrumPhrase.addNoteList(bassP10, bassD1)
  bassDrumPhrase.addNoteList(bassP11, bassD1)
  bassDrumPhrase.addNoteList(bassP12, bassD1)
  bassDrumPhrase.addNoteList(bassP13, bassD1)
  bassDrumPhrase.addNoteList(bassP14, bassD1)
  bassDrumPhrase.addNoteList(bassP15, bassD1)

  # Bridge PT2 16 4
  bassDrumPhrase.addNoteList(bassP11, bassD1)
  bassDrumPhrase.addNoteList(bassP15, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)
  bassDrumPhrase.addNoteList(bassP16, bassD1)
  bassDrumPhrase.addNoteList(bassP11, bassD1)
  bassDrumPhrase.addNoteList(bassP15, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)
  bassDrumPhrase.addNoteList(bassP16, bassD1)
  bassDrumPhrase.addNoteList(bassP11, bassD1)
  bassDrumPhrase.addNoteList(bassP15, bassD1)
  bassDrumPhrase.addNoteList(bassP7, bassD1)
  #12, 13, 14, 15, 16
  
  # Break 4 4

  # bassDrumPhrase.addNoteList(bassPitches, bassDurations)
  bassPart.addPhrase(bassDrumPhrase)

  # TODO This is only for testing instrument individually. Delete after finishing part.
  # score.addPart(bassPart)
  # Play.midi(score)

  return bassPart

def getOverdrivenGuitarPart():

  # TODO This is only for testing instrument individually. Delete after finishing part.
  # score = Score("Drum Machine Pattern #1", 145.0)

  overDrivePart = Part("OverdrivenGuitar", 0, 2)
  OverGuitarPhrase1 = Phrase(0.0) # Create phrase at beat 0.0
  OverGuitarPhrase2 = Phrase(0.0) 
  OverGuitarPhrase3 = Phrase(0.0) 

  OverGuitarPhrase1.setInstrument(OVERDRIVEN_GUITAR)
  OverGuitarPhrase1.setTempo(123)
  OverGuitarPhrase2.setInstrument(OVERDRIVEN_GUITAR)
  OverGuitarPhrase2.setTempo(123)
  OverGuitarPhrase3.setInstrument(OVERDRIVEN_GUITAR)
  OverGuitarPhrase3.setTempo(123)

  # Intro 20 4
  overP1 = [REST, REST]*12
  overD1 = [HN, HN]*12

  # Verse1 16 4
  # Silencios
  overPS1 = [REST, REST]*16
  overDS1 = [HN, HN]*16

  # Coro 16 4
  overPS2 = [REST, REST]*8
  overDS2 = [HN, HN]*8
  #         #       #       #
  overP2 = [F5, B5, F5, B5, F5, E4]
  overD2 = [QN, QN, EN, EN, EN, EN]
  overP3 = [E4, B5, E4, B5, B5, E4, B5]
  overD3 = [EN, QN, EN, EN, EN, EN, EN]
  #                     #       #    #
  overP4 = [E4, B5, E4, D4, E4, D4, D4]
  overD4 = [QN, EN, EN, EN, EN, EN, EN]
  overP5 = [E4, B5, E4, E4, B5, E4, B5]
  overD5 = [EN, EN, EN, EN, EN, EN, QN]

  # Bridge PT1 8 4
  overP6 =   [G4, D4, D4, F5] #  #  .  .  #
  overD6 =   [DHN, SN, SN, EN]   #  3  , 0.25, 0.25, 0.5
  overP6_1 = [G5, A4, A4, C4] #  #  .  .  #
  overP6_2 = [C4, E4, E4, F4] #  #  .  .  #

  overP7 =   [F5, D4, D4]     #  #  .  .
  overD7 =   [3.5, SN, SN]       # 3.5 , 0.25, 0.25
  overP7_1 = [C4, A4, A4]     #  #  .  .
  overP7_2 = [F4, E4, E4]     #  #  .  .

  overP8 =   [G4, D4, D4, G4] # . . . #
  overP8_1 = [D4, A4, A4, D4] # # . . #
  overP8_2 = [A4, E4, E4, C4] # # . . #

  overP9 =   [G4, D4, D4]     # # . .
  overP9_1 = [D4, A4, A4]     # # . .
  overP9_2 = [C4, E4, E4]     # # . .

  overP10 = [A4, D4, D4, E5]
  overP10_1 = [E4, A4, A4, B4]
  overP10_2 = [A5, E4, E4, E4]

  overP11 = [E5, D4, D4]
  overP11_1 = [B4, A4, A4]
  overP11_2 = [E4, E4, E4]

  overP12 = [A4, D4, D4, G4]
  overP12_1 = [E4, A4, A4, D4]
  overP12_2 = [A5, E4, E4, A4]

  overP13 = [G4]
  overP13_1 = [D4] 
  overP13_2 = [A4]
  overD8 = [WN]

  # Bridge PT2 16 4
  overPS3 = [REST, REST]*14
  overDS3 = [HN, HN]*14
  overP14 = [B4, B4, B4, B4, B4, B4, B4, B4]
  overP14_1 = [F4, F4, F4, F4, F4, F4, F4, F4]
  overP14_2 = [REST, REST, REST, REST, REST, REST, REST, REST]
  overD9 = [EN, EN, EN, EN, EN, EN, EN, EN]

  # Break 8 4
  # silence


  # Intro (Silencios) 12
  OverGuitarPhrase1.addNoteList(overP1, overD1)
  # just to avoid phrase lag (they are silent)
  OverGuitarPhrase2.addNoteList(overP1, overD1)
  OverGuitarPhrase3.addNoteList(overP1, overD1)

  # Verse (Silencios) 16
  OverGuitarPhrase1.addNoteList(overPS1, overDS1) 
  # just to avoid phrase lag(they are silent)
  OverGuitarPhrase2.addNoteList(overPS1, overDS1)
  OverGuitarPhrase3.addNoteList(overPS1, overDS1)

  # Chorus 8 s, 8, = 16
  OverGuitarPhrase1.addNoteList(overPS2, overDS2) #8
  OverGuitarPhrase1.addNoteList(overP2, overD2)
  OverGuitarPhrase1.addNoteList(overP3, overD3)
  OverGuitarPhrase1.addNoteList(overP4, overD4)
  OverGuitarPhrase1.addNoteList(overP5, overD5)
  OverGuitarPhrase1.addNoteList(overP2, overD2)
  OverGuitarPhrase1.addNoteList(overP3, overD3)
  OverGuitarPhrase1.addNoteList(overP4, overD4)
  OverGuitarPhrase1.addNoteList(overP5, overD5)
  # just to avoid phrase lag(they are silent)
  OverGuitarPhrase2.addNoteList(overPS1, overDS1) #16
  OverGuitarPhrase3.addNoteList(overPS1, overDS1) #16

  # Bridge 8
  OverGuitarPhrase1.addNoteList(overP6, overD6)
  OverGuitarPhrase2.addNoteList(overP6_1, overD6)
  OverGuitarPhrase3.addNoteList(overP6_2, overD6)

  OverGuitarPhrase1.addNoteList(overP7, overD7)
  OverGuitarPhrase2.addNoteList(overP7_1, overD7)
  OverGuitarPhrase3.addNoteList(overP7_2, overD7)

  OverGuitarPhrase1.addNoteList(overP8, overD6)
  OverGuitarPhrase2.addNoteList(overP8_1, overD6)
  OverGuitarPhrase3.addNoteList(overP8_2, overD6)

  OverGuitarPhrase1.addNoteList(overP9, overD7)
  OverGuitarPhrase2.addNoteList(overP9_1, overD7)
  OverGuitarPhrase3.addNoteList(overP9_2, overD7)

  OverGuitarPhrase1.addNoteList(overP10, overD6)
  OverGuitarPhrase2.addNoteList(overP10_1, overD6)
  OverGuitarPhrase3.addNoteList(overP10_2, overD6)

  OverGuitarPhrase1.addNoteList(overP11, overD7)
  OverGuitarPhrase2.addNoteList(overP11_1, overD7)
  OverGuitarPhrase3.addNoteList(overP11_2, overD7)

  OverGuitarPhrase1.addNoteList(overP12, overD6)
  OverGuitarPhrase2.addNoteList(overP12_1, overD6)
  OverGuitarPhrase3.addNoteList(overP12_2, overD6)

  OverGuitarPhrase1.addNoteList(overP13, overD8)
  OverGuitarPhrase2.addNoteList(overP13_1, overD8)
  OverGuitarPhrase3.addNoteList(overP13_2, overD8)

  # Bridge 2, 25 s , 2 =27 | se supone que es 16 aca pero en la que tengo marca 27
  OverGuitarPhrase1.addNoteList(overPS3, overDS3) 
  # just to avoid phrase lag (they are silent)
  OverGuitarPhrase2.addNoteList(overPS3, overDS3) 
  OverGuitarPhrase3.addNoteList(overPS3, overDS3) 

  OverGuitarPhrase1.addNoteList(overP14, overD9)
  OverGuitarPhrase2.addNoteList(overP14_1, overD9)
  OverGuitarPhrase3.addNoteList(overP14_2, overD9)

  OverGuitarPhrase1.addNoteList(overP14, overD9)
  OverGuitarPhrase2.addNoteList(overP14_1, overD9)
  OverGuitarPhrase3.addNoteList(overP14_2, overD9)

  # Break 8 s
  OverGuitarPhrase1.addNoteList(overPS2, overDS2) #8
  # just to avoid phrase lag (they are silent)
  OverGuitarPhrase2.addNoteList(overPS2, overDS2) #8
  OverGuitarPhrase3.addNoteList(overPS2, overDS2) #8

  # Chorus 2 2s

  #OverGuitarPhrase1.addNoteList(bassPitches, bassDurations)
  #OverGuitarPhrase2.addNoteList(bassPitches, bassDurations)
  #OverGuitarPhrase3.addNoteList(bassPitches, bassDurations)
  overDrivePart.addPhrase(OverGuitarPhrase1)
  overDrivePart.addPhrase(OverGuitarPhrase2)
  overDrivePart.addPhrase(OverGuitarPhrase3)

  # TODO This is only for testing instrument individually. Delete after finishing part.
  # score.addPart(overDrivePart)
  # Play.midi(score)
  #View.sketch(score)
  
  return overDrivePart

score = Score("Song", 123.0)

drumsPart = getDrumPart()
bassPart = getBassPart()
overdrivenPart = getOverdrivenGuitarPart()

score.addPart(drumsPart)
score.addPart(bassPart)
score.addPart(overdrivenPart)

Write.midi(score, "Drum.mid")
Play.midi(score)

