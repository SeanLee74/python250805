import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4&ackey=m8s4jbq1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 기사 제목 추출
titles = []
for span in soup.select('span.sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1.sds-comps-text-type-headline1'):
    titles.append(span.get_text(strip=True))

# 엑셀 저장
wb = Workbook()
ws = wb.active
ws.title = "Naver News"
ws.append(["번호", "기사 제목"])
for idx, title in enumerate(titles, start=1):
    ws.append([idx, title])

wb.save("naverResult.xlsx")
print("엑셀 파일로 저장되었습니다.")