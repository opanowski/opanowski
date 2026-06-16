with open('sw.js', 'r') as f:
    content = f.read()

old = """self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request))
  );
});"""

new = """self.addEventListener('fetch', e => {
  if (e.request.url.includes('onesignal.com') || e.request.url.includes('OneSignal')) {
    return;
  }
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request))
  );
});"""

content = content.replace(old, new)

with open('sw.js', 'w') as f:
    f.write(content)

print("Done!")