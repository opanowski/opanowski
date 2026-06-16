with open('index.html', 'r') as f:
    content = f.read()

old = 'await OneSignal.init({appId:"3a712b22-ae11-4ba7-934f-4fb9dd9eb013"});'
new = 'await OneSignal.init({appId:"3a712b22-ae11-4ba7-934f-4fb9dd9eb013",serviceWorkerParam:{scope:"/opanowski/"},serviceWorkerPath:"/opanowski/OneSignalSDKWorker.js"});'

content = content.replace(old, new)

with open('index.html', 'w') as f:
    f.write(content)

print("Done!")