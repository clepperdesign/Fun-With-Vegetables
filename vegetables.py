import math
lastfrost = {3 : 150, 4 : 150, 5 : 119, 6 : 119, 7 : 119, 8 : 88, 9 : 58, 10 : 30}
#days into the year of a zone's maximum last average frost
veglist = {'radish':[20,70],'bean':[45,100],'melon':[65,110],'potato':[80,120]}
monthlist = [None, "January","February","March","April","May","June","July","August","September","October","November","December"]
def main():
    yourzone = int(input('what usda hardiness zone do you live in? \n'))
    vegchoice = str.lower((input('Choose a vegetable: bean, melon, radish, potato \n')))
    harveststart= (math.ceil((lastfrost[yourzone]+veglist[vegchoice][0])/30))
    harveststop = (math.ceil((lastfrost[yourzone]+veglist[vegchoice][1])/30))
    usdastart = (math.ceil(lastfrost[yourzone]/30))
    def monthmath(x):
        month= monthlist[x]
        return(month)
    harvest0 = monthmath(harveststart)
    harvest1 = monthmath(harveststop)
    plantmonth = monthmath(usdastart)
    print("You may start planting in " + plantmonth + ". You can harvest a " + vegchoice + " crop between " + harvest0 + " and " + harvest1 + ".")
main()
