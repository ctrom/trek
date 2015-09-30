class Ellipse:
    def Ellipse(self,r):
        #Creates a blank 2d Array galaxy of radius 'r'
        galaxy = [[0 for i in range((r+1)*2)] for i in range((r+1)*2)]
        sectors = 0
        #Checks whether or not sectors are contained in galaxy
        for x in range (2*r+2):
            for y in range (2*r+2):
                d = pow(x-r-0.5,2)+pow(r-y+0.5,2)
                if d<pow(r,2):
                    #If sector is in upper right (Alpha Sector) it is marked 'I'
                    if x>r and y<r+1:
                        galaxy[y][x]="I"
                        sectors+=1
                    #If sector is in upper left (Beta Sector) it is marked 'II'
                    if x<r+1 and y<r+1:
                        galaxy[y][x]="II"
                        sectors+=1
                    #If sector is in upper right (Gamma Sector) it is marked 'III'
                    if x<r+1 and y>r:
                        galaxy[y][x]="III"
                        sectors+=1
                    #If sector is in upper right (Delta Sector) it is marked 'IV'
                    if x>r and y>r:
                        galaxy[y][x]="IV"
                        sectors+=1
                #If sector is outside of known galaxy it is marked '*'
                else:
                        galaxy[y][x]="*"
        #Displays number of sectors and galaxy map
        print(str(sectors)+'\n')
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in galaxy]))

gal = Ellipse()
#Prompts creation of galaxy
gal.Ellipse(int(input('galaxy size: ')))