import threading
import time
import cv2  # 保留 OpenCV 用于图像处理
from threading import Thread
import os

# --- 假设这些模块与此脚本在同一目录 ---
try:
    import img_function as predict  # 核心预测逻辑
    import img_math  # 用于 img_read
except ImportError:
    print("错误: 无法导入自定义模块 'img_function' 或 'img_math'。")
    print("请确保 'img_function.py' 和 'img_math.py' 文件在同一目录下。")
    exit()


# ---------------------------------------------------------------------


class ThreadWithReturnValue(Thread):
    """
    一个自定义线程子类，允许从目标函数检索返回值。
    这里修改为期望目标函数返回三个值。
    """

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
        self._return1 = None
        self._return2 = None
        self._return3 = None

    def run(self):
        """运行目标函数并存储其三个返回值。"""
        if self._target is not None:
            self._return1, self._return2, self._return3 = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        """等待线程完成并返回存储的值。"""
        Thread.join(self, *args)
        return self._return1, self._return2, self._return3


def run_prediction(image_path):
    """
    运行车牌识别逻辑的主函数。
    """

    # --- 1. 检查文件是否存在 ---
    if not os.path.exists(image_path):
        print(f"错误: 文件未找到: {image_path}")
        print("请检查 'IMAGE_PATH' 变量是否设置正确。")
        return

    # --- 2. 初始化识别器 ---
    print("正在初始化并训练 SVM 模型...")
    try:
        predictor = predict.CardPredictor()
        predictor.train_svm()
        print("SVM 模型训练完成。")
    except Exception as e:
        print(f"错误: 初始化识别器或训练 SVM 时出错: {e}")
        print("请确保 SVM 模型文件 (例如 'svm.dat') 存在且路径正确。")
        return

    # --- 3. 读取和预处理图像 ---
    print(f"正在处理图片: {image_path}")
    try:
        # 使用 img_math.img_read 来处理可能包含中文的路径
        img_bgr = img_math.img_read(image_path)
        if img_bgr is None:
            print(f"错误: 无法从 {image_path} 读取图像。")
            print("请检查文件路径和文件完整性。")
            return

        # 执行初始预处理
        first_img, oldimg = predictor.img_first_pre(img_bgr)
        print("图像预处理完成。")

    except Exception as e:
        print(f"错误: 读取或预处理图像时出错: {e}")
        return

    # --- 4. 并行运行预测 ---
    print("正在启动并行预测线程...")

    # 线程 1: 基于形状/轮廓的预测
    th1 = ThreadWithReturnValue(target=predictor.img_color_contours,
                                args=(first_img, oldimg))

    # 线程 2: 基于颜色的预测
    th2 = ThreadWithReturnValue(target=predictor.img_only_color,
                                args=(oldimg, oldimg, first_img))

    start_time = time.time()
    th1.start()
    th2.start()

    # 等待线程结束并获取结果
    r_c, roi_c, color_c = th1.join()
    r_color, roi_color, color_color = th2.join()

    end_time = time.time()
    print(f"预测完成，耗时 {end_time - start_time:.2f} 秒。")

    # --- 5. 在控制台显示结果 ---
    print("\n" + "=" * 30)
    print("           识别结果")
    print("=" * 30)

    # 结果 1 (基于形状)
    print(f"\n[方法 1: 形状定位]")
    print(f"  识别结果: {r_c}")
    print(f"  车牌颜色: {color_c}")

    # 结果 2 (基于颜色)
    print(f"\n[方法 2: 颜色定位]")
    print(f"  识别结果: {r_color}")
    print(f"  车牌颜色: {color_color}")
    print("\n" + "=" * 30)
    return r_c, r_color

    # --- 6. (可选) 使用 OpenCV 显示结果图像 ---
    # 如果需要显示裁剪出的车牌，请取消下面代码的注释

    # show_images = False
    # if r_c is not None and len(r_c) > 0:
    #     cv2.imshow("Shape-based ROI (形状定位结果)", roi_c)
    #     show_images = True

    # if r_color is not None and len(r_color) > 0:
    #     cv2.imshow("Color-based ROI (颜色定位结果)", roi_color)
    #     show_images = True

    # if show_images:
    #     print("\n正在显示结果图像... 在图像窗口按任意键关闭。")
    #     cv2.waitKey(0)  # 等待按键
    #     cv2.destroyAllWindows() # 关闭所有 OpenCV 窗口
    # else:
    #     print("\n未找到可显示的车牌图像。")

    print("处理完毕。")


# --- 脚本入口 ---
if __name__ == '__main__':

    # ==========================================================
    # ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
    #
    #  *** 请在这里填写你的图片路径 ***
    #
    #  示例 (Windows): r"C:\images\chepai.jpg"
    #  示例 (Mac/Linux): "/home/user/images/chepai.png"
    #  (使用 r"..." 可以避免转义斜杠)
    #
    IMAGE_PATH = r"E:\Study\School\LabView-OpenCV\车牌J.jpg"
    #
    # ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
    # ==========================================================

    if IMAGE_PATH == r"请替换为你的图片文件路径.jpg":
        print("=" * 50)
        print("错误: 请先在脚本中修改 'IMAGE_PATH' 变量为你自己的图片路径。")
        print("=" * 50)
    else:
        run_prediction(IMAGE_PATH)
