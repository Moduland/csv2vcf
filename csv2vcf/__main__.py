# -*- coding: utf-8 -*-
import time
from .VCF import *
if __name__=="__main__":
    if "contact.csv" in os.listdir():
        time_1=time.perf_counter()
        csv_reader("contact.csv")
        time_2=time.perf_counter()
        delta_time=time_2-time_1
        print("VCF Data Generated In " + time_convert(delta_time))
    else:
        print("[Error] There is no csv input file")