result=True
another_result = result
print(id(result))
print(id(another_result))   #cz the values is same of result and another result that's why it would print same value or same id
print()
result=False
print(id(result))
print()
answer= " Correct "
another_ans= answer
print(id(answer))
print(id(another_ans))
print()
result +="ish"

print(id(result))
