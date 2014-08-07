import os
for file in os.listdir("/home/pi/rd2/"):
	if ".mp3" in file.lower():
		print "Playing: ",file
		os.system('ffmpeg -i "'+file+'" -vol 512 -ab 128k -f s16le -ar 22.05k -ac 1 - | sudo ./pifm - 100.0')
	if ".wav" in file.lower():
                print "Playing: ",file
                os.system('ffmpeg -i "'+file+'" -vol 512 -ab 128k -f s16le -ar 22.05k -ac 1 - | sudo ./pifm - 100.0')
