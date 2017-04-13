from Portfolio import *

def main():
    example = Portfolio('Reid')
    print(example.getFunds())
    example.addFunds(100000000)
    print(example.getFunds())
    example.buyStock("AAV", 5)
    example.buyStock("ABT", 10)
    print(example.getFunds())
    example.sellStock("AAV", 2)
    example.sellStock("ABT", 3)
    print(example.getFunds())
    li = example.showOwnedStock()
    num = 0
    while num < len(li):
        print(li[num] + " " + li[num + 1])
        num += 2
    print(example.showNetGain())
    print(example.showNetLoss())

    example = Portfolio('Reid')
    example.ret_data()
    li = example.showOwnedStock()
    num = 0
    while num < len(li):
        print(li[num] + " " + li[num + 1])
        num += 2

    example.addFunds(100000000)
    example.buyStock("AAV", 2)
    example.buyStock("ABT", 3)

    li = example.showOwnedStock()
    num = 0
    while num < len(li):
        print(li[num] + " " + li[num + 1])
        num += 2

    di = example.showAmtStock()
    print(di)
    return

main()