import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Defining the confusion matrix
confusion_matrix = [
[6, 0, 0, 0],
 [0, 8, 8, 0],
 [1, 1, 2, 0],
 [1, 0, 2, 1]
]

# Flattening the confusion matrix for true and predicted labels
y_true = []
y_pred = []
for i in range(len(confusion_matrix)):
    for j in range(len(confusion_matrix[i])):
        y_true.extend([i] * confusion_matrix[i][j])
        y_pred.extend([j] * confusion_matrix[i][j])

# Calculating metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='macro', zero_division=0)
recall = recall_score(y_true, y_pred, average='macro', zero_division=0)
f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)


# Creating a DataFrame with the results
results = pd.DataFrame({
    "Metrica": ["Accuracy", "Precision", "Recall", "F1 Score"],
    "Valor": [accuracy, precision, recall, f1]
})

# Saving the results to an Excel file
results.to_excel(r"D:\Master\Testis\ComprobacionResultados\CombinacionEmociones\MetGenCombExp7MayProb.xlsx", index=False)

results