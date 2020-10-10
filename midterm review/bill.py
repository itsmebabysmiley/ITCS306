useg = 51.0  #kw
Ft = -12.43 # s/kw

charge = (useg*Ft)/100 #bath

if useg<50:
    print('Free')
else:
    if useg>36 and useg<100:
        sum = 235.54+32.41+29.88+35.23
    elif useg>101 and useg<101:
        sum = 185.56+235.54+32.41+29.88+35.23
    elif useg>151 and useg<400:
        sum = 1,055.45+185.56+235.54+32.41+29.88+35.23
    elif  useg>401:
        x = useg%400
        sum = (884.34+1,055.45+185.56+235.54+32.41+29.88+35.23)*x
    print(sum)
    