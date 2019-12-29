from pydub import AudioSegment
song = AudioSegment.from_file("file.m4a",format="m4a")
song.export("out.mp3", format="mp3")  # Is the same as:
# song.export("out.mp3", format="mp3")