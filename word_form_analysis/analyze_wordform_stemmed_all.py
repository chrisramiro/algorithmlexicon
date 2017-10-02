# The following code performs statistical tests and visualization on the comparative analysis of word form reuse and innovation in Section 1 of Supporting Information.

import pandas as pd
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
import scipy
from scipy import stats

df = pd.read_csv("word_form_stats_stem_all.csv")

t = df.Date
new = df.New
oldPart = df.ReusePart
old = df.Reuse
tot = df.Total

fig = plt.figure(figsize=(10.3, 5.0))

plt.subplot(121)
bch=plt.bar([1,2,3],[np.sum(oldPart)+np.sum(old),np.sum(old),np.sum(new)])
bch[0].set_color('k')
bch[1].set_color('0.5')
bch[2].set_color('0.8')
plt.legend([bch[0],bch[1],bch[2]],['Reused (exact+derived)','Reused (exact)','New'],loc=1)
plt.ylabel('Total count')
plt.xticks([])

plt.subplot(122)
plt.plot(t,old+oldPart-new,'k-')
plt.plot(t,old-new,'g:')
plt.xlabel('Year')
plt.ylabel('Count')
plt.ylim(-300,6000)
plt.legend(['Reused (exact+derived) $-$ New', 'Reused (exact) $-$ New'])
plt.hlines(0,t[0],t[len(t)-1],color='0.5') 
plt.show()

# time-course stats
print('#winning (reused) = ',np.sum((old-new)>0))
print('#winning (new) = ', np.sum((old-new)<0))
print('#tied or zero = ',np.sum((old-new)==0))

# binomial test
p = scipy.stats.binom_test(np.sum(old), n=np.sum(old)+np.sum(new), p=0.5)
print('p(Old) = p(New) = 0.5; p = ',p)
print('Reuse(+stem) count =',np.sum(old)+np.sum(oldPart))
print('Reuse(-stem) count =',np.sum(old))
print('New count =',np.sum(new))
