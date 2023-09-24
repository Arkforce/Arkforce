total_hours = 5
total_minutes = 25
total_seconds = 15

passed_hours = 2
passed_minutes = 45 
passed_seconds = 30

total_sec = (total_hours*60*60)+(total_minutes*60)+total_seconds
pased_total_sec = (passed_hours*60*60)+(passed_minutes*60)+passed_seconds

remain_sec = total_sec-pased_total_sec
remain_hours  = remain_sec//60//60
remain_minutes = remain_sec/60%60

print(f"Remained {remain_sec//60//60} hours, {remain_minutes}")