from music import *

# Funcion para exportar la parte (instrumento) que nos toca
def getDrumPart():

  # TODO This is only for testing instrument individually. Delete after finishing part.
  score = Score("Drum Machine Pattern #1", 145.0)

  drumsPart = Part("Bass", 0, 3)
  bassDrumPhrase = Phrase(0.0) # Create phrase at beat 0.0
  
  bassDrumPhrase.setInstrument(OVERDRIVEN_GUITAR)
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

   # Break 4 4

  bassDrumPhrase.addNoteList(bassPitches, bassDurations)
  drumsPart.addPhrase(bassDrumPhrase)

  # TODO This is only for testing instrument individually. Delete after finishing part.
  score.addPart(drumsPart)
  Play.midi(score)

  return drumsPart