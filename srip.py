import pandas as pd

df = pd.read_csv("test.csv")

# 把滿意度轉成 0/1
df['satisfaction'] = df['satisfaction'].map({
    'satisfied': 1,
    'neutral or dissatisfied': 0
})

features = [
    'Arrival Delay in Minutes',
    'Flight Distance',
    'Inflight wifi service',
    'Seat comfort',
    'Food and drink',
    'Online boarding'
]

X = df[features]
y = df['satisfaction']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

importance = pd.DataFrame({
    'Feature': features,
    'Coefficient': model.coef_[0]
}).sort_values(by='Coefficient', ascending=False)

print(importance)