import requests
from bs4 import BeautifulSoup
import csv
import time

# 定义获取单页电影信息的函数
def get_movies(url):
    headers = {
        # 设置请求头，模拟浏览器访问，防止被网站屏蔽
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    # 发送HTTP GET请求获取网页内容
    response = requests.get(url, headers=headers)
    # 用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = []
    # 选择所有电影条目
    for item in soup.select('.board-wrapper dd'):
        # 提取电影名称
        title = item.select_one('.name a').text.strip()
        # 提取主演信息
        star = item.select_one('.star').text.strip()
        # 提取上映时间
        release_time = item.select_one('.releasetime').text.strip()
        # 提取评分的整数部分
        score_int = item.select_one('.integer').text.strip()
        # 提取评分的小数部分
        score_frac = item.select_one('.fraction').text.strip()
        # 拼接成完整评分
        score = score_int + score_frac
        # 将电影信息添加到列表
        movies.append([title, star, release_time, score])
    return movies

# 定义保存数据到CSV文件的函数
def save_to_csv(movies):
    # 以写模式打开CSV文件，设置编码为utf-8-sig以兼容Excel
    with open('maoyan_top100.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        # 写入表头
        writer.writerow(['电影名', '主演', '上映时间', '评分'])
        # 写入所有电影数据
        writer.writerows(movies)

if __name__ == '__main__':
    all_movies = []
    # 猫眼TOP100分10页，每页10部电影，offset参数控制页码
    for i in range(0, 100, 10):
        url = f'https://maoyan.com/board/4?offset={i}'
        # 获取当前页的电影信息并添加到总列表
        all_movies.extend(get_movies(url))
        time.sleep(1)  # 防止请求过快被封，休眠1秒
    # 保存所有电影信息到CSV文件
    save_to_csv(all_movies)