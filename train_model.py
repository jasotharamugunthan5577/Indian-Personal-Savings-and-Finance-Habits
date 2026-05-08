import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import pickle
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("💎 WEALTHWISE AI - MODEL TRAINING")
print("=" * 60)

# Load data
df = pd.read_csv('data.csv')
print(f"\n📊 Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Display unique values
print(f"\n📋 Unique Occupations: {df['Occupation'].unique().tolist()}")
print(f"📋 Unique City Tiers: {df['City_Tier'].unique().tolist()}")

# Encode categorical variables
le_occupation = LabelEncoder()
le_city = LabelEncoder()

df['Occupation_encoded'] = le_occupation.fit_transform(df['Occupation'].astype(str))
df['City_Tier_encoded'] = le_city.fit_transform(df['City_Tier'].astype(str))

# Feature columns
feature_cols = ['Income', 'Age', 'Dependents', 'Occupation_encoded', 'City_Tier_encoded', 
                'Rent', 'Loan_Repayment', 'Insurance', 'Groceries', 'Transport', 
                'Eating_Out', 'Entertainment', 'Utilities', 'Healthcare', 'Education', 'Miscellaneous']

X = df[feature_cols].fillna(0)

# Train model 1: Disposable Income Prediction
print("\n🎯 Training Disposable Income Model...")
y_disposable = df['Disposable_Income'].fillna(0)
X_train, X_test, y_train, y_test = train_test_split(X, y_disposable, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_regressor = RandomForestRegressor(n_estimators=150, max_depth=12, random_state=42)
model_regressor.fit(X_train_scaled, y_train)
print(f"✅ Regressor R² Score: {model_regressor.score(X_test_scaled, y_test):.4f}")

# Train model 2: Savings Category Classifier
print("\n🎯 Training Savings Level Classifier...")
# Create savings categories based on desired savings percentage
df['Savings_Category'] = pd.cut(df['Desired_Savings_Percentage'], 
                                 bins=[0, 10, 20, 30, 100], 
                                 labels=['Low', 'Medium', 'High', 'Excellent'])

le_savings = LabelEncoder()
y_savings = le_savings.fit_transform(df['Savings_Category'].astype(str))

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X, y_savings, test_size=0.2, random_state=42)
X_train_s_scaled = scaler.fit_transform(X_train_s)
X_test_s_scaled = scaler.transform(X_test_s)

model_classifier = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model_classifier.fit(X_train_s_scaled, y_train_s)
print(f"✅ Classifier Accuracy: {model_classifier.score(X_test_s_scaled, y_test_s):.4f}")

# Calculate dataset averages for comparison
avg_data = {
    'avg_income': df['Income'].mean(),
    'avg_expenses': (df['Rent'].mean() + df['Loan_Repayment'].mean() + df['Insurance'].mean() + 
                    df['Groceries'].mean() + df['Transport'].mean() + df['Eating_Out'].mean() + 
                    df['Entertainment'].mean() + df['Utilities'].mean() + df['Healthcare'].mean() + 
                    df['Education'].mean() + df['Miscellaneous'].mean()),
    'avg_savings_percent': df['Desired_Savings_Percentage'].mean(),
    'avg_glucose': df['Potential_Savings_Groceries'].mean() if 'Potential_Savings_Groceries' in df.columns else 0,
    'avg_transport': df['Potential_Savings_Transport'].mean() if 'Potential_Savings_Transport' in df.columns else 0,
    'avg_entertainment': df['Potential_Savings_Entertainment'].mean() if 'Potential_Savings_Entertainment' in df.columns else 0,
}

# Save all models
with open('financial_model.pkl', 'wb') as f:
    pickle.dump(model_regressor, f)
with open('financial_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('label_encoders.pkl', 'wb') as f:
    pickle.dump({'occupation': le_occupation, 'city': le_city, 'savings': le_savings}, f)
with open('avg_data.pkl', 'wb') as f:
    pickle.dump(avg_data, f)

print("\n" + "=" * 60)
print("💾 ALL MODELS SAVED SUCCESSFULLY!")
print("=" * 60)