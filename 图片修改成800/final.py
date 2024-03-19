from PIL import Image
import os


def resize_image(image_path, output_folder, max_size=800):
    # 打开图片
    image = Image.open(image_path)

    image = image.convert("RGB")
    # 获取图片的原始大小
    width, height = image.size
    # 如果图片的宽度或高度大于800像素，则进行缩放
        # 计算缩放比例
    scale = min(max_size / width, max_size / height)
    # 计算新的宽度和高度
    new_width = int(width * scale)
    new_height = int(height * scale)
    # 缩放图片
    resized_image = image.resize((new_width, new_height))
    # 保存缩放后的图片
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    resized_image.save(output_path)


    # 图片所在的文件夹路径

def process_transparent_images(image_folder, output_folder):
    # 创建保存文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 遍历图像文件
    for filename in os.listdir(image_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            # 图像路径
            image_path = os.path.join(image_folder, filename)

            # 打开透明图片
            image = Image.open(image_path)
            image = image.convert("RGBA")

            # 创建白底背景
            background = Image.new("RGBA", (800, 800), (255, 255, 255))

            # 计算居中位置
            x = (background.width - image.width) // 2
            y = (background.height - image.height) // 2

            # 将透明图片放置在背景上
            background.paste(image, (x, y), image)
            # 保存图片
            output_path = os.path.join(output_folder, filename)
            background.save(output_path, format="PNG")

image_folder = ""
# 新建输出文件路径
os.mkdir(image_folder+'out/')
# 输出文件夹路径
output_folder = image_folder+'out/'
# 遍历文件夹中的所有图片文件
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # 根据需要调整文件类型
        image_path = os.path.join(image_folder, filename)
        resize_image(image_path, output_folder)
process_transparent_images(output_folder, output_folder)

#维护路径  最后不带/