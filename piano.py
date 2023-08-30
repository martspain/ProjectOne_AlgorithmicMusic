# furElise.py
# Generates the theme from Beethoven's Fur Elise.
 
from music import *
 
# theme has some repetition, so break it up to maximize economy
# (also notice how we line up corresponding pitches and durations)
#pitches1   = [D5, B4, F4, D5, E5]
#durations1 = [QN, QN, QN, EN, EN]
#pitches2   = [E5, C5, G4, E5, D5, C5]
#durations2 = [EN, QN, QN, EN, EN, EN]
#pitches3   = [D5, B4, G4, D5, E5]
#durations3 = [QN, QN, QN, EN, EN]
#pitches4   = [E5, B4, G4, E5, D5, C5]
#durations4 = [EN, QN, QN, EN, EN, EN]

pitches0   = [D5, B4, F4, D5, E5, E5, C5, G4, E5, D5, C5, D5, B4, G4, D5, E5, E5, B4, G4, E5, D5, C5]
durations0 = [QN, QN, QN, EN, EN, EN, QN, QN, EN, EN, EN] * 2

pitches1 = pitches0 * 3
durations1 = durations0 * 3

# create an empty phrase, and construct theme from the above motifs
theme = Phrase()   

theme.addNoteList(pitches1, durations1)

theme.setTempo(123)

# play it
Play.midi(theme)
