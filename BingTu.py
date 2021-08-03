import matplotlib.pyplot as plt

#labels = 'x','y','z'
colors = ['tomato', 'lightskyblue', 'goldenrod']
labels = [r'$\varphi$ ', r'$\theta$', r'$\psi$']

#sizes = [9.7,3.2,87.1] #00
#sizes = [2.8,2.0,95.2] #01
#sizes = [8.8,5.1,86.1] #02
#sizes = [5.5,3.3,91.2] #03
#sizes = [5.6,6.7,87.7] #04
#sizes = [5.8,2.7,91.5] #05
#sizes = [6.6,2.4,91.0] #06
#sizes = [6.5,2.8,90.7] #07
#sizes = [7.6,8.7,83.6] #08
#sizes = [7.5,3.4,89.2] #09
#sizes = [5.7,3.0,91.2] #10

#sizes = [13.3,75.6,11.1] #00
#sizes = [11.1,78.8,10.1] #01
#sizes = [13.8,74.0,12.2] #02
#sizes = [18.5,64.6,16.9] #03
#sizes = [34.9,16.3,48.8] #04
#sizes = [13.3,75.5,11.2] #05
#sizes = [9.9,83.1,7.0] #06
#sizes = [11.0,79.0,10.0] #07
#sizes = [12.7,75.5,11.8] #08
#sizes = [12.1,76.0,11.9] #09
sizes = [17.3,69.1,13.6] #10

explode = (0, 0, 0) 

plt.pie(sizes, explode=(0.1,0.05,0),labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)
plt.axis('equal') 

plt.show()
