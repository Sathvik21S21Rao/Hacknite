import csv
row2=[]
final_row = []
with open(f'../2023/linkplayers.csv', 'r') as out:
    header = next(out)
    for row in out:
        row2=row.split(',')
        teams = row.split(',')[0]
        if teams[2] in ["0","1","2","3","4","5","6","7","8","9"]:
            team = teams[0:2]
        elif teams[3] in ["0","1","2","3","4","5","6","7","8","9"]:
            team = teams[0:3]
        else:
            team = teams[0:4]
        with open(f'../2023/{team}.csv', 'r') as teamout:
            for r2 in teamout:
                if r2.split(',')[0] == teams:
                    #print(row2.split(','))
                    row2.append(r2.split(',')[2])
                    #print(row2)

        final_row.append(row2)
        
        
with open (f'../2023/combinedplayers.csv', 'w') as o2:
    csv_out=csv.writer(o2)
    csv_out.writerow(['player_id','player_name', 'player_role', 'points', 'credits'])
    csv_out.writerows(final_row)
