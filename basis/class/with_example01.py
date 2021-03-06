#!/usr/bin/env python
# with_example01.py

class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("In __exit__()")


def get_sample():
    return Sample()


with get_sample() as sample:
    print("sample:", sample)
