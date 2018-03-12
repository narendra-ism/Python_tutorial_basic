# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 23:16:58 2018

@author: narendra
"""

from datetime import datetime
now = datetime.now()

print('%s/%s/%s %s:%s:%s' % (now.month,now.day,now.year,now.hour, now.minute, now.second))