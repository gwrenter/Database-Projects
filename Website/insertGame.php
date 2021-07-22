
<style type="text/css">
    body{
        background-color: #E0FFFF;
        position:absolute;
        top: 25%;
        left: 30%;
        margin-top: -50px;
        margin-left: -100px;
        text-align: left;
        font-family: Arial,Helvetica,sans-serif;
        font-size: 25px;
    }

    h3{
        color: #191970
    }
</style>

<html>
<body>
<h3>Enter information about a game fixture to add to the database:</h3>
<script>
function homepage(){
    window.open("http://www.csce.uark.edu/~gwrenter/project_python/mainMenu.php","_self");
}
</script>
<form action="insertGame.php" method="post">
    Rank Team 1: <input type="number" name="Rank1"><br>
    Rank Team 2: <input type="number" name="Rank2"><br>
    Location: <input type="text" name="Location"><br>
    Date: <input type="date" name="Date"><br><br><br>
    <input name="submit" type="submit" ><br><br><br><br>
    <input type="button" value="<- Main Menu" onclick="homepage()">
</form>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $Rank1 = escapeshellarg($_POST[Rank1]);
    $Rank2 = escapeshellarg($_POST[Rank2]);
    $Location = escapeshellarg($_POST[Location]);
    $Date = escapeshellarg($_POST[Date]);

    $command = 'python3 insertGame.py' . ' '.  $Rank1 . ' ' . $Rank2 . ' ' . $Location . ' ' . $Date;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    //echo "<p>command: $command <p>"; 
    // run insertGame.py
    system($escaped_command);           
}
?>


