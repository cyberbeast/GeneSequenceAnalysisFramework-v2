__author__ = 'Sandesh'

from itertools import product


def CreateGeneDataStructure(graph, depth):
    pattern_count = 0
    ind = 0
    repeat_value_outer = 1

    while repeat_value_outer <= depth:
        for sub_combo_top in product('ACGT', repeat=repeat_value_outer):
            sub_combo_top = str(''.join(sub_combo_top))
            graph["nodes"].append({"name": sub_combo_top, "pattern-id": pattern_count, "group-id": repeat_value_outer})

            pattern_count += 1

            formatted_dict = {}
            repeat_value_inner = 1
            while repeat_value_inner <= depth:
                for sub_combo_inner in product('ACGT', repeat=repeat_value_inner):
                    sub_combo_inner = str(''.join(sub_combo_inner))
                    formatted_dict[sub_combo_inner] = 0
                repeat_value_inner += 1

            graph["links"].append({sub_combo_top: formatted_dict})
            ind += 1
            print()
        repeat_value_outer += 1