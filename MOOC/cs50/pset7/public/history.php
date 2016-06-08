<?php

    // configuration
    require("../includes/config.php"); 

    $rows = CS50::query("SELECT transaction, time, symbol, shares, price FROM history WHERE user_id = ?", $_SESSION["id"]);
    if (empty($rows))
    {
        apologize("No history data.");
    }
    
    $positions = [];
    foreach ($rows as $row)
    {
            $positions[] = [
                "transaction" => $row["transaction"],
                "time" => $row["time"], 
                "symbol" => $row["symbol"],
                "shares" => $row["shares"],
                "price" => $row["price"]
            ];

    }
    // render history
    render("history.php", ["positions" => $positions, "title" => "History"]);
?>
