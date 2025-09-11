stack = []

# push some numbers
stack.append(10)      # 🔴 Breakpoint 1 → see stack after first push
stack.append(20)      # 🔴 Breakpoint 2 → see stack after second push
stack.append(30)      # 🔴 Breakpoint 3 → see stack after third push

print("Stack after pushes:", stack)   # 🔴 Breakpoint 4 → check full stack

# pop one number    
popped = stack.pop()  # 🔴 Breakpoint 5 → see what gets popped
print("Popped:", popped)
print("Stack after pop:", stack)      # 🔴 Breakpoint 6 → check final stack
