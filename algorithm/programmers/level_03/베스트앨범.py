def solution(genres, plays):
    answer = []
    dictionary = dict()

    for genre in genres:
        dictionary[genre] = []

    for index, value in enumerate(plays):
        dictionary[genres[index]].append([index, value])

    dictionary = sorted(dictionary.items(), key=lambda x: -sumPlays(x[1]))

    for value in dictionary:
        songs = sorted(value[1], key=lambda x: (-x[1], x[0]))
        for song in songs[:2]:
            answer.append(song[0])

    return answer


def sumPlays(songs):
    result = 0

    for song in songs:
        result += song[1]

    return result
