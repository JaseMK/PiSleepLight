<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>
</head>

<body>


<p>
	<?php
// Connecting, selecting database
$link = mysql_connect('localhost', 'username', 'password')
    or die('Could not connect: ' . mysql_error());
//echo 'Connected successfully';
mysql_select_db('jasemk_sleeplight') or die('Could not select database');

// Performing SQL query
$query = 'SELECT name, value FROM flags';
$result = mysql_query($query) or die('Query failed: ' . mysql_error());

// Printing results in HTML
echo "<table>\n";
while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
    echo "\t<tr>\n";
    foreach ($line as $col_value) {
        echo "\t\t<td>$col_value</td>\n";
    }
    echo "\t</tr>\n";
}
echo "</table>\n";

// Free resultset
mysql_free_result($result);

// Closing connection
mysql_close($link);
?>
	</p>
<p><img src="img/red_on.png" width="106" height="106" /></p>
<p>&nbsp;</p>
<img src="img/green_off.png" width="106" height="106" />
</body>
</html>
