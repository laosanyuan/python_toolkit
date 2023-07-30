from PIL import Image


def invert_colors(image_path, output_path):
    """翻转图片颜色

    Args:
        image_path (_type_): _description_
        output_path (_type_): _description_
    """
    try:
        # 打开图片
        image = Image.open(image_path)

        # 获取图片的尺寸
        width, height = image.size

        # 创建一个新的空白图片，与原图尺寸相同
        inverted_image = Image.new("RGB", (width, height))

        # 遍历每个像素点，对颜色值进行反转
        for x in range(width):
            for y in range(height):
                pixel_color = image.getpixel((x, y))
                inverted_color = tuple(255 - value for value in pixel_color)
                inverted_image.putpixel((x, y), inverted_color)

        # 保存处理后的图片
        inverted_image.save(output_path)

        print("图片颜色反转完成。")
    except Exception as e:
        print("发生错误：", str(e))



# 调用函数来反转图片颜色
input_image_path = "D:\微信图片_20230730195644.jpg"   # 替换为你的输入图片路径
output_image_path = "D:\output_image.jpg" # 替换为输出图片路径
invert_colors(input_image_path, output_image_path)

