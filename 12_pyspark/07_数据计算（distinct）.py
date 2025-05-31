# 使用distinct方法处理RDD数据
from pyspark import SparkConf, SparkContext
import os

# 为pyspark配置python解释器路径
os.environ['PYSPARK_PYTHON'] = "G:/Python/3.10.6/python.exe"

# 创建spark连接配置
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 创建spark容器
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 1, 3, 3, 3])
# 使用distinct方法为RDD数据去重
rdd1 = rdd.distinct()
print(rdd1.collect())
