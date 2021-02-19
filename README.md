# 原神圣遗物半自动爬虫

## 说明

直接抓取原神界面中的圣遗物数据

目前只适配了**背包页面**的抓取

准确率：97.5%(普通通用接口，对 40 件随机圣遗物识别，统计完全正确的数量为 39)

(2021/2/18 统计，项目开发中，准确度会不断上升。也可以用高精度接口获得更好的效果)

## 使用说明

1. 修改 config.ini 中的 access_token 为自己的百度文字识别 access_token,选择自己使用的接口(高精度 or 普通)
2. 打开原神，进入背包圣遗物界面
3. 在原神中按<kbd>Alt</kbd>+<kbd>Enter</kbd>进入窗口模式
4. 运行 程序(此时可以隐藏原神窗口)
5. 点击抓取按钮抓取当前显示的圣遗物，点击保存按钮保存

## 配置文件说明

### [api]

**access_token**:百度 ocr access_token 获取方法不再赘述  
accurate_url/general_url:api 地址，一般不用更改  
use：使用高精度还是普通接口(accurate_url/general_url)

### [grasp_setting]

window_title:要抓取的窗口名，主要方便 PS 端/手机模拟器使用  
left,top,right,bottom:面板在窗口中的位置(按照比例出现,如 left=0.67 表示 left 线段占总窗口的 67%)(**典型的 16:9 分辨率使用预置选项即可**)  
![setting](https://github.com/yllhwa/GenshinSpider/blob/main/img/etting.png)

## 输出

- 以 json 格式保存到剪贴板
- 以 excel 形式保存到当前目录

## 示例图片

进入窗口模式：  
[![ygWHz9.md.png](https://s3.ax1x.com/2021/02/17/ygWHz9.md.png)](https://imgchr.com/i/ygWHz9)  
抓取：  
[![ygW7RJ.md.png](https://s3.ax1x.com/2021/02/17/ygW7RJ.md.png)](https://imgchr.com/i/ygW7RJ)  
输出表格：  
[![ygWoiF.md.png](https://s3.ax1x.com/2021/02/17/ygWoiF.md.png)](https://imgchr.com/i/ygWoiF)

## LOG

- [x] 重构、整理代码(2021/2/17)
- [x] 常见不合理错误纠正(2021/2/18)
- [x] 去除部分依赖以减小打包体积(已替换 pandas 依赖为 xlrd 和 xlutils，打包体积减半为 38MB)(2021/2/18)
- [x] 将配置项分离为文件
- [x] 重构、整理代码
- [ ] 优化抓取速度和反馈(doing)
- [ ] 其他界面抓取
- [ ] 武器等抓取

## 常见问题

1. 按<kbd>Alt</kbd>+<kbd>Enter</kbd>进入窗口模式是什么意思？  
   原神默认是以独占全屏的形式出现的，要置顶本窗口必须使其窗口化。  
   要返回独占全屏同样是按<kbd>Alt</kbd>+<kbd>Enter</kbd>
2. 抓取到启动器怎么回事？  
   抓取窗口是判断窗口标题为原神实现的，推荐不使用启动器启动，如果确实抓出来了把抓出的启动器窗口关闭即可。关闭后应该不会再次抓取。
3. 有封号风险吗？  
   抓取的原理是对窗口截图识别，没有对原神本身进行任何修改和干扰，理论上不会产生风险。~~这都要封号我就不玩了~~
4. 闪退？  
   目前异常处理还没有做完，发生闪退请将报错信息提供到 issue
5. 代码怎么写得这么烂？  
   临时学的 pyqt5，在改了在改了。欢迎 pull request~~或者直接写个更好的给我用~~
6. 为什么半自动？不能全自动？  
   先把半自动做好。
7. 关于百度文字识别？  
   可以在通用普通接口的情况下取得除等级外很好的效果，也可以使用高精度接口（每日 500 次免费）获得更好的效果。access_token 的获取方法不再赘述。
8. 显示效果相关问题？  
   作者优先在 4k 环境下开发，但是只要游戏界面比例是典型的 16:9 都可以正常抓取，只是显示效果可能有细微的差距。

## 致谢

[原神圣遗物记录脚本](https://github.com/kyloris0660/GenshinArtifactRecorder)
