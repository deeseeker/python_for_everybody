def computepay(h,r):
    try:
        if fh > 40:
            reg = fr * fh
            otp = (fh -40) * (fr * 0.5)
            xp = reg + otp
            return xp

        else:
            xp = fr * fh
            return xp
    except:
        print('enter a number')



xh = input("Enter Hours: ")
xr = input("Enter Rates: ")
#print(xh,xr)
fh = float(xh)
fr = float(xr)
p = computepay(fh,fr)
print('Pay',p)
