from pydub import AudioSegment
song = AudioSegment.from_ogg("out.ogg")
song.export("out.mp3", format="mp3")  # Is the same as:
# song.export("out.ogg", format="ogg", codec="libvorbis")