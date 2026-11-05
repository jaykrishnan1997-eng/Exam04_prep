def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    collector = []
    collector_copy = []
    queue_list = []
    # temp1_list = []
    # temp2_list = []
    if packages == {}:
        return []

    for key, value in packages.items():
        if key not in collector:
            collector.append(key)
        for unit in value:
            if unit not in collector:
                collector.append(unit)
    breakpoint()
    while collector != []:
        for key in collector:
            if packages[key] == []:
                queue_list.append(key)
            for a in collector:
                if a not in queue_list and packages[a] in queue_list:
                    queue_list.append(a)
                    for item in collector and item not in queue_list:
                        collector_copy.append(item)
        collector = collector_copy

            
    # breakpoint()
    # while True:
    #     for key, value in packages.items():
    #         if value == []:
    #             queue_list.append(key)
    #             temp1_list.append(key)
    #         if key not in collector:
    #             collector.append(key)
    #         for unit in value:
    #             if unit not in collector:
    #                 collector.append(unit)
    #     for item in temp1_list:
    #         for key, value in packages.items():
    #             if item in value:
    #                 queue_list.append(key)
    #                 temp2_list.append(key)
    #     temp1_list = []
    #     for unit in collector:
    #         if unit not in queue_list and unit not in temp2_list:
    #             temp1_list.append(unit)
    #     if temp1_list == []:
    #         break


    return queue_list


if __name__ == "__main__":
    print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))  # Expected: ["driver", "database", "app"]
    # print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))  # Expected: ["A", "B", "C"]
    # print(package_dependency_resolver({}))  # Expected: []
    # print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))  # Expected: []
    # print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))  # Expected: ["api", "web", "backend", "frontend"]