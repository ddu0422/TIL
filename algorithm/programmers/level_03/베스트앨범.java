import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Songs> results = new HashMap<>();

        for (String genre : genres) {
            results.put(
                    genre,
                    new Songs(new ArrayList<>())
            );
        }

        for (int i = 0; i < genres.length; i++) {
            results.get(genres[i]).add(new Song(i, plays[i]));
        }

        return results.values().stream()
                .sorted(Comparator.comparing(Songs::sum).reversed())
                .map(Songs::getSongs)
                .flatMap(Collection::stream)
                .mapToInt(Integer::intValue)
                .toArray();
    }

    private static class Songs {

        private final List<Song> songs;

        public Songs(List<Song> songs) {
            this.songs = songs;
        }

        public void add(Song song) {
            this.songs.add(song);
        }

        public int sum() {
            return songs.stream()
                    .mapToInt(Song::getPlayCount)
                    .sum();
        }

        public List<Integer> getSongs() {
            return songs.stream()
                    .sorted(
                            Comparator.comparing(Song::getPlayCount).reversed()
                                    .thenComparing(Song::getId)
                    )
                    .map(Song::getId)
                    .limit(2)
                    .collect(Collectors.toUnmodifiableList());
        }
    }

    private static class Song {

        private final int id;
        private final int playCount;

        public Song(int id, int playCount) {
            this.id = id;
            this.playCount = playCount;
        }

        public int getId() {
            return id;
        }

        public int getPlayCount() {
            return playCount;
        }
    }
}