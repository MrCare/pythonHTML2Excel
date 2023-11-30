'''
Author: Mr.Car
Date: 2023-11-30 16:21:24
'''
import argparse
import os
import pandas as pd
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(output_path):
    # 设置日志文件的路径
    log_file = os.path.join(output_path, 'error_log.txt')
    
    # 创建一个日志处理器，将日志写入文件
    file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024*5, backupCount=2)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # 添加处理器到根日志记录器
    logging.getLogger('').addHandler(file_handler)

def convert_html_to_csv(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    setup_logging(output_path)  # 设置日志

    fail_list = []

    for file_name in os.listdir(input_path):
        file_path = os.path.join(input_path, file_name)
        try:
            df = pd.read_html(file_path)
            csv_file = os.path.join(output_path, os.path.splitext(file_name)[0] + ".csv")
            df[0].to_csv(csv_file, index=False, header=False, encoding='utf-8')
        except Exception as e:
            logging.error(f"Error when changing file {file_name}: {e}")
            fail_list.append(file_name)

    with open(os.path.join(output_path, "failList.txt"), "w") as f:
        f.write("\n".join(fail_list))

    logging.info("Conversion completed. Output Path: %s", output_path)

def main():
    parser = argparse.ArgumentParser(description="Convert HTML files to CSV format.")
    parser.add_argument('input_path', type=str, help='Path to the directory containing HTML files')
    parser.add_argument('output_path', type=str, nargs='?', default=os.path.join(os.getcwd(), "out"), help='Path to save the output CSV files')
    
    args = parser.parse_args()

    convert_html_to_csv(args.input_path, args.output_path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
