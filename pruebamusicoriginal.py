from music import *

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

# Create a part to hold all the phrases
part = Part()
drumsPart = getDrumPart()

# Define the piano pattern and set its instrument
pianoPattern = [A3, C4, E4, A4] * 4
pianoPhrase = Phrase()
for note in pianoPattern:
    pianoPhrase.addNote(Note(note, QUARTER_NOTE))
pianoPhrase.setInstrument(PIANO)
part.addPhrase(pianoPhrase)
#
## Bassline to accompany the chords and give a rock feel
#basslinePattern = [
#    A2, A2, E2, E2, D2, D2, A2, A2,
#    A2, A2, E2, E2, D2, D2, A2, A2,
#    A2, A2, E2, E2, D2, D2, A2, A2,
#    G2, G2, D2, D2, C2, C2, G2, G2
#]
#
#bassPhrase = Phrase()
#for note in basslinePattern:
#    bassPhrase.addNote(Note(note, QUARTER_NOTE))
#bassPhrase.setInstrument(ELECTRIC_BASS)
#part.addPhrase(bassPhrase)

# Define the violin pattern and set its instrument
violinPattern = [E4, F4, A4, G4] * 4
violinPhrase = Phrase()
for note in violinPattern:
    violinPhrase.addNote(Note(note, QUARTER_NOTE))
violinPhrase.setInstrument(VIOLIN)
part.addPhrase(violinPhrase)

# Electric guitar power chords with more rock rhythm
A_MAJOR_CHORD = [A2, E3, A3]
E_MAJOR_CHORD = [E2, B2, E3]
D_MAJOR_CHORD = [D2, A2, D3]

guitarPattern = [A_MAJOR_CHORD, A_MAJOR_CHORD, E_MAJOR_CHORD, E_MAJOR_CHORD, D_MAJOR_CHORD, D_MAJOR_CHORD, A_MAJOR_CHORD, A_MAJOR_CHORD]
guitarPhrase = Phrase()
for chordNotes in guitarPattern:
    guitarPhrase.addChord(chordNotes, QUARTER_NOTE)
guitarPhrase.setInstrument(OVERDRIVEN_GUITAR)  # Assuming there's an OVERDRIVEN_GUITAR constant
part.addPhrase(guitarPhrase)


# Piano pattern for Verse 1
versePianoPattern = [A3, C4, D4, E4] * 4
versePianoPhrase = Phrase()
for note in versePianoPattern:
    versePianoPhrase.addNote(Note(note, QUARTER_NOTE))
versePianoPhrase.setInstrument(PIANO)
part.addPhrase(versePianoPhrase)

# Overdriven Guitar Riff for Verse 1
overdriveGuitarPattern = [E4, G4, A4] * 4
overdriveGuitarPhrase = Phrase()
for note in overdriveGuitarPattern:
    overdriveGuitarPhrase.addNote(Note(note, QUARTER_NOTE))
overdriveGuitarPhrase.setInstrument(30)
part.addPhrase(overdriveGuitarPhrase)

# Bass pattern for Verse 1
bassPattern = [E2, G2, A2] * 4
bassPhrase = Phrase()
for note in bassPattern:
    bassPhrase.addNote(Note(note, QUARTER_NOTE))
bassPhrase.setInstrument(BASS)
part.addPhrase(bassPhrase)

# Piano pattern for Bridge
bridgePianoPattern = [G3, B3, D4, G4] * 2
bridgePianoPhrase = Phrase()
for note in bridgePianoPattern:
    bridgePianoPhrase.addNote(Note(note, QUARTER_NOTE))
bridgePianoPhrase.setInstrument(PIANO)
part.addPhrase(bridgePianoPhrase)

# Rock Organ pattern for the Bridge
# Rock Organ pattern for the Bridge
organPattern = [
    G3, B3, D4, G4, 
    D3, F3, A3, D4,  # Corregido a F3
    C3, E3, G3, C4, 
    G3, B3, D4, G4
]

