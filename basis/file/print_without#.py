with open("E:\githubproject\Source-code\\basis\\file\\test.txt", mode='r') as f:
    for line in f:
        line = line.strip()
        if line[0] != "#":
            print(line)
