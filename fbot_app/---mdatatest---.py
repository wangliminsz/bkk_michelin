from mdata import *
from mdatalocation import *

import operator

testlocation = mdatalocation

# testlocation.sort(key=lambda x:x[0], reverse=True)

# testlocation.sort(key=operator.attrgetter('mbid'), reverse=True)

# sorted(testlocation, key=lambda x: x[0], reverse=True)

# 2022-01-23 成功

testlocation.sort(key=lambda x: x['mbid'], reverse=True)
print(testlocation)

# 2022-01-23 成功

# for tlocation in testlocation:
#     print(tlocation['mbid'], tlocation['mbstyle'], tlocation['mbdistance'])
    # tlocation.distance = lambda: None

#  ut.sorted(testlocation, key=lambda x: x[0], reverse=True)

# print(testlocation)

# obj.a = lambda: None
# setattr(obj.a, 'somefield', 'somevalue')

# mbid,mbname,mbstyle,mbtakeaway,mblat,mblng,mburl,mbimgurl,mbaddress,mbprice,mbview,mbcontact,mbservice,mbaward

# mbid,
# mbname,
# mbstyle,
# mbtakeaway,
# mblat,
# mblng,
# mburl,
# mbimgurl,
# mbaddress,
# mbprice,
# mbview,
# mbcontact,
# mbservice,
# mbaward