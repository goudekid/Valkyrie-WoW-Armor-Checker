# program to get the info from the armorlist and give me something more usable back

f2 = open('prunedlist', 'w')
f3 = open('sortedlist', 'w')


def main():

    n = 0

    with open('armorlist', 'r') as f:

        lines = f.readlines()

    for l in lines:

        if l.find('Armor') != -1:

            parts = l.split()

            try:

                if int(parts[1]) > 20:

                    ratio = int(parts[-1].replace(',', '')) / int(parts[1])

                    if ratio < 40:

                        f2.write("Level: " + parts[1] + ", Armor: " + parts[-1] + ", Ratio: " + str(round(ratio, 2)) +
                                 "----->")
                        npc = lines[n-1].split()[1]
                        f2.write("https://db.valkyrie-wow.org/?npc=" + npc + "\n")

            except (IndexError, ValueError) as e:
                pass

        n += 1


def sort_list():

    with open('prunedlist', 'r') as f:

        lines = f.readlines()

    split_lines = [l.split() for l in lines]

    split_lines.sort(key=lambda x: x[1])

    for lists in split_lines:

        for item in lists:

            f3.write(item)

        f3.write("\n")

main()

f2.close()

sort_list()

f3.close()
