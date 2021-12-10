## import modules here 
import pandas as pd
import numpy as np
import helper


################### Question 1 ###################

def read_data(filename):
    df = pd.read_csv(filename, sep='\t')
    return (df)


def buc_rec(input, stack):
    # Note that input is a DataFrame
    dims = input.shape[1]
    rows = input.shape[0]
    output = []
    
    if dims == 1:
        # only the measure dim
        input_sum = sum(helper.project_data(input, 0) )
        output = stack + [input_sum]
#         print(f'The output_3 is {output}')
        return output
    
    else:
        if rows == 1:
            temp = ['{:b}'.format(i) for i in range(2 ** (dims - 1))]
            temp.reverse()
            for index in temp:
                if len(index) != dims - 1:
                    index = '0' * (dims - 1 - len(index)) + index 
                temp_list = list(index)
                for i in range(dims - 1):
                    if temp_list[i] == '1':
                        temp_list[i] = int(input[input.columns[i]])
                    else:
                        temp_list[i] = 'ALL'
                output += stack + temp_list + [int(input[input.columns[dims - 1]])]
#                 print(f'The output_4 is {output}')
        else:
            # the general case
            dim0_vals = set(helper.project_data(input, 0).values)
            for dim0_v in dim0_vals:
                temp = stack + [dim0_v]
                sub_data = helper.slice_data_dim0(input, dim0_v)
                temp = buc_rec(sub_data, temp)
                output += temp
#                 print(f'The output_1 is {output}')
            ## for R_{ALL}
            temp = stack + ['ALL']
            sub_data = helper.remove_first_dim(input)
            temp = buc_rec(sub_data, temp)
            output += temp
#             print(f'The output_2 is {output}')
            
    return output

def buc_rec_optimized(df):# do not change the heading of the function
    stack = []
    result = buc_rec(df, stack)
    length = len(result)
    temp = np.array(result)
    output = temp.reshape(int(length / df.shape[1]), df.shape[1])
    final = pd.DataFrame(output, columns = df.columns)
    
    return final
