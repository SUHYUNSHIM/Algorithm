class Rec:
    width =0
    height =0
    color =''
square1 = Rec()
square2 = Rec()

square1.width =10
square1.height =5
square1.color ='red'

square2.width =7
square2.height =7
square2.color ='blue'

print(square1.width, square1.height, square1.color)
print(square2.width, square2.height, square2.color)

class Quardrangle:
    width =0
    height =0
    color ="black"

    ##method는 항상 첫 번째 파라미터로 self 사용
    ##인자가 필요없을 때에도 self 사용

    def get_area(self):
        return self.width * self.height
    def set_area(self,data1, data2):
        self.width =data1
        self.height =data2

square =Quardrangle()
square.set_area(5,5)

print(square.width) ##5출력
print(square.get_area()) ##25출력
