'''
Author: Mr.Car
Date: 2023-11-30 12:41:55
'''
import sys
import os
import pandas as pd

if len(sys.argv) < 2:
    print("error:need input path")
    exit()
    
input_path = sys.argv[1]  

if len(sys.argv) > 2:
    output_path = sys.argv[2] 
else:
    output_path = os.path.join(os.getcwd(), "out")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

fail_list = []

for file_name in os.listdir(input_path):
    file_path = os.path.join(input_path, file_name)
    
    try:
        df = pd.read_html(file_path) 
        csv_file = os.path.join(output_path, os.path.splitext(file_name)[0] + ".csv")
        df[0].to_csv(csv_file, index=False, header=False, encoding='gbk')

    except Exception as e:
        print("Eorror happens when change File {} :{}".format(file_name, e)) 
        fail_list.append(file_name)
        
with open(os.path.join(output_path, "failList.txt"), "w") as f:
    f.write("\n".join(fail_list))
        
print("Done! output Path:", output_path)