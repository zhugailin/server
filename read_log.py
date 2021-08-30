l1 = []
l2 = []
f = open("/data/server_mini.log", "r")
for line in f.readlines():
    line_s = line.split("Incorrect input at")[1].split(",")
    l1.append(int(line_s[0][-4:]))
    l2.append(int(line_s[1][10:-1]))
    # print(line_s)
    # break
print(sorted(l1) == sorted(l2))


l2 = []
f = open("server_ip_2inst.log", "r")
for line in f.readlines():
    line_s = line.split("put : ")[1]
    try:
        l2.append(float(line_s))
    except Exception as e:
        l2.append(float(line_s.split("E0828")[0]))
        print(e)

l1 = []
f = open("server_ip_1inst.log", "r")
for line in f.readlines():
    line_s = line.split("put : ")[1]
    try:
        l1.append(float(line_s))
    except Exception as e:
        l1.append(float(line_s.split("E0828")[0]))
        print(e)

# import numpy as np
# output_1instance = np.load('outputs_used/outputs-000000000000.npz')['output__0']
# output1 = [output_1instance[i*8][0] for i in range(10833//8)]

# print(sorted(l1) == sorted(output1))
print(sorted(l2) == sorted(l1))

# >>> print(sorted(l2)[:10])
# [-6.51953, -6.48828, -6.48438, -6.47266, -6.44531, -6.44531, -6.4375, -6.4375, -6.43359, -6.43359]
# >>> print(sorted(l1)[:10])
# [-6.47656, -6.47266, -6.46484, -6.46484, -6.44531, -6.44531, -6.44531, -6.4375, -6.43359, -6.43359]
# >>> 
