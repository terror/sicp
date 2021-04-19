def main(a, b, c):
    return (max(a, b, c) ** 2) + ((sum([a, b, c]) - (max(a, b, c) + min(a, b, c))) ** 2)

if __name__ == '__main__':
    print(main(2, 3, 4)) # 25
