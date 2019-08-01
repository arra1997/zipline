#
# Copyright 2013 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pandas as pd
import requests


def get_benchmark_returns(symbol):
    """
    Get a Series of benchmark returns from IEX associated with `symbol`.
    Default is `SPY`.

    Parameters
    ----------
    symbol : str
        Benchmark symbol for which we're getting the returns.

    The data is provided by IEX (https://iextrading.com/), and we can
    get up to 5 years worth of data.
    """
    IEX_KEY = "pk_4942e3d625c549659029b738494afc9d"
    r= requests.get(
        "https://cloud.iexapis.com/stable/stock/{}/chart/5y?chartCloseOnly=True&token={}".format(symbol, IEX_KEY)
    )
    data = r.json()

    df = pd.DataFrame(data)

    df.index = pd.DatetimeIndex(df['date'])
    df = df['close']
    filled_dates = pd.date_range(start = df.date.min(),
                                 end = df.date.max())
    
    df.set_index('date').reindex(filled_dates).fillna(method='ffill') 

    return df.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]
