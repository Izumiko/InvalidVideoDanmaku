# 下载失效视频的弹幕

失效视频的BvId或AvId可以通过[哔哩哔哩(B站|Bilibili)收藏夹Fix](https://greasyfork.org/zh-CN/scripts/383143)，或者直接右键对应的收藏夹视频，检查元素，从`data-aid`属性处获得。

有了ID之后，通过B站的protobuf弹幕接口下载历史弹幕。旧的xml接口无法使用了，所以需要一个脚本把protobuf的弹幕转换一下，因而有了本脚本。

## 用法

```bash
python3 main.py <BVxxxx/avxxxxx>
# 或
python3 main.py
```
