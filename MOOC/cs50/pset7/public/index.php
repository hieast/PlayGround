<?php

    // configuration
    require("../includes/config.php"); 


    $rows = CS50::query("SELECT symbol, shares FROM portfolios WHERE user_id = ?", $_SESSION["id"]);
    $positions = [];
    foreach ($rows as $row)
    {
        $stock = lookup($row["symbol"]);
        if ($stock !== false)
        {
            $positions[] = [
                "name" => $stock["name"],
                "price" => $stock["price"],
                "shares" => $row["shares"],
                "symbol" => $row["symbol"]
            ];
        }
        else
        {
            apologize("Symbol not found.");
        }
    }
    
    $user = CS50::query("SELECT username, cash FROM users WHERE id = ?", $_SESSION["id"]);
    
    
    // render portfolio
    render("portfolio.php", ["user" => $user, "positions" => $positions, "title" => "Portfolio"]);
?>
