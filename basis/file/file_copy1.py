with open("E:\githubproject\Source-code\\basis\\file\\test.txt", mode='r') as f:
    contents = f.read()
    with open("E:\githubproject\Source-code\\basis\\file\\test_bak.txt", mode='w') as f_bak:
        f_bak.write(contents)
