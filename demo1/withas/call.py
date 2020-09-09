from demo1.withas.d_sth import sth
from pymysql import cursors
i = sth()
with i.say() as st:
    print(st)
    pass


