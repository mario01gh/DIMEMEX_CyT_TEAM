# CyT_TEAM DIMEMEX

## Data and Model Checkpoints

Data and model checkpoints can be accessed in the following [Drive folder](https://drive.google.com/file/d/1ORiaeYBQ6NNJE1kHS8ZqYI9WvW2zffsI/view?usp=sharing).

### Data

- `split_data`: Contains images divided into splits. The train split is extended with data extracted from Gemini.
- `text_augmentations`: Contains CSV files with augmented texts for tasks 1 and 2.
  - `train_data_augmented.csv`: Image-like augmentation
  - `real_augmentation.csv`: Real-text augmentation

### Models

- `models`: Contains each model, their loss & accuracy evolution graphs, classification reports, and confusion matrices. To identify the models, you can see the identifier of each model in the tables in the results section of the paper.

### Notebooks

- `train_with_splits`: Notebooks for training using different models with train, val, and test splits, storing the results.
- `real_text_augmentation`: Notebooks for training using different models with the Real_Text_Augmentation approach.
- `test_models`: Notebooks for loading and testing all models over the testing data provided by the competition, generating the output files.
- `auxiliary_notebooks`: Various utility notebooks.
  - `gemini_vision.ipynb`: Expands the dataset using Gemini 1.5 Pro API.
  - `data_aug_text.ipynb`: Creates text augmentations using LM Studio with LLama 3 as a local API.
  - `data_split.py`: Decodes the one-hot labels and splits the data into train, val, and test.
  - `graphs.ipynb`: Creates dataset graphs.
  - `task2_submission_generate.py`: Combines the output CSV files with predictions for task 1 and task 2, resulting in the submission for the second task.

### Results

- `results.csv`: Stores train, val, and test loss & accuracy, and the best epoch for each model.

