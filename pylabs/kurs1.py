x=2^ceil(numbits(N)/2
loop:
    y=floor((x+floor(N/x))/2)
    if y>=x
        return x 
    x = y
