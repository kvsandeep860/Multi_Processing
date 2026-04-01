# Python Multiprocessing 🚀
-- asyncio, there are no better examples on internet than these on Asyncio.
## What is this about?

Multiprocessing in Python is a way to run multiple tasks **at the same time using multiple CPU cores**.

Unlike multithreading (where everything shares the same space), multiprocessing creates **separate processes**, each with its own memory. That’s why it’s perfect for heavy computations.

---

## When should you actually use it?

Multiprocessing is useful when:

* Your code is doing **heavy computations** (math, ML, image processing, etc.)
* You want to **fully use your CPU cores**
* Your program feels slow because of computation, not waiting

If your program is mostly waiting (API calls, file reads), then multithreading or asyncio is better.

---

## The basic idea

Think of processes like workers in **separate rooms**.

* Each worker has their own desk (memory)
* They don’t interfere with each other
* But communicating between them takes effort

---

## A simple example

```python
from multiprocessing import Process
import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

if __name__ == "__main__":
    p1 = Process(target=task, args=("Process-1",))
    p2 = Process(target=task, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
```

What’s happening:

* Two processes run independently
* Both execute in parallel (on different CPU cores)
* Total time ~2 seconds instead of 4

---

## A better way (cleaner)

Most of the time, you’ll want to use this:

```python
from concurrent.futures import ProcessPoolExecutor
import time

def square(n):
    time.sleep(1)
    return n * n

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(square, [1, 2, 3, 4]))

    print(results)
```

Why this is better:

* No manual process handling
* Cleaner code
* Python manages everything for you

---

## The big advantage (no GIL issue)

In multithreading, Python has something called the GIL, which limits execution.

Multiprocessing avoids this completely because:

* Each process has its **own Python interpreter**
* So they truly run in parallel

---

## The tricky part: communication 😬

Since processes don’t share memory, passing data is not straightforward.

You need special tools like:

```python
from multiprocessing import Queue
```

Example:

```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello from process")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))
    
    p.start()
    print(q.get())
    p.join()
```

---

## Real-world use case

Processing images:

```python
from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageFilter
import os

def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(10))
    img.save(f"processed/{img_name}")

if __name__ == "__main__":
    images = os.listdir("images")

    with ProcessPoolExecutor() as executor:
        executor.map(process_image, images)
```

Each image gets processed in parallel → huge speedup 🚀

---

## One important rule (very important ⚠️)

Always use:

```python
if __name__ == "__main__":
```

Especially on Windows.
Without this, your program can go into an infinite loop of creating processes.

---

## Some practical advice

* Use multiprocessing for **heavy tasks only**
* Don’t spawn too many processes (CPU overload)
* Avoid passing large data between processes
* Prefer `ProcessPoolExecutor` for most use cases

---

## Quick comparison (to connect things)

* **Multithreading** → good for waiting (I/O)
* **Multiprocessing** → good for heavy computation
* **Asyncio** → best for massive I/O with fewer resources

---

## Quick summary

* Multiprocessing = true parallel execution
* Best for CPU-heavy tasks
* Bypasses GIL
* Slightly heavier than threads (more overhead)

---

## One last way to think about it

* **Threads** → roommates sharing everything
* **Processes** → neighbors in separate houses
* **Asyncio** → one person multitasking smartly

---

If you combine this with what you learned about threading and asyncio, you’re already thinking like a solid backend/ML engineer.

If you want next step, I can give you a **mini project where you use all three together** — that’s where things really click 🔥
