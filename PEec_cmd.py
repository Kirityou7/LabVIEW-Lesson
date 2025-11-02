import threading
import time
import cv2
from threading import Thread
import os
import sys  # 导入 sys 模块来处理命令行参数
import io  # 导入 io 模块来设置输出编码

# --- 确保标准输出使用 UTF-8 编码 ---
# 这对于LabVIEW正确捕获中文结果至关重要
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='ansi')

try:
    import img_function as predict
    import img_math
except ImportError:
    print("ERROR: 无法导入自定义模块 'img_function' 或 'img_math'。")
    sys.exit(1)  # 退出并返回错误码


# (ThreadWithReturnValue 类的代码保持不变)
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
        self._return1 = None
        self._return2 = None
        self._return3 = None

    def run(self):
        if self._target is not None:
            self._return1, self._return2, self._return3 = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return1, self._return2, self._return3


# (run_prediction 函数修改为返回结果，而不是打印)
def run_prediction(image_path):
    """
    运行车牌识别逻辑并返回结果。
    """

    # 1. 检查文件
    if not os.path.exists(image_path):
        return f"ERROR: 文件未找到 {image_path}", "ERROR: N/A"

    # 2. 初始化识别器 (只在需要时初始化)
    # 为了效率，我们可以将 predictor 设为全局变量，只初始化一次
    # 但对于命令行脚本，每次运行重新初始化更简单
    try:
        predictor = predict.CardPredictor()
        predictor.train_svm()
    except Exception as e:
        return f"ERROR: 初始化SVM失败 {e}", "ERROR: N/A"

    # 3. 读取和预处理图像
    try:
        img_bgr = img_math.img_read(image_path)
        if img_bgr is None:
            return f"ERROR: 无法读取图像 {image_path}", "ERROR: N/A"
        first_img, oldimg = predictor.img_first_pre(img_bgr)
    except Exception as e:
        return f"ERROR: 预处理图像失败 {e}", "ERROR: N/A"

    # 4. 并行运行预测
    th1 = ThreadWithReturnValue(target=predictor.img_color_contours,
                                args=(first_img, oldimg))
    th2 = ThreadWithReturnValue(target=predictor.img_only_color,
                                args=(oldimg, oldimg, first_img))

    th1.start()
    th2.start()

    r_c, _, _ = th1.join()  # 形状定位结果
    r_color, _, _ = th2.join()  # 颜色定位结果

    # 5. 返回两个需要的结果
    return r_c, r_color


# --- 脚本主入口 ---
if __name__ == '__main__':

    # 1. 检查是否传入了足够的参数 (脚本名 + 1个图片路径)
    if len(sys.argv) != 2:
        print("ERROR: 脚本需要一个图片路径作为参数。")
        sys.exit(1)

    # 2. 从命令行获取图片路径
    image_path_from_labview = sys.argv[1]

    # 3. 运行预测
    r_c_result, r_color_result = run_prediction(image_path_from_labview)

    # 4. *** 关键步骤 ***
    # 以LabVIEW易于解析的格式打印结果
    # 我们使用一个特殊的分隔符，比如 "|||"

    # 处理None或空字符串的情况，确保有东西输出
    r_c_safe = r_c_result if r_c_result else "NULL"
    r_color_safe = r_color_result if r_color_result else "NULL"
    if r_c_safe != "NULL":
        r_c_output = ''
        for i in r_c_safe:
            r_c_output += i
    else:
        r_c_output = "未识别"
    if r_color_safe != "NULL":
        r_color_output = ''
        for i in r_color_safe:
            r_color_output += i

    # 打印到标准输出
    print(f"{r_c_output}|||{r_color_output}")