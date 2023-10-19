from itertools import islice

import pytest
import responses

from pynyaasi.client import Directory, File, SortBy, Order
from pynyaasi.sukebei import CategoryType, FilterType


@pytest.fixture()
def dir_1():
    return Directory("FC2-PPV-3861736", [
        File(
            "AV\u5927\u5e73\u53f0-\u4e2d\u6587\u5b57\u5e55,\u6210\u4eba\u5f71\u7247,AV,\u56fd\u4ea7,\u7dda\u4e0a\u770b.url",
            "118 Bytes"),
        File("FC2-PPV-3861736-D.jpg", "217.9 KiB"),
        File("FC2-PPV-3861736-SP.mp4", "13.1 MiB"),
        File("FC2-PPV-3861736.jpg", "37.3 KiB"),
        File("FC2-PPV-3861736_1.mp4", "1.2 GiB"),
        File("FC2-PPV-3861736_2.mp4", "232.7 MiB"),
        File(
            "\u221e GAMES \u6781\u9650\u65e0\u7801\u624b\u6e38\u4efb\u60a8\u9009!\u8bf7\u4e0a atv89.com.url",
            "116 Bytes"),
        File(
            "\u2605\u6700\u5f3a\u795e\u4f5c-\u661f\u795e\u5c11\u5973 ! \u516b\u79cdR18\u73a9\u6cd5\uff0c\u6ee1\u8db3\u4f60\u5bf9\u795e\u754c\u7684\u6b32\u671b~.url",
            "119 Bytes"),
        File(
            "\u300a\u4e09\u56fd\u5fd7H\u7248\u300b\u7eb5\u6b32\u540e\u5bab\u82b1\u56ed,\u4fb5\u7565\u4e71\u4e16\u4f73\u4eba~.url",
            "119 Bytes"),
        File(
            "\u300a\u5929\u4f7f\u8a08\u5283\u306e\u9006\u8972\u300b\u6e38\u620f\u653b\u7565+\u9650\u65f6\u5151\u6362\u7801 op666.txt",
            "829 Bytes"),
        File(
            "\u300a\u6597\u7f57\u5927\u9646S\u7248\u300b\u5c0f\u821e\u5f52\u6765(\u54e5~\u6765\u64cd\u6211\u5427).url",
            "118 Bytes"),
        File(
            "\u3010\u5168\u65b0\u624b\u6e38\u3011\u6211\u7684\u4eba\u5de5\u5c11\u5973 ! \u4e3a\u60a8\u8ba2\u5236\u4eba\u5de5\u667a\u80fd\uff0c\u7b49\u5f85\u4e3b\u4eba\u7684\u4f7f\u7528~.url",
            "119 Bytes"),
        File(
            "\u3010\u626b\u7801\u514d\u8d39\u73a9\u3011\u5947\u8ff9\u5c11\u5973-\u6deb\u840c\u5c11\u5973\u732e\u8eab\u62b5\u6297.gif",
            "1.7 MiB"),
        File(
            "\u3010\u626b\u7801\u514d\u8d39\u73a9\u3011\u5973\u795e\u7981\u4e66-\u732e\u796d\u8089\u4f53,\u8c03\u6559\u8272\u60c5\u9b54\u5973.gif",
            "1.5 MiB"),
        File(
            "\u3010\u6781\u54c1\u8272\u6e38\u3011\u5973\u7687\u8c03\u6559\u624b\u518c \u79d8\u871c\u64cd\u7ec3,\u4e8c\u6b21\u5143\u89d2\u8272\u80b2\u6210\u591a\u4eba\u6218\u7565.url",
            "120 Bytes"),
        File(
            "\uff20 \u706b\u71b1\u62db\u5546\u3002\u7247\u5934\u5e7f\u544a\u3002\u6c34\u5370\u5ba3\u4f20 \uff20.txt",
            "87 Bytes")
    ])


@pytest.fixture()
def dir_2():
    return Directory("Tina mercenaire de l'espace - French [DVDFRA] -LTPD",
                     [File("TINA.iso", "2.3 GiB")])


