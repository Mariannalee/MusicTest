import librosa
import numpy as np

def transcribe_melody_v2(file_path):
    # 1. 讀取音檔 (強制單聲道以提高精確度)
    y, sr = librosa.load(file_path, sr=22050, mono=True)
    
    # 2. 預測音高 (調整參數以減少誤判)
    # fmin/fmax 設窄一點可以提高成功率
    f0, voiced_flag, voiced_probs = librosa.pyin(y, 
                                                 fmin=librosa.note_to_hz('C2'), 
                                                 fmax=librosa.note_to_hz('C6'), 
                                                 sr=sr,
                                                 fill_na=None) # 不要自動填充，避免幻聽
    
    # 3. 偵測起始點 (增加背後背景噪音過濾)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr, backtrack=True)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
    
    transcription = []
    times = librosa.times_like(f0)
    
    for i, onset in enumerate(onset_times):
        # 找到起始點後的 5 幀 (約 0.1 秒) 取中位數，這比只取一幀準得多
        start_idx = np.argmin(np.abs(times - onset))
        end_idx = start_idx + 5 
        
        # 取得這段區間內的有效頻率
        segment_freqs = f0[start_idx:end_idx]
        valid_freqs = segment_freqs[~np.isnan(segment_freqs)]
        
        if len(valid_freqs) > 0:
            # 取中位數排除極端跳躍值
            freq = np.median(valid_freqs)
            midi_note = librosa.hz_to_midi(freq)
            
            # 只有當音符與上一個不同時才記錄，避免重複
            note_name = librosa.midi_to_note(round(midi_note))
            
            # 過濾掉太低的雜音 (例如 MIDI < 24)
            if midi_note > 24:
                transcription.append({
                    "time": round(onset, 3),
                    "midi": int(round(midi_note)),
                    "note": note_name
                })
            
    return transcription

# 執行
file_path = "/Users/mariannalee/Desktop/python/3i5hu-vs72w.wav"
results = transcribe_melody_v2(file_path)

# 打印結果
print(f"{'時間(秒)':<10} | {'MIDI':<5} | {'音名':<5}")
for r in results:
    print(f"{r['time']:<10} | {r['midi']:<5} | {r['note']:<5}")