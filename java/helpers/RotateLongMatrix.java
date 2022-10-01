package helpers;

public class RotateLongMatrix {
    public static void rotate(long[][] matrix) {
        int rows = matrix.length;
        int columns = matrix[0].length;

        //William's algorithm? Not confusing at all...
        for (int i = 0; i < rows/2; i++) {
            for (int j = 0; j < (columns-2*i-1); j++) {
                long tmp = matrix[i][i+j];
                matrix[i][i+j] = matrix[rows-1-i-j][i];
                matrix[rows-1-i-j][i] = matrix[rows-1-i][columns-1-i-j];
                matrix[rows-1-i][columns-1-i-j] = matrix[i+j][columns-1-i];
                matrix[i+j][columns-1-i] = tmp;
            }
        }
    }
}
