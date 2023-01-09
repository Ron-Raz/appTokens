import sys
from KalturaClient import *
from KalturaClient.Plugins.Core import *

# 
# get parameters from commandline in the format name=val
# 
cli={}
for arg in sys.argv:
    nameValuePair= arg.split('=')
    if len(nameValuePair)==2:
        cli[nameValuePair[0].upper()]= nameValuePair[1]

# 
# start Kaltura session
# 
config = KalturaConfiguration()
config.serviceUrl = cli['SERVICEURL']
client = KalturaClient(config)
ks = client.session.start(cli['ADMINSECRET'], cli['USERID'], KalturaSessionType.USER, cli['PID'], 86400, '')
client.setKs(ks)

# 
# create the app token
# 
appToken = KalturaAppToken()
appToken.hashType = KalturaAppTokenHashType.SHA256
appToken.description = "Created by appToken_add.py"
result = client.appToken.add(appToken)
print('token id  =',result.id,'\ntoken hash=',result.token)
