import re
from copy import deepcopy

PATTERN = re.compile(r"([a-z]+ [a-z]+) bags contain ([a-z0-9, ]+)")
COLORS = {}
with open("day7/input.txt") as reader:
    for l in reader.readlines():
        color, contains = re.match(PATTERN, l.strip("\n")).groups()
        COLORS[color] = [bags.strip() for bags in re.sub(
            r" bags|bag\.*", "", contains).split(", ")]
COLORS2 = deepcopy(COLORS)


def det_num_bag(color_dict: dict, root_color: str, target_color: str = None) -> int:
    """
    :param color_dict: the dict to use when counting (int values of keys are the return values for that colored bag)
    :param root_color: the current node
    :param target_color: it is the color to look for
    :return (when recursion is done)
        - if target_color: how many target_colors there in root_color bag
        - if target_color is None: how many bags in total are in root_color bag (including that bag)
    """
    if target_color == "":
        raise Exception("You must provide a color, not an empty string")

    # if the amount of target_color bags was already determined, just return it
    if isinstance(bags := color_dict[root_color], int):
        return bags

    count = 0

    if root_color == target_color:
        # since this is already the target color bag, any bags within this bag does not need to be counted
        for bag in bags:
            num, clr = re.match(r"(\d+) ([a-z0-9 ]+)", bag).groups()

            color_dict[clr] = 0
    elif bags[0] != "no other":  # if no bags within that bag, skip this
        for bag in bags:
            num, clr = re.match(r"(\d+) ([a-z0-9 ]+)", bag).groups()

            # add the amount of target_color bags and move on
            if clr == target_color:
                count += int(num)
                continue

            # look into the current bag to find any other colors
            count += int(num) * det_num_bag(color_dict, clr, target_color)

    # count the bag that contains the bags
    if target_color is None:
        count += 1

    color_dict[root_color] = count
    return count


for clr in COLORS:
    det_num_bag(COLORS, clr, "shiny gold")

print(len(tuple(color for color, number in COLORS.items() if number > 0)))
print(det_num_bag(COLORS2, "shiny gold") - 1)
