def generatorBasic():
    print('First call')
    yield 10

    print('Second call')
    yield 20

    print('Last call')
    yield 30



if __name__ == "__main__":
    gen= generatorBasic()
    r1=next(gen)
    r2=next(gen)
    r3=next(gen)
    print(f'1: {r1}, 2: {r2}, 3: {r3}')
    print(gen)

'''
will response --> 
First call
Second call
Last call
1: 10, 2: 20, 3: 30

'''