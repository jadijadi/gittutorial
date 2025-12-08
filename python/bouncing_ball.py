def bouncing_ball():
    a,b,c,d,e,n='+- |*\n'
    w=d+c*18+d+n
    s=a+b*18+a+n
    x,y=0,0
    g,h=17,7
    j,k=1,1
    global clear_command
    count_sec = 0
    print('Bouncing Ball! for 10 seconds')
    time.sleep(1.5)
    try:
        while count_sec < 10:
            if 0>x or x>g:j*=-1;x+=j
            if 0>y or y>h:k*=-1;y+=k
            os.system(clear_command);print( s+w*y+d+c*x+e+c*(g-x)+d+n+w*(h-y)+s );x+=j;y+=k;time.sleep(0.1)
            count_sec += 0.1
    except KeyboardInterrupt:
        print('\nbouncing ball STOPED!')
    
if __name__ == "__main__":
    import os
    import time
    import platform

    # Determine the clear command based on the operating system
    if platform.system() == "Windows":
        clear_command = "cls"
    else:
        clear_command = "clear"

    bouncing_ball() 