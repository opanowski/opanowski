const CACHE = 'bunker-v1';
const ASSETS = [
  '/opanowski/',
  '/opanowski/index.html',
  '/opanowski/shared.css',
  '/opanowski/latest-posts.js',
  '/opanowski/blog/index.html',
  '/opanowski/projects/index.html'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
  ));
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request))
  );
});
