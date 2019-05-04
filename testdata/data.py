URL = 'https://jqueryui.com/droppable/'
UN = 'admin'
PWD = 'manager'

import inspect
def whoami():
    return inspect.stack()[1][3]
