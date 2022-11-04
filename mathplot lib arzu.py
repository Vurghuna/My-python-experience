import matplotlib.pyplot as plt 
  
# x-coordinates of left sides of bars  
left = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] 
  
# heights of bars 
height = [7,6.9,6.8,6.9,7,0,3.1,7.4,5.6,7.45,8.2,4.95,6.2,6.25,7.35,7.4,7.2,7.1,7,7.15,2,5.2,7.49,7.3,7.38,7.25,5.4,0,7.2,8] 
  
# labels for bars 
tick_label = ['1', '2', '3', '4', '5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'] 
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['cyan','turquoise']) 
  
# naming the x-axis 
plt.xlabel('Days of month') 
# naming the y-axis 
plt.ylabel('Hours you study per day') 
# plot title 
plt.title('This chart will make you FORTUNE!') 
  
# function to show the plot 
plt.show() 
