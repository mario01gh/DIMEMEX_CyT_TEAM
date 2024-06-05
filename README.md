Data used and models checkpoints can be accessed in the following drive folder

data --> folder containing all the data
-
-- split_data --> images divided into splits (train split is extended with data extracted from Gemini)
-
-- text_augmentations --> csv files with augmented texts for tasks1 and 2,  train_data_augmented.csv (image-like augmentation) and real_augmentation.csv (real-text augmentation)


models --> folder for storing each of the models, their loss&accuracy evolution graphs, classification reports and confusion matrices


notebooks --> notebooks used for the models development
-
-- train_with_splits --> contains notebooks for training using all different models with train, val and tests splits storing the results
-
-- real_text_augmentation--> contains notebooks for training using all different models using the Real_Text_Augmentation approach
-
-- test_models --> contains notebooks for loading and testing all the models over the testing data provided by the competition generating the output files
-
-- auxiliary_notebooks
   -
   -- gemini_vision.ipynb --> used for expanding the dataset using Gemini 1.5 Pro API
   -
   -- data_aug_text.ipynb --> used for creating the tex augmentations using LM Studio with LLama 3 as a local API
   -
   -- data_split.py --> used for decoding the one-hot labels and splitting the data into train val and test
   -
   -- graphs.ipynb --> used for creating the dataset graphs
   -
   -- task2_submission_generate.py --> used for combining the output csv files with predictions for task1 and task2, the result is the submission for the second task


results.csv  -->  file used for storing train&val&test loss&accuracy and the best epoch for each model
