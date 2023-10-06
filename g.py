# g1p1
# for i in range(0,32,2):
#     print(f'PG1_{int(i/2)}: pg port map(pu => p0({i+1}), pl => p0({i}), gu => g0({i+1}), gl => g0({i}), pr => p1({int(i/2)}), gr => g1({int(i/2)}));')


# g2p2
# for i in range(0,16,2):
#     print(f'PG2_{int(i/2)}: pg port map(pu => p1({i+1}), pl => p1({i}), gu => g1({i+1}), gl => g1({i}), pr => p2({int(i/2)}), gr => g2({int(i/2)}));')

#g3p3
# for i in range(0,8,2):
#     print(f'PG3_{int(i/2)}: pg port map(pu => p2({i+1}), pl => p2({i}), gu => g2({i+1}), gl => g2({i}), pr => p3{int(i/2)}), gr => g3({int(i/2)}));')

# g4p4
# for i in range(0,4,2):
#     print(f'PG4_{int(i/2)}: pg port map(pu => p3({i+1}), pl => p3({i}), gu => g3({i+1}), gl => g3({i}), pr => p4{int(i/2)}), gr => g4({int(i/2)}));')

# g5p5
# for i in range(0,2,2):
    # print(f'PG5_{int(i/2)}: pg port map(pu => p4({i+1}), pl => p4({i}), gu => g4({i+1}), gl => g4({i}), pr => p5{int(i/2)}), gr => g5({int(i/2)}));')

# carry last stage
# for i in range(0,32,2):
    # print(f'C_{i+1}: carry port map(ci => c({i}), gi => g0({i}), pi => p0({i}), co => c({i+1}));')

for i in range(0,32):
    print(f"S_{i}: sum port map(pi => p0({i}), ci => c({i}), s => S({i}));")