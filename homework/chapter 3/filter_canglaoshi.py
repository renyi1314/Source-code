list_filter = ["苍老师", "东京热", "苍"]
input_content = input("Please input: ")


# 苍老师在东京热
# def filter_content():
#     out_content = input_content
#     for i in list_filter:
#         if i in out_content:
#             out_content = out_content.replace(i, "*" * len(i))
#     return out_content


def filter_content():
    out_content = input_content
    for i in (i for i in list_filter if i in input_content):
        out_content = out_content.replace(i, "*" * len(i))
    return out_content


if __name__ == "__main__":
    print(filter_content())
