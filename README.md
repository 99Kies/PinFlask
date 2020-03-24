# PinFlask
**启动服务**

```bash
git clone https://github.com/99kies/pinflask
cd pinflask
docker build -t pinflask .
docker run -id -p [YourPort]:5000 --name pinflask pinflask
```



------



**题目小结**

所以千万不要在生产环境下打开debug，当然SSTI也一样需要防范！