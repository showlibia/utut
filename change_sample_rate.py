import librosa
import soundfile as sf

def change_sample_rate(input_file_path, output_file_path, new_sample_rate):
    audio, original_sample_rate = librosa.load(input_file_path, sr=None)  
    
    resampled_audio = librosa.resample(audio, orig_sr=original_sample_rate, target_sr=new_sample_rate)
    
    sf.write(output_file_path, resampled_audio, new_sample_rate)

input_file = "/root/project/Datasets/cv-corpus-16.1-delta-2023-12-06/en/clips/common_voice_en_38487551.mp3"   
output_file = "/root/project/ZY/utut/samples/en/common_voice_en_38487551.wav"  
new_sample_rate = 16000 

change_sample_rate(input_file, output_file, new_sample_rate)
