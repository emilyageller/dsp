# Hint:  use Google to find python function

import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

d1 = datetime.datetime.strptime(date_start, '%m-%d-%Y')
d2 = datetime.datetime.strptime(date_stop, '%m-%d-%Y')

print(abs((d2-d1).days))

####b)  
date_start = '12312013'  
date_stop = '05282015'  

d3 = datetime.datetime.strptime(date_start, '%m%d%Y')
d4 = datetime.datetime.strptime(date_stop, '%m%d%Y')

print(abs((d4-d3).days))

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

d5 = datetime.datetime.strptime(date_start, '%d-%b-%Y')
d6 = datetime.datetime.strptime(date_stop, '%d-%b-%Y')

print(abs((d6-d5).days))


