genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# 2. 장르 내에서 많이 재생된 노래를 먼적 수록한다.
# 3. 장르 내에서 재생횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
# 노래의 장르 를 나타내는 문자배열 genres
# 노래별 재생횟수를 나타내는 정수배열 plays
# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.
# 장르별 두곡
def get_melon_best_album(genre_array, play_array):
    genres_tot_play_dic = {}
    genre_index_play_dic = {}
    n = len(genre_array)

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genres_tot_play_dic:
            genres_tot_play_dic[genre] = play
            genre_index_play_dic[genre] = [[i, play]]
        else:
            genres_tot_play_dic[genre] += play
            genre_index_play_dic[genre].append([i, play])

    # print(genres_tot_play_dic)
    # print(genre_index_play_dic)

    sorted_gen_play_arr = sorted(genres_tot_play_dic.items(), key=lambda item: item[1], reverse=True)  # 첫번째 값으로 정렬.
    #print(sorted_gen_play_arr)

    result = []
    for gen, _value in sorted_gen_play_arr:
        # [[1, 600], [[4, 2500]]
        index_play_arr = genre_index_play_dic[gen]
        sorted_index_play_arr = sorted(index_play_arr, key=lambda item: item[1], reverse=True)
        print(sorted_index_play_arr)

        for i in range(len(sorted_index_play_arr)):
            if i > 1:
                break
            result.append(sorted_index_play_arr[i][0])
    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
