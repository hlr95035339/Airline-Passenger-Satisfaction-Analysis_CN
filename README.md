# 航空旅客滿意度分析

## 專案簡介
本專案使用 Kaggle 公開資料集 **test.csv**，並透過 Python (`script.py`) 進行數據清理與分析，搭配 Tableau 建立互動式儀表板，探討 **航班延誤、艙等、旅客忠誠度** 對旅客滿意度的影響。

---

## 數據來源
- Kaggle Airline Passenger Satisfaction Dataset (`test.csv`)
- 主要欄位：
  - 滿意度 (Satisfaction)
  - 艙等 (Economy, Economy Plus, Business)
  - 旅客類型 (忠誠 vs 非忠誠)
  - 航班延誤時間 (Arrival Delay in Minutes)

---

## 分析方法
- **Python (`script.py`)**
  - 使用 Pandas 進行資料清理與轉換
  - 計算延誤與滿意度的相關性
  - 分組比較不同艙等與旅客類型的差異
- **Tableau**
  - 建立 KPI 卡片、長條圖、散點圖、圓餅圖
  - 儀表板整合，提供互動式探索

---

## 視覺化成果
![航空旅客滿意度儀表板](Dashboard.png)

👉 [查看 Tableau Public 互動版儀表板](https://public.tableau.com/views/AirlinePassengerSatisfactionAnalysis_17768549589120/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

 <small> 👉 English version available at [Airline Passenger Satisfaction Analysis](https://github.com/hlr95035339/Airline-Passenger-Satisfaction-Analysis)   
---

## 商業洞察
- **延誤顯著降低滿意度**，尤其在經濟艙旅客中更明顯。  
- **商務艙旅客**對延誤的容忍度較高。  
- **忠誠旅客**在延誤情況下仍維持較高滿意度，顯示忠誠計畫的重要性。  
- **營運 KPI 建議**：將平均延誤控制在 15 分鐘以內，以維持整體滿意度。  

---

## 結論
透過改善航班準點率、加強經濟艙補償措施，以及強化忠誠計畫，航空公司能有效提升旅客滿意度並促進長期收益。

---

## 展示技能
- Python 數據分析 (`script.py`)  
- Tableau 儀表板設計與 KPI 故事化  
- 商業洞察與策略建議  