organPhrase = Phrase()
for note in organPattern:
    organPhrase.addNote(Note(note, QUARTER_NOTE))
organPhrase.setInstrument(ROCK_ORGAN)  # Asumiendo que hay una constante ROCK_ORGAN
part.addPhrase(organPhrase)

# Rock Organ to accompany the guitar solo
organSoloBackground = [
    A3, E3, D3, A3,
    A3, E3, D3, A3,
    G3, D3, C3, G3,
    G3, D3, C3, G3
]

organSoloPhrase = Phrase()
for chord in organSoloBackground:
    organSoloPhrase.addChord([chord, chord + 4, chord + 7], WHOLE_NOTE)
organSoloPhrase.setInstrument(ROCK_ORGAN)
part.addPhrase(organSoloPhrase)


# Clean Electric Guitar Power Chords for Bridge
G_MAJOR_CHORD = [G3, D4, G4]
D_MAJOR_CHORD = [D3, A3, D4]
C_MAJOR_CHORD = [C3, G3, C4]
bridgeGuitarPattern = [G_MAJOR_CHORD, D_MAJOR_CHORD, C_MAJOR_CHORD, G_MAJOR_CHORD]
bridgeGuitarPhrase = Phrase()

for chordNotes in bridgeGuitarPattern:
    bridgeGuitarPhrase.addChord(chordNotes, HALF_NOTE)
bridgeGuitarPhrase.setInstrument(GUITAR)
part.addPhrase(bridgeGuitarPhrase)


# Solo de guitarra basado en la escala pentatónica menor de A

soloPattern = [
    A4, A4, C5, D5, E5, D5, C5,
    A4, G4, E4, G4, A4, A4, E5, D5, 
    C5, A4, C5, E5, D5, C5, A4,
    E4, D4, A4, G4, A4, C5, A4, E5, G5, E5,
    D5, E5, D5, C5, A4, D5, E5, D5, C5, A4,
    A4, G4, E4, D4, E4, G4, A4, G5, A5, G5, E5,
    D5, C5, A4, G4, A4
]


rhythmPattern = [
    QUARTER_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE,
    QUARTER_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, QUARTER_NOTE, EIGHTH_NOTE, EIGHTH_NOTE,
    QUARTER_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE,
    QUARTER_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE,
    QUARTER_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, QUARTER_NOTE,
    EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE,
    QUARTER_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, EIGHTH_NOTE, HALF_NOTE
]

# una octava hacia arriba y otra hacia abajo
# desfaarlo medio bit

soloPhrase = Phrase()
for i, note in enumerate(soloPattern):
    soloPhrase.addNote(Note(note, rhythmPattern[i]))
soloPhrase.setInstrument(OVERDRIVEN_GUITAR)  # Asumiendo que tienes una constante para la guitarra con distorsión
part.addPhrase(soloPhrase)


# Solo de guitarra con sordina
mutedGuitarSoloPattern = [
    A4, C5, D5, C5, A4, G4, A4,
    A4, D5, E5, D5, C5, A4, C5,
    D5, E5, G5, E5, D5, C5, D5,
    A4, G4, A4, E4, D4, E4, A4
]

rhythmPattern = [
    SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE,
    SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE,
    SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE,
    SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE, SIXTEENTH_NOTE
]

mutedGuitarPhrase = Phrase()
for i, note in enumerate(mutedGuitarSoloPattern):
    mutedGuitarPhrase.addNote(Note(note, rhythmPattern[i]))
mutedGuitarPhrase.setInstrument(MUTED_GUITAR)  # Asumiendo que tienes una constante MUTED_GUITAR
part.addPhrase(mutedGuitarPhrase)


# Combine all parts into a score
score = Score()
score.addPart(part)
score.addPart(drumsPart)
score.setTempo(200)

View.sketch(score)
# Play the score
Write.midi(score, "Original.mid")
Play.midi(score)
