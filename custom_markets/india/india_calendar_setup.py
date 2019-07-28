import pandas as pd
from trading_calendars import get_calendar

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities

start_session = pd.Timestamp('1997-1-1')
end_session = pd.Timestamp('2020-12-31')

indian_calendar = get_calendar('XBOM')

register('bse-equities-daily', csvdir_equities(['daily', '/path/to/your/csvs',),
	calendar_name = 'XBOM', start_session = start_session, end_session = end_session)



# To complete: go to https://www.zipline.io/bundles.html
