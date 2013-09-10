import java.util.Scanner;
        
public class Exercise {
    static void main(String[] args) {
        
	Scanner scnr = new Scanner(System.in);
        String houseType = "Unknown";
        int choice = 0;

        System.out.println("Enter the type of house you want to purchase");
        System.out.println("1. Single Family");
        System.out.println("2. Townhouse");
        System.out.println("3. Condominium");
        System.out.print("Your Choice? ");
        choice = scnr.nextInt();

        if (choice == 1)
            houseType = "Single Family";
        if (choice == 2)
            houseType = "Townhouse";
        if (choice == 3)
            houseType = "Condominium";

        System.out.println("Desired House Type: " + houseType);
   }
}