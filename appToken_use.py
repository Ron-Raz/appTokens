import sys
from KalturaClient import *
from KalturaClient.Plugins.Core import *
import hashlib

# 
# get parameters from commandline in the format name=val
# 
cli={}
for arg in sys.argv:
    nameValuePair= arg.split('=')
    if len(nameValuePair)==2:
        cli[nameValuePair[0].upper()]= nameValuePair[1]

# 
# generate a widget session in order to use the app token
# 

config = KalturaConfiguration()
config.serviceUrl = cli['SERVICEURL']
client = KalturaClient(config)

result = client.session.startWidgetSession('_'+cli['PID'], 86400)
client.setKs(result.ks)

# 
# use the appToken ID and appToken Hash
# 
hashString = hashlib.sha256((result.ks + cli['TOKENHASH']).encode('ascii')).hexdigest()
result = client.appToken.startSession(cli['TOKENID'], hashString, cli['USERID'], KalturaSessionType.ADMIN, 86400);

client.setKs(result.ks)

# 
# now do your Kaltura processing
# 
result = client.media.list(KalturaMediaEntryFilter(), KalturaFilterPager())
for entry in result.getObjects():
    print(entry.id,entry.name)