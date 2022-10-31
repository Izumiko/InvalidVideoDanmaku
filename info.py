from typing import Any
import requests


def get_video_info(bvid: str) -> dict[str, Any]:
    """Get video info from bvid.

    Args:
        bvid (str): BvId
    """
    id = bvid[2:] if bvid.startswith("av") else bvid
    info_api = "https://www.biliplus.com/api/view?id={id}"
    res_json = requests.get(info_api.format(id=id)).json()
    try:
        id = res_json["id"]
    except KeyError:
        raise Exception(f"无法下载该视频 {bvid}，原因：{res_json['message']}")

    return {
        "aid": res_json["v2_app_api"]["aid"],
        "bvid": bvid,
        "cid": [i["cid"] for i in res_json["v2_app_api"]["pages"]],
        "duration": [i["duration"] for i in res_json["v2_app_api"]["pages"]],
        "title": res_json["title"],
    }