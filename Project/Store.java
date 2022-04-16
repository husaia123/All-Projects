import java.util.ArrayList;
import java.util.Collections;

/**
 * @author Anwarul Patwary 
 * @version 1.00, 01 April 2022
 */
public class Store
{
    // instance variables 
    private FileReader file;
    private ArrayList<Product> listOfproduct;

    /**
     * 1) Constructor for objects of class Store
     * 2) Initialise instance variables
     * 2) Get the list of line from fileReader class. Create anonymous Product type of objects, then add them into listOfproduct.
     */
    
    public Store(String fileName)
    {
        file = new FileReader(fileName);
        listOfproduct = new ArrayList<>();
        
        for (String row: file.getLines()){
            // loops through lines from .txt and adds as a Product type
            listOfproduct.add(new Product(row));
        }
    }

    /**
     * 1)Find the most expensive product of a category.
     * @param e.g. "veg"
     * 2)Return the product id of the product.
     */
    public String expensiveItem(String prod_category)
    {
        double max_price = 0.0;
        String prodID = "";
        
        for (Product item: listOfproduct){
            if (item.getCategory().equals(prod_category) && max_price < item.getPrice()){
                //if category equals and prev max price is less than item price 
                max_price = item.getPrice();
                //change max price to new max price (item price)
                prodID = item.getProductID();
                //ID of max price item
            }
        }
        return prodID;
    }

    /**
     * 1) Find the most expensive product of a category from a particular store.
     * 2) Return the product id and price of a product. Return the value in a single line as a string using string concatenation. 
     * Example output: P10982,21.0
     */

    public String expensiveItemStore(String prod_category, String store_id){
        double max_price = 0;
        String prodID = "";

        for (Product item: listOfproduct){
            if (item.getCategory().equals(prod_category) && item.getStoreID().equals(store_id)){
                if (max_price < item.getPrice()){
                    max_price = item.getPrice();
                    prodID = item.getProductID();
                }
            }
        }
        
        return (prodID + "," + max_price);
    }

    /**
     * 1) Find the list of product and price which price is between "min" and "max". 
     * @param e.g min = 2, and max =10. 
     * 2) Return the list in an accumulated string using string concatenation.
     * 3) The list should be a String type, each product details seperate by a new line using "\n".  
     * 4) Throw an exception for a negative argument and "min" must not be greater than "max" value.
     * 
     * An example of returning list:
     * P10082,4.71
     * P10032,3.54
     */

    public String findProduct(int min, int max) {
        String in_between = "";
        if (min > max || min < 0){
            throw new IllegalArgumentException("Max should be greater than min and both not negative");
        } else{
            for (Product item: listOfproduct){
                if (min < item.getPrice() &&  item.getPrice() < max){
                    //adds ID and price if price in between min and max
                    in_between += item.getProductID() + "," + item.getPrice() + "\n";
                }
            }
        }
        
        return in_between;
    } 

    /**
     * Use the prod_id to check the price of that product. Throw an exception if no product matches the product id.
     * @param e.g "P10982"
     */
    public double checkPrice(String prod_id){
        for (Product item: listOfproduct){
            if (item.getProductID().equals(prod_id)){
                //if productID matches searched id return price
                return item.getPrice();
            } 
        }
        throw new IllegalArgumentException("No matching " + prod_id + " product id");
    }

    /**
     * 1) Find the list of products in a store using a store ID. Return the product id and price using an ArrayList of String type
     * 2) Throw an exception if no store matches the store id.
     * @param e.g store_id = "S0198"
     * Example output: 
     * P10082,4.71
     * P10032,3.54
     */

    public ArrayList<String> getproductbyStoreID(String store_id){
        ArrayList<String> storeProducts = new ArrayList<String>();
        for (Product item: listOfproduct){
            if (item.getStoreID().equals(store_id)){
                //if store id equals, adds id and price to array
                storeProducts.add(item.getProductID() + "," + item.getPrice());
            } 
        }
        
        if (storeProducts.size() == 0){
            //if nothing has been added throw exception
            throw new IllegalArgumentException("No matching " + store_id + " store id");
        }
        return storeProducts;
    }

    /**
     * 1) Get the average cost of an item in an item category.
     * @param e.g "veg"
     * 2) Throw an exception in calculating the average that a value can not be divided by zero.
     * 3) Return the value with two decimal places. For Example: from 19.887 to 19.89
     */

    public double averageCost(String prod_category){
        double totalCategoryPrice = 0.0;
        int itemCategory = 0;
        for (Product item: listOfproduct){
            if (item.getCategory().equals(prod_category)){
                totalCategoryPrice += item.getPrice();
                //adds single item price to total price
                itemCategory++;
                //+1 to total amount of items
            }
        }
        
        if (itemCategory == 0){
            throw new IllegalArgumentException("No matching " + prod_category + " category");
        }
        
        return Math.round(totalCategoryPrice/itemCategory*100.0)/100.0;
    }
}

