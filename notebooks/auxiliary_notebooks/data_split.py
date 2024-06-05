import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os
import shutil


def decode_one_hot(dataframe, filename, labels, col_name):
  one_hot_labels = np.genfromtxt(dataset_path+filename, delimiter=',')
  index_labels = np.argmax(one_hot_labels, axis=1)
  labels_train = list(map(lambda x: labels[x], index_labels))

  dataframe.insert(dataframe.shape[1], col_name, labels_train, True)
  return dataframe

dataset_path = "E:/Master/PLN/data/"

split_dataset_path = dataset_path + "split_data/"
if not os.path.exists(split_dataset_path):
        os.mkdir(split_dataset_path)


df = pd.read_csv(dataset_path+"labeled_data.csv", names=["IMG", "Text"])

df = decode_one_hot(df, "labels_subtask_1.csv", ["hate_speech", "inappropiate_content", "none"], "Label_1")

df = decode_one_hot(df, "labels_subtask_2.csv", ["classicism", "racism", "sexism", "other", "inappropiate_content", "none"], "Label_2")


# Primero, divida los datos en entrenamiento (70%) y un conjunto temporal (30%)
df_train, df_test = train_test_split(df, test_size=0.3, random_state=42)

# Ahora, divide el conjunto temporal en conjuntos de validación y prueba (50% cada uno)
df_val, df_test = train_test_split(df_test, test_size=0.5, random_state=42)

# almacenar los splits en archivos .csv
df_train.to_csv(split_dataset_path +'train_data.csv', index=False)
df_val.to_csv(split_dataset_path + 'validation_data.csv', index=False)
df_test.to_csv(split_dataset_path + 'test_data.csv', index=False)


def split_images(dataframe, destination_path):
  if not os.path.exists(destination_path):
          os.mkdir(destination_path)

  for index, row in dataframe.iterrows():
    # Combinar la ruta del directorio con el nombre de la imagen
    img_name = row["IMG"] + ".jpg"
    origin = dataset_path + "labeled_images/" + img_name

    # Copiar la imagen
    shutil.copyfile(origin, destination_path + img_name)

# CUIDADO CREA EL SPLIT DE IMAGENES(TARDA MUCHO)
train_destination_path = split_dataset_path + "train_images/"
split_images(df_train, train_destination_path)

val_destination_path = split_dataset_path + "val_images/"
split_images(df_val, val_destination_path)

test_destination_path = split_dataset_path + "test_images/"
split_images(df_test, test_destination_path)



