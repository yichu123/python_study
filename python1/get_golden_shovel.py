# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup

# # 设置Chrome驱动服务
# service = Service(ChromeDriverManager().install())

# # 创建Chrome浏览器实例
# driver = webdriver.Chrome(service=service)

# # 创建空的DataFrame来存储数据
# data = {
#     "英雄名称": [],
#     "英雄技能": [],
#     "技能描述": [],
#     "属性信息": [],
#     "羁绊信息": [],
#     "费用":[]
# }
# print(pd.__version__)
# df = pd.DataFrame(data)

# # 循环遍历英雄ID范围
# # for hero_id in range(1190, 1202):
# # for hero_id in range(2177, 2193):
# # for hero_id in range(3194, 3209):
# # for hero_id in range(4185, 4199):
# for hero_id in range(5158, 5171):
#     try:
#         # 构建URL
#         url = f"https://jcc.qq.com/#/heroDetail/10,S11,10.4.5/{hero_id}"
#         driver.get(url)

#         # 获取页面内容
#         html_content = driver.page_source

#         # 使用Beautiful Soup解析HTML
#         soup = BeautifulSoup(html_content, "html.parser")

#         # 找到英雄详情的容器
#         heroDetailWrap = soup.find("div", class_="hero-detail-wrap")
#         if heroDetailWrap is None:
#             continue

#         # 提取英雄信息
#         hero_name = heroDetailWrap.find("p", class_="name").text
#         hero_skill = heroDetailWrap.find("p", class_="title skill-name").text.strip()
#         hero_skill_description = heroDetailWrap.find("p", class_="active").text.strip()

#         #TODO 费用
#         price_element = heroDetailWrap.find("li", class_="price1")
#         price = price_element.text.strip() if price_element else None

#         # 提取属性信息
#         attributes = heroDetailWrap.find("div", class_="attri").find_all("td")
#         attributes_info = [attr.text for attr in attributes]

#         # 提取羁绊信息
#         synergy_names = heroDetailWrap.find_all("p", class_="title skill-name")

#         # 构建一个字典以便将数据添加到DataFrame
#         hero_data = {
#             "英雄名称": hero_name,
#             "英雄技能": hero_skill,
#             "技能描述": hero_skill_description,
#             "属性信息": "\n".join(attributes_info),
#             "羁绊信息": "\n".join([name.text for name in synergy_names[1:]]),  # 跳过第一个元素（英雄技能）
#             "费用": price
#         }

#         # 将字典转换为DataFrame并追加到现有DataFrame
#         df = df._append(pd.DataFrame(hero_data, index=[0]), ignore_index=True)

#     except Exception as e:
#         print(e)
#         print(f"Hero with ID {hero_id} does not exist.")

# # 关闭浏览器
# driver.quit()

# # 保存DataFrame到Excel文件
# df.to_excel("hero_details_五费.xlsx", index=False)

import requests
from bs4 import BeautifulSoup
import csv

# 获取金铲铲之战TOP10阵容信息的函数
# def get_top10_lineups():
#     # 目标网页URL
#     url = 'https://www.jccwz.com/lineup/top'
#     # 设置请求头，模拟浏览器访问，防止被网站屏蔽
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
#     }
#     # 发送HTTP GET请求获取网页内容
#     response = requests.get(url, headers=headers)
#     # 设置响应内容的编码为utf-8
#     response.encoding = 'utf-8'
#     # 用BeautifulSoup解析HTML内容
#     soup = BeautifulSoup(response.text, 'html.parser')
#     lineups = []
#     # 选择所有阵容条目，只取前10个
#     for item in soup.select('.lineup-list .lineup-item')[:10]:
#         # 提取阵容名称
#         name = item.select_one('.lineup-title').get_text(strip=True)
#         # 提取主C英雄，如果没有则为空字符串
#         main_hero = item.select_one('.main-hero').get_text(strip=True) if item.select_one('.main-hero') else ''
#         # 提取阵容羁绊，如果没有则为空字符串
#         bonds = item.select_one('.lineup-bonds').get_text(strip=True) if item.select_one('.lineup-bonds') else ''
#         # 提取阵容评分，如果没有则为空字符串
#         score = item.select_one('.score').get_text(strip=True) if item.select_one('.score') else ''
#         # 提取推荐装备，多个装备用逗号连接
#         equips = ','.join([e.get_text(strip=True) for e in item.select('.equip-list .equip-name')])
#         # 将阵容信息添加到列表
#         lineups.append([name, main_hero, bonds, score, equips])
#     # 返回包含所有阵容信息的二维列表
#     return lineups

# # 保存阵容信息到CSV文件的函数
# def save_to_csv(lineups):
#     # 以写模式打开CSV文件，设置编码为utf-8-sig以兼容Excel
#     with open('golden_shovel_top10.csv', 'w', newline='', encoding='utf-8-sig') as f:
#         writer = csv.writer(f)
#         # 写入表头
#         writer.writerow(['阵容名称', '主C英雄', '羁绊', '评分', '推荐装备'])
#         # 写入所有阵容数据
#         writer.writerows(lineups)

# # 主程序入口
# if __name__ == '__main__':
#     # 获取TOP10阵容信息
#     lineups = get_top10_lineups()
#     # 保存到CSV文件
#     save_to_csv(lineups)

import requests
import csv

def get_top10_tft_lineups():
    # op.gg 阵容API（S11赛季，需根据实际赛季调整）
    api_url = 'https://op.gg/api/v1.0/internal/bypass/tft/meta-comps?region=cn&type=star'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'accept': 'application/json'
    }
    response = requests.get(api_url, headers=headers)
    data = response.json()
    comps = data['data']['metaComps'][:10]  # 取前10个阵容

    lineups = []
    for comp in comps:
        # 阵容名称
        name = comp.get('name', '')
        # 主C英雄（取carry列表第一个）
        carries = [c['name'] for c in comp.get('carries', [])]
        main_carry = carries[0] if carries else ''
        # 羁绊（取全部羁绊名）
        traits = [t['name'] for t in comp.get('traits', [])]
        bonds = ','.join(traits)
        # 胜率
        win_rate = comp.get('winRate', '')
        # 平均排名
        avg_rank = comp.get('avgPlacement', '')
        # 推荐英雄（全部棋子）
        units = [u['name'] for u in comp.get('units', [])]
        units_str = ','.join(units)
        lineups.append([name, main_carry, bonds, win_rate, avg_rank, units_str])
    return lineups

def save_to_csv(lineups):
    with open('tft_top10_lineups.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['阵容名称', '主C英雄', '羁绊', '胜率', '平均排名', '推荐英雄'])
        writer.writerows(lineups)

if __name__ == '__main__':
    lineups = get_top10_tft_lineups()
    save_to_csv(lineups)

