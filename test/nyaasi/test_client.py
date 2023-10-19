import dateparser
import pytest
import responses

from pynyaasi.nyaasi import CategoryType


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
        assert resource.seeders == 30
        assert resource.leechers == 6
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
