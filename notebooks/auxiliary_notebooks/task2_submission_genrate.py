import pandas as pd

# Leer los archivos CSV
path = # insert csv path
df1 = pd.read_csv(path+'Multi-CLIP(ST)_FINAL.csv', header=None) # predictions for task 1 csv
df2 = pd.read_csv(path+'Multi-CLIP(ST)_FINAL_TASK_2.csv', header=None) # predictions for task 2 csv
nuevas_filas = []


for idx, fila in df1.iterrows():
    if fila[0] == 0:
        nueva_fila = [0, 0, 0] + fila.tolist()
    elif fila[0] == 1:
        nueva_fila = df2.iloc[idx].tolist() + [0, 0]
    nuevas_filas.append(nueva_fila)

df_nuevo = pd.DataFrame(nuevas_filas)

df_nuevo.to_csv('Multi-CLIP(ST)_FINAL_TASK_2.csv', index=False, header=False)