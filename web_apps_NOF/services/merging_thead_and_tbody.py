def merging_thead_and_tbody(th, ts):
    i = 0
    merged_dict_final = {}
    for key, value in ts.items():
        pass
        # print(key, value)
    # print(ts)
    # print(th)
    for key, value in th.items():
        for key1, value1 in value.items():
            merged_dict_final.update({key: []})
            merged_dict_final[key] = value
            # print(key, value)
            i += 1
    # print(merged_dict_final)
    # i = len(th)
    for key, value in ts.items():
        # print(key, value)
        for key1, value1 in value.items():

            merged_dict_final[key].update({i: ''})
            merged_dict_final[key][i] = value1
            i += 1

    j = 0
    # print(merged_dict_final)

    for item in merged_dict_final.values():
        # print(item)

        for key, value in item.items():
            pass
            j += 1
            # print(value)
            for el in value:
                # print(el)


                # print(item1)

                # print(el1)
                el['row_start'] = j
                rowspan = int(el['rowspan'])
                rowspan = rowspan + j - 1
                el['row_end'] = rowspan
                # print(j, item)
    #
    for item in merged_dict_final.values():
        for key, value in item.items():
            # print(value)
            for el in value:
                print(el['column_start'], el['column_end'], el['row_start'], el['row_end'])
    print(merged_dict_final)
    return merged_dict_final
