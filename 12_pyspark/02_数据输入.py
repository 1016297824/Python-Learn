# 数据输入
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

# 通过parallelize方法将Python对象加载到Spark内，成为RDD对象
# RDD：弹性分布式数据集
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize("霸气可爱小蜜蜂")
rdd4 = sc.parallelize({1, 2, 3, 4, 5})
rdd5 = sc.parallelize({"key1": "value1", "key2": "value2", "key3": "value3"})  # 注意：字典只会存储key

print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())
print()
# 通过textFile方法，读取文件数据加载到spark内，成为RDD对象
rdd = sc.textFile("hello.txt")
print(rdd.collect())

sc.stop()