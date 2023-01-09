Simple examples of how to add and use appTokens in Kaltura.

For more details:

https://developer.kaltura.com/api-docs/VPaaS-API-Getting-Started/application-tokens.html

## add appToken
```bash
python3 appToken_add.py pid=xxx adminSecret=xxx userId=xxx serviceUrl=https://www.kaltura.com/
```
The result would look something like this:
```bash
id   = 1_r5xxxxzt 
token= 756b1e6b6b44e7bea843d7ae18d66733
```

## use appToken
```bash
python3 appToken_use.py pid=xxx tokenid=1_r5xxxxzt tokenhash=756b1e6b6b44e7bea843d7ae18d66733 userid=ron.raz@kaltura.com serviceurl=https://www.kaltura.com/
```
