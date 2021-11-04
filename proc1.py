import pickle
import sys
from multiprocessing import shared_memory

try:
    shm = shared_memory.SharedMemory(create=True, size=30, name="test")
except:
    print("Error")
    sys.exit(1)
    

while True:
    brother = {
        "1": "taro",
        "2": "jiro",
        "3": "saburo"
    }
    data = pickle.dumps(brother)
    shm.buf[:len(data)] = data
    
