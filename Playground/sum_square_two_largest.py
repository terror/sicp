def main(x):
    x.sort()
    return (x[-1] * x[-1]) + (x[-2] * x[-2])


if __name__ == '__main__':
    print(main([1, 2, 3, 4, 5]))  # 41
