import pickle
import time
import sys
from multiprocessing import shared_memory


count = 0
start = time.time()

while True:
    try:
        shm = shared_memory.SharedMemory(name="test")
    except:
        #"""
        if count < 5:
            time.sleep(1)
            print("取得エラー")
            count += 1
            continue
        else:
            break
        #"""
        break
        
    else:
        try:
            data = pickle.loads(shm.buf)
        except pickle.UnpickingError:
            continue
        except:
            print("読み込みエラー")
            sys.exit(1)
        else:
            print(time.time() - start)
            if (time.time() - start) > 3:

                shm.close()
                #shm.unlink()
                print("close")

                break

