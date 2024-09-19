def main():
    score = input("점수를 ,로 구분하여 입력하세요 > ")
    try:
        scores = score.split(',')
        cnt = 0
        minVal = 0
        maxVal = 0
        midVal = 0
        totVal = 0

        print (len(scores))
        for i in range (0, len(scores)):
            x = scores[i].strip()
            
            print(x)
            if not x.isdigit():
                print("not number : " + x)
            else :
                x = float(x)

                if cnt == 0 :
                    minVal = x  
                    maxVal = x

                cnt += 1
                totVal += x
                if minVal > x :
                    minVal = x
                if maxVal < x :
                    maxVal = x
        
        if cnt == 0:
            print("유효한 숫자가 없습니다.")
        else :
            midVal = totVal/cnt
            print("최소값 : {:.3f}".format(minVal))
            print("최대값 : {:.3f}".format(maxVal))
            print("평균값 : {:.3f}".format(midVal))
    except:
        print("Error Occured")
        exit()
    
    
if __name__ == "__main__":
    main()