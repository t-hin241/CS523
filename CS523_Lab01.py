import os
import sys
import glob
from os import path
from typing import Union

#class for storing segments and replaced index during merging
class DataProvider:
    def __init__(self, file_data, cur_value):
        self.file_data = file_data
        self.cur_value = cur_value


#devide the input data to segments fitted with limit memory
def devide_data(input_file, tmp_dir, limit_mem):
    num = -1
    end_flag = False

    with open(input_file, 'r') as input:
        while not end_flag:
            seg = []
            num += 1
            #segment sizes not larger than limit_mem/2
            while sys.getsizeof(seg) < (limit_mem/2) * 1024 * 1024:
                number = input.readline()
                if not number:
                    end_flag = True
                    break
                seg.append(number)

            seg.sort(reverse=False)
            seg_filename = f'part{num}'
            with open(path.join(tmp_dir, seg_filename), 'w') as seg_output:
                seg_output.writelines(map(lambda v: f'{str(v)}', seg))    


#merge sorted segments
def merge_results(tmp_dir, output_dir, output_name):

    #create base data providers
    providers = []
    for path_to_part in glob.iglob(f"{tmp_dir}/part*"):
        fd = open(path_to_part, 'r')
        provider = DataProvider(fd, int(fd.readline()))
        providers.append(provider)


    output_file = path.join(output_dir, f'Sorted{output_name}')
    buffer = []
    with open(output_file, 'w') as out_f:
        count = 0
        while providers:
            #get min value index in temp
            min_idx: Union[int, None] = None
            for idx, provider in enumerate(providers):
                if not min_idx or providers[min_idx].cur_value > provider.cur_value:
                    min_idx = idx

            #get min in temp and write it in output file
            while prev_value is None or prev_value == providers[min_idx].cur_value:
                out_f.write(f"{str(providers[min_idx].cur_value)}\n")
                prev_value, providers[min_idx].cur_value = providers[min_idx].cur_value, providers[min_idx].fd.readline()

            #no element in data providers
            if not providers[min_idx].cur_value:
                providers[min_idx].fd.close()
                del providers[min_idx]

def main():
    limit_mem_mb = 1024
    input_file = "*//ExSort.IN"
    segs_dir = "*//Temp//"
    output_dir = "*//"

    devide_data(input_file, segs_dir, limit_mem_mb)
    merge_results(segs_dir,output_dir,output_name="ExSort.OUT")


if __name__ == "__main__":
    main()