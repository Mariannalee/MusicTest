### MusicTest
##  需安裝的套件(適用Mac)：

音檔轉MIDI檔：

> [!NOTE]
> Basic pitch套件只能用舊版python 3.10－3.11 

         虛擬環境退出：deactivate

         建制新環境：python3.11 -m venv ~/Desktop/python/musicMIDI

         進入新環境：source ~/Desktop/python/musicMIDI/bin/activate

         確認版本：python --version

         安裝套件：pip install --upgrade pip pip install basic-pitch
         
         安裝 torch、basic-pitch 以及處理 MIDI 用的 pretty-midi：pip install torch basic-pitch pretty-midi

         安裝 TensorFlow：pip install tensorflow-macos

         在 Mac 上，讓 Basic Pitch 運作最快的方法是安裝 TensorFlow，因為 Basic Pitch 預設是用 TensorFlow 訓練的（TensorFlow是開源機器學習框架）

> [!IMPORTANT]
> 要command + shift + P切換 Python: Select Interpreter，然後選擇路徑包含 musicMIDI 的那個 Python 3.11。

> [!IMPORTANT]
> 如果找不到模型位置：找模型的資料夾：find /Users/mariannalee/Desktop/python/musicMIDI/lib/python3.11/site-packages/basic_pitch -name "saved_model.pb"

> [!IMPORTANT]
>TensorFlow版本不能太新，要2.15以下
    1. 移除目前太新版的 TensorFlow：pip uninstall -y tensorflow tensorflow-macos tensorflow-metal
    2. 安裝與模型相容的舊版本 (2.15.0)：pip install tensorflow-macos==2.15.0

> [!NOTE]
> 連接Tonnze：

<blockquote>安裝解析庫：
        
         pip install pretty-midi
