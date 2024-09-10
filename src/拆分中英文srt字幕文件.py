import os
import re


def split_srt(input_file, output_cn_folder, output_en_folder):
    with open(input_file, 'r', encoding='ansi') as f:
        content = f.read()

    # 分割每个字幕块
    subtitle_blocks = re.split(r'\n\n', content.strip())

    cn_srt = []
    en_srt = []
    new_index = 1  # 用于重新编号

    for block in subtitle_blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            time = lines[1]
            text = '\n'.join(lines[2:])

            # 分离中文和英文
            text_lines = text.split('\n')
            cn_text = ''
            en_text = ''

            for line in text_lines:
                if re.search(r'[\u4e00-\u9fff]', line):
                    cn_text = line
                elif re.search(r'[a-zA-Z]', line):
                    en_text = line

            # 只有当中英文都存在时，才添加到结果中，并使用新的序号
            if cn_text and en_text:
                cn_srt.append(f"{new_index}\n{time}\n{cn_text}\n")
                en_srt.append(f"{new_index}\n{time}\n{en_text}\n")
                new_index += 1  # 增加序号

    # 写入中文SRT文件
    output_cn = os.path.join(output_cn_folder, os.path.basename(input_file))
    with open(output_cn, 'w', encoding='ansi') as f:
        f.write('\n\n'.join(cn_srt))  # 使用两个换行符分隔字幕块

    # 写入英文SRT文件
    output_en = os.path.join(output_en_folder, os.path.basename(input_file))
    with open(output_en, 'w', encoding='ansi') as f:
        f.write('\n\n'.join(en_srt))  # 使用两个换行符分隔字幕块


def process_folder(input_folder, output_folder):
    output_cn_folder = os.path.join(output_folder, '中文字幕')
    output_en_folder = os.path.join(output_folder, '英文字幕')

    if not os.path.exists(output_cn_folder):
        os.makedirs(output_cn_folder)
    if not os.path.exists(output_en_folder):
        os.makedirs(output_en_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.srt'):
            input_path = os.path.join(input_folder, filename)
            split_srt(input_path, output_cn_folder, output_en_folder)
            print(f"处理完成: {filename}")


# 使用示例
input_folder = 'D:\\The.Big.Bang.Theory.S01.720p.BluRay.x264-SiNNERS.chs&eng'
output_folder = 'D:\\The.Big.Bang.Theory.S01.720p.BluRay.x264-SiNNERS.chs&eng'
process_folder(input_folder, output_folder)
