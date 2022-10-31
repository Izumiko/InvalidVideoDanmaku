"""
从BiliPlus获取失效视频的信息，然后根据avid，cid从B站的Protobuf弹幕接口下载弹幕
"""
import sys
import info
import danmaku

def main():
    if len(sys.argv) < 2:
        bvid = input("请输入BvId：")
    else:
        bvid = sys.argv[1]
    video_info = info.get_video_info(bvid)
    for i in range(len(video_info["cid"])):
        print(f"正在下载第{i+1}P的弹幕")
        segments = video_info["duration"][i] // 360 if video_info["duration"][i] % 360 == 0 else video_info["duration"][i] // 360 + 1
        segments = 0
        danmakupb = danmaku.get_danmaku(video_info["cid"][i], video_info["aid"], segments)
        danmakuFileName = f"{video_info['bvid']}_{video_info['title']}_P{i+1}.ass"
        danmaku.write_danmaku(danmakupb, danmakuFileName)

if __name__ == '__main__':
    main()
