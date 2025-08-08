import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.naver?code=KPI200"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="tbl_1")
stocks = []

if table:
    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        # class="ctg"인 td가 있는 행만 처리 (실제 종목 데이터 행)
        if cols and cols[0].get("class") and "ctg" in cols[0].get("class"):
            stock = {
                "종목명": cols[0].find("a").get_text(strip=True),
                "현재가": cols[1].get_text(strip=True).replace(",", ""),
                "전일비": cols[2].find("span", class_="tah").get_text(strip=True).replace(",", ""),
                "등락률": cols[3].find("span", class_="tah").get_text(strip=True).strip(),
                "거래량": cols[4].get_text(strip=True).replace(",", ""),
                "거래대금": cols[5].get_text(strip=True).replace(",", ""),
                "시가총액": cols[6].get_text(strip=True).replace(",", "")
            }
            stocks.append(stock)

print("\n코스피200 편입종목 상위 리스트:")
for stock in stocks:
    print(f"종목명: {stock['종목명']}")
    print(f"현재가: {stock['현재가']}원")
    print(f"전일비: {stock['전일비']}")
    print(f"등락률: {stock['등락률']}")
    print(f"거래량: {stock['거래량']}")
    print(f"거래대금: {stock['거래대금']}백만")
    print(f"시가총액: {stock['시가총액']}억")
    print("-" * 50)