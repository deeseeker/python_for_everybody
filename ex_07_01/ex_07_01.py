fname = input('Enter file name: ')
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    line = line.rstrip()
    ipos = line.find(":")
    piece = line[ipos+1:]
    piece = float(piece)
    tot = tot + piece
    count = count + 1

print(f"Average spam confidence: {tot/count}")
