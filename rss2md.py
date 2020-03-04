#!/usr/bin/env python
import urllib, re, html2markdown
tre = re.compile(r'<title>(.*)<\/title>')
lre = re.compile(r'<link>(.*)<\/link>')
pudre = re.compile(r'<pubDate>(.*)<\/pubDate>')
cre = re.compile(r'<category domain="(.*)">(.*)</category>')
pre = re.compile(r'<guid isPermaLink\="false">.*?\?p\=(\d+)<\/guid>')
conre = re.compile(r'<content\:encoded><\!\[CDATA\[(.*)\]\]><\/content\:encoded>')

rss = 'https://www.camelway.com/rss-%d.xml'
item = '''<item>
    <title>Small Concrete Batching Plant of Low Price and Small footprint</title>
    <link>https://www.camelway.com/view/small-concrete-batching-plant-of-low-price-and-small-footprint.html</link>
    <pubDate>Wed, 26 Feb 2020 14:08:04 +0800</pubDate>
    <dc:creator><![CDATA[Hito Yang]]></dc:creator>
    <category domain="https://www.camelway.com/view/">Industry Views</category>
    <guid isPermaLink="false">https://www.camelway.com/?p=510</guid>
    <description>Camelway&#39;s HZS25 Lite Concrete Batching Plant is a Miniaturized Batching Plant for Small Applications. It has the advantages of short mixing time, long service life of consumables, ease of operation and maintenance, HZS25 Lite mainly composed of a twin shaft mixer with skip hoists, a 2 bins aggregate batcher, cement silo, and screw conveyor. This HZS25 Lite Concrete Batching Plant can be equipped with a full automatic weighing system ;to promise the accuracy weight of aggregate, powder and liquid through electronic scales and microcomputers.Camelway&#39;s HZS25 and HZS35 Concrete Batching Plant is specialized design for small applications, they use the skip hoists to load the sand the rocks to the mixer, which help to reduce the footprint of a batching plant. As shown in the image above, a HZS25 or HZS35 only occupies only 200 square meters land.For the price, Thanks to rich manufacturing experience, Our transaction price is lower than many companies. Not only that, we also design small concrete batching plants</description>
    <content:encoded><![CDATA[<p>Camelway&#39;s HZS25 Lite Concrete Batching Plant is a Miniaturized Batching Plant for Small Applications. It has the advantages of short mixing time, long service life of consumables, ease of operation and maintenance, HZS25 Lite mainly composed of a <a href="https://www.camelway.com/batch-plant/mixer/twin-shaft-mixer-with-skip-hoists.html" target="_self">twin shaft mixer with skip hoists</a>, a 2 bins aggregate batcher, cement silo, and screw conveyor. This HZS25 Lite Concrete Batching Plant can be equipped with a full automatic weighing system ;to promise the accuracy weight of aggregate, powder and liquid through electronic scales and microcomputers.</p><p><img src="https://www.camelway.com/dm-content/uploads/hzs25-lite-small-concrete-batching-plant.webp" alt="hzs25 lite Small Concrete Batching Plant" width="600" height="500" border="0" vspace="0" style="width: 600px; height: 500px;"/></p><p>Camelway&#39;s HZS25 and HZS35 Concrete Batching Plant is specialized design for small applications, they use the skip hoists to load the sand the rocks to the mixer, which help to reduce the footprint of a batching plant. As shown in the image above, a HZS25 or HZS35 only occupies only 200 square meters land.</p><p>For the price, Thanks to rich manufacturing experience, Our transaction price is lower than many companies. Not only that, we also design small concrete batching plants according to customers&#39; needs to help reduce costs.</p><p>Camelway&#39;s Skip Hoists type concrete plant equipped with highly efficient equipment, produces plastic, hard concrete and other types of concrete mixtures. Widely used in small and medium-sized buildings, expressways, bridges, ideal for the production of ready-mixed concrete. It&#39;s An ideal choice for a high-quality concrete construction organization.</p>]]></content:encoded>
</item>'''

def remove_no_md(content)
    content.replace(r'<script>.*?<\/script>', '')





def parse_article(string):
    title = tre.findall(string)[0]
    link = lre.findall(string)[0]
    pubdate = pudre.findall(string)[0]
    categorylink = cre.findall(string)[0][0]
    category = cre.findall(string)[0][1]
    postid = pre.findall(string)[0]
    content = conre.findall(string)[0]
    content = content.replace(' target="_self"', '')
    contentmd = html2markdown.convert(content)

    #return (title, link, pubdate, categorylink, category, postid, contentmd)
    return  ("\r\n\r\n", contentmd)


print(parse_article(item))
