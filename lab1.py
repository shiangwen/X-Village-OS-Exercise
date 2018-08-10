
import threading
import multiprocessing
import random
import time
import numpy as np

matA = np.random.randint(10, size = (10, 10))
matB = np.random.randint(10, size = (10, 10))

print(matA)
print(matB)

result = np.zeros((matA.shape[0], matB.shape[1]))

def thread_function(i,matB):
    result[i] = np.matmul(matA[i], matB)
    #print("thread_function:\n",result)

def process_function(i,matA,matB,result_queue):
    ii=np.matmul(matA[i],matB)
    result_queue.put((i,ii))


def main_numpy():
    
    start_time_numpy=time.time()  
    for row in range(0, matA.shape[0]):
        result[row] = np.matmul(matA[row], matB) #直接這樣寫
    end_time_numpy=time.time()

    print('Answer is correct:', np.all(np.matmul(matA, matB) == result)) #判斷是否正確
    print("numpy計算之時間為：",end_time_numpy-start_time_numpy)
if __name__== "__main__":
    main_numpy()
print("==========================================================")
def main_thread():

    start_time_thread=time.time()  
    threads=[]
    for i in range(matA.shape[0]):

        thread = threading.Thread(target = thread_function, args = (i, matB)) 
        threads.append(thread)

    
    for thread in threads:
        thread.start()


    for thread in threads:
        thread.join()
    end_time_thread=time.time()

    print('Answer is correct:',np.all(np.matmul(matA, matB) == result))
    print("thread計算之時間為：",end_time_thread-start_time_thread)
if __name__== "__main__":
    main_thread()
print("==========================================================")
def process_func(i,matA,matB,result_queue):
    ii = np.matmul(matA[i], matB)
    result_queue.put((i, ii))

def main_process():
    matA = np.random.randint(10, size = (10, 10))
    matB = np.random.randint(10, size = (10, 10))
    result = np.zeros((matA.shape[0], matB.shape[1]))
    print(matA)
    print(matB)
    start_time = time.time()
    result_queue = multiprocessing.Manager().Queue()
    process=10
    jobs = []

    for i in range(0, matA.shape[0]):
        process = multiprocessing.Process(target = process_func, args = (i,matA,matB,result_queue))
        jobs.append(process)

    for process in jobs:
        process.start()

    for process in jobs:
        process.join()

    while not result_queue.empty():
        q = result_queue.get()
        result[q[0]]=q[1]
        # print(q[0], q[1])

    print('Answer is correct:', np.all(np.matmul(matA,matB) == result))
    end_time = time.time()
    print('process計算之時間為：', end_time - start_time)
if __name__== "__main__":
    main_process()
'''
import threading
import multiprocessing
import random
import time
import numpy as np


def process_function(i,matA,matB,result_queue):
    ii=np.matmul(matA[i],matB)
    result_queue.put((i,ii))
def main():
    matA = np.random.randint(10, size = (100, 100))
    matB = np.random.randint(10, size = (100, 100))

    #print(matA)
    #print(matB)

    result = np.zeros((matA.shape[0], matB.shape[1]),dtype=np.int)

    start_time_process=time.time()

    result_queue = multiprocessing.Manager().Queue()
    
    process=10

    
    jobs = []

    for i in range(0,matA.shape[0]):
        process = multiprocessing.Process(target = process_function, args = (i,matA,matB,result_queue)) #??????????
        jobs.append(process)

    for process in jobs:
        process.start()

    for process in jobs:
        process.join()

    while not result_queue.empty():
        res = result_queue.get()
        result[res[0]]=res[1] #??????????
    print(result)

    end_time_process=time.time()
    print("process:\n",res)
    print("process time is ",end_time_process-start_time_process)
    print('Answer is correct:',np.all(np.matmul(matA, matB) == result))

#process最慢 

if __name__ == "__main__":
    main()
'''