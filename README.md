# 航空旅客滿意度分析

## 專案簡介
 **航班延誤如何影響旅客滿意度，應該優先改善哪些因素？** <small>透過分析航班延誤、艙等與旅客忠誠度，找出影響滿意度的關鍵因素，並提出可執行的營運策略。

---

## 核心發現
- **當航班延誤超過15分鐘時，滿意度明顯下降**，影響在經濟艙最為顯著
- **商務艙旅客對延誤較不敏感**，顯示價格與服務品質具緩衝效果
- **忠誠旅客在延誤情境下仍維持較高滿意度**，有助於降低顧客流失
 
---

## 商業建議
基於分析結果與影響程度評估：
- 優先控制延誤時間（最高影響） → 建議將平均延誤控制在 15 分鐘內，以避免滿意度顯著下降
- 針對經濟艙提供補償機制（高CP策略） → 結合空服員實務經驗，經濟艙旅客對延誤的不滿多來自資訊透明度與補償不足。透過餐券或里程補償，可有效提升延誤情境下的滿意度
- 強化忠誠計畫（長期策略） → 提高顧客對負面體驗的容忍度，降低流失率

---

## 視覺化成果
![航空旅客滿意度儀表板](Dashboard.png)

---

## 模型分析
為了進一步量化各因素對滿意度的影響，本專案使用模型分析建立預測模型：

- 目標變數：滿意 / 不滿意
- 特徵變數：
  - 航班延誤時間
  - 艙等
  - 旅客類型（忠誠 vs 非忠誠）

## 模型洞察
- 延誤時間為**最顯著負向影響因子**
- 商務艙與忠誠旅客具有**正向影響係數**
- 模型結果與探索性分析一致，強化結論可信度
  
![Logistic Regression 分析結果](Dashboard_1.png)


👉 [查看 Tableau Public 互動版儀表板](https://public.tableau.com/views/AirlinePassengerSatisfactionAnalysis_17768549589120/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

👉 [查看進階分析儀表板（Drivers Analysis）](https://public.tableau.com/views/AirlineSatisfactionDrivers/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_lin)

<small>👉 English version available at [Airline Passenger Satisfaction Analysis](https://github.com/hlr95035339/Airline-Passenger-Satisfaction-Analysis)</small>

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
- 使用 Python（Pandas）進行資料清理與探索性分析
- 分析延誤時間與滿意度之關聯
- 使用 Logistic Regression 建立預測模型
- 使用 Tableau 建立互動式儀表板，支援決策分析
  

---

## 專案價值
展示數據分析到商業決策的完整流程，能協助企業：
- 找出影響顧客滿意度的關鍵因素
- 制定優先改善策略
- 在提升服務品質的同時優化營運成本
  
---

## 技能展示
- Python（資料清理、探索性分析）
- Tableau（儀表板設計與數據敘事）
- Logistic Regression（預測建模）
- 商業分析與洞察轉化
