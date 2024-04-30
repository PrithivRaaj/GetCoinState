def GetCoinState(state, n):
    if n % 2 == 0:
        return state
    else:
        return "H" if state == "T" else "T"