### possible deps ###



### Get mining pool url
print("please enter mining pool url\nexample: ycash.dapool.io:3344")
pool_url = input()

### Get mining address
print("please enter a ycash address\nexample: s1QZvkYSqZWGQwTpw3Zbe9VmScoinsDD5LM\n or: ys1enumq74mkcv22werl905h56qcmmqum9dztu2gwsr73tv75g20s5xdful800hd2n4gh9vuee9yvm")
ycash_address = input()

### Write information to a file
miner_info = "./miner --algo 192_7 --pers ZcashPOW --server " + pool_url + " --user " + ycash_address
miner_file =  open("mine_yec.sh", "w")
miner_file.write(miner_info)
miner_file.close()