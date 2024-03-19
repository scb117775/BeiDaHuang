import tkinter as tk
from tkinter import filedialog
import warnings
warnings.filterwarnings('ignore')
# 创建主窗口
root = tk.Tk()
# 隐藏主窗口
root.withdraw()

# 打开文件选择对话框
file_path = filedialog.askopenfilename()

# 显示选择的文件路径
print("选择的文件路径是：", file_path)