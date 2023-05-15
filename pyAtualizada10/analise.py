from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, when

# Inicializar sessão do Spark
spark = SparkSession.builder.appName("LargeDataAnalysis").getOrCreate()

# Carregar dados em um DataFrame do Spark
df = spark.read.csv("large_data.csv", header=True, inferSchema=True)

# Adicionar uma nova coluna ao DataFrame com base em uma condição
df = df.withColumn("new_column", when(col("column_name") > 5, 1).otherwise(0))

# Agrupar dados por uma coluna e calcular a média de outra coluna
grouped = df.groupby("group_column_name").agg(avg(col("column_to_average")), count("*"))

# Filtrar linhas com base em uma condição
filtered = grouped.filter(col("avg(column_to_average)") > 10)

# Mostrar as primeiras linhas do DataFrame filtrado
filtered.show(10)

# Parar a sessão do Spark
spark.stop()
