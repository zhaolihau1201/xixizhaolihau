from pydub import AudioSegment
import webdriver as webdriver

# 读取wav格式的音频文件

music = AudioSegment.from_wav('百年孤独.wav')

music = AudioSegment.from_mp3('music.mp3')

music = AudioSegment.from_ogg("music.ogg")

music = AudioSegment.from_flv("music.flv")
