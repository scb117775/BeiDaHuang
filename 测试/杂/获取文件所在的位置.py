import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

# 使用 os.path.dirname 获取文件路径，但不包含文件名
directory_path = os.path.dirname(file_path)

print(directory_path)