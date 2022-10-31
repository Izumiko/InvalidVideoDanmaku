import requests
from biliass import Danmaku2ASS

def get_protobuf_danmaku(cid: int, aid: int, segment_id: int = 1) -> bytes:
    danmaku_api = "https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&pid={aid}&segment_index={segment_id}"
    return requests.get(danmaku_api.format(cid=cid, aid=aid, segment_id=segment_id)).content

def get_danmaku(cid: int, aid: int, last_n_segments: int = 2) -> list[bytes]:
    danmaku_data: list[bytes] = []
    if last_n_segments == 0:
        i = 1
        while True:
            danmaku = get_protobuf_danmaku(cid, aid, i)
            if len(danmaku) == 0:
                break
            danmaku_data.append(danmaku)
            i += 1
    else:
        for i in range(1, last_n_segments + 1):
            danmaku_data.append(get_protobuf_danmaku(cid, aid, i))
    return danmaku_data

def write_danmaku(danmaku_data: list[bytes], filename: str) -> None:
    with open(filename, "w", encoding="utf-8", errors="replace") as f:
        f.write(Danmaku2ASS(danmaku_data, 1920, 1080,
                            input_format="protobuf",reserve_blank=0,
                            font_face="Microsoft YaHei", font_size=40,
                            text_opacity=0.75, duration_marquee=15.0,
                            duration_still=10.0, comment_filter=None,
                            is_reduce_comments=False, progress_callback=None))