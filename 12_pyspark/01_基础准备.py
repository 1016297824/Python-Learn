# pyspark入门准备
from pyspark import SparkConf, SparkContext

# 创建SparkConf对象
# conf = SparkConf()
# conf.setMaster("local[*]")
# conf.setAppName("test_spark_app")
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")  # 链式调用

# 基于SparkConf对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 打印spark运行版本
print(sc.version)

#停止SparkContext运行（停止PySpark程序运行）
sc.stop()