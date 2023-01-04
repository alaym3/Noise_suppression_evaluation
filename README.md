# Noise suppression evaluation

## In this repository we calculate the [PESQ](http://www.recursosvoip.com/docs/english/pap465.pdf) score for noisy audio files run through various noise suppression and voice enhancement models that we evaluated in our project. 

**Evaluation process:**
- Eight random and balanced, clean speech (no noise) samples were chosen.
- Two types of noise were chosen: gaussian and babble noise:
  - Gaussian noise was chosen since it is the easiest to remove;
  - Babble noise was chosen since it is the most difficult to remove.
- Clean speech samples were underlayed with noise at -5, 0, 5, and 10 dB SNR each.
- Audios were normalized and volume regulated to the required testing ratio.
- Noise and speech was merged into one audio channel.
  - All 4 models were tested on each noisy speech file, producing an output audio file for all the combinations of test file, dB level, and noise type.
  - Metrics of speech quality and intelligibility of the output files was calculated and compared.

The noisy files are inside the test_data folder, and segmented based on noise type.
The output files are inside the testing_output folder, and segmented based on the model.

**PESQ** is an objective measure of speech quality, ranging from -0.5 to 4.5, using sharpness, volume, background noise. 

The PESQ results for each model are shown below.

<img width="539" alt="pesq_scores" src="https://user-images.githubusercontent.com/93861536/210414584-085f043c-263c-4d6a-953d-15bd239718a6.png">

