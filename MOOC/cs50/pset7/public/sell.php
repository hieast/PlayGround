<?php

    // configuration
    require("../includes/config.php"); 

    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        $positions = CS50::query("SELECT symbol FROM portfolios WHERE user_id = ?", $_SESSION["id"]);

        // else render form
        render("sell_form.php", ["positions" => $positions, "title" => "Sell"]);
    }
    
    // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        if (empty($_POST["symbol"]))
        {
            apologize("No share to sell.");
        }
        $rows = CS50::query("SELECT symbol, shares FROM portfolios WHERE user_id = ? and symbol = ?", $_SESSION["id"], $_POST["symbol"]);
        $stock = lookup($_POST["symbol"]);
        $result1 = CS50::query("DELETE FROM portfolios WHERE user_id = ? AND symbol = ?", $_SESSION["id"], $_POST["symbol"]);
        $result2 = CS50::query("UPDATE users SET cash = cash + ? WHERE id = ?", $rows[0]["shares"] * $stock["price"] ,$_SESSION["id"]);
        $result3 = CS50::query("INSERT INTO history (user_id, transaction, symbol, shares, price) VALUES(?, 'SELL', ?, ?, ?)", $_SESSION["id"], $stock["symbol"], $rows[0]["shares"], $stock["price"]);
        
        
        if ($result1 !== 0 && $result2 !== 0)
        {
            // redirect portfolio
            redirect("/");
        }

        else if($result1 == 0 && $result2 !== 0)
        {
            apologize("DELETE goes wrong.");
        }
        else if($result1 !== 0 && $result2 == 0)
        {
            apologize("UPDATE goes wrong.");
        }
        else
        {
            pologize("Both DELETE and UPDATE go wrong.");
        }
        
    }
?>