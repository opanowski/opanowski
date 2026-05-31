f = open('/Users/user/Desktop/opanowski/blog/blog-log-001-peresmian-markas.html', 'r')
content = f.read()
f.close()
tags = '\n<meta name="description" content="Log pertama Bunker Opanowski — peresmian markas digital Om Opan di Villa Ciracas, Jakarta Timur. Awal dari semua catatan.">\n<meta property="og:title" content="Log #001 — Peresmian Markas Digital — Bunker Opanowski">\n<meta property="og:type" content="article">\n<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="Log #001 — Peresmian Markas Digital — Bunker Opanowski">\n<meta name="twitter:image" content="https://opanowski.github.io/opanowski/images/nJFlqNX.jpg">'
content = content.replace('</title>', '</title>' + tags, 1)
open('/Users/user/Desktop/opanowski/blog/blog-log-001-peresmian-markas.html', 'w').write(content)
print('Done')