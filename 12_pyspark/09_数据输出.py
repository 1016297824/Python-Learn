# RDD数据输出到Python的数据容器
from pyspark import SparkConf, SparkContext
import os

# 为pyspark配置python解释器路径
os.environ['PYSPARK_PYTHON'] = "G:/Python/3.10.6/python.exe"

# 创建spark连接配置
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 创建spark容器
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd1 = sc.parallelize([[0, 1], 2, 3, 4, 5])

# collect() -> list
rdd_list = rdd.collect()
rdd_list1 = rdd1.collect()
print(f"{type(rdd_list)} : {rdd_list}")
print(f"{type(rdd_list1)} : {rdd_list1}")

# ruduce()将RDD数据进行两两聚合
rdd_num = rdd.reduce(lambda a, b: a + b)
rdd_mul = rdd.reduce(lambda a, b: a * b)
print(f"{type(rdd_num)} : {rdd_num}")
print(f"{type(rdd_mul)} : {rdd_mul}")

# take()取出RDD中的前N个元素，组成一个list
rdd_take = rdd.take(3)
print(f"{type(rdd_take)} : {rdd_take}")

# count()计算RDD内有多少条数据
rdd_count = rdd.count()
rdd_count1 = rdd1.count()
print(f"{type(rdd_count)} : {rdd_count}")
print(f"{type(rdd_count1)} : {rdd_count1}")
