# pyspark练习2
# 整理每个单词的个数
import json
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "G:/Python/3.10.6/python.exe"
os.environ['HADOOP_HOME'] = "G:/Hadoop/3.3.6"

conf = SparkConf().setMaster("local[*]").setAppName("practice_spark")
conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

# 读取文件中的数据
rdd = sc.textFile("search_log.txt")
# print(rdd.collect())
# 通过 "\t" 分割数据
rdd_map = rdd.map(lambda x: x.split("\t"))
# print(rdd_map.collect())

# 需求一：打印输出->热门搜索时间段Top3
# 取得时间数据,并组成二元元组
rdd_time_total = rdd_map.map(lambda x: (x[0][:2], 1))
# print(rdd_time_single.collect())
# 统计每个时间段的使用量，并从大到小排序后取出前三个元素
rdd_time_top3 = rdd_time_total.reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).take(3)

# 需求二：打印输出热门搜索词Top3
# 取得搜索词数据
rdd_search_total = rdd_map.map(lambda x: (x[2], 1))
# 统计每个搜索词个数,并从大到小排序后取出前三个元素
rdd_search_top3 = rdd_search_total.reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)

# 需求三：统计“黑马程序员”关键字在那个时间段最多
# 取得带有“黑马程序员”的时间数据，并组成二元元组
rdd_time_total = rdd_map.filter(lambda x: x[2] == "黑马程序员").map(lambda x: x[0]). \
    map(lambda x: ((x[0] + x[1]), 1))
# 统计每个时间段的使用量，并从大到小排序后出第一个元素
rdd_time_top1 = rdd_time_total.reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(1)

# 需求四：将数据转换为JSON格式，输出为文件夹
rdd_map.map(lambda x: \
                {"time": x[0], "user_id": x[1], "search_word": x[2], \
                 "rank1": x[3], "rank2": x[4], "url": x[5]}). \
    saveAsTextFile("search_log")

# 需求一：输出前三的时间段
print("搜索前三的时间段：", end="")
for time in rdd_time_top3:
    print(time[0], end="点；")
print()

# 需求二：输出前三的搜索词
print("搜索前三的搜索词：", end="")
for search in rdd_search_top3:
    print(search[0], end="；")
print()

# 需求三：输出“黑马程序员”关键字搜索最多的时间段
print("搜索“黑马程序员”最多的时间段是：" + str(rdd_time_top1[0][0]) + "点")
print()
