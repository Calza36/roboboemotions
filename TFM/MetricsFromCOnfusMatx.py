
import pandas as pd
import numpy as np

# Cargamos los datos de la tabla de confusión proporcionada por el usuario
confusion_matrix_data = np.array([
[6, 0, 0, 0],
 [0, 8, 8, 0],
 [1, 1, 2, 0],
 [1, 0, 2, 1]
])


# Vamos a calcular las métricas de manera manual

# Inicializamos los contenedores para las métricas de cada clase
precision_per_class = []
recall_per_class = []
f1_score_per_class = []

# Creamos las etiquetas para las clases
#classes = ['Happy', 'Angry', 'Neutral', 'Fear', 'Surprise', 'Sad', 'Disgust']
classes = ['Happy', 'Negativo', 'Neutral', 'Surprise']

# Calculamos las métricas para cada clase
for i in range(len(classes)):
    TP = confusion_matrix_data[i, i]
    FP = confusion_matrix_data[:, i].sum() - TP
    FN = confusion_matrix_data[i, :].sum() - TP
    TN = confusion_matrix_data.sum() - TP - FP - FN
    
    # Calculamos la precisión, recall y f1-score para cada clase
    precision = TP / (TP + FP) if TP + FP > 0 else 0
    recall = TP / (TP + FN) if TP + FN > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    
    precision_per_class.append(precision)
    recall_per_class.append(recall)
    f1_score_per_class.append(f1)

# # Calculamos las métricas generales
# TP_general = sum([confusion_matrix_data[i, i] for i in range(len(classes))])
# total_predictions = confusion_matrix_data.sum()
# FP_general = total_predictions - TP_general
# FN_general = FP_general

# precision_general = TP_general / (TP_general + FP_general) if TP_general + FP_general > 0 else 0
# recall_general = TP_general / (TP_general + FN_general) if TP_general + FN_general > 0 else 0
# f1_general = 2 * precision_general * recall_general / (precision_general + recall_general) if (precision_general + recall_general) > 0 else 0
# accuracy_general = TP_general / total_predictions if total_predictions > 0 else 0

# Organizamos las métricas en un DataFrame para mejor visualización
metrics_manual = pd.DataFrame({
    'Emocion': classes,   # + ['General'],
    'Precision': precision_per_class,  # + [precision_general],
    'Recall': recall_per_class,  # + [recall_general],
    'F1-Score': f1_score_per_class # + [f1_general],
    #'Accuracy': [None] * len(classes) + [accuracy_general]  # La exactitud se da solo a nivel general
})
print("Métricas calculadas de manera manual: Emotion2Vec para mis Audios")
print(metrics_manual)

#prepare the confusion matrix to be imported into a CSV file
confusion_matrix = pd.DataFrame(confusion_matrix_data, columns=classes, index=classes)
confusion_matrix['Total'] = confusion_matrix.sum(axis=1)
confusion_matrix.loc['Total'] = confusion_matrix.sum(axis=0)

#Save the confusion matrix and the metrics to the same CSV file for easy comparison
output_csv_path = r"D:\Master\Testis\ComprobacionResultados\CombinacionEmociones\MetCombExp7MayProb.csv" 
confusion_matrix.to_csv(output_csv_path, index=True)
divider = pd.DataFrame(index=[''])
divider.to_csv(output_csv_path, mode='a')
metrics_manual.to_csv(output_csv_path, mode='a', index=True)




