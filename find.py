with open('ids.txt') as f:
    lines=f.readlines()
f.close()

with open('ids.txt', 'w', encoding="ASCII") as f:
    for x in lines:
        try:
            split=x.split('\t')
            first=split[0]
            hexy=hex(int(first))
            final=bytes.fromhex(hexy[2:])
            ascii=final.decode("ASCII")
            f.write(ascii)
            f.write('\n')
        except:
            print("invalid encoding")
