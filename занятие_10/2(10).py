a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11, 12]])
mat = np.matrix(a)
with open('КувайсковаАлинаВладимировна_у232_vvod.txt','wb') as f:
    for line in mat:
        np.savetxt(f, line, fmt='КувайсковаАлинаВладимировна_у232_vivod.txt')
