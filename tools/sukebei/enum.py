from typing import List, Tuple

from pyquery import PyQuery as pq

from pynyaasi.utils import get_session

WEBSITE_ROOT = 'https://sukebei.nyaa.si'


def get_c_list() -> List[Tuple[str, str]]:
    session = get_session()
    resp = session.get(WEBSITE_ROOT)
    resp.raise_for_status()
    page = pq(resp.text)

    select, *_ = page('form select[name=c]').items()
    retval = []
    for item in select('option').items():
        if not item.attr('value'):
            continue
        retval.append((item.attr('title'), item.attr('value')))

    return retval


def get_f_list() -> List[Tuple[str, str]]:
    session = get_session()
    resp = session.get(WEBSITE_ROOT)
    resp.raise_for_status()
    page = pq(resp.text)

    select, *_ = page('form select[name=f]').items()
    retval = []
    for item in select('option').items():
        if not item.attr('value'):
            continue
        retval.append((item.attr('title'), item.attr('value')))

    return retval
