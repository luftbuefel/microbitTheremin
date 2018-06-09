from microbit import *

beatLength = music.beat(BeatFraction.Whole)
beatSwitcher = 0
playMusic = False

notes = [C4, D4, E4, F4, G4, A5, B5, C5, D5, E5, F5, G5, A6, B6]


while True:
    
    #control whether music plays or not
    if playMusic == True:
        playNote()
    
    # A button toggles the music playing on and off
    if button_a.was_pressed():
        if (playMusic == False) {
            playMusic = True
        } else {
            playMusic = False
            #music.stop()
        }
    # B button changes the length of the note being played
    if button_b.was_pressed():
        beatSwitcher += 1
        #reset the beatSwitcher back to 0 when it gets too big
        if beatSwitcher >= 5:
            beatSwitcher = 0
        #use the beatSwitcher to lookup the beat length we want to use
        if beatSwitcher == 0:
            beatLength = music.beat(BeatFraction.Whole)
        elif beatSwitcher == 1:
            beatLength = music.beat(BeatFraction.Half)
        elif beatSwitcher == 2:
            beatLength = music.beat(BeatFraction.Quarter)
        elif beatSwitcher == 3:
            beatLength = music.beat(BeatFraction.Eighth)
        else:
            beatLength = music.beat(BeatFraction.Sixteenth)


def playNote():
    if input.lightLevel() <= 15:
        music.play(notes[0], beatLength)
    elif input.lightLevel() <= 30:
        music.play(notes[1], beatLength)
    elif input.lightLevel() <= 45:
        music.play(notes[2], beatLength)
    elif input.lightLevel() <= 60:
        music.play(notes[3], beatLength)
    elif input.lightLevel() <= 75:
        music.play(notes[4], beatLength)
    elif input.lightLevel() <= 90:
        music.play(notes[5], beatLength)
    elif input.lightLevel() <= 105:
        music.play(notes[6], beatLength)
    elif input.lightLevel() <= 120:
        music.play(notes[7], beatLength)
    elif input.lightLevel() <= 135:
        music.play(notes[8], beatLength)
    elif input.lightLevel() <= 150:
        music.play(notes[9], beatLength)
    elif input.lightLevel() <= 165:
        music.play(notes[10], beatLength)
    elif input.lightLevel() <= 180:
        music.play(notes[11], beatLength)
    else:
        music.play(notes[12], beatLength)
        
        
'''
#You can use this to get more creative with the notes that you play with the theremin
import music

while True:
    for freq in range(880, 1760, 16):
        music.pitch(freq, 6)
    for freq in range(1760, 880, -16):
        music.pitch(freq, 6)
        '''

