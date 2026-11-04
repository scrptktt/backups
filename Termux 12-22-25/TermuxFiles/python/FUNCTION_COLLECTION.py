

# STRINGS
def string_to_array(user_string):
    arr = []
    for i in range(len(user_string)):
        arr.append(user_string[i])
    return arr

def array_to_string(user_array):    
        user_string = ''
        for i in user_array:
            user_string = user_string + i
        return user_string

def content_wrap(str1):
    def paragraph_break(str2):
        a = 0
        b = 0
        arr = []
        for i in str2:              
            if (i == "."):          
                str3 = str2[a:b+1]  
                arr.append(str3)
                arr.append('\n\n')    
                a = b + 1           
            b = b + 1               
        return array_to_string(arr)
    
    def line_break(str2):
        j_step = 20
        j = j_step
        k = 0
        l = 0
        arr = []
        for i in str2:
            if (k > j) and (i == " "):
                str3 = str2[l:k]
                arr.append(str3)
                arr.append('\n')
                l = k
                j = j + j_step    
            k = k + 1
        return array_to_string(arr)
    
    return paragraph_break(line_break(str1))