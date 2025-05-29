# 使用reduceByKey方法处理RDD数据
from pyspark import SparkConf, SparkContext
import os

# 为pyspark配置python解释器路径
os.environ['PYSPARK_PYTHON'] = "G:/Python/3.10.6/python.exe"

# 创建spark连接配置
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 创建spark容器
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(
    [("男", 15), ("女", 56), ("男", 85), ("女", 73), ("男", 34), ("女", 45), ("男", 52), ("女", 76), ("男", 18)])
# 使用reduceByKey方法处理RDD
# 注意reduceByKey方法针对KV型数据：如(key,value)二元元组
rdd1 = rdd.reduceByKey(lambda x, y: x + y)
result = rdd1.collect()
print(result)
