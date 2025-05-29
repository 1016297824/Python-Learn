# pyspark练习1
# 整理每个单词的个数
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "G:/Python/3.10.6/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("practice_spark")
sc = SparkContext(conf=conf)

# 获取文件内容，存入列表
item_list: list[str] = []
with open("pyspark1.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        line = line.replace("  ", " ")
        # print(line.split(" "))
        item_list += line.split(" ")
# print(item_list)

# 将获得的数据导入RDD
rdd = sc.parallelize(item_list)
# 将RDD数据存储为二元元组
rdd_KY = rdd.map(lambda x: (x, 1))
# 统计每个元素的个数
rdd_reduce = rdd_KY.reduceByKey(lambda x, y: x + y)
# 输出结果
result = rdd_reduce.collect()
print(result)
