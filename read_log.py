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
