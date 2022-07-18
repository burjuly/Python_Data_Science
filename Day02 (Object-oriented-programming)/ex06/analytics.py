#!/usr/bin/env python3

import os
import json
import logging
import requests
from random import randint

from config import MESSAGE_SUCCESS, MESSAGE_FAIL, WEB_HOOK_URL

class Research:
    logging.basicConfig(filename="analytics.log", level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

    def __init__(self, path):
        self.path = path
    
    class Calculations:
        def __init__(self, data):
            self.data = data  
        
        def counts(self):
            logging.info("Сount the number of heads and tails")
            lst = self.data
            heads = sum(l[0] for l in lst)
            tails = sum(l[1] for l in lst)
            return heads, tails
        
        def fractions(self, heads, tails):
            logging.info("Сalculate the percentage of heads and tails")
            s = heads + tails
            if s == 0:
                return (0, 0)
            else:
                return heads/s * 100, tails/s * 100

    class Analytics(Calculations):
        def predict_random(self, num):
            logging.info("Predict the following observations")
            if num <= 0:
                raise Exception('Wrong number')
            predict = []
            for i in range(num):
                predict.append([0,1]) if randint(0,1) == 0 else predict.append([1,0])
            return predict
        
        def predict_last(self):
            logging.info("Finding the last observation")
            return self.data[-1]

        def save_file(self, report, file_name, extension='txt'):
            logging.info("Save the report to the file")
            with open(file_name + '.' + extension, 'w') as f:
                f.write(report)
                return True

    def str_to_list(lines, has_header):
        logging.info("Convert to a list")
        tab = lines.split('\n')
        if has_header == True:
            tab = tab[1::]
        lst = [list(map(int, l.split(','))) for l in tab]
        return(lst)

    def file_reader(self, has_header = True):
        logging.info("Read the file")
        try:
            with open(self.path, 'r') as f:
                try:
                    lines = f.read()
                    return(Research.str_to_list(lines, has_header))
                except:
                    logging.info("It is impossible to read the file")
                    raise Exception("It is impossible to read the file")
        except:
            logging.info("File could not be opened")
            raise Exception("File could not be opened")
           
    def validation(self, data):
        logging.info("Validate file data")
        for i in data:
            if i in [[0,1],[1,0]]:
                continue
            else:
                return False
        return True

    def send_message_to_slack(self, message):
        slack_msg = {'text': message}
        requests.post(WEB_HOOK_URL, data=json.dumps(slack_msg))



