#!/usr/bin/env python3

from config import NUM_OF_STEP, INPUT_FILE, OUTPUT_FILE, REPORT, HAS_HEADER
from analytics import Research

def main():
    f = Research(INPUT_FILE)
    lst = f.file_reader(HAS_HEADER)
    if f.validation(lst) == False:
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
    a.save_file(report, OUTPUT_FILE)

if __name__ == '__main__':
    main()
