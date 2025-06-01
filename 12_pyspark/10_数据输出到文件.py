# 将RDD数据输出到文件夹中
from pyspark import SparkConf, SparkContext
import os

# 为pyspark配置python解释器路径
os.environ['PYSPARK_PYTHON'] = "G:/Python/3.10.6/python.exe"
os.environ['HADOOP_HOME'] = "G:/Hadoop/3.3.6"

# 创建spark连接配置
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
conf.set("spark.default.parallelism", "1")  # 设置全局默认并行度为1
# 创建spark容器
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd1 = sc.parallelize([1, 2, 3, 4, 5], 6)  # 单个设置并行度为6

# 将RDD数据输出到文件
rdd.saveAsTextFile("save")
rdd1.saveAsTextFile("save1")