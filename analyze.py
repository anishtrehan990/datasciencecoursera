from pathlib import Path
import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

root = Path(__file__).resolve().parent
url = 'https://d396qusza40orc.cloudfront.net/predmachlearn/pml-{}.csv'
for kind in ('training', 'testing'):
    path = root / f'pml-{kind}.csv'
    if not path.exists():
        pd.read_csv(url.format(kind), low_memory=False).to_csv(path, index=False)
train = pd.read_csv(root / 'pml-training.csv', low_memory=False,
                    na_values=['#DIV/0!', 'NA', ''])
test = pd.read_csv(root / 'pml-testing.csv', low_memory=False,
                   na_values=['#DIV/0!', 'NA', ''])
# The first seven columns identify users, times or collection windows.
# Retain sensor measurements present in every training and test row.
features = [c for c in train.columns[7:-1]
            if pd.api.types.is_numeric_dtype(train[c])
            and train[c].notna().all() and test[c].notna().all()]
X, y = train[features], train['classe']
X_dev, X_val, y_dev, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
def forest():
    return RandomForestClassifier(n_estimators=100, random_state=42,
                                  n_jobs=-1)
cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
cv_accuracy = cross_val_score(forest(), X_dev, y_dev, cv=cv,
                              scoring='accuracy', n_jobs=1)
model = forest().fit(X_dev, y_dev)
validation_predictions = model.predict(X_val)
validation_accuracy = accuracy_score(y_val, validation_predictions)
final_model = forest().fit(X, y)
predictions = final_model.predict(test[features])
(root / 'predictions.txt').write_text('\n'.join(predictions) + '\n')
summary = {
    'n_training': len(train), 'n_testing': len(test), 'n_features': len(features),
    'n_development': len(X_dev), 'n_validation': len(X_val),
    'cv_accuracy': cv_accuracy.tolist(),
    'cv_mean': float(cv_accuracy.mean()),
    'validation_accuracy': float(validation_accuracy),
    'validation_error': float(1-validation_accuracy),
    'confusion': confusion_matrix(y_val, validation_predictions,
                                  labels=list('ABCDE')).tolist(),
    'predictions': predictions.tolist(), 'features': features,
}
(root / 'results.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps({k:v for k,v in summary.items() if k != 'features'}, indent=2))
