#!/usr/bin/env python3
import os
import json
import logging
import requests


from config import NUM_OF_STEP, INPUT_FILE, OUTPUT_FILE, REPORT, HAS_HEADER, MESSAGE_SUCCESS, MESSAGE_FAIL
from analytics import Research

def main():
    f = Research(INPUT_FILE)
    try:
        lst = f.file_reader(HAS_HEADER)
    except Exception as e:
        print(f'Error: {e}')
        f.send_message_to_slack(MESSAGE_FAIL)
        return
    if f.validation(lst) == False:
        f.send_message_to_slack(MESSAGE_FAIL)
        raise Exception("Invalid file structure")
    a = f.Analytics(lst)
    heads,tails = a.counts()
    p_heads, p_tails = a.fractions(heads,tails)
    lst_predict = a.predict_random(NUM_OF_STEP)
    predict_heads = sum(l[0] for l in lst_predict)
    predict_tails = sum(l[1] for l in lst_predict)
    report = REPORT.format(
        len(lst), tails, heads, 
        round(p_heads,2), round(p_tails, 2), 
        NUM_OF_STEP, predict_tails, predict_heads
    )
    if a.save_file(report, OUTPUT_FILE) == True:
        f.send_message_to_slack(MESSAGE_SUCCESS)
    else:
        f.send_message_to_slack(MESSAGE_FAIL)

if __name__ == '__main__':
    main()
