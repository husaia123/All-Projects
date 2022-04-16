import java.util.ArrayList;

/**
 * @author Anwarul Patwary 
 * @version 1.00 01 April 2022
 */
public class Product
{
    // instance variables 
    private String product_id;
    private double discount;
    private double price;
    private String store_id;
    private String prod_category;
    

    /**
     * Constructor for objects of class Product
     * Initialise instance variables
     */
    public Product(String product_details)
    {
        //splits itemdetails (rows) into 5 
        String[] itemDetails = product_details.split(" ", 5);
        product_id = itemDetails[0];
        price = new Double (itemDetails[1]);
        discount = new Double(itemDetails[2]);
        store_id = itemDetails[3];
        prod_category = itemDetails[4];
    }
    
    /**
     * Return the product ID
     */
    public String getProductID(){
        return product_id;
    }
    
    /**
     * Return the product price
     */
    
    public double getPrice(){
        return price;
    }
    
    /**
     * Return the discount of a product 
     */
    public double getDiscount(){
        return discount;
    }
    
    /**
    * Return the category of a product 
    */ 
    public String getCategory(){
        return prod_category;
    }
    
    /**
     * Return the store ID of a product 
     */
       public String getStoreID(){
        return store_id;
    }
}
