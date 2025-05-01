# 文件追加
# 打开/创建一个文件
f = open("add.txt", "a", encoding="utf-8")
# 文件写入（缓存）
f.write("霸气可爱小蜜蜂\n")
f.write("霸气可爱小州官")
# 刷新，将缓存内容写入文件
f.flush()
f.close()
