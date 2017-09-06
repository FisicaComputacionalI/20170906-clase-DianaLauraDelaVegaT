import matplotlib as mpl
import pylab as pl 
x=(6000,7000,8000,9000,10000)
y=(73,80,85,87,89)
pl.plot(x,y)
x1=(7000,8000,9000,10000,11000)
y1=(80,83,85,86,88)
pl.plot(x1,y1)
pl.xlabel('Voltaje (V)')
pl.ylabel('Eficiencia (%)')
pl.title('Nueva tec & antigua tec')
pl.savefig('graficas.png')
pl.show ('graficas.png')

