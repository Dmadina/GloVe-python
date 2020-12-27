# GloVe-python

Python implementation of GloVe algorithm  
Pre-trained 100 dimensional GLoVE model used in this project can be downloaded from link below:  
http://nlp.stanford.edu/data/glove.6B.zip  
After downloading put the glove.6B.100d.txt file next to ***main.py***

#How to use guide
There are ***sim*** and ***closest*** functions in ***main.py*** file  
Similarity function takes 2 lists, positive and negative
```
sim([['paris', 'germany'], ['france']])
Output: [('berlin', 0.8810450434684753), ('frankfurt', 0.7958396673202515), ('vienna', 0.760452151298523), ('munich', 0.7508679628372192), ('germany', 0.7424822449684143)]
```

Closest words function takes string as input
```
closest('compute')
Output: [('compute', 0.99999994), ('calculate', 0.7222062), ('algorithm', 0.6441058), ('computed', 0.6136234), ('algorithms', 0.61343837)]
```
