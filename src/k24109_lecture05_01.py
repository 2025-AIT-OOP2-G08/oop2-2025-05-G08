import numpy as np
import cv2
from my_module.k21999.lecture05_camera_image_capture import MyVideoCapture

def k24109_lecture05_01():
 
    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    capture_img : cv2.Mat = "app.get_img()"

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    # ★追加: 置換時のインデックス範囲を合わせるためにサイズを揃える
    capture_img = cv2.resize(capture_img, (g_width, g_hight), interpolation=cv2.INTER_LINEAR)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
               pass
            #implement me

    google_img[y, x] = capture_resized[y, x]

    # 書き込み処理
capture_img : cv2.Mat = cv2.imread('images/camera_capture.png')

