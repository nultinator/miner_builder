### possible deps ###


### Get miner type
print("Do you use miniZ or Gminer")
miner = input()
while miner.lower() != "gminer" and miner.lower() != "miniz":
    print("Selection not valid, please choose either Gminer or miniZ")
    miner = input()
### Get mining pool url
print("please enter mining pool url\nexample: ycash.dapool.io:3344")
pool_url = input()

### Get mining address
print("please enter a ycash address\nexample: s1QZvkYSqZWGQwTpw3Zbe9VmScoinsDD5LM\n or: ys1enumq74mkcv22werl905h56qcmmqum9dztu2gwsr73tv75g20s5xdful800hd2n4gh9vuee9yvm")
ycash_address = input()

### Write information to a file
if miner.lower() == "gminer":
    miner_info = "./miner --algo 192_7 --pers ZcashPOW --server " + pool_url + " --user " + ycash_address
elif miner.lower() == "miniz":
    miner_info = "./miniZ --url=" + ycash_address + "@" + pool_url + " --par=192,7 --pers ZcashPOW -p x"
else:
    print("Something went wrong")
miner_file =  open("mine_yec.sh", "w")
miner_file.write(miner_info)
miner_file.close()