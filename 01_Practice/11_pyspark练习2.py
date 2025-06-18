# pyspark练习2
# 整理每个单词的个数
import json
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "G:/Python/3.10.6/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("practice_spark")
sc = SparkContext(conf=conf)

# 通过spark容器读取文件到RDD
rdd = sc.textFile("orders.txt")
# print(rdd.collect())
# 分割并转化为单个JSON数据
rdd_JSON = rdd.flatMap(lambda line: line.split("|")).map(lambda line: json.loads(line))
# print(rdd_JSON.collect())

# 需求一：从大到小排名各个城市销售额
# 创建二元元组存储城市和销售额
rdd_city_sales = rdd_JSON.map(lambda data: (data["areaName"], int(data["money"])))
# print(rdd_city_sales.collect())
# 统计各个城市的总销售额并从大到小排序
rdd_city_total = rdd_city_sales.reduceByKey(lambda x, y: x + y).sortBy(lambda data: data[1], ascending=False,
                                                                       numPartitions=1)
print(rdd_city_total.collect())

# 需求二：查询全部城市的商品类别
# 存储所有商品
rdd_wares_type = rdd_JSON.map(lambda data: data["category"])
# 商品去重
rdd_type_total = rdd_wares_type.distinct()
print(rdd_type_total.collect())

# 需求三：查询北京的商品类别
# 存储北京的商品
rdd_BeiJing = rdd_JSON.filter(lambda data: data["areaName"] == "北京").map(lambda data: data["category"]).distinct()
print(rdd_BeiJing.collect())
