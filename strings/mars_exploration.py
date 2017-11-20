S = input().strip()

print(len([1 for signal, check in zip(S, 'SOS'*33) if signal != check]))