# 更新

8月7号的时候，Enpass Beta 的版本现在已经支持了MacOS 15 Beta，但我写代码的时候不知道，写都写了干脆就直接迁移吧，避免后面再出幺蛾子……

---

# 起因

见: https://discussion.enpass.io/index.php?/topic/31387-browser-extension-not-working-on-mac-os-15-sequoia/

~~由于Enpass的浏览器不支持MacOS 15 Beta版本~~

由于Enpass的三哥开发团队极慢的响应效率

由于Enpass运营团队不太美妙的态度

由于Enpass极差的导出格式

所以有了此项目

实测转换后可以完美兼容苹果新出的iCloud 密码App

# 用法

打开enpass，用json格式导出密码，然后改名为`enpass_export.json`，放到本目录下，直接运行main.py即可