xh = input("Enter Hours: ")
xr = input("Enter Rates: ")
#print(xh,xr)
try:
    fh = float(xh)
    fr = float(xr)
    #print(fh,fr)
    if fh > 40:
        print('overtime')
        reg = fr * fh
        otp = (fh -40) * (fr * 0.5)
        print(reg,otp)
        xp = reg + otp
        print('Pay: ',xp)

    else:
        #print('Regular')
        xp = fr * fh
        print('Pay: ',xp)
except:
    print('enter a number')
