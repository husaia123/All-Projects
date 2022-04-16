import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;

/**
 * The test class StoreTest.
 *
 * @author Anwarul Patwary 
 * @version 1.00 01 April 2022
 */
public class StoreTest
{
    /**
     * Default constructor for test class StoreTest
     */
    private Store store;
    public StoreTest()
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
        store = new Store("input.txt"); 
    }

    @Test
    public void testexpensiveItem(){
        assertEquals("P10982", store.expensiveItem("veg"));

    }

    @Test
    public void testexpensiveItemStore(){
        assertEquals("P10982,21.0", store.expensiveItemStore("veg", "S0198"));

    }

    @Test
    public void testfindProduct(){

        assertEquals("P10082,4.71\nP10032,3.54\n", store.findProduct(3, 10)); 

    }
    @Test
    public void testcheckprice(){

        assertEquals(21, store.checkPrice("P10982"));

    }

    @Test 
    public void testgetproductbyStoreID(){

        ArrayList<String> name = new ArrayList<>();
        name.add("P10982,21.0");
        name.add("P10761,29.5");
        name.add("P10972,1.89");
        assertEquals(name,store.getproductbyStoreID("S0198")); 

    }

    @Test
    public void testaverageCost(){

        assertEquals(11.45, store.averageCost("veg"));
    }

}
