import os

import markdown
from pdfkit import pdfkit


def convert_markdown_to_pdf(directory, output_directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            print(path)

            # 读取 Markdown 文件
            with open(path, 'r', encoding='utf-8') as file:
                md_text = file.read()

            # 将 Markdown 转换为 HTML
            html = markdown.markdown(md_text)

            tmp_htmp_file = os.path.join(
                output_directory, path.replace('.md', '.html'))
            with open(os.path.join(output_directory, tmp_htmp_file), 'w', encoding='utf-8') as tmp_file:
                tmp_file.write(html)

            options = {
                'page-size': 'A4',
                'encoding': "UTF-8",
                'custom-header': [
                    ('Accept-Charset', 'ISO-8859-1,utf-8'),
                    ('Accept-Language', 'en-US,en;q=0.8'),
                ],
                'no-outline': True
            }

            kit = pdfkit.PDFKit(tmp_htmp_file, 'file', options=options)
            kit.to_pdf(os.path.join(output_directory,
                       file.name.split('\\')[-1].replace('.md', '.pdf')))
            
            os.remove(tmp_htmp_file)


# 需要安装wkhtmltopdf
os.environ['Path'] = 'D:\\Software\\wkhtmltopdf\\bin'
directory = 'd:\\新建文件夹'
output_directory = 'd:\\输出'

convert_markdown_to_pdf(directory, output_directory)
