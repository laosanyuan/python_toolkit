from PIL import Image


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def classify_colors(image_path, output_path, threshold, target_color):
    """替换图片背景颜色

    Args:
        image_path (_type_): _description_
        output_path (_type_): _description_
        threshold (_type_): _description_
        target_color (_type_): _description_
    """
    try:
        # 将十六进制格式的颜色转换为 RGB 颜色值
        target_color = hex_to_rgb(target_color)

        # 打开图片
        image = Image.open(image_path)

        # 转换为RGB模式，以便处理彩色图片
        image = image.convert("RGB")

        # 获取图片的宽度和高度
        width, height = image.size

        # 创建一个新的空白图片，与原图尺寸相同
        new_image = Image.new("RGB", (width, height))

        # 遍历原图像的每一个像素
        for x in range(width):
            for y in range(height):
                pixel_color = image.getpixel((x, y))

                # 计算像素的灰度值（用RGB三个通道的平均值表示）
                gray = sum(pixel_color) // 3

                # 判断灰度值是否大于阈值
                if gray < threshold:
                    # 深色部分替换为指定颜色
                    new_image.putpixel((x, y), target_color)
                else:
                    # 浅色部分替换为白色
                    new_image.putpixel((x, y), (255, 255, 255))

        # 保存处理后的图片
        new_image.save(output_path)

        print("颜色二值分类完成。")
    except Exception as e:
        print("发生错误：", str(e))


# 调用函数来转换背景颜色
input_image_path = "D:\output_image.jpg"   # 替换为你的输入图片路径
output_image_path = "output_image.jpg"  # 替换为输出图片路径
target_color = "#242C3B"
threshold = 128  # 替换为阈值，灰度值大于阈值为深色，灰度值小于等于阈值为浅色
classify_colors(input_image_path, output_image_path, threshold, target_color)
