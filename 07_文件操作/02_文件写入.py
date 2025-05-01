# 文件写入
# 打开/新建文件
f = open("write.txt", "w", encoding="utf-8")
# 写入文件（缓存）
f.write("霸气可爱小蜜蜂")
# 刷新，将缓存内容写入文件
f.flush()
f.close()
