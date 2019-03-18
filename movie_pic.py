from lxml import etree
from urllib import request

if __name__ == '__main__':
    url = "https://movie.douban.com/top250"
    resp = request.urlopen(url) # 发送请求
    if resp.status == 200:
        e_nodes = etree.HTML(resp.read().decode())  # 将HTML字符串转换为根节点
        pic_paths = e_nodes.xpath("//div[@class='pic']//img/@src") # 执行xpath搜索路径，结果以列表返回
        for pic_path in pic_paths:   # 遍历25张图片路径
            pic_name = pic_path.split("/")[-1]  # 获取当前遍历的图片名称
            request.urlretrieve(pic_path,filename="./imgs/"+pic_name)  # 下载图片
            print(pic_name+"下载完毕！")