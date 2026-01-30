import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd

# 1. 한화오션(042660) 데이터 가져오기 (2024년 ~ 2026년 1월 23일)
df = fdr.DataReader('042660', '2024-01-01', '2026-01-23')

# 2. 월별 평균 데이터로 계산하기
df_monthly = df['Close'].resample('ME' \
'gi').mean()

# 3. 점선 그래프 그리기
plt.figure(figsize=(10, 5))
plt.plot(df_monthly.index, df_monthly.values, marker='o', linestyle='--', color='blue')
plt.title('Hanwha Ocean Stock Price (Monthly Average)')
plt.grid(True)

# 4. 그래프 저장 및 엑셀 저장
plt.savefig('stock_chart.png') # 그래프 이미지 저장
df.to_excel('hanwha_ocean.xlsx') # 데이터 엑셀 저장
print("작업 완료! 엑셀 파일과 그래프 이미지가 생겼어요.")