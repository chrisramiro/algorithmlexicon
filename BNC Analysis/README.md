  
This folder is meant to give an example of the type of data and code used for the log-likelihood analysis used to compare the models. 

The folder contains the following:

  - 4 Python files: word.py, sense.py, word_data_structures.py, models.py
  - \_word_list.xlsx - an excel file containing a master list of the following excel files - it becomes populated with scores for each model once the analysis is run
  - 500 xlsx files containing information (date, word form, identifieres, classification codes, part-of-speech) regarding each sense of that given word in the HTE
  
  In order to run the analysis, use the models.py script. The script should then place log-likelihood scores within their appropriate places in the \_word_list.xlsx excel file.
