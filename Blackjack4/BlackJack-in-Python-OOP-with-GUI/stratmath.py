
print("hello world")

sum = 0

init = 703
growth = (init-150)/346

for i in range(411):
    sum = sum + init
    init = init + growth

print(init)
print(sum)