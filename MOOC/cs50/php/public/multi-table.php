<!DOCTYPE html>
<html>
    <head>
        <title>multit-table</title>
        <link rel="stylesheet" href="../css/table.css" type="text/css" />
    </head>
    <body>

        <table>
            <th colspan="<?= ($_POST["maxnum"]); ?>">The input is <?= ($_POST["maxnum"]); ?></th>
            <?php
                for($row = 0; $row < $_POST["maxnum"]; $row++)
                {
                    echo ("<tr>");
                    for($col = 0; $col < $_POST["maxnum"]; $col++)
                    {
                        $product = ($row + 1) * ($col + 1);
                        echo("<td> {$product} </td>");
                    }
                    echo ("</tr>");
                }
            ?>
            

        </table>
    </body>
</html>

