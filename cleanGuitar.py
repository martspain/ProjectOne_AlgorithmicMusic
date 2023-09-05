from music import *

def add_chords(pitches_list, durations_list, chords_pitches, chords_durations):
    """Función para añadir acordes y duraciones a las listas."""
    for pitches, duration in zip(pitches_list, durations_list):
        chords_pitches.append(pitches)
        chords_durations.append(duration)

# Inicialización y configuración
theme = Phrase()
phrase = Phrase()
individual_phrase = Phrase()

CLEAN_GUITAR_INSTRUMENT_NUMBER = 27
MIDI_CHANNEL = 0
cleanGuitarPart = Part(CLEAN_GUITAR_INSTRUMENT_NUMBER, MIDI_CHANNEL)

# Establecer dinámica y tempo para todas las frases
for p in [theme, individual_phrase]:
    p.setDynamic(F)
    p.setTempo(123)
 
phrase.setDynamic(FF)
phrase.setTempo(123)

# Intro
cleanNotes = [F4, B4, F4, B4, F4, B4, G4, G4, C4, G4, C4, G4, C4, G4, G4, D4, G4, D4, G4, D4, E4, E4, B4, E4, B4, E4, B4, E4] * 2
cleanNotesDurations = [EN, EN, EN, QN, EN, EN, EN] * 8

# Añadir silencios y notas
theme.addNoteList([REST] * 9 + cleanNotes * 3, [WN] * 9 + cleanNotesDurations * 3)

# Añadir el tema al Part
cleanGuitarPart.addPhrase(theme)

# Bridge + Gtr. Solo 1
chords_pitches = [[REST]] * 8
chords_durations = [WN] * 8

DURATIONS1 = [QN, EN, EN, EN, EN, EN, EN]
DURATIONS2 = [EN, EN, EN, QN, EN, EN, EN]

# Definición de acordes
CHORDS_1_1 = [[E4, E4, C4, G4, C4], [E4, E4, C4, G4, C4], [REST], [E4, C4, G4, C4], [E4, E4, C4, G4], [E4, C4, G4, C4], [F4, C4, A4, F4, C4, F4]]

CHORDS_1_2 = [[F4, C4, A4, F4, C4, F4], [F4, C4, A4, F4, C4, F4], [REST], [F4, C4, A4, F4, C4, F4], [C4, A4, F4, C4, F4], [F4, C4, A4, F4, C4], [C4, A4, F4, C4, F4]]

CHORDS_1_3 = [[G4, D4, A4, G4, D4], [G4, D4, A4, G4, D4], [REST], [D4, A4, G4, D4], [G4, D4, A4, G4], [D4, A4, G4, D4], [G4, D4, B4, G4, D4, G4]]

CHORDS_1_4 = [[G4, D4, B4, G4, D4, G4], [G4, D4, B4, G4, D4, G4], [REST], [G4, D4, B4, G4, D4, G4], [D4, B4, G4, D4, G4], [G4, D4, B4, G4, D4], [D4, B4, G4, D4, G4]]

CHORDS_1_5 = [[E4, C4, A4, E4, A4], [E4, C4, A4, E4, A4], [REST], [C4, A4, E4, A4], [E4, C4, A4, E4], [C4, A4, E4, A4], [E4, B4, G4, E4, B4, E4]]

CHORDS_1_6 = [[E4, B4, G4, E4, B4, E4], [E4, B4, G4, E4, B4, E4], [REST], [E4, B4, G4, E4, B4, E4], [B4, G4, E4, B4, E4], [E4, B4, G4, E4, B4], [B4, G4, E4, B4, E4]]

CHORDS_1_7 = [[E4, C4, A4, E4, A4], [E4, C4, A4, E4, A4], [REST], [C4, A4, E4, A4], [E4, C4, A4, E4], [C4, A4, E4, A4], [G4, D4, A4, G4, D4]]

CHORDS_1_8 = [[G4, D4, A4, G4, D4], [G4, D4, A4, G4, D4], [REST], [G4, D4, A4, G4, D4], [D4, A4, G4, D4], [G4, D4, A4, G4], [D4, A4, G4, D4]]

# Añadir acordes y duraciones
add_chords(CHORDS_1_1, DURATIONS1, chords_pitches, chords_durations)
add_chords(CHORDS_1_2, DURATIONS2, chords_pitches, chords_durations)

add_chords(CHORDS_1_3, DURATIONS1, chords_pitches, chords_durations)
add_chords(CHORDS_1_4, DURATIONS2, chords_pitches, chords_durations)

add_chords(CHORDS_1_5, DURATIONS1, chords_pitches, chords_durations)
add_chords(CHORDS_1_6, DURATIONS2, chords_pitches, chords_durations)

add_chords(CHORDS_1_7, DURATIONS1, chords_pitches, chords_durations)
add_chords(CHORDS_1_8, DURATIONS2, chords_pitches, chords_durations)


for pitches, duration in zip(chords_pitches, chords_durations):
    phrase.addChord(pitches, duration)

cleanGuitarPart.addPhrase(phrase)

# Bridge p.2a
bridgeNotes = [B4, G4, D4, B4, G4, D4, D4, A4, F4, D4, A4, F4, D4, D4, B4, G4, E4, B4, G4, E4, E4, F4, D4, B4, F4, E4, F4, E4]
bridgeNotesDurations = [EN, EN, QN, EN, EN, EN, EN] * 3 + [EN, EN, EN, EN, QN, EN, EN]

individual_phrase.addNoteList(bridgeNotes * 4, bridgeNotesDurations * 4)
cleanGuitarPart.addPhrase(individual_phrase)

# Visualización y reproducción
View.sketch(cleanGuitarPart)
Play.midi(cleanGuitarPart)
