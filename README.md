# shared_memory
Shared Memory Existing from Python3.8 is not Released

## SharedMemory.close() is Dangerous

Shared Memory Cannot be Released

```bash:bash
UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
warnings.warn(‘resource_tracker: There appear to be %d ‘
```

## How To Use

Execute Process 2 after Executing Process 1

```bash:bash
python proc1.py
```

```bash:bash
python proc2.py
```

## Detailed Explanation(Japanese)
・[Blog](https://atchicken.com/shared_memory/)
