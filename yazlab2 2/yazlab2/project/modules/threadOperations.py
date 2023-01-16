
from modules.bigDataOperations import dataOperations
from multiprocessing import Pool,Process,current_process
from itertools import product
import numpy as np
from pandasql import sqldf
import pandas as pd
import time

def createThreads(function, threadNumber, column1, similarityRate):
    results = []
    with Pool(threadNumber) as pool:
        df = dataOperations()
        columnList1 = df.get(column1)
        tuples = list(product(columnList1, columnList1))
        for id in range(len(tuples)):
            tuples[id] += (similarityRate/100,)
        start_time = time.perf_counter()
        results = pool.starmap(function, tuples)
        results = list(filter(lambda row: row is not None, results))
        end_time = time.perf_counter()
        job_time=end_time-start_time
        pool.close()
        pool.join()
        return results,job_time


def createThreadsForSpecific(function, threadNumber, column1, column2, variable, similarityRate):
    response = []
    with Pool(threadNumber) as pool:
        df = dataOperations()
        results = df[df[column1] == variable]
        results = results[column2]
        columnList2 = df.get(column2)
        tuples = list(product(results, columnList2))
        for id in range(len(tuples)):
            tuples[id] += (similarityRate/100,)
        start_time = time.perf_counter()
        response = pool.starmap(function, tuples)
        response = list(filter(lambda row: row is not None, response))
        end_time = time.perf_counter()
        pool.close()
        pool.join()
        job_time = end_time-start_time
    return response,job_time


def query(df, column1):
    return sqldf("SELECT {0} FROM df GROUP BY {1}".format(column1, column1), locals())


def createThreadsForQuery(df, function, threadNumber, column1, column2, column3, similarityRate):
    results = []
    return_list=[]
    response=[]
    with Pool(threadNumber) as pool:
        attributes = query(df, column1)
        start_time = time.perf_counter()
        for res in attributes[column1]:
            # column1=product column2=issue column3=company
            check_list = df[df[column1] == res][column2]
            tuples = list(product(check_list, check_list))
            for id in range(len(tuples)):
                tuples[id] += (similarityRate/100,)
            results.append(
                list(filter(lambda row: row is not None, pool.starmap(function, tuples))))
            for res1 in results:
                return_list.append((res1[0][0], res1[0][1], res1[0][2], pd.Series.to_list(df[((df[column2] == res1[0][1]) | (
                    df[column2] == res1[0][2])) & (df[column1] == res)][column3])))
        end_time = time.perf_counter()
        pool.close()
        pool.join()
        for res in return_list:
            if bool(res[3]):
                response.append(res)    
        job_time = end_time-start_time
        return response,job_time
