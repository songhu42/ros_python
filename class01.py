import keyword
import class02

class Abc() :
    # 연산자 overriding 
    def __add__(self, bb):
        return 'abc'
    

def main():
    a = Abc()
    b = Abc()
    
    print(a+b)
    
    print(10, 20, '삼십', sep = '\t', end = '\t\n\n')
    print("""
여러줄 출력
여러줄 출력
여러줄 출력""")

    # issubclass
    print(type(10), type(10.0), "issubclass(int, object) : ", issubclass(int, object))
    # python 키워드 출력 
    # print(keyword.kwlist)

    #  내부변수 출력 
    # print(globals())
    pass

#  내부변수 : import시에는 실행되지 않고, 현재 파일 실행시에만 main() 실행 .. 
if __name__ == '__main__' : 
    main()
