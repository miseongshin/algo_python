# Q. 멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.

# 노래는 인덱스 구분하며, 노래를 수록하는 기준은 다음과 같다.

# 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.

# 노래의 장르를 나타내는 문자열 배열 genres와
# 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,

# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 1. genres
    # 2. 노래
    # 3. 고유 번호

    genres_tot_play_dic = {}
    genre_index_play_dic={}
    n = len(genre_array)

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre not in genres_tot_play_dic:
            genres_tot_play_dic[genre] = play
            genre_index_play_dic[genre] = [[i,play]]

        else:
            genres_tot_play_dic[genre] +=play
            genre_index_play_dic[genre].append([i,play])

    #print(genres_tot_play_dic, genre_index_play_dic)

    sorted_gen_play_arr = sorted(genres_tot_play_dic.items(),key=lambda items:items[1], reverse=True)

    #print(sorted_gen_play_arr)

    result = []

    for gen, _value in sorted_gen_play_arr:
        index_play_arr = genre_index_play_dic[gen]
        sorted_index_play_arr = sorted(index_play_arr,key=lambda item:item[1],reverse=True)
        #print(sorted_index_play_arr)

        for i in range(len(sorted_index_play_arr)):
            if i >1:
                break
            result.append(sorted_index_play_arr[i][0])

    return result

print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
