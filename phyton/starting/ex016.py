from scipy import stats

x = [2,3,4,5,6,7,8,9,10]
y = [40,41,35,34,29,31,28,23,22]

slope,intercept,a,b,std_err = stats.linregress(x,y)

def calculadora(z):
    return slope * z + intercept

valorPrevisto = calculadora(11)
print(valorPrevisto)