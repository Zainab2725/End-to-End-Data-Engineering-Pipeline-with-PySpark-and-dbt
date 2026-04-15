from pyspark.sql.functions import *
from pyspark.sql.types import *
from typing import List
from pyspark.sql import DataFrame
from pyspark.sql.window import Window

class custom_transformations:

    def dedup(self,df:DataFrame,target_cols:List,latest_time):
        df = df.withColumn('dedupconcat',concat(*target_cols))
        df = df.withColumn('dedupCount',row_number().over(Window.partitionBy('dedupconcat').orderBy(desc(latest_time))))
        df = df.filter(col('dedupCount')==1)
        df = df.drop('dedupconcat','dedupCount')

        return df

