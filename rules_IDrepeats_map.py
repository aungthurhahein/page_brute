#! /usr/bin/env/ python

"""
# 
# usage: python rules_IDrepeats_map.py allpage.repeats allpage.lst.sort > allpage.repeats.map 
# output: 
# Dev: __author__ = 'aung' 
# Date: 20151019
"""
import sys
repeatlist = sys.argv[1]
allpage = sys.argv[2]

page_rule = []
page_id = []
with open(allpage,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        page_rule.append(l1_split[0])
        page_id.append(l1_split[1].strip('\n'))

with open(repeatlist,'rb') as f2:
    for l2 in f2:        
        repid = l2.strip('\n')
        ind = [i for i, e in enumerate(page_id) if e == repid]
        rules= ""
        for i in ind:
            if rules == "":
                rules = page_rule[i]
            else:
                rules += ";"+page_rule[i]
        sys.stdout.write(repid+'\t'+rules+'\n')

