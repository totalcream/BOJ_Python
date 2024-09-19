def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def check_conflict(events):
    events = sorted(events)
    for i in range(1, len(events)):
        if events[i][0] < events[i-1][1]:
            return "conflict"
    return "no conflict"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    index = 0
    while True:
        N = int(data[index])
        if N == 0:
            break
        index += 1
        events = []
        for _ in range(N):
            start, end = data[index].split('-')
            start_minutes = time_to_minutes(start)
            end_minutes = time_to_minutes(end)
            events.append((start_minutes, end_minutes))
            index += 1
        print(check_conflict(events))

if __name__ == "__main__":
    main()
