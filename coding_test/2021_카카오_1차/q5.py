def solution(play_time, adv_time, logs):
    logs_start_sec = list()
    logs_end_sec = list()

    # log 시간 초로 변환
    for log in logs:
        times = log.split("-")

        start = list(map(lambda x: int(x), times[0].split(":")))
        end = list(map(lambda x: int(x), times[1].split(":")))

        logs_start_sec.append(3600 * start[0] + 60 * start[1] + start[2])
        logs_end_sec.append(3600 * end[0] + 60 * end[1] + end[2])

    # play_time 변환
    play_time_sec = list(map(lambda x: int(x), play_time.split(":")))
    play_time_sec = 3600 * play_time_sec[0] + 60 * play_time_sec[1] + play_time_sec[2]

    # adv_time 변환
    adv_time_sec = list(map(lambda x: int(x), adv_time.split(":")))
    adv_time_sec = 3600 * adv_time_sec[0] + 60 * adv_time_sec[1] + adv_time_sec[2]

    total_time = [0 for _ in range(400000)]

    # 구간별 누적합
    for i in range(len(logs)):
        total_time[logs_start_sec[i]] += 1
        total_time[logs_end_sec[i]] -= 1

    # 구간별 재생 횟수
    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i - 1]

    # 구간별 재생횟수의 누적합
    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i - 1]


    # 시작 지점부터 play_time까지 누적합의 최댓값을 리턴하는 시간을 찾는다.
    max_time = 0
    max_played = total_time[adv_time_sec]
    print(max_played)
    for start_time in range(1, play_time_sec):
        end_time = start_time + adv_time_sec if start_time + adv_time_sec < play_time_sec else play_time_sec
        sum_played = total_time[end_time] - total_time[start_time]
        if max_played < sum_played:
            max_played = sum_played
            max_time = start_time + 1

    hour = max_time // 3600
    min = (max_time - hour * 3600) // 60
    sec = (max_time - hour * 3600 - min * 60) 
    result  = "{:02d}:{:02d}:{:02d}".format(hour, min, sec)
    
    return result