@pytest.mark.unittest
class TestSukebeiClient:
    @responses.activate
    def test_get_resource_1(self, client, text_aligner, dir_1, dir_2):
        resource = client.get_resource(3981804)

        assert resource.id == 3981804
        assert resource.category == CategoryType.REAL_LIFE_VIDEOS
        assert resource.title == "FC2-PPV-3861736 \u72ed\u3059\u304e\u308b\u8d85\u540d\u5668\u306b\u5927\u304d\u306a\u8089\u68d2\u3010\u9ad8\u6e05\u65e0\u7801\u3011"
        assert resource.information == "http://jpgm.cc"
        assert resource.torrent_download_url == "https://sukebei.nyaa.si/download/3981804.torrent"
        assert resource.magnet_url == "magnet:?xt=urn:btih:2747c438c89cfe2c78102efb9128a1c0e43f1e35&dn=FC2-PPV-3861736%20%E7%8B%AD%E3%81%99%E3%81%8E%E3%82%8B%E8%B6%85%E5%90%8D%E5%99%A8%E3%81%AB%E5%A4%A7%E3%81%8D%E3%81%AA%E8%82%89%E6%A3%92%E3%80%90%E9%AB%98%E6%B8%85%E6%97%A0%E7%A0%81%E3%80%91&tr=http%3A%2F%2Fsukebei.tracker.wf%3A8888%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce"
        assert resource.size_raw == "1.4 GiB"
        assert resource.timestamp == 1697708504
        assert resource.seeders == 15
        assert resource.leechers == 117
        assert resource.downloads == 18
        assert resource.is_trusted == False
        assert resource.is_remake == False
        assert resource.is_batch == False
        assert resource.info_hash == "2747c438c89cfe2c78102efb9128a1c0e43f1e35"
        assert resource.submitter == "XIAOW114514"
        assert resource.submitter_url == "https://sukebei.nyaa.si/user/XIAOW114514"
        text_aligner.assert_equal(
            resource.description_md,
            """
            ![A7jqHp.jpg](https://qpic.ws/images/2023/10/19/A7jqHp.jpg)
            """
        )

        assert resource.directory_tree == dir_1
        assert resource.directory_tree != dir_2

    @responses.activate
    def test_get_resource_2(self, client, text_aligner, dir_1, dir_2):
        resource = client.get_resource(3973877)

        assert resource.id == 3973877
        assert resource.category == CategoryType.ART_ANIME
        assert resource.title == "Tina mercenaire de l'espace - French [DVDFRA] -LTPD"
        assert resource.information == "No information."
        assert resource.torrent_download_url == "https://sukebei.nyaa.si/download/3973877.torrent"
        assert resource.magnet_url == "magnet:?xt=urn:btih:30f5d735857b5e38c0bc05cf93c02e5da95a7504&dn=Tina%20mercenaire%20de%20l%27espace%20-%20French%20%5BDVDFRA%5D%20-LTPD&tr=http%3A%2F%2Fsukebei.tracker.wf%3A8888%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce"
        assert resource.size_raw == "2.3 GiB"
        assert resource.timestamp == 1696677898
        assert resource.seeders == 13
        assert resource.leechers == 2
        assert resource.downloads == 596
        assert resource.is_trusted == False
        assert resource.is_remake == False
        assert resource.is_batch == False
        assert resource.info_hash == "30f5d735857b5e38c0bc05cf93c02e5da95a7504"
        assert resource.submitter == "Anonymous"
        assert resource.submitter_url == None
        text_aligner.assert_equal(
            resource.description_md,
            """
        ![alt text](https://i.imgur.com/Uvevlnw.jpg)
        ![alt text](https://i.imgur.com/f5uSto2.jpg)
            """
        )

        assert resource.directory_tree != dir_1
        assert resource.directory_tree == dir_2

    @responses.activate
    def test_iter_items(self, client):
        items = list(islice(client.iter_items('euphoria'), 200))
        assert len(items) == 200

        resource = items[0]
        assert resource.id == 3831069
        assert resource.category == CategoryType.ART_ANIME
        assert resource.comments == 2
        assert resource.title == "[Diogo4D] [BD][1080p] Euphoria - 01 [4965A23F].mkv"
        assert resource.url == "https://sukebei.nyaa.si/view/3831069"
        assert resource.torrent_download_url == "https://sukebei.nyaa.si/download/3831069.torrent"
        assert (resource.magnet_url ==
                "magnet:?xt=urn:btih:e0cd38a5f586cd8836c3ff3a87488c3e49f83065&dn=%5BDiogo4D%5D%20%5BBD%5D%5B1080p%5"
                "D%20Euphoria%20-%2001%20%5B4965A23F%5D.mkv&tr=http%3A%2F%2Fsukebei.tracker.wf%3A8888%2Fannounce&tr"
                "=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannoun"
                "ce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%"
                "2Fannounce")
        assert resource.size_raw == "970.7 MiB"
        assert resource.timestamp == 1676665352
        assert resource.seeders == 5
        assert resource.leechers == 0
        assert resource.downloads == 1628
        assert resource.is_trusted == False
        assert resource.is_remake == False
        assert resource.is_batch == False

        resource = items[-1]
        assert resource.id == 110878
        assert resource.category == CategoryType.ART_PICTURES
        assert resource.comments == 0
        assert (resource.title ==
                "(\u540c\u4ebaCG\u96c6)[Meta\uff1aEuphoria] \u304a\u3058\u3055\u3093\u306b\u25cb\u5b66\u751f\u5973"
                "\u5b50\u304c\u5b55\u307e\u3055\u308c\u308b\u4e8b\u6848\u304c\u767a\u751f\u3057\u307e\u3057\u305f"
                "\u3002.zip")
        assert resource.url == "https://sukebei.nyaa.si/view/110878"
        assert resource.torrent_download_url == "https://sukebei.nyaa.si/?f=0&c=0_0&q=euphoria&p=3"
        assert resource.magnet_url == \
               ("magnet:?xt=urn:btih:74867d314b51607a29b2ab3681722e5a687a3f20&dn=%28%E5%90%8C%E4%BA%BACG%E9%9B%8"
                "6%29%5BMeta%EF%BC%9AEuphoria%5D%20%E3%81%8A%E3%81%98%E3%81%95%E3%82%93%E3%81%AB%E2%97%8B%E5%AD%"
                "A6%E7%94%9F%E5%A5%B3%E5%AD%90%E3%81%8C%E5%AD%95%E3%81%BE%E3%81%95%E3%82%8C%E3%82%8B%E4%BA%8B%E6"
                "%A1%88%E3%81%8C%E7%99%BA%E7%94%9F%E3%81%97%E3%81%BE%E3%81%97%E3%81%9F%E3%80%82.zip&tr=http%3A%2"
                "F%2Fsukebei.tracker.wf%3A8888%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%"
                "3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fanno"
                "unce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce")
        assert resource.size_raw == "0 Bytes"
        assert resource.timestamp == 1330045980
        assert resource.seeders == 0
        assert resource.leechers == 0
        assert resource.downloads == 0
        assert resource.is_trusted == False
        assert resource.is_remake == False
        assert resource.is_batch == False

    @responses.activate
    def test_iter_items_no_remake(self, client):
        items = list(islice(client.iter_items('euphoria', filter=FilterType.NO_REMAKES), 200))
        assert len(items) == 189

        for item in items:
            assert not item.is_remake

    @responses.activate
    def test_iter_items_trusted_only(self, client):
        items = list(islice(client.iter_items('euphoria', filter=FilterType.TRUSTED_ONLY), 200))
        assert len(items) == 34

        for item in items:
            assert item.is_trusted

    @responses.activate
    def test_iter_items_art_anime(self, client):
        items = list(islice(client.iter_items('euphoria', category=CategoryType.ART_ANIME), 200))
        assert len(items) == 167

        for item in items:
            assert item.category == CategoryType.ART_ANIME

    @responses.activate
    def test_iter_items_art_anime_comments(self, client):
        items = list(islice(client.iter_items('euphoria', category=CategoryType.ART_ANIME,
                                              sort_by=SortBy.COMMENTS), 200))
        assert len(items) == 167

        for item in items:
            assert item.category == CategoryType.ART_ANIME

        resource = items[-1]
        assert resource.comments == 0

        resource = items[0]
        assert resource.comments == 7

    @responses.activate
    def test_iter_items_art_anime_comments_asc(self, client):
        items = list(islice(client.iter_items('euphoria', category=CategoryType.ART_ANIME,
                                              sort_by=SortBy.COMMENTS, order=Order.ASC), 200))
        assert len(items) == 167

        for item in items:
            assert item.category == CategoryType.ART_ANIME

        resource = items[0]
        assert resource.comments == 0

        resource = items[-1]
        assert resource.comments == 7
