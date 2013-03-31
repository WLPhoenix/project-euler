import java.io.*;
import java.util.*;

/*
 * This was amazingly easy to brute force...
 */
public class p11 {

	private static int[][] grid = new int[20][20];
	public static void loadData() {
		try {

			Scanner in = new Scanner(new File("p11-grid.txt"));
			for(int i = 0; i < grid.length; i++)
				for(int j = 0; j < grid[i].length; j++) {
					grid[i][j] = in.nextInt();
				}
		} catch (IOException ioe) {
			ioe.printStackTrace();
		}
	}

	public static void main(String[] args) {
		loadData();
		int max = -1;
		int vert = findVerticalMax();
		if (vert > max)
			max = vert;

		int hori = findHorizontalMax();
		if (hori > max)
			max = hori;

		int asc = findAscendingMax();
		if (asc > max)
			max = asc;

		int desc = findDescendingMax();
		if (desc > max)
			max = desc;

		System.out.println(max);
	}

	public static int findVerticalMax() {
		int max = -1;
		for(int i = 0; i < grid.length; i++)
			for(int j = 0; j < (grid[i].length - 3); j++) {
				int temp = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3];
				if (temp > max)
					max = temp;
			}

		return max;
	}

	public static int findHorizontalMax() {
		int max = -1;
		for(int i = 0; i < (grid.length - 3); i++)
			for(int j = 0; j < grid[i].length; j++) {
				int temp = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j];
				if (temp > max)
					max = temp;
			}

		return max;
	}

	public static int findAscendingMax() {
		int max = -1;
		for(int i = 0; i < (grid.length - 3); i++)
			for(int j = 3; j < grid[i].length; j++) {
				int temp = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3];
				if (temp > max)
					max = temp;
			}

		return max;
	}

	public static int findDescendingMax() {
		int max = -1;
		for(int i = 0; i < (grid.length - 3); i++)
			for(int j = 0; j < (grid[i].length - 3); j++) {
				int temp = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3];
				if (temp > max)
					max = temp;
			}

		return max;
	}
}