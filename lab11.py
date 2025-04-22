import os
import matplotlib.pyplot as plt

d = 'data'
students = {}
for l in open(d + '/students.txt'):
    l = l.strip()
    students[l[3:]] = l[:3]
assign = {}
points = {}
lines = open(d + '/assignments.txt').read().splitlines()
for i in range(0, len(lines), 3):
    name = lines[i]
    aid = lines[i+1]
    pts = int(lines[i+2])
    assign[name] = aid
    points[aid] = pts
subs = []
for f in os.listdir(d + '/submissions'):
    if f.endswith('.txt'):
        line = open(f'{d}/submissions/{f}').read().strip()
        sid, aid, pct = line.split('|')
        subs.append((sid, aid, float(pct)))
print("1. Student grade")
print("2. Assignment statistics")
print("3. Assignment graph")
sel = input("Enter your selection: ")
if sel == '1':
    name = input("What is the student's name: ")
    if name not in students:
        print("Student not found")
    else:
        total = 0
        for sid, aid, pct in subs:
            if sid == students[name]:
                total += pct / 100 * points[aid]
        print(f"{round(total / 1000 * 100)}%")
elif sel == '2':
    aname = input("What is the assignment name: ")
    if aname not in assign:
        print("Assignment not found")
    else:
        lst = [pct for sid, aid, pct in subs if aid == assign[aname]]
        print(f"Min: {round(min(lst))}%")
        print(f"Avg: {round(sum(lst) / len(lst))}%")
        print(f"Max: {round(max(lst))}%")
elif sel == '3':
    aname = input("What is the assignment name: ")
    if aname not in assign:
        print("Assignment not found")
    else:
        lst = [pct for sid, aid, pct in subs if aid == assign[aname]]
        plt.hist(lst, bins=[0,25,50,75,100])
        plt.show()
