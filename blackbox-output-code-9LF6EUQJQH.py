from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc
from sklearn.preprocessing import StandardScaler
import joblib
import matplotlib.pyplot as plt

# Load processed data
X = pd.read_csv('processed_features.csv')
y = pd.read_csv('labels.csv').values.ravel()

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Random Forest for classification
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    min_samples_split=10,
    random_state=42
)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# Isolation Forest for anomaly detection (treats attacks as anomalies)
iso_model = IsolationForest(
    contamination=0.05,  # Assume 5% anomalies
    n_estimators=100,
    random_state=42
)
iso_model.fit(X_train)
iso_pred = iso_model.predict(X_test)  # -1 for anomaly (attack), 1 for normal

# Ensemble: Combine predictions (e.g., if RF says attack or ISO says anomaly, flag as attack)
ensemble_pred = np.where((rf_pred == 1) | (iso_pred == -1), 1, 0)

# Evaluate
accuracy = accuracy_score(y_test, ensemble_pred)
precision = precision_score(y_test, ensemble_pred)
recall = recall_score(y_test, ensemble_pred)
f1 = f1_score(y_test, ensemble_pred)
cm = confusion_matrix(y_test, ensemble_pred)
fpr = cm[0][1] / (cm[0][0] + cm[0][1])  # False Positive Rate

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"False Positive Rate: {fpr:.4f}")

# Plot ROC Curve
fpr_roc, tpr_roc, _ = roc_curve(y_test, rf_model.predict_proba(X_test)[:, 1])
roc_auc = auc(fpr_roc, tpr_roc)
plt.figure()
plt.plot(fpr_roc, tpr_roc, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.savefig('roc_curve.png')
plt.show()

# Save models
joblib.dump(rf_model, 'rf_model.pkl')
joblib.dump(iso_model, 'iso_model.pkl')
joblib.dump(scaler, 'scaler.pkl')