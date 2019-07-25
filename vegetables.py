import math
lastfrost = {3 : 150, 4 : 150, 5 : 119, 6 : 119, 7 : 119, 8 : 88, 9 : 58, 10 : 30}
#days into the year of a zone's maximum last average frost
vegearly = {'radish':20,'bean':45,'melon':65,'potato':80}
veglate = {'radish':70,'bean':100,'melon':110,'potato':120}
#first and last available harvest date from time of planting of given produce type from data set
def main():
    yourzone = int(input('what usda hardiness zone do you live in? \n'))
    vegchoice = str.lower((input('Choose a vegetable: bean, melon, radish, potato \n')))
    harveststart = (math.ceil((lastfrost[yourzone]+vegearly[vegchoice])/30))
    harveststop = (math.ceil((lastfrost[yourzone]+veglate[vegchoice])/30))
    usdastart = (math.ceil(lastfrost[yourzone]/30))
    print(usdastart)
    def monthmath(x):
        month = "Month"
        if x == 1:
            month = "January"
        elif x == 2:
            month = "February"
        elif x == 3:
            month = "March"
        elif x == 4:
            month = "April"
        elif x == 5:
            month = "May"
        elif x == 6:
            month = "June"
        elif x == 7:
            month = "July"
        elif x == 8:
            month = "August"
        elif x == 9:
            month = "September"
        elif x == 10:
            month = "October"
        elif x == 11:
            month = "November"
        elif x == 12:
            month = "December"
        else:
            month = "An error has occurred"
        return(month)
    harvest0 = monthmath(harveststart)
    harvest1 = monthmath(harveststop)
    plantmonth = monthmath(usdastart)
    print("You may start planting in " + plantmonth + ". You can harvest a " + vegchoice + " crop between " + harvest0 + " and " + harvest1 + ".")
main()
