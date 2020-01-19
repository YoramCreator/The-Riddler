"""
@author: Yoram Houtsma
Riddle at https://fivethirtyeight.com/features/can-you-track-the-delirious-ducks/
"""

import matplotlib.pyplot as plt
import numpy as np

s1 = [0.9,1.0] #prob to score against defense [d1,d2]
s2 = [0.6,0.4]

att_list = list(np.linspace(0,1,101).round(2))
def_list = list(np.linspace(0,1,101).round(2))
exp_scores = {}

for a1 in att_list:
    a2 = 1-a1
    exp_scores[a1] = []
    for d1 in def_list:
        d2 = 1-d1
        exp1 = a1*1*(d1*s1[0]+d2*s1[1]) 
        exp2 = a2*2*(d1*s2[0]+d2*s2[1])
        exp = exp1 + exp2
        exp_scores[a1].append(exp)


### Calculate best expected score
s_min = []
def_best = []
for a1 in att_list:
    s = min(exp_scores[a1])
    s_min.append(s) #minimum score for certain attack means best defense possible
    def_best.append(def_list[int(exp_scores[a1].index(s))])

best_score = max(s_min)
best_score_index = s_min.index(best_score)


### Results
print('Attack for 1pt. conversion:', att_list[best_score_index])
print('Defense:', def_best[best_score_index], '% for 1pt. conversion but every percentage is possible')
print('Expected best score:',best_score)

### Plot maximum score for each attack choice prob
plt.plot(np.array(range(0,101))/100,np.array(s_min))
plt.xlabel('Attack choice prob for 1pt.')
plt.ylabel('Expected score')
plt.xlim(0,1)
plt.show()


