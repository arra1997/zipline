import pandas as pd
from trading_calendars import get_calendar

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities


register('shanghai-equities-daily', csvdir_equities(['daily'], '/home/custom_markets/china/data',), calendar_name = 'XSHG')
register('india-bse-equities-daily', csvdir_equities(['daily'], '/home/custom_markets/india/data',), calendar_name = 'XBOM')
