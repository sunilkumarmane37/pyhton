URL = 'http://localhost:8080/'
UN = 'admin'
PWD = 'manager'

import inspect
def whoami():
    return inspect.stack()[1][3]
