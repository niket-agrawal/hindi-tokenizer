print("\n\n ----------------------------------------------------------------")
print("Hindi Corpus Sentence Tokenizer and Frequency Count Generator + filters (all symbols, digits, english characters)")
print("\t * input - give FIRST in argument, eg: (sample_text.txt)")
print("\t * output - give SECOND in argument, eg: (sample_tokens.csv)")
print("\t example - $python code_tokenizer.py sample_text.txt sample_tokens.csv")
print(" -----------------------------------------------------------------\n\n")

import sys
sys.path.append("D:/IITK Temp/NonWords_Vivek/custom-packages")
#https://github.com/taranjeet/hindi-tokenizer#printsen
#from Hindi_tokenizer import Tokenizer
from HindiTokenizer3 import Tokenizer
from functools import reduce #Havok method
from collections import defaultdict #NPE method
import pandas as pd
import csv
#https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
import timing

#Comparision for diffect methods for summation of dictionaries
#https://stackoverflow.com/questions/10461531/merge-and-sum-of-two-dictionaries/46128481#46128481
#╔═══════════════════════════╦═══════╦═════════════════════════════╗
#║                           ║       ║    Best of Time Per Loop    ║
#║         Algorithm         ║  By   ╠══════════════╦══════════════╣
#║                           ║       ║  small_tests ║  large_tests ║
#╠═══════════════════════════╬═══════╬══════════════╬══════════════╣
#║ functools reduce          ║ Havok ║       3.1 µs ║   103,000 µs ║
#║ defaultdict sum           ║ NPE   ║       3.2 µs ║   119,000 µs ║
#║ Counter().update loop     ║ Scott ║       9.1 µs ║   123,000 µs ║
#║ Counter().update static   ║ Scott ║      14.4 µs ║   136,000 µs ║
#║ set unions without sum()  ║ georg ║       4.6 µs ║   280,000 µs ║
#║ set unions with sum()     ║ georg ║       7.8 µs ║   347,000 µs ║
#║ Counter() without sum()   ║ Scott ║      18.9 µs ║   289,000 µs ║
#║ Counter() with sum()      ║ Scott ║      24.9 µs ║   324,000 µs ║
#╚═══════════════════════════╩═══════╩══════════════╩══════════════╝
#################################################################################################

################ METHOD-1 (Havok) ######################################
def havok_method(tests):
    def reducer(accumulator, element):
        for key, value in element.items():
            accumulator[key] = accumulator.get(key, 0) + value
        return accumulator
    return reduce(reducer, tests, {})

################ METHOD-2 (NPE) ########################################
def dsum(*dicts):
    ret = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    return dict(ret)

################ METHOD-3 (Me) ######################################## (This is best method)
def join_dict(big_dict, small_dict): 
    for key in small_dict:
        if key in big_dict:
            big_dict[key] = big_dict[key]+small_dict[key]
        else:
            big_dict[key] = small_dict[key]
    return big_dict
#######################################################################

#input_path = 'hix'
#input_path = 'D:/IITK Temp/NonWords_Vivek/iitm_indic-nlp/database_indic/hi.txt'
input_path = sys.argv[1]
output_path = sys.argv[2]
#output_path = 'madras_tokens_clean.csv'

all_tokens = {}
cnt_line, cnt_unq_tokens = 0, 0
print("\n\nprint('Running for,',input_file)")
with open(input_path, encoding='utf-8') as wf:
    for line in wf:
        line = line.strip()
        # Taranjeet's github code
        t = Tokenizer(line)
        t.clean_text()
        t.tokenize()
        tok_in_line = t.tokens
        freq_dict = t.generate_freq_dict()
        # Till here
        
        #All_tokens using Method-1
        ## dict_list = [all_tokens,freq_dict]
        ## all_tokens = havok_method(dict_list)
        
        #All_tokens using Method-2
        ## all_tokens = dsum(all_tokens,freq_dict)

        #All_tokens using Method-3
        all_tokens = join_dict(all_tokens,freq_dict)

        cnt_line+=1
        cnt_unq_tokens=len(all_tokens)

        print("Total sentences read = ", cnt_line," and total unique tokens till now = ",cnt_unq_tokens,"\r",end="",flush=True)

print('\n\nSUCCESS - Tokenized, length =',len(all_tokens))

#print(all_tokens)
print('\tnow saving csv file (utf-8-sig),',output_path)
with open(output_path,'w',encoding='utf-8-sig',newline='') as f:
    #w = csv.writer(sys.stderr) # to check
    w = csv.writer(f)
    w.writerows(all_tokens.items())
print('SUCCESS - DONE, you can exit')