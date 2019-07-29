import pandas as pd
import matplotlib.pyplot as plt

import pdb; pdb.set_trace()
perf = pd.read_pickle('shanghai_buy.pickle') # read in perf DataFrame
perf.head()

alg_returns = perf.algorithm_period_return

ax1 = plt.subplot(211)
perf.portfolio_value.plot(ax=ax1)
ax1.set_ylabel('Portfolio Value')
plt.savefig('performance.png')


#ax2 = plt.subplot(212, sharex=ax1)
#perf.AAPL.plot(ax=ax2)
#ax2.set_ylabel('AAPL Stock Price')
