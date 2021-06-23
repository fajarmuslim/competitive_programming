def generate_all_subset(list_, toggles, i):
    if i == len(list_):
        res = []
        for idx in range(len(toggles)):
            if toggles[idx] == 1:
                res.append(list_[idx])

        print(res)
    else:
        toggles[i] = 0
        generate_all_subset(list_, toggles, i + 1)

        toggles[i] = 1
        generate_all_subset(list_, toggles, i + 1)


generate_all_subset([1, 2, 3, 4, 5], [0, 0, 0, 0, 0], 0)
