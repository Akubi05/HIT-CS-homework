from collections import deque
import copy
from actions import Goto, Pushbox, Climbbox, Grasp
from predicates import SITE, HANG, ON, HOLDS


# ---------------------------
# 状态生成（后继状态）
# ---------------------------
def successors(state):
    """
    根据当前状态生成所有可行的后继状态，并附带操作说明。
    返回的列表元素为 (操作描述, 新状态) 对。
    此处我们尝试所有可能的动作，不保证动作顺序，只用于 BFS 搜索。
    """
    actions = []
    # 可用位置
    sites = ["a", "b", "c"]

    # Goto 动作
    for u in sites:
        for v in sites:
            if u != v:
                new_state = Goto(state, u, v)
                if new_state is not None:
                    actions.append((f"Goto({u} -> {v})", new_state))

    # Pushbox 动作
    for v in sites:
        for w in sites:
            if v != w:
                new_state = Pushbox(state, v, w)
                if new_state is not None:
                    actions.append((f"Pushbox({v} -> {w})", new_state))

    # Climbbox 动作
    new_state = Climbbox(state)
    if new_state is not None:
        actions.append(("Climbbox", new_state))

    # Grasp 动作
    new_state = Grasp(state)
    if new_state is not None:
        actions.append(("Grasp", new_state))

    return actions


# ---------------------------
# 目标状态判断
# ---------------------------
def is_goal(state):
    """
    判断目标状态：猴子是否摘到香蕉
    目标：HOLDS(Monkey) ∈ state
    """
    return HOLDS("Monkey") in state


# ---------------------------
# 广度优先搜索（BFS）求解
# ---------------------------
def bfs(initial_state):
    """
    使用广度优先搜索寻找从初始状态到目标状态的一条路径。
    返回的是一个由操作描述构成的方案列表。
    """
    # 队列中每个元素为 (state, plan)，plan 是操作描述列表
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, plan = queue.popleft()
        # 状态标识使用 frozenset（因为 state 是 set，不可哈希）
        state_id = frozenset(current_state)
        if state_id in visited:
            continue
        visited.add(state_id)

        if is_goal(current_state):
            return plan

        for action_desc, new_state in successors(current_state):
            queue.append((new_state, plan + [action_desc]))

    return None  # 未找到解
