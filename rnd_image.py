import random
def getRndFile():
	note = random.randint(1,7)
	notes = ["A", "B", "C", "D", "E", "F", "G"]
	octave = random.randint(1,3)
	filename = notes[note-1] + str(octave) + ".png"
	return filename

