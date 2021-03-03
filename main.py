''' main '''
from cbMath import myArithmetic,myCalcArea,myStatistics
m = 0
for i in range(5):
    n = int(input(str(i+1) + "."))
    m = myArithmetic.myAdd(m, n)
print(myArithmetic.myDiv(m, 5))
