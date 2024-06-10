def solution(n, times):
    answer = 0 
    left = 1
    right = n * max(times)
    
    while right >= left:
        mid = (left + right) //2
        
        pass_people = how_many_people(times, mid)
        
        if pass_people >= n:
            right  = mid -1
            answer = mid
            
        elif pass_people < n:
            left = mid + 1
            
    return answer

def how_many_people(times, pass_time):
    total = 0
    for time in times:
        total+= pass_time // time
    return total