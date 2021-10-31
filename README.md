# Google-Spider
谷歌爬虫，自动解析谷歌搜索信息，需搭配clash使用，生成cvs

代理端口：7890 请自行设置（搭建clash）
![image](https://user-images.githubusercontent.com/71580418/139575873-ba24e826-44fe-4295-a6e4-1470fe4578e3.png)



# 使用方法

简单粗暴  python3 mian.py 就ok

![image](https://user-images.githubusercontent.com/71580418/139575882-54e2e397-8227-4d79-8523-8ed7bf726f1e.png)
搜索：渗透测试博客
爬取100页数据
![image](https://user-images.githubusercontent.com/71580418/139575911-7e408ffe-058b-4f68-b6c9-c1c44bad2326.png)
会创建同名文件，记录100也所有的数据
![image](https://user-images.githubusercontent.com/71580418/139575929-fb769818-fdf8-4a13-a6ad-bd88fc3166d2.png)
接着会对数据进行去重，整理，规范格式，读取ip，处理后的数据保存在同名的csv文件中
![image](https://user-images.githubusercontent.com/71580418/139576000-e5a3d6f4-758e-4d1e-8001-050d735c5499.png)
![image](https://user-images.githubusercontent.com/71580418/139576013-7dfb03f1-637d-4983-a1e8-635dd28d2452.png)





