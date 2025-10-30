import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():
    # --- カメラキャプチャ実行 ---
    app = MyVideoCapture()
    app.run()
    app.write_img("images/camera_capture.png")  # 撮った画像を保存

    # --- 画像を読み込み ---
    google_img: cv2.Mat = cv2.imread("images/google.png")              # 1280x640
    capture_img: cv2.Mat = cv2.imread("images/camera_capture.png")     # 640x480

    if google_img is None or capture_img is None:
        raise FileNotFoundError("画像の読み込みに失敗しました。パスを確認してください。")

    g_h, g_w, _ = google_img.shape
    c_h, c_w, _ = capture_img.shape
    print("Google画像サイズ:", google_img.shape)
    print("カメラ画像サイズ:", capture_img.shape)

    # --- カメラ画像をタイル状に並べてGoogle画像と同じ大きさにする ---
    tiled_img = np.tile(capture_img, (int(np.ceil(g_h / c_h)), int(np.ceil(g_w / c_w)), 1))
    tiled_img = tiled_img[:g_h, :g_w]  # サイズをぴったり合わせる

    # --- 白色(255,255,255)の部分だけ置換 ---
    white_mask = np.all(google_img == [255, 255, 255], axis=-1)  # 白色部分を検出
    result = google_img.copy()
    result[white_mask] = tiled_img[white_mask]

    # --- 保存 ---
    cv2.imwrite("images/replaced_google.png", result)
    print("✅ 完了: images/replaced_google.png に保存しました。")

if __name__ == "__main__":
    lecture05_01()
