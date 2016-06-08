<?php

    // configuration
    require("../includes/config.php"); 

    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // else render form
        render("buy_form.php", ["title" => "Buy"]);
    }
    
    // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        if (empty($_POST["symbol"]))
        {
            apologize("You must specify a stock to buy.");
        }
        else if (empty($_POST["shares"]))
        {
            apologize("You must specify a number of shares.");
        }
        else if (!preg_match("/^\d+$/", $_POST["shares"]))
        {
            apologize("Shares must be an integer.");
        }
        $stock = lookup($_POST["symbol"]);
        if (empty($stock))
        {
            apologize("Symbol not found.");
        }
        
        $rows = CS50::query("SELECT cash FROM users WHERE id = ? ", $_SESSION["id"]);
        if ($rows[0]["cash"] < $stock["price"] * $_POST["shares"])
        {
            apologize("You can't afford that.");
        }
        
        $result1 = CS50::query("INSERT INTO portfolios (user_id, symbol, shares) VALUES(?, ?, ?) ON DUPLICATE KEY UPDATE shares = shares + ?", $_SESSION["id"], $stock["symbol"], $_POST["shares"], $_POST["shares"]);
        $result2 = CS50::query("UPDATE users SET cash = cash - ? WHERE id = ?", $_POST["shares"] * $stock["price"] ,$_SESSION["id"]);
        $result3 = CS50::query("INSERT INTO history (user_id, transaction, symbol, shares, price) VALUES(?, 'BUY', ?, ?, ?)", $_SESSION["id"], $stock["symbol"], $_POST["shares"], $stock["price"]);
        if ($result1 !== 0 && $result2 !== 0)
        {
            // redirect portfolio
            redirect("/");
        }

        else if($result1 == 0 && $result2 !== 0)
        {
            apologize("INSERT goes wrong.");
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