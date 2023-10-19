# pynyaasi

[![PyPI](https://img.shields.io/pypi/v/pynyaasi)](https://pypi.org/project/pynyaasi/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pynyaasi)
![Loc](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/narugo1992/98f4fbc161c1f159764420446bd5b4e8/raw/loc.json)
![Comments](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/narugo1992/98f4fbc161c1f159764420446bd5b4e8/raw/comments.json)

[![Code Test](https://github.com/narugo1992/pynyaasi/workflows/Code%20Test/badge.svg)](https://github.com/narugo1992/pynyaasi/actions?query=workflow%3A%22Code+Test%22)
[![Package Release](https://github.com/narugo1992/pynyaasi/workflows/Package%20Release/badge.svg)](https://github.com/narugo1992/pynyaasi/actions?query=workflow%3A%22Package+Release%22)
[![codecov](https://codecov.io/gh/narugo1992/pynyaasi/branch/main/graph/badge.svg?token=XJVDP4EFAT)](https://codecov.io/gh/narugo1992/pynyaasi)

![GitHub Org's stars](https://img.shields.io/github/stars/narugo1992)
[![GitHub stars](https://img.shields.io/github/stars/narugo1992/pynyaasi)](https://github.com/narugo1992/pynyaasi/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/narugo1992/pynyaasi)](https://github.com/narugo1992/pynyaasi/network)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/narugo1992/pynyaasi)
[![GitHub issues](https://img.shields.io/github/issues/narugo1992/pynyaasi)](https://github.com/narugo1992/pynyaasi/issues)
[![GitHub pulls](https://img.shields.io/github/issues-pr/narugo1992/pynyaasi)](https://github.com/narugo1992/pynyaasi/pulls)
[![Contributors](https://img.shields.io/github/contributors/narugo1992/pynyaasi)](https://github.com/narugo1992/pynyaasi/graphs/contributors)
[![GitHub license](https://img.shields.io/github/license/narugo1992/pynyaasi)](https://github.com/narugo1992/pynyaasi/blob/master/LICENSE)

Python client for [nyaa.si](https://nyaa.si) and [sukebei.nyaa.si](https://sukebei.nyaa.si)

## Installation

You can simply install it with `pip` command line from the official PyPI site.

```shell
pip install pynyaasi
```

For more information about installation, you can refer
to [Installation](https://narugo1992.github.io/pynyaasi/main/tutorials/installation/index.html).

## Quick Start

### nyaa.si

```python
from pynyaasi.client import SortBy
from pynyaasi.nyaasi import NyaaSiClient, CategoryType

# create nyaa.si client
client = NyaaSiClient()

# search resource on nyaa.si
# NOTE: page is not necessary here, because `iter_items`
#       will grab the next page once the items on current page are all iterated 
#       until all the search result item run out
for item in client.iter_items('fire force'):
    print(item)

# The output should be:
# ListItem(id=1726561, category=<CategoryType.LITERATURE_ENGLISH: '3_1'>, comments=2, title='Enen no Shouboutai / Fire Force (2016-2023) (Digital) (danke-Empire)', url='https://nyaa.si/view/1726561', torrent_download_url='https://nyaa.si/download/1726561.torrent', magnet_url='magnet:?xt=urn:btih:3b60c0ca90427a845b1f3881a74cbda6cb120a46&dn=Enen%20no%20Shouboutai%20%2F%20Fire%20Force%20%282016-2023%29%20%28Digital%29%20%28danke-Empire%29&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce', size_raw='5.9 GiB', timestamp=1696796810, seeders=33, leechers=3, downloads=505, is_trusted=False, is_remake=False, is_batch=False)
# ListItem(id=1724856, category=<CategoryType.LITERATURE_ENGLISH: '3_1'>, comments=1, title='[0v3r] Fire Force v34 (2023) (Digital) (0v3r)', url='https://nyaa.si/view/1724856', torrent_download_url='https://nyaa.si/download/1724856.torrent', magnet_url='magnet:?xt=urn:btih:0e16fc5a42da95284846cca46fb57d4260d1432b&dn=%5B0v3r%5D%20Fire%20Force%20v34%20%282023%29%20%28Digital%29%20%280v3r%29&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce', size_raw='285.4 MiB', timestamp=1696514955, seeders=8, leechers=0, downloads=494, is_trusted=False, is_remake=False, is_batch=False)
# ListItem(id=1706354, category=<CategoryType.ANIME_NON_ENGLISH: '1_3'>, comments=0, title='[Pourquoi] Fire Force Henshū (Fan-Kaï) - Saison 01 - 1080p.MULTI.VFVOSTFR.x264', url='https://nyaa.si/view/1706354', torrent_download_url='https://nyaa.si/download/1706354.torrent', magnet_url='magnet:?xt=urn:btih:1a2f365364a6546988191f20d1bacad4621c34e9&dn=%5BPourquoi%5D%20Fire%20Force%20Hensh%C5%AB%20%28Fan-Ka%C3%AF%29%20-%20Saison%2001%20-%201080p.MULTI.VFVOSTFR.x264&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce', size_raw='12.0 GiB', timestamp=1692523341, seeders=10, leechers=1, downloads=114, is_trusted=False, is_remake=False, is_batch=False)
# ...

# search `fire force`, raw anime (without subtitle) only, order by comments
for item in client.iter_items('fire force', category=CategoryType.ANIME_RAW, sort_by=SortBy.COMMENTS):
    print(item)

# get resource on nyaa.si with id
resource = client.get_resource(1639366)

# see basic information
print(resource.id)  # 1639366
print(resource.title)  # [AI-Raws] 炎炎ノ消防隊 / Fire Force S1 BDRip 1080p MKV
print(resource.time)  # 2023-02-19T03:48:04+00:00
print(resource.is_trusted)  # False
print(resource.is_remake)  # False
print(resource.magnet_url)  # magnet:?xt=urn:btih:6869cfa3a7c03e41d7004205deca7e6bf62630c6&dn=%5BAI-Raws%5D%20%E7%82%8E%E7%82%8E%E3%83%8E%E6%B6%88%E9%98%B2%E9%9A%8A%20%2F%20Fire%20Force%20S1%20BDRip%201080p%20MKV&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce
print(resource.torrent_download_url)  # https://nyaa.si/download/1639366.torrent
print(resource.seeders)  # 1 (may be different when you run yourself)
print(resource.leechers)  # 1 (may be different when you run yourself)
print(resource.downloads)  # 226 (may be different when you run yourself)
print(resource.submitter)  # Anonymous

# directory tree is also here
print(resource.directory_tree)
# [AI-Raws][Fire Force] [folder, 20.6 GiB]
# ├── [AI-Raws] 炎炎の消防隊 #01 (BD HEVC 1920x1080 yuv444p10le FLAC)[00359E87].mkv [file, 1.1 GiB]
# ├── [AI-Raws] 炎炎の消防隊 #02 (BD HEVC 1920x1080 yuv444p10le FLAC)[DAC5E163].mkv [file, 807.8 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #03 (BD HEVC 1920x1080 yuv444p10le FLAC)[ED84DE60].mkv [file, 1.1 GiB]
# ├── [AI-Raws] 炎炎の消防隊 #04 (BD HEVC 1920x1080 yuv444p10le FLAC)[4D006A6F].mkv [file, 935.0 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #05 (BD HEVC 1920x1080 yuv444p10le FLAC)[25ACB9BA].mkv [file, 789.5 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #06 (BD HEVC 1920x1080 yuv444p10le FLAC)[ABE87DE7].mkv [file, 1.1 GiB]
# ├── [AI-Raws] 炎炎の消防隊 #07 (BD HEVC 1920x1080 yuv444p10le FLAC)[BD4F5594].mkv [file, 956.5 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #08 (BD HEVC 1920x1080 yuv444p10le FLAC)[62C1CD6B].mkv [file, 828.8 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #09 (BD HEVC 1920x1080 yuv444p10le FLAC)[917EA0CE].mkv [file, 922.5 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #10 (BD HEVC 1920x1080 yuv444p10le FLAC)[B310DA52].mkv [file, 656.0 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #11 (BD HEVC 1920x1080 yuv444p10le FLAC)[7DB51188].mkv [file, 671.2 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #12 (BD HEVC 1920x1080 yuv444p10le FLAC)[5B313F70].mkv [file, 718.8 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #13 (BD HEVC 1920x1080 yuv444p10le FLAC)[B0A57086].mkv [file, 737.4 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #14 (BD HEVC 1920x1080 yuv444p10le FLAC)[205D3328].mkv [file, 1017.5 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #15 (BD HEVC 1920x1080 yuv444p10le FLAC)[F938397F].mkv [file, 874.5 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #16 (BD HEVC 1920x1080 yuv444p10le FLAC)[635E0F84].mkv [file, 845.5 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #17 (BD HEVC 1920x1080 yuv444p10le FLAC)[62A10712].mkv [file, 828.2 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #18 (BD HEVC 1920x1080 yuv444p10le FLAC)[9EE1364F].mkv [file, 832.4 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #19 (BD HEVC 1920x1080 yuv444p10le FLAC)[30EB7A35].mkv [file, 852.6 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #20 (BD HEVC 1920x1080 yuv444p10le FLAC)[075B7425].mkv [file, 838.2 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #21 (BD HEVC 1920x1080 yuv444p10le FLAC)[A92DBA56].mkv [file, 748.0 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #22 (BD HEVC 1920x1080 yuv444p10le FLAC)[43A840DC].mkv [file, 820.5 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #23 (BD HEVC 1920x1080 yuv444p10le FLAC)[4185E25F].mkv [file, 829.0 MiB]
# ├── [AI-Raws] 炎炎の消防隊 #24 (BD HEVC 1920x1080 yuv444p10le FLAC)[2B28C1FE].mkv [file, 851.3 MiB]
# ├── [AI-Raws] 炎炎の消防隊 ノンクレジットED (BD HEVC 1920x1080 yuv444p10le FLAC)[797400C4].mkv [file, 102.5 MiB]
# ├── [AI-Raws] 炎炎の消防隊 ノンクレジットED2 (BD HEVC 1920x1080 yuv444p10le FLAC)[40B0883F].mkv [file, 58.6 MiB]
# ├── [AI-Raws] 炎炎の消防隊 ノンクレジットOP (BD HEVC 1920x1080 yuv444p10le FLAC)[1B2232B5].mkv [file, 113.4 MiB]
# └── [AI-Raws] 炎炎の消防隊 ノンクレジットOP2 (BD HEVC 1920x1080 yuv444p10le FLAC)[B452057F].mkv [file, 78.5 MiB]

```

For more usage, refer
to [documentation of NyaaSiClient](https://narugo1992.github.io/pynyaasi/main/api_doc/nyaasi/index.html#nyaasiclient).

### sukebei.nyaa.si

Similar with nyaa.si, you simply need to use a `SukebeiClient`, and oth

```python
from pynyaasi.client import SortBy
from pynyaasi.sukebei import SukebeiClient, CategoryType

# create sukebei.nyaa.si client
client = SukebeiClient()

# search resource on sukebei.nyaa.si
for item in client.iter_items('euphoria'):
    print(item)

# search `euphoria`, art anime (no human porn) only, order by comments
client.iter_items('euphoria', category=CategoryType.ART_ANIME, sort_by=SortBy.COMMENTS)

# get resource on sukebei.nyaa.si with id
resource = client.get_resource(3973877)
```

For more usage, refer
to [documentation of SukebeiClient](https://narugo1992.github.io/pynyaasi/main/api_doc/sukebei/index.html#sukebeiclient).


