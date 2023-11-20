with open('КувайсковаАлинаВладимировна_у232_vvod.txt', 'r') as f:
    l = [[int(num) for num in line.split(',')] for line in f]
print(l)
