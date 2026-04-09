import pretty_midi
import json
import os

def export_to_tonnze(midi_path, output_json):
    
    midi_path = "/Users/mariannalee/Desktop/python/output_midi/fpxt5-2jzf8_basic_pitch.mid"
    pm = pretty_midi.PrettyMIDI(midi_path)
    
    tonnze_timeline = []

    # 遍歷所有樂器軌道
    for instrument in pm.instruments:
        # 遍歷所有音符
        for note in instrument.notes:
            tonnze_timeline.append({
                "time": round(note.start, 3),      # 開始秒數
                "end": round(note.end, 3),        # 結束秒數
                "duration": round(note.get_duration(), 3),
                "midi_number": note.pitch,         # MIDI 編號 (如 60)
                "note_name": pretty_midi.note_number_to_name(note.pitch), # 音名 (如 C4)
                "velocity": note.velocity          # 彈奏力度
            })

    # 按照時間排序，這對 Tonnze 播放很重要
    tonnze_timeline.sort(key=lambda x: x["time"])

    # 存成 JSON
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(tonnze_timeline, f, indent=4, ensure_ascii=False)

    print(f"✅ 轉換成功！共處理了 {len(tonnze_timeline)} 個音符。")
    print(f"📂 數據已存至: {output_json}")

# --- 執行處 ---
# 請指向你剛才轉出來的那個 MIDI 檔
midi_input = "/Users/mariannalee/Desktop/python/output_midi/your_generated_file.mid" 
output_json = "/Users/mariannalee/Desktop/python/tonnze_data.json"

export_to_tonnze(midi_input, output_json)