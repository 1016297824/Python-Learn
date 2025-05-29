# 使用map方法处理RDD数据
from pyspark import SparkConf, SparkContext
import os

# 为pyspark配置python解释器路径
os.environ['PYSPARK_PYTHON'] = "G:/Python/3.10.6/python.exe"

# 创建spark连接配置
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 创建spark容器
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])


# rdd = sc.textFile("hello.txt")
def func(data):
    return data * 10


# rdd2 = rdd.map(func)
rdd2 = rdd.map(lambda x: x * 10)
print(rdd2.collect())

# 链式调用
rdd3 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)
print(rdd3.collect())

sc.stop()
