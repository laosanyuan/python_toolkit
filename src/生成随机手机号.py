from openpyxl import Workbook
from faker import Faker

fake = Faker('zh_CN')  # 创建中文环境的 Faker 对象

# 生成随机中国人姓名和手机号
def generate_random_info():
    name = fake.name()
    phone = fake.phone_number()
    return name, phone

# 生成多个随机中国人姓名和手机号
def generate_random_infos(num):
    infos = []
    for _ in range(num):
        name, phone = generate_random_info()
        infos.append((name, phone))
    return infos

# 生成1000个随机中国人姓名和手机号
infos = generate_random_infos(5000)

# 创建一个新的 Excel 文件
workbook = Workbook()
sheet = workbook.active

# 将数据写入 Excel 文件
sheet.append(["姓名", "手机号"])  # 写入表头
for name, phone in infos:
    sheet.append([name, phone])

# 保存 Excel 文件
workbook.save("random_data.xlsx")
