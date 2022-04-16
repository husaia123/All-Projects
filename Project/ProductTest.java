

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * The test class ProductTest.
 *
 * @author Anwarul Patwary 
 * @version 1.00 01 April 2022
 */
public class ProductTest
{
    /**
     * Default constructor for test class ProductTest
     */
    private Product p;
    
    public ProductTest()
    {
    }

    /**
     * Sets up the test fixture.
     *
     * Called before every test case method.
     */
    @BeforeEach
    public void setUp()
    {
        p = new Product("P10982 21 5.3 S0198 veg");
    }

@Test
public void testgetproductID(){

assertEquals("P10982", p.getProductID());

}

@Test
public void testgetPrice(){
assertEquals(21.0, p.getPrice());
}

@Test
public void testgetDiscount(){
assertEquals(5.3, p.getDiscount());
}

@Test
public void testgetCategory(){
assertEquals("veg", p.getCategory());
}


@Test
public void testgetStoreID(){
assertEquals("S0198", p.getStoreID());
}
}
