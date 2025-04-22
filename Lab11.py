import os

d = 'data'
students = {}
for l in open(d + '/students.txt'):
    l = l.strip()
    students[l[3:]] = l[:3]
assign = {}
points = {}
lines = open(d + '/assignments.txt').read().splitlines()
for i in range(0, len(lines), 3):
    name, aid, pts = lines[i], lines[i+1], int(lines[i+2])
    assign[name] = aid
    points[aid] = pts
subs = []
for f in os.listdir(d + '/submissions'):
    if f.endswith('.txt'):
        sid, aid, pct = open(f'{d}/submissions/{f}').read().strip().split('|')
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
        total = sum(pct/100 * points[aid] for sid, aid, pct in subs if sid == students[name])
        print(f"{round(total/1000*100)}%")

elif sel == '2':
    aname = input("What is the assignment name: ")
    if aname not in assign:
        print("Assignment not found")
    else:
        lst = [pct for sid, aid, pct in subs if aid == assign[aname]]
        print(f"Min: {int(min(lst))}%")
        print(f"Avg: {int(sum(lst)/len(lst))}%")
        print(f"Max: {int(max(lst))}%")

elif sel == '3':
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed—run `pip install matplotlib` and try again.")
        exit()
    aname = input("What is the assignment name: ")
    if aname not in assign:
        print("Assignment not found")
    else:
        lst = [pct for sid, aid, pct in subs if aid == assign[aname]]
        plt.hist(lst, bins=[0,25,50,75,100])
        plt.show()
