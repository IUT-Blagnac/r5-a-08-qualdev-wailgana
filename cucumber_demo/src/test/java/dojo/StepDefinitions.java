package dojo;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertEquals;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;


public class StepDefinitions {

    private Order order;

    @Given("{word} who wants to buy a drink")
    public void someone_who_wants_to_buy_a_drink(String someone) {
        order = new Order();
        order.declareOwner(someone);
    }

    @When("an order is declared for {word}")
    public void an_order_is_declared_for_someone(String someone) {
        order.declareTarget(someone);
    }

    @Then("there is {int} cocktails in the order")
    public void there_is_nb_cocktail_in_the_order(Integer number) {
        List<String> cocktails = order.getCocktails();
        assertEquals((int)number, cocktails.size());
    }
}


