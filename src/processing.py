def filter_dict_list(in_dict_list: list, in_state: str = "EXECUTED") -> list:
    if in_state not in ["EXECUTED", "CANCELED"]:
        return ["error"]
    sort_list = []
    for item in in_dict_list:
        if item["state"] == in_state:
            # print(item)
            sort_list.append(item)
    return sort_list
