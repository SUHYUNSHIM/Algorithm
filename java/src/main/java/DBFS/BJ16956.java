package DBFS;
import java.io.*;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class Pair {
    int r, c;
    Pair(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

public class BJ16956 {
    static BufferedReader br;
    static BufferedWriter bw;
    static StringTokenizer st;
    static StringBuilder sb;
    static Queue<Pair> que;

    static int n, m;
    static boolean isPossible = true;
    static char[][] map;
    static boolean[][] check;
    static int[] rArr = {-1, 1, 0, 0};
    static int[] cArr = {0, 0, -1, 1};

    public static void bfs() {
        while(!que.isEmpty()) {
            Pair p = que.poll();

            for(int i = 0; i < 4; i++) {  // 상하좌우 검사
                int nr = p.r + rArr[i];
                int nc = p.c + cArr[i];

                if(-1 < nr && nr < n && -1 < nc && nc < m && !check[nr][nc]) {  // 범위, 방문여부 검사
                    if(map[nr][nc] == '.') {
                        map[nr][nc] = 'D';
                    }else if(map[nr][nc] == 'S') {
                        isPossible = false;
                        return;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();
        que = new ArrayDeque<>();

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new char[n][m];
        check = new boolean[n][m];

        for(int i = 0; i < n; i++) {
            String input = br.readLine();
            for(int j = 0; j < m; j++) {
                char ch = input.charAt(j);
                map[i][j] = ch;
                if(ch == 'W') {
                    que.add(new Pair(i, j));
                    check[i][j] = false;
                }
            }
        }

        bfs();

        if(isPossible) {
            sb.append("1\n");
            for(int i = 0; i < n; i++) {
                for(int j = 0; j < m; j++) {
                    sb.append(map[i][j]);
                }
                sb.append("\n");
            }
        }else {
            sb.append("0");
        }
        bw.write(sb.toString());
        br.close();
        bw.close();
    }
}