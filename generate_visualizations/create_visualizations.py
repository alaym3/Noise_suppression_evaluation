# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:39:26 2022

following this guide:
    https://learnpython.com/blog/plot-waveform-in-python/

"""
import os
import wave
import numpy as np
import matplotlib.pyplot as plt

# following this guide:
#  https://learnpython.com/blog/plot-waveform-in-python/

# change path to relevant model output
path = '../testing_output/DeepFilterNet2_Results/16khz_gaussian'
directory = os.fsencode(path)

os.mkdir(path+'Aplitude/')
os.mkdir(path+'Frequency/')
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".wav"):
         wav_obj = wave.open(path+filename,'rb')

         # sampling rate of the sound
         sample_freq = wav_obj.getframerate()
         print(f"Sample freq: {sample_freq}")

         # number of individual samples in audio file
         n_samples = wav_obj.getnframes()
         print(f"N-samples: {n_samples}")

         # calculate how long audio file is in seconds
         t_audio = n_samples/sample_freq
         print(f"length of audio: {t_audio}")

         # check number of channels in audio
         n_channels = wav_obj.getnchannels()
         print(f"Number channels: {n_channels}")

         # get the amplitude of the wave at a point in time
         signal_wave = wav_obj.readframes(n_samples)
         # translate the bytes object into signal values
         signal_array = np.frombuffer(signal_wave, dtype=np.int16)
         print(f"Signal array: {signal_array}")

         #calculate time at which each sample is taken for plotting it
         times = np.linspace(0, n_samples/sample_freq, num=n_samples)

         print(f"Times: {times}")
         print(f"Signal array: {signal_array}")

         #%%
         # create the aplitude plot
         plt.figure(figsize=(15,5))
         plt.plot(times,signal_array)
         plt.title('Signal')
         plt.xlabel('Time(s)')
         plt.xlim(0,t_audio)
         plt.ylim([-8000, 8000])
         plt.savefig(path+'Aplitude/'+filename[:-4]+'apl.png')
         plt.show()
         

         # create the frequency spetcrum plot
         plt.figure(figsize=(15,5))
         plt.specgram(signal_array, Fs=sample_freq, vmin = -20, vmax=50)
         plt.title('Signal')
         plt.ylabel('Frequency(Hz)')
         plt.xlabel('Time(s)')
         plt.xlim(0,t_audio)
         plt.ylim([0, 8000])
         plt.colorbar()
         plt.savefig(path+'Frequency/'+filename[:-4]+'freq.png')
         plt.show()
         
