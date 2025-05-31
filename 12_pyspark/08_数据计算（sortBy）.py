# 使用sortBy方法处理RDD数据
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

# 获取文件内容，存入列表
rdd = sc.textFile("pyspark1.txt")


# print(rdd.collect())
def func(line):
    line = line.strip()
    line = line.replace("  ", " ")
    result = line.split(" ")
    return result


rdd_list = rdd.flatMap(func)
# print(rdd_list.collect())
# 将RDD数据存储为二元元组
rdd_KY = rdd_list.map(lambda x: (x, 1))
# print(rdd_KY.collect())
# 统计每个元素的个数
rdd_reduce = rdd_KY.reduceByKey(lambda x, y: x + y)

# 使用sortBy方法排序
# 使用个数排序
rdd1 = rdd_reduce.sortBy(lambda x: x[1], ascending=True, numPartitions=1)
print(rdd1.collect())
# 使用名称进行排序
rdd2 = rdd_reduce.sortBy(lambda x: x[0], ascending=True, numPartitions=1)
print(rdd2.collect())
# 对比test
test_rdd = sc.parallelize(["霸气可爱小天才", "霸气可爱小鲤鱼", "霸气可爱小懒虫", "霸气可爱小蜜蜂", "霸气可爱小州官"])
new_rdd = test_rdd.sortBy(lambda x: x, ascending=True, numPartitions=1)
print(new_rdd.collect())


# 使用名称最后一个汉字排序
def func(data: tuple[str, int]):
    index = len(data[0]) - 1
    # print(data[0][index])
    return data[0][index]


rdd3 = rdd_reduce.sortBy(func, ascending=True, numPartitions=1)
print(rdd3.collect())
# 对比test
test_rdd1 = sc.parallelize(["蜂", "才", "官", "虫", "鱼"])
new_rdd1 = test_rdd1.sortBy(lambda x: x, ascending=True, numPartitions=1)
print(new_rdd1.collect())
