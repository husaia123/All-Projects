import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * The test class OrderTest.
 *
 * @author Anwarul Patwary 
 * @version 1.00 01 April 2022
 */
public class OrderTest
{
    /**
     * Default constructor for test class OrderTest
     */
    private Order order;
    public OrderTest()
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
       order =new Order("input.txt", "AN"); 
    }

    /**
     * Tears down the test fixture.
     *
     * Called after every test case method.
     */
    
    @Test
    public void testplaceOrder(){
    
    assertEquals(39.77, order.placeOrder("P10982" , 2));
    }
    
    @Test
    public void testgetTotalPrice(){
    assertEquals(39.77,order.placeOrder("P10982" , 2) );
    assertEquals(39.77,order.getTotalPrice() );
    }
    @Test
    public void testgetTotalDiscount(){
    assertEquals(39.77,order.placeOrder("P10982" , 2) );
    assertEquals(2.23, order.getTotalDiscount());
    }
    
    @Test
    public void testTotalItem(){
    
    assertEquals(39.77,order.placeOrder("P10982" , 2) );
    assertEquals(2, order.getTotalItem()); 
    }
    
}
