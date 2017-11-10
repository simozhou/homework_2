time = input().strip()
time_arr = time.strip('AMP').split(':')

hh, mm, ss = map(int, time_arr)

if ("PM" in time) and hh != 12:
    hh += 12
if ("AM" in time) and (hh == 12):
    hh = 0

print('%(hh)02d:%(mm)02d:%(ss)02d' % {"hh": hh, "mm": mm, "ss": ss})
