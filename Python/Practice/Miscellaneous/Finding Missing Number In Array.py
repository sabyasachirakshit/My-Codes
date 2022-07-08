def find_missing_number(lst):
    last_num=lst[len(lst)-1]
    overall_sum=(last_num*(last_num+1))//2
    actual_sum=sum(lst)
    missing_number=overall_sum-actual_sum
    print('Missing Number:',missing_number)
find_missing_number([1,2,4,5,6,7])