import pandas as pd
import numpy as np
import csv
import pathlib
import os

file_name = os.getcwd() + '\\create_data\\data\\transporter.csv'
file = pathlib.Path(file_name)


class transporter:
    def __init__(self, no, available_weight, empty_speed, work_speed):
        self.no = no
        self.available_weight = available_weight
        self.empty_speed = empty_speed
        self.work_speed = work_speed
        self.works = []

    def __str__(self, flag=True):
        ret = 'no: {}, available_weight: {}, empty_speed: {}, work_speed: {}, works: {}'.format(self.no,
                                                                                                self.available_weight,
                                                                                                self.empty_speed,
                                                                                                self.work_speed,
                                                                                                self.works)
        return ret


if file.exists():
    df = pd.read_csv(file)
    temp = list(zip(df['no'] - 1, df['available_weight'], df['empty_speed'], df['work_speed']))
    transporters = []
    for n, a, e, w in temp:
        transporters.append(transporter(n, a, e, w))

else:
    print(0)
