from itertools import islice

import dateparser
import pytest
import responses

from pynyaasi.client import SortBy, Order
from pynyaasi.nyaasi import CategoryType, FilterType


@pytest.mark.unittest
class TestNyaasiClient:
    @responses.activate
    def test_get_resource_1(self, client, text_aligner, complex_dir, simple_dir):
        resource = client.get_resource(1174590)

        assert resource.id == 1174590
        assert resource.category == CategoryType.ANIME_RAW
        assert resource.title == ('[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! / '
                                  '私に天使が舞い降りた! 10-bit 1080p HEVC BDRip [Fin]')
        assert resource.information == 'https://vcb-s.com'
        assert resource.torrent_download_url == 'https://nyaa.si/download/1174590.torrent'
        assert (resource.magnet_url ==
                'magnet:?xt=urn:btih:16711e0fea5b6ffa47933a2dd3f856ac2c596a05&dn=%5BAirota%26VCB-Studio%5D%20Watashi'
                '%20ni%20Tenshi%20ga%20Maiorita%21%20%2F%20%E7%A7%81%E3%81%AB%E5%A4%A9%E4%BD%BF%E3%81%8C%E8%88%9E%E3'
                '%81%84%E9%99%8D%E3%82%8A%E3%81%9F%21%2010-bit%201080p%20HEVC%20BDRip%20%5BFin%5D&tr=http%3A%2F%2Fny'
                'aa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftrack'
                'er.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F'
                '%2Ftracker.torrent.eu.org%3A451%2Fannounce')
        assert resource.size_raw == '13.6 GiB'
        assert resource.timestamp == 1567920907
        assert resource.seeders == 27
        assert resource.leechers == 7
        assert resource.downloads == 2921
        assert resource.is_trusted == False
        assert resource.is_remake == False
        assert resource.is_batch == False
        assert resource.info_hash == '16711e0fea5b6ffa47933a2dd3f856ac2c596a05'
        assert resource.submitter == 'VCB-Studio'
        assert resource.submitter_url == 'https://nyaa.si/user/VCB-Studio'
        text_aligner.assert_equal(
            resource.description_md,
            """
![image](http://img.2222.moe/images/2019/09/04/img.jpg)  
  

Watashi ni Tenshi ga Maiorita! / 私に天使が舞い降りた! BDRip  
10-bit 1080p HEVC + FLAC + AAC, MKV format. ~ 700 MB / EP.   

This project is in cooperation with Airota. Thanks to them for elaborating Chinese subtitles.
  
The Blu-ray of 'Watashi ni Tenshi ga Maiorita!' is of good quality without obvious artifacts. We only applied compensatory sharpening to improve the visual sharpness. The video is quite bitrate-saving due to the soft image. Therefore, rich details could be maintained even with such small file size. 
   
Please refer to "readme about WebP.txt" if you have trouble viewing WebP images.  
  

* * *

Comparison (right click on the image and open it in a new tab to see the full-size one)
Source________________________________________________Encode

[![](https://img.2222.moe/images/2019/09/02/178s.png)](https://img.2222.moe/images/2019/09/02/178.png) [![](https://img.2222.moe/images/2019/09/02/178s.png)](https://img.2222.moe/images/2019/09/02/178v.png)
[![](https://img.2222.moe/images/2019/09/02/3736s.png)](https://img.2222.moe/images/2019/09/02/3736.png) [![](https://img.2222.moe/images/2019/09/02/3736s.png)](https://img.2222.moe/images/2019/09/02/3736v.png)
[![](https://img.2222.moe/images/2019/09/02/4241s.png)](https://img.2222.moe/images/2019/09/02/4241.png) [![](https://img.2222.moe/images/2019/09/02/4241s.png)](https://img.2222.moe/images/2019/09/02/4241v.png)
[![](https://img.2222.moe/images/2019/09/02/4815s.png)](https://img.2222.moe/images/2019/09/02/4815.png) [![](https://img.2222.moe/images/2019/09/02/4815s.png)](https://img.2222.moe/images/2019/09/02/4815v.png)
[![](https://img.2222.moe/images/2019/09/02/5079s.png)](https://img.2222.moe/images/2019/09/02/5079.png) [![](https://img.2222.moe/images/2019/09/02/5079s.png)](https://img.2222.moe/images/2019/09/02/5079v.png)
[![](https://img.2222.moe/images/2019/09/02/8122s.png)](https://img.2222.moe/images/2019/09/02/8122.png) [![](https://img.2222.moe/images/2019/09/02/8122s.png)](https://img.2222.moe/images/2019/09/02/8122v.png)
[![](https://img.2222.moe/images/2019/09/02/28230s.png)](https://img.2222.moe/images/2019/09/02/28230.png) [![](https://img.2222.moe/images/2019/09/02/28230s.png)](https://img.2222.moe/images/2019/09/02/28230v.png)
[![](https://img.2222.moe/images/2019/09/02/29912s.png)](https://img.2222.moe/images/2019/09/02/29912.png) [![](https://img.2222.moe/images/2019/09/02/29912s.png)](https://img.2222.moe/images/2019/09/02/29912v.png)
"""
        )

        assert resource.size >= '10 GB'
        assert resource.size > '10 GB'
        assert resource.size <= '80 GB'
        assert resource.size < '80 GB'
        assert repr(resource.size) == '13.6 GiB'

        assert dateparser.parse(resource.time).timestamp() == pytest.approx(1567920907.0)
        assert resource.datetime.timestamp() == pytest.approx(1567920907.0)

        assert resource.directory_tree == complex_dir
        assert resource.directory_tree != simple_dir

    @responses.activate
    def test_get_resource_2(self, client, text_aligner, complex_dir, simple_dir):
        resource = client.get_resource(1639366)

        assert resource.id == 1639366
        assert resource.category == CategoryType.ANIME_RAW
        assert resource.title == '[AI-Raws] 炎炎ノ消防隊 / Fire Force S1 BDRip 1080p MKV'
        assert resource.information == 'http://www.mahou-shoujo.moe/'
        assert resource.torrent_download_url == 'https://nyaa.si/download/1639366.torrent'
        assert (resource.magnet_url ==
                'magnet:?xt=urn:btih:6869cfa3a7c03e41d7004205deca7e6bf62630c6&dn=%5BAI-Raws'
                '%5D%20%E7%82%8E%E7%82%8E%E3%83%8E%E6%B6%88%E9%98%B2%E9%9A%8A%20%2F%20Fire%'
                '20Force%20S1%20BDRip%201080p%20MKV&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%'
                '2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ft'
                'racker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3'
                'A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce')
        assert resource.size_raw == '20.6 GiB'
        assert resource.timestamp == 1676778484
        assert resource.seeders == 1
        assert resource.leechers == 1
        assert resource.downloads == 226
        assert resource.is_trusted == False
        assert resource.is_remake == False
        assert resource.is_batch == False
        assert resource.info_hash == '6869cfa3a7c03e41d7004205deca7e6bf62630c6'
        assert resource.submitter == 'Anonymous'
        assert resource.submitter_url is None
        text_aligner.assert_equal(
            resource.description_md,
            """
            #### No description.
            """
        )

        assert resource.directory_tree != complex_dir
        assert resource.directory_tree == simple_dir

    @responses.activate
    def test_list_items(self, client):
        items = list(islice(client.iter_items('fire force'), 200))
        assert len(items) == 200

        resource = items[0]
        assert resource.id == 1726561
        assert resource.category == CategoryType.LITERATURE_ENGLISH
        assert resource.comments == 2
        assert resource.title == 'Enen no Shouboutai / Fire Force (2016-2023) (Digital) (danke-Empire)'
        assert resource.url == 'https://nyaa.si/view/1726561'
        assert resource.torrent_download_url == 'https://nyaa.si/download/1726561.torrent'
        assert resource.magnet_url == \
               ('magnet:?xt=urn:btih:3b60c0ca90427a845b1f3881a74cbda6cb120a46&dn=Enen%20no%20Shouboutai%20%2F%'
                '20Fire%20Force%20%282016-2023%29%20%28Digital%29%20%28danke-Empire%29&tr=http%3A%2F%2Fnyaa.tr'
                'acker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftrac'
                'ker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=ud'
                'p%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce')
        assert resource.size_raw == '5.9 GiB'
        assert resource.timestamp == 1696796810
        assert resource.seeders == 34
        assert resource.leechers == 4
        assert resource.downloads == 505
        assert resource.is_trusted == False
        assert resource.is_remake == False
        assert resource.is_batch == False
        assert dateparser.parse(resource.time).timestamp() == pytest.approx(1696796810.0)
        assert resource.datetime.timestamp() == pytest.approx(1696796810.0)
        assert '5.8 GiB' < resource.size < '6.0 GiB'

        resource = items[1]
        assert resource.id == 1724856
        assert resource.category == CategoryType.LITERATURE_ENGLISH
        assert resource.comments == 1
        assert resource.title == '[0v3r] Fire Force v34 (2023) (Digital) (0v3r)'
        assert resource.url == 'https://nyaa.si/view/1724856'
        assert resource.torrent_download_url == 'https://nyaa.si/download/1724856.torrent'
        assert resource.magnet_url == \
               ('magnet:?xt=urn:btih:0e16fc5a42da95284846cca46fb57d4260d1432b&dn=%5B0v3r%5D%20Fire%20Force%20'
                'v34%20%282023%29%20%28Digital%29%20%280v3r%29&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannou'
                'nce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1'
                '337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.tor'
                'rent.eu.org%3A451%2Fannounce')
        assert resource.size_raw == '285.4 MiB'
        assert resource.timestamp == 1696514955
        assert resource.seeders == 8
        assert resource.leechers == 0
        assert resource.downloads == 494
        assert resource.is_trusted == False
        assert resource.is_remake == False
        assert resource.is_batch == False
        assert dateparser.parse(resource.time).timestamp() == pytest.approx(1696514955.0)
        assert resource.datetime.timestamp() == pytest.approx(1696514955.0)
        assert '280 MiB' < resource.size < '290 MiB'

        resource = items[-1]
        assert resource.id == 1262975
        assert resource.category == CategoryType.ANIME_ENGLISH
        assert resource.comments == 1
        assert resource.title == '[Anime Time] (Fire Force) Enen No Shouboutai S2 - 01[720p][HEVC 10bit x265][AAC].mkv'
        assert resource.url == 'https://nyaa.si/view/1262975'
        assert resource.torrent_download_url == 'https://nyaa.si/download/1262975.torrent'
        assert resource.magnet_url == \
               ('magnet:?xt=urn:btih:13975b5efa90cb6e74d5ee2382f1550e9ce8fc23&dn=%5BAnime%20Time%5D%20%28Fire%20'
                'Force%29%20Enen%20No%20Shouboutai%20S2%20-%2001%5B720p%5D%5BHEVC%2010bit%20x265%5D%5BAAC%5D.mkv'
                '&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannoun'
                'ce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6'
                '969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce')
        assert resource.size_raw == '211.8 MiB'
        assert resource.timestamp == 1594832469
        assert resource.seeders == 0
        assert resource.leechers == 0
        assert resource.downloads == 95
        assert resource.is_trusted == False
        assert resource.is_remake == True
        assert resource.is_batch == False
        assert dateparser.parse(resource.time).timestamp() == pytest.approx(1594832469.0)
        assert resource.datetime.timestamp() == pytest.approx(1594832469.0)
        assert '205 MiB' < resource.size < '215 MiB'

    @responses.activate
    def test_list_items_no_remake(self, client):
        items = list(islice(client.iter_items('fire force', filter=FilterType.NO_REMAKES), 200))
        assert len(items) == 200

    @responses.activate
    def test_list_items_trusted_only(self, client):
        items = list(islice(client.iter_items('fire force', filter=FilterType.TRUSTED_ONLY), 200))
        assert len(items) == 1

    @responses.activate
    def test_list_items_raw(self, client):
        items = list(islice(client.iter_items('fire force', category=CategoryType.ANIME_RAW), 200))
        assert len(items) == 19

    @responses.activate
    def test_list_items_raw_order(self, client):
        items = list(islice(client.iter_items('fire force', category=CategoryType.ANIME_RAW,
                                              sort_by=SortBy.COMMENTS), 200))
        assert len(items) == 19

        resource = items[0]
        assert resource.id == 1646231
        assert resource.category == CategoryType.ANIME_RAW
        assert resource.comments == 8
        assert resource.title == '[Moozzi2] Enen no Shouboutai (Fire Force S1) (BD 1920x1080 x265-10Bit Flac) - TV + SP'
        assert resource.url == 'https://nyaa.si/view/1646231'
        assert resource.torrent_download_url == 'https://nyaa.si/download/1646231.torrent'
        assert resource.magnet_url == \
               ('magnet:?xt=urn:btih:c2434cf09f824ded1c7e08f922f60619d844e521&dn=%5BMoozzi2%5D%20Enen%20no%20Sh'
                'ouboutai%20%28Fire%20Force%20S1%29%20%28BD%201920x1080%20x265-10Bit%20Flac%29%20-%20TV%20%2B%2'
                '0SP&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fan'
                'nounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.co'
                'm%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce')
        assert resource.size_raw == '21.5 GiB'
        assert resource.timestamp == 1678245189
        assert resource.seeders == 4
        assert resource.leechers == 2
        assert resource.downloads == 777
        assert resource.is_trusted == False
        assert resource.is_remake == False
        assert resource.is_batch == False

        resource = items[-1]
        assert resource.comments == 0

    @responses.activate
    def test_list_items_raw_order_asc(self, client):
        items = list(islice(client.iter_items('fire force', category=CategoryType.ANIME_RAW,
                                              sort_by=SortBy.COMMENTS, order=Order.ASC), 200))
        assert len(items) == 19

        resource = items[0]
        assert resource.comments == 0

        resource = items[-1]
        assert resource.id == 1646231
        assert resource.category == CategoryType.ANIME_RAW
        assert resource.comments == 8
        assert resource.title == '[Moozzi2] Enen no Shouboutai (Fire Force S1) (BD 1920x1080 x265-10Bit Flac) - TV + SP'
        assert resource.url == 'https://nyaa.si/view/1646231'
        assert resource.torrent_download_url == 'https://nyaa.si/download/1646231.torrent'
        assert resource.magnet_url == \
               ('magnet:?xt=urn:btih:c2434cf09f824ded1c7e08f922f60619d844e521&dn=%5BMoozzi2%5D%20Enen%20no%20Sh'
                'ouboutai%20%28Fire%20Force%20S1%29%20%28BD%201920x1080%20x265-10Bit%20Flac%29%20-%20TV%20%2B%2'
                '0SP&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fan'
                'nounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.co'
                'm%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce')
        assert resource.size_raw == '21.5 GiB'
        assert resource.timestamp == 1678245189
        assert resource.seeders == 4
        assert resource.leechers == 2
        assert resource.downloads == 777
        assert resource.is_trusted == False
        assert resource.is_remake == False
        assert resource.is_batch == False

    @responses.activate
    def test_get_resource_without_directory_tree(self, client):
        resource = client.get_resource(915257)

        assert resource.id == 915257
        assert resource.category == CategoryType.ANIME_ENGLISH
        assert resource.title == '[HorribleSubs] Barakamon (01-12) [1080p] (Unofficial Batch)'
        assert resource.information == 'http://horriblesubs.info/shows/barakamon/'
        assert resource.torrent_download_url is None
        assert resource.magnet_url.startswith('magnet:?xt=urn:btih:f56d7d17898e0f6f038b1b1eaa1cd0292a5cc235')
        assert resource.size_raw == '6.1 GiB'
        assert resource.timestamp == 1491613260
        assert resource.seeders == 3
        assert resource.leechers == 1
        assert resource.downloads == 1335
        assert resource.is_trusted is False
        assert resource.is_remake is False
        assert resource.is_batch is False
        assert resource.info_hash == 'f56d7d17898e0f6f038b1b1eaa1cd0292a5cc235'
        assert resource.submitter == 'thedarkness000'
        assert resource.submitter_url == 'https://nyaa.si/user/thedarkness000'
