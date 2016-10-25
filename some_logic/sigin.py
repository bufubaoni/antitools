def signin():
    last_top_1=list(1)
    sign_in_history = new Sign_in_history();
    if last_top_1.time == datetime.now():
        return False
    else:
        if (datetime.now() - last_top_1.time).day == 1:
            if last_top_1.credits < 40:
                signin_in_history += 5
            else
                signin_in_history = last_top_1.credits
        else
            signin_in_history = 5
        
def info():
    sign_in_days = count(days)
    return sign_in_days
    
    

