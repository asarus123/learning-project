for n1 in range(1, 33):
    for n2 in range(1, 33):
        for n3 in range(1, 33):
            for n4 in range(1, 33):
                if n1**3 + n2**3 == n3**3 + n4**3 and n1 != n2 and n1 != n3 and n1 != n4 and n2 != n1 and n2 != n3 and n2 != n4 :
                    print(n1**3 + n2**3, n3**3 + n4**3)