# 使用filter方法处理RDD数据
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
# 使用filter方法过滤RDD数据
# 保留偶数
rdd1 = rdd.filter(lambda x: x % 2 == 0)
print(rdd1.collect())


# 保留奇数
def func(data):
    if data % 2 == 0:
        return False
    else:
        return True


rdd2 = rdd.filter(func)
print(rdd2.collect())
