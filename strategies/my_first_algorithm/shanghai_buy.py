from zipline.api import order, record, symbol

def initialize(context):
    #import pdb; pdb.set_trace()
    pass


def handle_data(context, data):
    #import pdb; pdb.set_trace()
    #pass
    order(symbol('600000'), 10)
    record(_600000=data.current(symbol('600000'), 'price'))


