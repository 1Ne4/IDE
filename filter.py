from old_filter import Mosaica


info = input().split(" ")
result = Mosaica(info[0], int(info[1]), int(info[2])).mosaic()
resName = "res.jpg"
if len(info) == 4:
    resName = info[3]
result.save(resName)

