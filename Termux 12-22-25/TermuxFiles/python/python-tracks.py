# row_entry = ["12 4.6789",
#              "1.34567 912 4.678 9",
#              "12 456 8912 4.678912 4.6789", 
#              "12 456 8912 4.6789112 456 8912 4.67891",
#              "12 456 8912 4.6789112 456 89",
#              ".6789112 4564.67 891",
#              ]


# def string_to_array(str1):
#     arr = []
#     for i in range(len(str1)):
#         arr.append(str1[i])
#     return arr
# def array_to_string(arr):    
#     str1 = ''
#     for i in arr:
#         str1 = str1 + i
#     return str1

# def content_wrap(str1):
#     int1 = 0

#     def line_break(str2, wrap_lines):
#         j_step = 1
#         j = j_step
#         k = 0
#         l = 0
#         arr = []   

#         for i in str2:
#             if (k > j) and (i == " "):
#                 str3 = str2[l:k]
#                 arr.append(str3)
#                 arr.append('\n')
                
#                 wrap_lines = wrap_lines + 1
                
#                 l = k
#                 j = j + j_step    
#             k = k + 1
        
#         str2 = array_to_string(arr)
#         int2 = wrap_lines
#         return str2, int2
#     def paragraph_break(str2, wrap_lines):
#         a = 0
#         b = 0
#         arr = []
 
#         for i in str2:
#             if (i == "."):
#                 str3 = str2[a:b+1]  
#                 arr.append(str3)
#                 arr.append('\n\n')    
                
#                 wrap_lines = wrap_lines + 1

#                 a = b + 1
#             b = b + 1
    
#         str2 = array_to_string(arr)
#         int2 = wrap_lines
#         return str2, int2
    
#     def decide_content_type(str2, lines): 
#         if type(str2) == str: 
#             data, lines = paragraph_break(str2, lines)
#             data, lines = line_break(str2, lines)
#         elif type(str2) == list:
#                 arr = []
#                 max = 0

#                 for i in str2:
#                     i, lines = line_break(i, lines)
#                     i, lines= paragraph_break(i, lines)

#                     arr.append(i)

#                     if lines >= max:
#                         max = lines

#                     lines = 0
#                 data = arr
#                 lines = max
#         else: print(f"[\033[31mTYPE ERROR\033[0m]::[\033[34m{type(str1).__name__.upper()}\033[0m : \033[32mFix: pass a string/list.\033[0m]") 
        
#         str1 = data
#         int1 = lines
#         return str1, int1
#     return decide_content_type(str1, int1)


# # char_col_count(cell_length)
# # cell_char_length


def cell_char_length(n):
    # Returns End of Cell position
    n_terms = []
    x = 0
    o = 0

    for i in n:
        x = len(i)
        term = (3 + x)
        o = o + term 
        
        n_terms.append(o)
    
    return n_terms

# def char_row_count(n):
#     row_chars = []
#     char_total = 0

#     for term in n:
#         row_chars.append(2 + term)
#         term = term + 2
#         char_total = (2 + term)

#     return char_total
# def char_col_count(n):
#     col_chars = []
#     char_total = 0

#     for term in n:
#         term = term - 3
#         col_chars.append(2 + term)
#         char_total = (2 + term) 
#         # n = n / o
#     return char_total

def generate_row(content):
    c = content

    if type(content) == list:
        col_num = len(content)
    elif type(content) == str:
        col_num = 1
    
    # string vs array decide
    
    begin = 0
    row_end = row_chars
    col_end = col_chars

    # print(f"{content}")
    # print(f"[{row_chars}] row_chars")
    # print(f"[{col_chars}] col_chars")

    # print(f"[{row_end}] row_end")
    # print(f"[{col_end}] col_end")
    


    # m = 0
    
    
    arr = []
    n = 0
    # 12345
    # acebd
    
    content_length = len(c)
    cell_length = content_length + 3
    cell_count = 
    for i in range(col_end + 1):
        print(f'content: {c}')
        arr.append('\n')

        


        for k in range(row_end + 1):            
            if (i == begin) and (k == begin):
                arr.append('┏')
            elif (i == col_end) and (k == row_end):
                arr.append('┓')
            ###### one little package #######

            elif (k > begin) and (k < rrow_end):    # all the way
                if k == cell_end - 2:
                    arr.append('━' * (len(content[n])+2))


                    print(f'[{n}]:{content[n]}')
                    n = n + 1
                elif k == cell_end:
                    arr.append('┳')



    # top = ('┏', '━', "┳", '┓')
    # mid = ('┃', f'{c}')
    
    # ext = ('┃', '━', "╋", '┃')
    # bot = ('┗', '━', "┻", '┛')

    


    str1 = array_to_string(arr)
    return str1


practice_array = ["aaa","c","e","b","d"]
ans = generate_row(practice_array)

print(ans)



#         ┏━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┓
#         ┃ Vertex 1  ┃ Vertex 2  ┃ Vertex 3  ┃
#         ┣━━━┳━━━┳━━━╋━━━┳━━━┳━━━╋━━━┳━━━┳━━━┫
#         ┃ x ┃ y ┃ z ┃ x ┃ y ┃ z ┃ x ┃ y ┃ z ┃
#         ┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛
# BYTE:   0   4   8   12  16  20  24  28  32  36
# STRIDE:             12          12          12
# OFFSET: 00000000000000000000000000000000000000


        



def count_row_characters(entries):
    sep = len(entries) - 1
    end = 2    
    char_len = 0
    
    for entry in entries:
        for char in entry:
            char_len = char_len + 1
    
    int1 = (end * 2) + (sep * 3) + char_len
    return  int1

def count_col_characters(lines):
    return lines + 2


