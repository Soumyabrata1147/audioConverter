from pydub import AudioSegment
song = AudioSegment.from_mp3("file.mp3")
song.export("out.ogg", format="ogg")  # Is the same as:
song.export("out.ogg", format="ogg", codec="libvorbis")