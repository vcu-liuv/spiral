def spiralize(number):
    spiral_sum = 1
    spiral_counter = 1
    extra = number / 2
    
    curr_num = 1
    
    while spiral_counter < number - extra:
        for x in range(4):
            curr_num = curr_num + spiral_counter * 2
            spiral_sum += curr_num
        spiral_counter += 1

    return spiral_sum