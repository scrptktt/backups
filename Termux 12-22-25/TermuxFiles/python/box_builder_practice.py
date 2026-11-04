#######################
#       Mistakes      #
#############################
#                           #
# PROGRAMMING TECHNIQUES?   #
#                           #
#############################









    # for i in range(col_end + 1):
    # # ::REMEMBER: XOR bar training::#
    #     if (i == begin) or (i == col_end):
        
    #         if i == begin:
    #             char_set = top

    #         elif i == col_end:
    #             char_set = bot
    #         elif (i == col_end) and (col_num > 1):
    #             char_set = ext

    #         for k in range(row_end + 1):
    #             # top = ('┏', '━', "┳", '┓')
    #             if (char_set == top):
    #                 if (k == begin) or (k == row_end): 
    #                     if k == begin: arr.append(char_set[0])    
    #                     elif k == row_end: arr.append(char_set[3])
    #                 elif begin < k < row_end: 
    #                     if k == cell_end[m] - 2:
    #                         print(content[n])
    #                         arr.append(char_set[1]*len(content[n])) # ━
    #                         n = n + 1        
    #                     elif k == cell_end[m]:
    #                         arr.append(char_set[2])


    #             # mid = ('┃', f'{c}')
    #             elif (char_set == mid):
    #                 if (k == begin) or (k == row_end):
    #                     # arr.append(char_set[0])
    #                     if k == begin: arr.append(char_set[0])    
    #                     elif k == row_end: arr.append(char_set[0])    
    #                 elif begin < k < row_end: 
                    
    #                     if k == cell_end[m] - 2:
    #                         arr.append(content[n])
    #                     elif k == cell_end[m]:
    #                         arr.append(char_set[0])







    #             # Bot
    #             elif (char_set == bot) or (char_set == ext):
    #                 if char_set == bot:
    #                     if k == begin: arr.append(char_set[0])    
    #                     elif k == row_end: arr.append(char_set[3])
    #                     elif begin < k < row_end: arr.append(char_set[1])
    #                 if char_set == ext:
    #                     if k == begin: arr.append(char_set[0])    
    #                     elif k == row_end: arr.append(char_set[3])
    #                     elif begin < k < row_end: arr.append(char_set[1])

        
        
    #     elif begin < i < col_end: char_set = mid





######################################################################################333





                
        # else: arr.append("\n")
        # print(f"i[{i}] k[{k}]")
                
            
            # # Top Row
            # if i == 0:
            #     if k == f:
            #         arr.append("┳")
            #         f = f + 4
            #     elif k == 0:
            #         arr.append("┏")
            #     elif k == row:
            #         arr.append("┓")
            #         arr.append('\n')
            #         f = 4
            #     else: 
            #         arr.append("━" * len(content[x]))
                
            # # Middle Row
            # elif  0 < i < (col - 1):
            #     if k == f:
            #         arr.append("┃")
            #         f = f + 4
            #     elif k == 0:
            #         arr.append("┃")
            #     elif k == row:
            #         arr.append("┃")
            #         arr.append('\n')
            #         f = 4
            #     elif k == d:
            #         arr.append(content[x]) # maybe edit for strings
                       
            #         d = d + len(content[x]) + 3
            #         x = x + 1
            #     else: arr.append(' ')
                                    
            # # Bottom Row
            # elif i == col:
            #     if k == f:
            #         arr.append("┻")
            #         f = f + 4
            #     elif k == 0:
            #         arr.append("┗")
                
            #     elif k == row:
            #         arr.append("┛")
            #         arr.append('\n')
            #         f = 4
            #     else: arr.append("━" * len(content[x-1]))
        
