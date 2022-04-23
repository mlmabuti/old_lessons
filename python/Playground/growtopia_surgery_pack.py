# write a code to determine the profit in N number of surg packs.

# heart monitor - 3/1
#bed - 20/1
#traine - 2/1
#medcheck - 25/1

#stitch - 1.8
#sponge - 15/wl
#antibiotic - 15/wl
#scalpel - 15/wl
# the rest (9 tools) - 16/wl

pack_count = input("How many packs did you purchase? ")
pack_cost = input("How much did you purchase each pack? ")
total_pack_cost = int(pack_count) * float(pack_cost)

hmonitor = 1
bed = 1
traine = 1
medacheck = 10
stitch = 5
sponge = 5
antibiotic = 5
scalpel = 5
commons = 45

hmonitor_price = input("How many heart monitors per wl? ")
bed_price = input("How many hospital beds per wl? ")
traine_price = input("How many train E per wl? ")
medacheck_price = input("How many med a check per wl? ")
sponge_price = input("How many sponges per wl? ")
antibiotic_price = input("How many anitbiotics per wl? ")
scalpel_price = input("How many scalpels per wl? ")
stitch_price = input("Stitches 200/? ")
commons_price = input(
    "How many common tools (antiseptic, anesthethic, etc.) per wl? ")

hmonitor_count = int(pack_count) * int(hmonitor)
bed_count = int(pack_count) * int(bed)
traine_count = int(pack_count) * int(traine)
medacheck_count = int(pack_count) * int(medacheck)
sponge_count = int(pack_count) * int(sponge)
antibiotic_count = int(pack_count) * int(antibiotic)
scalpel_count = int(pack_count) * int(scalpel)
commons_count = int(pack_count) * int(commons)
stitch_count = int(pack_count) * int(stitch)

hmonitor_total = int(hmonitor_count) / int(hmonitor_price)
bed_total = int(bed_count) / int(bed_price)
traine_total = int(traine_count) / int(traine_price)
medacheck_total = int(medacheck_count) / int(medacheck_price)
sponge_total = int(sponge_count) / int(sponge_price)
antibiotic_total = int(antibiotic_count) / int(antibiotic_price)
scalpel_total = int(scalpel_count) / int(scalpel_price)
commons_total = int(commons_count) / int(commons_price)
stitch_total = int(stitch_count) / 200 * int(stitch_price)

total_sold = int(hmonitor_total) + int(bed_total) + int(traine_total) + int(medacheck_total) + int(
    sponge_total) + int(antibiotic_total) + int(scalpel_total) + int(commons_total) + int(stitch_total)
profit = int(total_sold) - int(total_pack_cost)

print(f"\nNumber of packs: {pack_count}")
print(f"Total world locks spent: {total_pack_cost}")
print(f"Total world locks to be sold: {total_sold}")
print(f"Total profit to be gained: {profit}")
