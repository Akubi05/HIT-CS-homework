#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search import *


# ---------------------------
# 主函数
# ---------------------------
def main():
    # 初始状态 S₀：
    # 猴子在 a；箱子在 b；香蕉悬挂在 c
    S0 = {SITE("Monkey", "a"), SITE("Box", "b"), HANG("Banana", "c")}

    print("Initial state:")
    for pred in sorted(S0, key=lambda x: repr(x)):
        print("  ", pred)

    plan = bfs(S0)
    if plan:
        print("\n找到的方案：")
        for step in plan:
            print("  ", step)
    else:
        print("没有找到可行的方案。")


if __name__ == "__main__":
    main()
