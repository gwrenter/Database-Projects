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
<h3>Enter information about a game result to add to the database:</h3>
<script>
function homepage(){
    window.open("http://www.csce.uark.edu/~gwrenter/project_python/mainMenu.php","_self");
}
</script>
<form action="insertResult.php" method="post">
    Game ID: <input type="number" name="GameID"><br>
    Team One ID: <input type="number" name="TeamOneId"><br>
    Team Two ID: <input type="number" name="TeamTwoId"><br>
    Score One: <input type="number" name="ScoreOne"><br>
    Score Two: <input type="number" name="ScoreTwo"><br><br><br>
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
    $GameID = escapeshellarg($_POST[GameID]);
    $TeamOneId = escapeshellarg($_POST[TeamOneId]);
    $TeamTwoId = escapeshellarg($_POST[TeamTwoId]);
    $ScoreOne = escapeshellarg($_POST[ScoreOne]);
    $ScoreTwo = escapeshellarg($_POST[ScoreTwo]);

    $command = 'python3 insertResult.py' . ' '.  $GameID . ' ' . $TeamOneId . ' ' . $TeamTwoId . ' ' . $ScoreOne . ' ' . $ScoreTwo;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    //echo "<p>command: $command <p>";
    // run insertResult.py
    system($escaped_command);           
}
?>


