# from threading import Thread
# import time
# class A(Thread):
#     def run(self):
#         for i in range(10):
#             time.sleep(1)
#             print("starting Thread",i)
# t1=A()
# t2=A()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("MAin thread")
##########
# import threading
# import time
# def worker(name,delay):
#     for i in range(3):
#         time.sleep(delay)
#         print(f"{threading.current_thread().name} iteration{i}")
# t1=threading.Thread(target=worker)
#############
# import threading
# import time
# def say(msg):
#     print(f"{threading.current_thread().name} {msg}")
# t=threading.Thread(target=say, args=("hello",), name="greet thread")
# print(f"main starting {t.name}")
# t.start()
# t.join()
# print("main thread has finished",t.is_alive())
##########################
import threading
lock=threading.Lock()
