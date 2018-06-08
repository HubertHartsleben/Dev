import doctest

def prep_save_file(content,tickersymbl):

    for i in range(0,len(content)):
        line=content[i].split(',')
        if line==['']:
            break
        tmp=[]
        for j in range(len(line)):
            #Search for Header
            if line[j].isalpha():
                #Search for Date an change representation
                if line[j].find('Date')>=0:
                    line.pop(j)
                    line.insert(j,'Day')
                    line.insert(j+1,'Month')
                    line.insert(j+2,'Year')
                    break
            else:
                #DATE :Content of date found
                year_idx = line[j].find('-')
                if year_idx>=0:
                    for k in range(0,3):
                        if k==0:
                            year = line[j][0:year_idx]
                            month_idx = line[j].find('-',year_idx+1)
                            continue
                        if (k==1 and month_idx>=0):
                            month = line[j][year_idx+1:month_idx]
                            continue
                        if k==2:
                            day = line[j][month_idx+1:len(line[j])]
                            tmp.append(int(day))
                            tmp.append(int(month))
                            tmp.append(int(year))
                else:
                    tmp.append(float(line[j]))
        if line[j].isalpha():
            content[i]=line
        else:
            content[i]=tmp   
    return content

if __name__ == "__main__": 
    doctest.testmod()