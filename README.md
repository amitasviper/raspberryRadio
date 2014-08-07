raspberryRadio
==============
This module is to convert your Raspberry Pi into a FM Radio Station. 

Dependencies:
ffmpeg streamer
python 2.7
gcc

To run the radio station:
Connect the 7th pin of the raspberry pi to a wire of almost 1-2 meters in length, which will act as antenna.
Now place all the mp3 or wav files in the current folder containing all other project files in this repository and execute the
startRadio.py by writting:

          python startRadio.py
          
Now tune your radio receiver at 100.0 Mhz... You will listen the music.

To change the broadcasting frequency:
  open startRadio.py file and replace the 100.0 with your desired frequency. CAUTION: The broadcasting frequency must
  be between 88 t0 108.
