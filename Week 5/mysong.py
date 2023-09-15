'''This program allows for manipulation of the song using the functions provided that requires inputs such as audio,
start,end,line and loops'''


# description: 
from earsketch import *
#sets the music speed
setTempo(100)
#a definition that takes audio, start, end, line
def intro(audio,start,end,line):
    fitMedia(audio, line, start, end)
finish()
#a definition that takes audio, start, end, line as well as how many loops
def sound(audio,start,end,line,loop):
    fitMedia(audio, line, start, end)
    if loop > 1:
        length = end - start
        for i in range(1, loop):
            fitMedia(audio, line, start + length * i, end + length * i)
finish()
#a definition that takes audio, start, end, line
def drum(audio,start,end,line):
    fitMedia(audio, line, start, end)
finish()
#a def that mimics the sound def but with a while loop instead
def bass(audio,start,end,line,loop):
    fitMedia(audio, line, start, end)
    if loop > 1:
        length = end - start
        i = 1
        while i < loop:
            fitMedia(audio, line, start + length * i, end + length * i)
            i += 1
finish()

#Utilises the Def functions and inserts audio and inputs required

intro(RD_ELECTRO_SFX_RINGMODRISER_1,1,5,1)
sound(RD_EDM_CHORDPART_1,5,9,2,3)
drum(KHALID_NORM_DRUMBEAT,9,17,3)
bass(RD_ELECTRO_RAWBASSLINE_6,17,21,4,2)
sound(RD_EDM_CHORDPART_2,17,21,5,2)
sound(RD_EDM_CHORDPART_1,21,25,2,3)
drum(KHALID_NORM_DRUMBEAT,21,33,3)
bass(ELECTRO_ANALOGUE_BASS_022,25,33,1,1)




#fitMedia(RD_TRAP_MAIN808_BEAT_15, 3, 5, 12)



finish()