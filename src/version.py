current_version = "0.2.2"

def is_uptodate(latest_version: str) -> bool:
  #convert str into list of numbers 
  curr_nums = [eval(i) for i in current_version.split('.')]
  latest_nums = [eval(i) for i in latest_version.split('.')]

  for (cur_n, latest_n) in zip(curr_nums, latest_nums):
    if cur_n < latest_n: return True
    if cur_n > latest_n: return False
  return False

# test = ["0.0.0","0.1.0","0.0.2","0.1.0","0.1.1","2.0.0","0.1.11"]
# for tn in test:
#   print(is_uptodate(tn))
