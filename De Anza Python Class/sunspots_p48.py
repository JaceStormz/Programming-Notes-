# sunspots_p48.py 
# Gautam Rao
# 3/07/26
# Python 3.13.9
'''
Write a program which reads the data from file sunspots.txt 
'''
file_name = "sunspots.txt"

years = []
sunspots = []

with open(file_name) as f:
    for line in f:
        parts = line.split()

        year = int(parts[0])          # first value is the year
        months = []

        for value in parts[1:]:       # remaining 12 values
            months.append(float(value))

        years.append(year)
        sunspots.append(months)

# Display some of the data
for i in range(5):
    print("Year:", years[i])
    print("Monthly sunspots:", sunspots[i])
    print()

    '''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python sunspots_p48.py
Year: 1945
Monthly sunspots: [18.5, 11.8, 19.7, 31.6, 26.6, 37.3, 37.4, 24.6, 34.0, 71.3, 46.3, 28.4]

Year: 1946
Monthly sunspots: [55.2, 92.0, 87.5, 81.0, 83.5, 79.6, 115.1, 112.7, 115.7, 112.7, 136.2, 127.4]

Year: 1947
Monthly sunspots: [128.2, 145.5, 153.0, 161.0, 224.2, 166.3, 166.6, 216.4, 195.0, 191.7, 155.0, 148.3]

Year: 1948
Monthly sunspots: [130.1, 107.3, 103.8, 222.5, 194.8, 203.6, 184.3, 205.0, 174.6, 166.3, 129.9, 177.1]

Year: 1949
Monthly sunspots: [153.3, 228.0, 198.8, 190.7, 147.4, 154.5, 153.6, 163.7, 183.7, 172.2, 190.9, 152.1]
    
    '''