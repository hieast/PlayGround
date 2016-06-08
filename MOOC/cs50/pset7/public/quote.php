<?php

    // configuration
    require("../includes/config.php");
    
    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // else render form
        render("quote_form.php", ["title" => "Get Quote"]);
    }
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        //validate submission
        if (empty($_POST["symbol"]))
        {
            apologize("You must provide stock symbol.");
        }
        $stock = lookup($_POST["symbol"]);
        if (empty($stock))
        {
            apologize("Symbol not found.");
        }
       
        render("quote_answer.php", ["title" => "Quote", "stock" => $stock]);
    }
?>