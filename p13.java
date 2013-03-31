import java.io.*;
import java.util.*;
import java.math.*;

public class p13 {

	public static List<BigInteger> loadData() {

		List<BigInteger> nums = new ArrayList<BigInteger>();

		try {

			Scanner in = new Scanner(new File("p13-data.txt"));
			while (in.hasNextLine()) {
				String temp = in.nextLine();
				BigInteger num = new BigInteger(temp);
				nums.add(num);
			}
			System.out.println("Loading succeeded.");
		} catch (IOException ioe) {
			ioe.printStackTrace();
		}

		return nums;
	}

	public static void main(String[] args) {
		List<BigInteger> nums = loadData();
		
		BigInteger total = new BigInteger("0");
		for(BigInteger num : nums) {
			total = total.add(num);
		}
		String totalString = total.toString();
		System.out.println(totalString.substring(0, 10));
	}
}