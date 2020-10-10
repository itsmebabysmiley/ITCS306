# ทศนิยมมันเพ้ียนๆ คิดแบบผสม(binocalculate) รุ้จักป่าว55555
useg = 123  #kw
Ft = -12.43 # s/kw
sum = 0
charge = (useg*Ft)/100 #bath
print('Customer used Energy           :   {:7.2f}    KWh/Month'.format(useg))
print('Ft                             :   {:7.2f}    Satang/KWh'.format(Ft))
print("======================================================")
if useg<=50:
    print('Free บ้านคุนพี่จุดเทียนหรอค่ะ')
    
else:
    print('First 15 kWh ( 1st – 15th)     :   {:7.2f}    Bath'.format(35.23))
    print('Next  10 kWh (16th – 15th)     :   {:7.2f}    Bath'.format(29.88))
    print('Next  10 kWh (26th – 35th)     :   {:7.2f}    Bath'.format(32.41))
    if useg>=36 and useg<100:
        sum = (useg-35)*3.6237+32.41+29.88+35.23
        print('Next  65 kWh (36th – 100th)    :   {:7.2f}    Bath'.format(sum))
    elif useg>=101 and useg<150:
        sum = 235.54
        print('Next  65 kWh (36th – 100th)    :    {:7.2f}   Bath'.format(sum))
        sum = (useg-100)*3.7171+235.54+32.41+29.88+35.23
        print('Next  50 kWh (101th – 150th)   :    {:7.2f}   Bath'.format(sum))
    elif useg>=151 and useg<400:
        sum = 235.54
        print('Next  65 kWh (36th – 100th)    :    {:7.2f}   Bath'.format(sum))
        sum = 185.86
        print('Next  50 kWh (101th – 150th)   :    {:7.2f}   Bath'.format(sum))
        sum = (useg-150)*4.2218+185.56+235.54+32.41+29.88+35.23
        print('Next  250 kWh (151th – 400th)  :   {:7.2f}   Bath'.format(sum))
    elif  useg>=401:
        sum = 235.54
        print('Next  65 kWh (36th – 100th)    :    {:7.2f}   Bath'.format(sum))
        sum = 185.86
        print('Next  50 kWh (101th – 150th)   :    {:7.2f}   Bath'.format(sum))
        sum = 1055.45
        print('Next  250 kWh (151th – 400th)  :   {:7.2f}   Bath'.format(sum))
        x = useg%400
        sum = (useg-400)*4.4217+1055.45+185.56+235.54+32.41+29.88+35.23
        print('Over  400 kWh (up from 401st)  :   {:7.2f}    Bath'.format((useg-400)*4.4217))
    
    print("======================================================")
    print('Total                          :   {:7.2f}    Bath'.format(sum))
    print('Service Charge                 :   {:7.2f}    Bath'.format(8.19))
    print()
    print('Total Base Tariff              :   {:7.2f}    Bath'.format(sum+8.19))
    print("======================================================")
    print('Section 2 [Ft] Charge')
    print('Used Energy x Ftrate           :   {:7.2f}    Bath'.format((useg*Ft)/100))
    print()
    print('Section 3 Tax 7%')
    print('|Base Tariff + Ft| x 0.07      :   {:7.2f}    Bath'.format( (((sum+8.19)+(useg*Ft)/100))*0.07) )
    print()
    print('Total Electricity Charge       :   {:7.2f}    Bath'.format(+((sum+8.19) + ((useg*Ft)/100)) + (((sum+8.19)+(useg*Ft)/100))*0.07))
    print("======================================================")