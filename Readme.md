Wordle Analysis
===

The code in this repo is a small analysis for the [Wordle in Spanish](https://wordle.danielfrg.com) game. 

I was fascinated by the game and wanted to know the best words to start a game, for me this meant words that contain letters in their highest probability position.

This python script gets the probability of each letter appearing in an specific position and then assigns a value to each word according to the letters position in the word. The most probable words score higher.

The list of words was extracted directly from the javascript in the webpage and includes some words that are not valid and can't be played because they contain an "-" symbol.

Results
---

### The top 10 words with the highest probability are: 

|Word  |   Value|
|------|------:|   
|careo |   8358  |   
|pareo |   8124  |   
|caneo |   8036  |   
|corea |   8010  |   
|mareo |   7967  |   
|pares |   7935  |   
|cales |   7914  |   
|paleo |   7869  |   
|cateo |   7860  |   
|caseo |   7833  | 


### Words without repeating any letters:
|Word  |   Points|   
|------|------:|  
|careo |   8358  |   
|pulis |   6181  | 


### Top words without previously repeating any consonant:
|Word |    Points|   
|------|------:|  
|careo|    8358  |   
|paleo|    7869  |   
|maneo|    7645  |   
|bateo|    7316  |   
|gaseo|    7115  |   
|fajeo|    6863  |   
|vadeo|    6808  |   
|aqueo|    5661  |   
|heñia|    5574  |   
|zuiza|    5009  |   
|yauya|    2998  |

Here are the tables used to calculate the value for each word, each letter has a different value acording to the position in which they appear.

### Values for position:  1



| Letter | Appeareances | Percent |
|----------|-------------|------:|
|a|        1356|            12.121%|
|c    |   1130         |   10.101% |
|p    |    896         |    8.009% |
|t    |    768         |    6.865% |
|m    |    739         |    6.606% |
|r    |    649         |    5.801% |
|b    |    586         |    5.238% |
|s    |    584         |    5.220% |
|l    |    555         |    4.961% |
|f    |    473         |    4.228% |
|g    |    412         |    3.683% |
|h    |    378         |    3.379% |
|o    |    375         |    3.352% |
|d    |    372         |    3.325% |
|v    |    340         |    3.039% |
|n    |    293         |    2.619% |
|j    |    283         |    2.530% |
|e    |    279         |    2.494% |
|u    |    179         |    1.600% |
|i    |    151         |    1.350% |
|z    |    150         |    1.341% |
|y    |    118         |    1.055% |
|q    |    50          |    0.447% |
|ñ    |    34          |    0.304% |
|k    |    22          |    0.197% |
|x    |    9           |    0.080% |
|w    |    6           |    0.054% |


### Values for position:  2
|Letter   |Appeareances    |Percent|
|----------|:-------------|------:|  
|a        |2350            |21.007%| 
|o        |1576            |14.088%| 
|u        |1448            |12.944%| 
|e        |1394            |12.461%| 
|i        |1377            |12.309%| 
|r        |754             |6.740% |
|l        |429             |3.835% |
|n        |217             |1.940% |
|s        |190             |1.698% |
|h        |183             |1.636% |
|c        |161             |1.439% |
|t        |151             |1.350% |
|m        |145             |1.296% |
|p        |136             |1.216% |
|b        |118             |1.055% |
|d        |93              |0.831% |
|v        |86              |0.769% |
|j        |68              |0.608% |
|f        |62              |0.554% |
|g        |59              |0.527% |
|z        |54              |0.483% |
|ñ        |52              |0.465% |
|x        |39              |0.349% |
|y        |33              |0.295% |
|q        |7               |0.063% |
|w        |3               |0.027% |
|k        |2               |0.018% |


### Values for position:  3
|Letter|   Appeareances    |Percent|
|----------|:-------------|------:|    
|r     |   1110            |9.922% |
|l     |   855             |7.643% |
|a     |   836             |7.473% |
|i     |   810             |7.241% |
|n     |   788             |7.044% |
|e     |   779             |6.963% |
|c     |   647             |5.783% |
|t     |   612             |5.471% |
|s     |   585             |5.229% |
|u     |   530             |4.738% |
|o     |   489             |4.371% |
|m     |   464             |4.148% |
|p     |   368             |3.290% |
|b     |   359             |3.209% |
|d     |   350             |3.129% |
|g     |   332             |2.968% |
|j     |   272             |2.431% |
|ñ     |   205             |1.832% |
|f     |   176             |1.573% |
|z     |   175             |1.564% |
|y     |   136             |1.216% |
|v     |   128             |1.144% |
|q     |   61              |0.545% |
|h     |   56              |0.501% |
|x     |   55              |0.492% |
|k     |   8               |0.072% |
|w     |   1               |0.009% |


### Values for position:  4
|Letter   |Appeareances    |Percent| 
|----------|:-------------|------:|   
|a        |1871            |16.725%| 
|e        |1593            |14.240%| 
|i        |996             |8.903% |
|o        |969             |8.662% |
|r        |660             |5.900% |
|t        |628             |5.614% |
|l        |601             |5.372% |
|d        |475             |4.246% |
|c        |450             |4.023% |
|n        |400             |3.576% |
|s        |337             |3.012% |
|u        |308             |2.753% |
|m        |298             |2.664% |
|g        |266             |2.378% |
|p        |237             |2.119% |
|b        |229             |2.047% |
|j        |185             |1.654% |
|z        |153             |1.368% |
|h        |149             |1.332% |
|v        |140             |1.251% |
|ñ        |83              |0.742% |
|f        |69              |0.617% |
|y        |64              |0.572% |
|k        |13              |0.116% |
|x        |9               |0.080% |
|w        |4               |0.036% |


### Values for position:  5
|Letter   |Appeareances|    Percent|  
|----------|:-------------|------:|  
|a        |2601        |    23.250%| 
|o        |2175        |    19.442%| 
|s        |1986        |    17.753%| 
|e        |1486        |    13.283%| 
|n        |1144        |    10.226%| 
|r        |639         |    5.712% |
|l        |359         |    3.209% |
|i        |299         |    2.673% |
|z        |93          |    0.831% |
|-        |92          |    0.822% |
|y        |91          |    0.813% |
|u        |43          |    0.384% |
|t        |39          |    0.349% |
|d        |32          |    0.286% |
|x        |26          |    0.232% |
|c        |20          |    0.179% |
|m        |16          |    0.143% |
|k        |12          |    0.107% |
|h        |10          |    0.089% |
|j        |6           |    0.054% |
|b        |6           |    0.054% |
|p        |5           |    0.045% |
|f        |4           |    0.036% |
|g        |3           |    0.027% |

