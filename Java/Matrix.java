import java.util.Scanner;

public class Matrix {
    static void Matrix_Operation(int mat1[][], int mat2[][], int r, int c, String op) {
        int i;
        int j;
        if (op == "+") {
            int[][] mat_res = new int[10][10];
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    mat_res[i][j] = mat1[i][j] + mat2[i][j];
                }
            }
            System.out.println("Addition result:");
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    System.out.print(mat_res[i][j] + " ");
                }
                System.out.println("");
            }

        } else if (op == "-") {
            int[][] mat_res = new int[10][10];
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    mat_res[i][j] = mat1[i][j] - mat2[i][j];
                }
            }
            System.out.println("Substraction result:");
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    System.out.print(mat_res[i][j] + " ");
                }
                System.out.println("");
            }
        } else if (op == "x") {
            int[][] mat_res = new int[10][10];
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    for (int k = 1; k <= r; k++) {
                        mat_res[i][j] += mat1[i][k] + mat2[k][j];
                    }
                }
            }
            System.out.println("Multiplication result:");
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    System.out.print(mat_res[i][j] + " ");
                }
                System.out.println("");
            }
        } else {
            int[][] mat_res = new int[10][10];
            int[][] mat_res2 = new int[10][10];
            for (i = 0; i <= r; i++) {
                for (j = 0; j <= c; j++) {
                    mat_res[i][j] = mat1[j][i];
                }
            }
            System.out.println("Transpose of Matrix A:");
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    System.out.print(mat_res[i][j] + " ");
                }
                System.out.println("");
            }
            for (i = 0; i <= r; i++) {
                for (j = 0; j <= c; j++) {
                    mat_res2[i][j] = mat2[j][i];
                }
            }
            System.out.println("Transpose of Matrix B:");
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    System.out.print(mat_res2[i][j] + " ");
                }
                System.out.println("");
            }
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int[][] matrix1 = new int[10][10];
        int[][] matrix2 = new int[10][10];
        int row;
        int col;
        System.out.println("Enter Row and Column of both matrices:");
        row = sc.nextInt();
        col = sc.nextInt();
        System.out.println("Enter elements for matrix1:");
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                matrix1[i][j] = sc.nextInt();
            }
        }
        System.out.println("Matrix 1:");
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                System.out.print(matrix1[i][j] + " ");
            }
            System.out.println("");
        }
        System.out.println("Enter elements for matrix2:");
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                matrix2[i][j] = sc.nextInt();
            }
        }
        System.out.println("Matrix 2:");
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                System.out.print(matrix2[i][j] + " ");
            }
            System.out.println("");
        }
        System.out.println("1.Addition \n2.Substraction \n3.Multiplication \n4.Transpose");
        System.out.println("Enter Choice(1-4):");
        int ch = sc.nextInt();
        switch (ch) {
            case 1:
                Matrix_Operation(matrix1, matrix2, row, col, "+");
                break;
            case 2:
                Matrix_Operation(matrix1, matrix2, row, col, "-");
                break;
            case 3:
                Matrix_Operation(matrix1, matrix2, row, col, "x");
                break;
            case 4:
                Matrix_Operation(matrix1, matrix2, row, col, "t");
                break;
            default:
                System.out.println("Wrong Choice!");
        }
    }

}
