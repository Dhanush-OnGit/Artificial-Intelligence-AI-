def main():
    rooms = {'A':0,'B':0}
    cost = 0
    
    print("vaccum cleaner")
    print("[1]for dirt\n[2]for clean\n")
    
    for i in rooms.keys():
        rooms[i] = int(input(f"enter the status {i} : "))
    print()
    
    for i in rooms.keys():
        if(rooms[i] == 1):
            print(f"[-]room {i} is dirty and cleaning..")
            rooms[i]=0
            
            print(f"[*]room {i} is cleaned...")
            cost += 1
            
        else:
            print(f"[--] room {i} is already cleaned")
            
    print(f"the total cost is {cost}",end="\n\n")
if __name__ == "__main__":
    main()