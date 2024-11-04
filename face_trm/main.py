import os
from PIL import Image
import face_recognition

# 入力ディレクトリと出力ディレクトリのパスを設定
INPUT_DIR = "images/input"
OUTPUT_DIR = "images/output"
MARGIN = 200

# 出力ディレクトリが存在しない場合は作成
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 入力ディレクトリ内の全ての画像ファイルを処理
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 画像ファイルのパスを取得
        image_path = os.path.join(INPUT_DIR, filename)
        
        # 画像を読み込む
        image = face_recognition.load_image_file(image_path)
        pil_image = Image.fromarray(image)
        
        # 顔の位置を検出
        face_locations = face_recognition.face_locations(image)
        
        # 各顔の位置に対して処理を行う
        for face_location in face_locations:
            top, right, bottom, left = face_location

            # 余白を設定する
            top = max(0, top - MARGIN)
            right = min(image.shape[1], right + MARGIN)
            bottom = min(image.shape[0], bottom + MARGIN)
            left = max(0, left - MARGIN)

            # 顔をトリミングする
            face_image = pil_image.crop((left, top, right, bottom))

            # トリミングした顔画像を保存する
            output_path = os.path.join(OUTPUT_DIR, f"face_{top}_{left}_{filename}")
            face_image.save(output_path)

print("全ての画像のトリミングが完了しました。")