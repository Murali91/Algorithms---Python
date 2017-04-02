def pattern_table(pattern,length):
    length = len(pattern)
    table = {} #dictionary to store the value against index
    table[0]=0
    mtch_ptr=0
    seq_ptr = 1
    while seq_ptr<length: #runs through the length of pattern
        if pattern[mtch_ptr]==pattern[seq_ptr]: #check for equality of both pointers
            '''Increments the matching pointer by 1 and stores it in the evaluation table
            to show the previous occurence of that prefix'''
            mtch_ptr+=1 
            table[seq_ptr]=mtch_ptr
            seq_ptr+=1
        else:
            '''If the values are not match, then the matching pointer jumps to the 
            index of previous matched value without incrementing the sequence pointer'''
            if mtch_ptr:
                mtch_ptr=table[mtch_ptr-1]
            else:
            '''If the matching pointer, then it means no match has been found yet, so 
            sequence pointer is alone incremented'''
                table[seq_ptr]=0
                seq_ptr+=1
    return table
    
    def knuth_morris_pratt(text,pattern):
    p_len = len(pattern)
    t_len = len(text)
    pattern_eval = pattern_table(pattern,p_len) #receives the evaluation table value
    txt_ptr = pt_ptr = 0
    if text == pattern or not pattern:
        return 0
    else:
        while txt_ptr<t_len: #runs through the length of text
            if text[txt_ptr] == pattern[pt_ptr]:
                if pt_ptr==p_len-1: #checks if end of pattern is reached
                    return txt_ptr-p_len+1
                txt_ptr+=1 #both the pointers values are incremented
                pt_ptr+=1
            else:
                if pt_ptr:
                    pt_ptr = pattern_eval[pt_ptr-1] 
                    '''if the pattern pointer is in the middle, 
                    it jumps to previous matched position based on the values from evaluation table.'''
                else:
                    txt_ptr+=1
        return -1
