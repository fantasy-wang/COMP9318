## import modules here
import numpy as np
from collections import defaultdict
from math import sqrt
################# Question 1 #################

def distance(a, b):
    dis_x = (a[0] - b[0]) ** 2
    dis_y = (a[1] - b[1]) ** 2
    dis = sqrt(dis_x + dis_y)
    return dis


def distance_matrix(data):
    matrix = defaultdict(dict)
    max_sim = 10000
    res = 0
    
    for i in range(len(data)):
        if i == len(data) - 1:
            matrix[i] = {}
            break
        index = i + 1

        
        while (index < len(data)):
            temp_dict = {}
            
            if (index != i):
                res = distance(data[i], data[index])
            
            if (res < max_sim):
                max_sim = res
                info = []
                info.append(res)
                info.append(i)
                info.append(index)

            matrix[i][index] = res
            index += 1
    return matrix, info

def original_matrix(data):
    
    res = 0
    matrix = defaultdict(dict)
    
    for i in range(len(data)):
        index = 0
        while (index < len(data)):
            temp_dict = {}
            
            if (index != i):
                res = distance(data[i], data[index])
            else:
                res = 0
            
            matrix[i][index] = res
            index += 1
            
    return matrix

def change_matrix(matrix, og_matrix, info, vertex, length, num, result):
#     print(f'The vertex is {vertex}\n')
    vertex_1 = info[1]
    vertex_2 = info[2]
    min_dis = float('inf')
#     print(f'The vertexs is {vertex_1, vertex_2}')
    
    #add new point into vertex
    new_vertex = length + num
    if vertex_1 >= length:
        temp1 = vertex[vertex_1]
    else:
        temp1 = [vertex_1]  
    if vertex_2 >= length:
        temp2 = vertex[vertex_2]
    else:
        temp2 = [vertex_2]
    point = temp1 + temp2
#     print(f'The new vertex is {new_vertex}')
    vertex[new_vertex] = point
    vertex[new_vertex].sort()
#     print(f'\nThe Vertex is {vertex}')
    if vertex_1 in matrix:
        matrix.pop(vertex_1)
    if vertex_2 in matrix:
        matrix.pop(vertex_2)
#     print(f'The matrix is {matrix}\n')
    
    
    for key in matrix:
        dis = 0
        if key >= length:
            for subkey in vertex[key]:
                for index in vertex[new_vertex]:
                    if og_matrix[subkey][index] > dis:
                        dis = og_matrix[subkey][index]
            
        else:
            for index in vertex[new_vertex]:
                if og_matrix[key][index] > dis:
                    dis = og_matrix[key][index]
                    
                    

        if vertex_1 in matrix[key]:
            matrix[key].pop(vertex_1)
        if vertex_2 in matrix[key]:
            matrix[key].pop(vertex_2)        
        matrix[key][new_vertex] = dis  
        
        # find out the highest similarity
        point = min(matrix[key], key = matrix[key].get)
        if matrix[key][point] < min_dis:
            min_dis = matrix[key][point]
            info[0] = matrix[key][point]
            info[1] = key
            info[2] = point

    
    matrix[new_vertex] = {}
#     print(f'The matrix is {matrix}')
    
    temp = result[:]
    for i in temp:
        if (isinstance(i, int) and i in vertex[new_vertex]) or (isinstance(i, list) and set(i).issubset(set(vertex[new_vertex]))):
            result.remove(i)
    result.append(vertex[new_vertex])
    
#     print(f'In the {num + 1} clustering, the matrix is {matrix}\n')
    
#     print(f'\nThe result is {result}\n')

    return result

def hc(data, k):# do not change the heading of the function
    
    og_matrix = original_matrix(data) 
    matrix, info = distance_matrix(data)
    vertex = defaultdict(list)
    length = len(data)
    result = [x for x in range(length)]
#     print(f'The result is {result}')
    num = 0
#     print(f'This is the {num + 1} clustering')
#     print(f'-----------------------------------\n')
    if k >= length - 2:
        k = length - 2
    while(len(matrix) > k):
        result = change_matrix(matrix, og_matrix, info, vertex, length, num, result)
        num += 1
#         print(f'This is the {num + 1} clustering')
#         print(f'-----------------------------------\n')
    
    output = [x for x in range(length)]
    for i in result:
        if isinstance(i, int):
            output[i] = k - 1
        else:
            for index in i:
                output[index] = k - 1
        k -= 1
    
    return output