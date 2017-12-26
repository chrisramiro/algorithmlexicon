# algorithmlexicon

The main purpose of the accompanying files is to provide the codebase for the lexicon analysis seen in "Mental Algorithms in the Historical Emergence of Word Meanings". Note that this repository does not include all the base data used (from the Historical Thesaurus of English) due to licensing requirements of the HTE database (see References section); the code base includes a subset of
the data used for analysis in the manuscript. Independent licenses need to be obtained for greater access to the HTE database.

Many of the functions are explained underneath the function headers and class definitions. A brief summary of each Folder follows:

# BNC Analysis

  An example of the code and data used to generate the log-likelihood scores with the sample set being a sampling of the top 500 most frequent words* in the BNC that are amenable to analysis.
  
  \* nouns, verbs, adjectives, and adverbs

# model_cost

 The python file simulates and computes the model costs as in SI S4.2
 
# word_form_analysis

  The python file performs statistical tests and visualization on the comparative analysis of word form reuse and innovation in SI S1
  
# word_similarity

  The python file performs the tests the approximation of HTE sense similarities to real human judgements in the Methods (sub-section Semantic Similarity) section of the manuscript
  
--------------------------------------------------------------------------------------------------------------------------------------
  DATA REFERENCES
  
  - Kay, C., Roberts, J., Samuesl, M., Wotherspoon, I., & Alexander, M. (2015). The historical thesaurus of english, version 4.2. Glasgow: University of Glasgow. URL: http:http://historicalthesaurus.arts.gla.ac.uk/
  
  - The British National Corpus, version 3 (BNC XML Edition). (2007). (Distributed by Oxford University Computing SErvices on behalf of the BNC Consortium. URL: http://www.natcorp.ox.ac.uk/)
  
- 353:
  Lev Finkelstein, Evgeniy Gabrilovich, Yossi Matias, Ehud Rivlin, Zach Solan, Gadi Wolfman, and Eytan Ruppin, "Placing Search in Context: The Concept Revisited", ACM Transactions on Information Systems, 20(1):116-131, January 2002. URL: http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/

- 999:
  SimLex-999: Evaluating Semantic Models with (Genuine) Similarity Estimation. 2014. Felix Hill, Roi Reichart and Anna Korhonen. Computational Linguistics. 2015. URL: https://www.cl.cam.ac.uk/~fh295/simlex.html

  --------------------------------------------------------------------------------------------------------------------------------------
  © Copyright 2017 Christian Ramiro
  
  Anyone who uses this code should cite and acknowledge the follow:

  Ramiro, Srinivasan, Malt, & Xu (in submission). Algorithms in the
  historical emergence of word senses.
  --------------------------------------------------------------------------------------------------------------------------------------
