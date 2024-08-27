import os

os.system("python youtube-downloader.py")
os.system("python audio-converter.py")
os.system("python audio-merge.py")
os.system("python zip.py outputFolder3 outputFolder3.zip")
os.system("python sendToEmail.py outputFolder3.zip guryanshsingla@gmail.com")
