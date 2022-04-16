import java.util.ArrayList;
import java.util.Random;
import java.util.Arrays;


/**
 *
 * @author Anwarul Patwary 
 * @version 1.00, 01 April 2022
 */
public class Order
{
    // instance variables 
    private FileReader file;
    private ArrayList<Product> product_list; 
    private String orderID;
    private double total_price;
    private double total_discount; 
    private String invoice_reference;
    private int total_item;
    
    /**
     * 1) Constructor for objects of class Order
     * 2) Initialise instance variables
     * 3) Provide the input file name and first letter of your first name and last as an order ID
     * e.g ("input.txt" "CP") CP for Collin Peter
     * 4) Get the list of lines from fileReader class. Create anonymous Product type of objects, then add them into product_list. 
       */
    
    public Order(String fileName, String order_id)
    {
        orderID = order_id;
        total_price = 0.0;
        total_discount = 0.0;
        invoice_reference = "";
        total_item = 0;
        
        product_list = new ArrayList<Product>();
        file = new FileReader(fileName);
        
        for (String row: file.getLines()){
            //loops through lines from .txt and adds as a Product type
            product_list.add(new Product(row));
        }
    }

    /**
     * Generate invoice ID using OrderID and random generated value. String concatenation is applicable here. 
     * if orderID = "AN", and random value is 18. 
     * example output: AN18
     */

    public String generateInvoice(){
        Random ran = new Random();
        int randomNum = ran.nextInt(100) + 1;
        //random int from 1-100
        
        invoice_reference = orderID + Integer.toString(randomNum);
        //adds ID to ranInt (AH45)
        return invoice_reference;
    }

    /**
     * 1) This method must communicate with Product class
     * 2) The method should be able to place the order using product id and unit. It will take one product item at a time. 
     * 3) Calculate the total payable amount by the customer
     * 4) To place multiple orders method should be able to get called multiple times. The total price and total discount will be accumulated to the field variable total_price total_discount respectively.
     * 5) Return the accumulated total price from this method
     * @param e.g prod_id = "P10982" and unit = 2
     * 6) Return the value with two decimal places. For Example: from 19.887 to 19.89
     */
    public double placeOrder(String prod_id, int unit){
        for (Product item: product_list){
            if (item.getProductID().equals(prod_id)) {
                    total_item += unit;
                    // total = unit*(discount total)
                    total_price += unit*(item.getPrice()*(1-(item.getDiscount()/100)));
                    // discount = unit*(discounted amount)
                    total_discount += unit*(item.getPrice()*item.getDiscount()/100);
                }
            }
        total_price = Math.round(total_price*100.0)/100.0;
        return (total_price);
    }
    
    /**
     * 1) This method must communicate with Product class
     * 2) Return the accumulated total price after placing the order. 
     * 3) Return the value with two decimal places. For Example: from 19.887 to 19.89
     */
    public double getTotalPrice() { 
        return total_price;
    }

    /**
     * 1) This method must communicate with Product class
     * 2) Get the accumulated total amount of discount that has been applied after placing the order.
     * 3) Return the value with two decimal places. For Example: from 1.113 to 1.11
     */

    public double getTotalDiscount(){
        return  Math.round(total_discount*100.0)/100.0;
    }

    /**
     * Return total number of items ordered by a customer
     */
    public int getTotalItem(){
        return total_item;
    }

    /**
     * print orders in the follwing format. 
     * *******Order Details*******
     * Invoice Number: AN43
     * Total items :2
     * Amount Payable: 36.7
     * Discount Applied: 2.4
     */

    public void printOrder(){
       System.out.println("*******Order Details*******\n"
                        + "Invoice Number: " + generateInvoice() + "\n"
                        + "Total items: " + getTotalItem() + "\n"
                        + "Amount Payable: "+ getTotalPrice() + "\n"
                        + "Discount Applied: " + getTotalDiscount() + "\n");
    }
  
}
