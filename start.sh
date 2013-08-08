#! /bin/bash

chmod +x create-freq-dict.py
chmod +x WikiExtractor.py

wget http://dumps.wikimedia.org/bewiki/latest/bewiki-latest-pages-articles.xml.bz2
mkdir extracted
echo "Extracting articles from dump... (About 5 minutes)"
bzip2 -dc bewiki-latest-pages-articles.xml.bz2 | ./WikiExtractor.py -cb 250K -o extracted > /dev/null
echo "Extracting words..."

find extracted -name '*bz2' -exec bzip2 -dc {} \; > text
rm -rf extracted

./create-freq-dict.py
