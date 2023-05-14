
with open("tpmon.txt", "r") as temp_data:
    x = []
    lines = temp_data.readlines()[1:] # readlines() --> 각 줄을 원소로 가지는 리스트가 반환
    for line in lines: # 한 줄씩 보기
        new_line = line.strip().split() # 각 줄에서 양 끝 공백을 잘라내고, 띄어쓰기 기준으로 자릅니다
        x.append(new_line) # 각 줄을 띄어쓰기로 자르고, 그 결과물을 x에 넣기




    with open("tpmon.csv", "w") as write_csv:
        for i, year_info in enumerate(x): # year_info는 각 연도의 월별 기온이 원소로 들어있는 리스트


            current_year = 1723 + i
            print("{}:\t {:.1f} / {:.1f}".format(current_year, (float(year_info[0])+float(year_info[1]))/2, (float(year_info[6])+float(year_info[7]))/2))

            write_csv.write(f"{', '.join(year_info)}, {current_year}") # 한 줄 쓰기
            write_csv.write("\n")

