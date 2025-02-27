# width formating

for i in range(0, 20, 2):
    print('given i={0} : i ^ 4 ={1} i ^ 3 ={2}'.format(i, i * i * i * i, i * i * i))
    ## printing given i=0 : i ^ 4 =0 i ^ 3 =0
    #given i=2 : i ^ 4 =16 i ^ 3 =8
    # given i=4 : i ^ 4 =256 i ^ 3 =64
    # given i=6 : i ^ 4 =1296 i ^ 3 =216
    # given i=8 : i ^ 4 =4096 i ^ 3 =512
    # given i=10 : i ^ 4 =10000 i ^ 3 =1000
    # given i=12 : i ^ 4 =20736 i ^ 3 =1728
    # given i=14 : i ^ 4 =38416 i ^ 3 =2744
    # given i=16 : i ^ 4 =65536 i ^ 3 =4096
    # given i=18 : i ^ 4 =104976 i ^ 3 =5832


# you can make it right aligned  {:2} , {:4} , {:7}
# you can make it left aligned  {:<2} , {:<4} , {:<7}
# you can make it mid aligned  {:^2} , {:^4} , {:^7}
