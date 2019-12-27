def day_odd(day_):
    return day_ % 7

def month_day(month):
    odd_day = 0
    if month < 7:

        for i in range(1, month):
            if i == 2:
                continue
            elif i % 2 == 0:
                odd_day += 2
            else:
                odd_day += 3
        return odd_day % 7
    else:

        for i in range(1, 8):
            if i == 2:
                continue
            elif i % 2 == 0:
                odd_day += 2
            else:
                odd_day += 3


        for i in range(8, month):
            if i % 2 == 0:
                odd_day += 3
            else:
                odd_day += 2

        return odd_day % 7


def day(day_,month,year):
    odd_day = 0
    p_l_y = 0
    rem = 0
    h_y =0
    if year-1 % 400 ==0:
        odd_day += (month_day(month) + day_odd(day_)) % 7

    else:

        p_l_y = 400 *(year // 400)
        rem = year - p_l_y -1
        h_y = 100*(rem // 100)
        odd_day += ((5*h_y)//100) % 7
        rem = rem - h_y
        l_p = rem // 4
        n_y = rem - l_p
        odd_day += (2* l_p + n_y) % 7
        odd_day += (month_day(month) + day_odd(day_)) % 7
    return odd_day





if __name__=='__main__':
    # input in the format dd - mm - yy
    date = input().split('-')
    date = list(map(lambda x:int(x),date))
    day_ = ['sun','mon','tue','wed','thu','fri','sat','sun']
    result = day(date[0],date[1],date[2])
    print(day_[result])

