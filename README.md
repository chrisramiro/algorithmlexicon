# algorithmlexicon

The main purpose of the accompanying files is to provide the codebase for the lexicon analysis seen in "Mental Algorithms in the Historical Emergence of Word Meanings". Note that this repository does not include all the base data used (from the Historical Thesaurus of English) due to licensing requirements of the HTE database (see References section); the code base includes a subset of
the data used for analysis in the manuscript. Independent licenses need to be obtained for greater access to the HTE database.

Many of the functions are explained underneath the function headers and class definitions. A brief summary of each Python file is as follows.

# word.py
  
  Contains the Word class, which represents a word in the HTE.

# sense.py

  Contains the Sense class, which represents one sense for a word, for use by the Word class. Also contains helper functions to clean the HTE data.

# word_models.py

  Contains the model functions (Progenitor, Markov, Exemplar, Chaining, Dynamic), the null model, helper functions for the models, and the scoring metric function.

# iteration.py

  Contains the function that calls all the functions for a given list of words and organizes them neatly into an excel file (See below).

# excel.py

  Contains a function for you to get an organized excel file containing all of a word's senses.

# Formatting your Excel File

  The code works with .xlsx files organized in the following way:
  
  THESE ARE SUPPLIED BY YOU:
  Column 1 = Word
  Column 2 = Corresponding Part of Speech
  
  THESE ARE SUPPLIED BY THE ANALYSIS:
  Column 3 = Result of Progenitor Analysis
  Column 4 = Result of Markov Analysis
  Column 5 = Result of Exemplar Analysis
  Column 6 = Result of Chaining Analysis
  Column 7 = Result of Dynamic Analysis
  Column 8 = Label of Winning Analysis
  Column 9 = Number of Senses encapsulated by that word
  Column 10 = Number of Existing Senses (i.e. those that didn't die off) encapsulated by that word
  Column 11 = Start Date of word (1000 is 'OE')
  
# How To Use Iteration
  You will need the following information:
  - The name of the excel file, formatted as above, ending in '.xlsx' (e.g. "BNC (Top 500).xlsx")
  - The ending index of the Excel File (the last index of filled row in your excel file)
  - True/False constraint for whether you want to consider all senses (False) or only specific senses related to a part-of-speech (True) [defaults to False]
  - Optional: The start index of the filled row [defaults to 2 because of row headers]
  
  
  Go to the file iteration.py and call the function with the following information.
  
  --------------------------------------------------------------------------------------------------------------------------------------
  DATA REFERENCES
  
  - Kay, C., Roberts, J., Samuesl, M., Wotherspoon, I., & Alexander, M. (2015). The historical thesaurus of english, version 4.2. Glasgow: University of Glasgow.
  
  - The British National Corpus, version 3 (BNC XML Edition). (2007). (Distributed by Oxford University Computing SErvices on behalf of the BNC Consortium. URL: http://www.natcorp.ox.ac.uk/)
  
  --------------------------------------------------------------------------------------------------------------------------------------
  © Copyright 2016 Christian Ramiro
  
  Anyone who uses this code should cite and acknowledge the follow:

  Ramiro, Srinivasan, Malt, & Xu (in submission). Mental algorithms in the
  historical emergence of word meanings.
  --------------------------------------------------------------------------------------------------------------------------------------
