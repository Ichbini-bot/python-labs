'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
# convert into miles per minute => 20 miles in 61 minutes
# calculate miles per hour
# convert miles into km

mtk = 1.6 # mtk = mile to km

miles_per_hour = (20 / 61) * 60
print(miles_per_hour)

km = miles_per_hour * mtk
print(km)