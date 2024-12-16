import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
# 从 output.txt 文件中读取词频数据
def read_word_frequencies(file_path):
    word_frequencies = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 解析每一行，格式为 "词: 频率,"
            word, freq = line.split(': ')
            freq = int(freq.strip().rstrip(','))
            word_frequencies[word.strip('"')] = freq
    return word_frequencies
# 读取形状图像
mask = np.array(Image.open('MLP.png'))
# 读取词频
word_frequencies = read_word_frequencies('output2.txt')

# 创建词云对象
wordcloud = WordCloud(
    mask=mask,
    font_path='simfang.ttf',  # 指定中文字体路径
    width=800,
    height=400,
    background_color='white'
).generate_from_frequencies(word_frequencies)

# 绘制词云
plt.figure(figsize=(50, 25))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 关闭坐标轴
plt.title('词云示例')
plt.show()
