## 郑州工业应用技术学院迎新系统抢床位脚本

下载main.py
安装python 和 requests 模块

```bash
pip install requests
```

运行
```bash
python main.py
```

这几个必须填写

![image](https://sudo0m.github.io/picx-images-hosting/20240824/image.45hljpora0.webp)

进入这个网站登录账号

https://welcomepc.zzuit.edu.cn/#/

进入到 *自选宿舍*

![image](https://sudo0m.github.io/picx-images-hosting/20240824/image.4xuh1g52a6.webp)

打开控制台 刷新 然后 找到这一栏

### 获取 Authorization

![image](https://sudo0m.github.io/picx-images-hosting/20240824/image.60u6cbyg9c.webp)

### 获取 cookie

![image](https://sudo0m.github.io/picx-images-hosting/20240824/image.3d4q1z5sod.webp)



### 获取 BedId

![image](https://sudo0m.github.io/picx-images-hosting/20240824/image.wihzae8y5.webp)
## StudentId 就是你的学号

把这些数据填写到脚本上即可

