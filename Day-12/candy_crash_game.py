moves=30
while moves>0:
    status=input("[W] in or [c] continue: ").upper()
    if status=='W':
        print("You won the game")
        break
    moves-=1
    print(f'{moves} moves are left')
else:
    print("Game Over")
