from predicates import SITE, HANG, ON, HOLDS

# ---------------------------
# 状态操作（动作定义）
# ---------------------------


def Goto(state, u, v):
    """
    动作 Goto(u, v)
    前提条件：SITE(Monkey, u) ∈ state，且猴子不在箱子上 (即 ON(Monkey) 不在 state)
    删除列表：SITE(Monkey, u)
    添加列表：SITE(Monkey, v)
    """
    monkey_in_u = SITE("Monkey", u)
    monkey_not_on_box = ON("Monkey") not in state
    if monkey_in_u in state and monkey_not_on_box:
        new_state = state.copy()
        new_state.remove(monkey_in_u)
        new_state.add(SITE("Monkey", v))
        print(f"Action: Goto({u} -> {v})")
        return new_state
    return None


def Pushbox(state, v, w):
    """
    动作 Pushbox(v, w)
    前提条件：SITE(Monkey, v) ∈ state ∧ SITE(Box, v) ∈ state (猴子与箱子在同一位置且猴子未在箱子上)
    删除列表：SITE(Monkey, v) 和 SITE(Box, v)
    添加列表：SITE(Monkey, w) 和 SITE(Box, w)
    """
    monkey_at_v = SITE("Monkey", v)
    box_at_v = SITE("Box", v)
    if monkey_at_v in state and box_at_v in state and (ON("Monkey") not in state):
        new_state = state.copy()
        new_state.remove(monkey_at_v)
        new_state.remove(box_at_v)
        new_state.add(SITE("Monkey", w))
        new_state.add(SITE("Box", w))
        print(f"Action: Pushbox({v} -> {w})")
        return new_state
    return None


def Climbbox(state):
    """
    动作 Climbbox
    前提条件：存在一个位置 x，使得 SITE(Monkey, x) ∈ state 和 SITE(Box, x) ∈ state，且猴子未在箱子上
    删除列表：无（可以保留猴子的位置描述）
    添加列表：ON(Monkey)
    """
    for loc in ["a", "b", "c"]:
        if (
            SITE("Monkey", loc) in state
            and SITE("Box", loc) in state
            and (ON("Monkey") not in state)
        ):
            new_state = state.copy()
            new_state.add(ON("Monkey"))
            print(f"Action: Climbbox (at {loc})")
            return new_state
    return None


def Grasp(state):
    """
    动作 Grasp
    前提条件：存在一个位置 y，使得 ON(Monkey) ∈ state, SITE(Monkey, y) ∈ state 且 HANG(Banana, y) ∈ state
    删除列表：HANG(Banana, y)
    添加列表：HOLDS(Monkey)
    """
    # 遍历所有可能的位置
    for loc in ["a", "b", "c"]:
        if (
            ON("Monkey") in state
            and SITE("Monkey", loc) in state
            and HANG("Banana", loc) in state
        ):
            new_state = state.copy()
            new_state.remove(HANG("Banana", loc))
            new_state.add(HOLDS("Monkey"))
            print(f"Action: Grasp (at {loc})")
            return new_state
    return None
