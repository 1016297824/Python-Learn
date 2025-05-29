# 使用flatMap方法处理RDD数据
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
    ["霸气可爱小蜜蜂 年龄 18", "霸气可爱小州官 身高 180", "霸气可爱大耐人 体重 108", "霸气可爱小懒虫 性别 女"])
# 将RDD中的数据一个个短语提取出来
# result = rdd.collect()
rdd1 = rdd.map(lambda x: x.split(" "))
# result = rdd1.collect()
print(rdd1.collect())
# 以上结果中有嵌套，可以改用flatMap取消嵌套
# result = rdd.collect()
rdd2 = rdd.flatMap(lambda x: x.split(" "))
# result = rdd2.collect()
print(rdd2.collect())
