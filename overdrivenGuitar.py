from music import *

# Funcion para exportar la parte (instrumento) que nos toca
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