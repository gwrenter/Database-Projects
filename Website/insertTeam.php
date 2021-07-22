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
<h3>Enter information about a team to add to the database:</h3>
<script>
function homepage(){
    window.open("http://www.csce.uark.edu/~gwrenter/project_python/mainMenu.php","_self");
}
</script>
<form action="insertTeam.php" method="post">
    University Name: <input type="text" name="University_Name"><br>
    Nickname: <input type="text" name="Nickname"><br>
    Rank: <input type="number" name="Rank"><br><br><br>
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
    $University_Name = escapeshellarg($_POST[University_Name]);
    $Nickname = escapeshellarg($_POST[Nickname]);
    $Rank = escapeshellarg($_POST[Rank]);

    $command = 'python3 insertTeam.py' . ' '.  $University_Name . ' ' . $Nickname . ' ' . $Rank;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    //echo "<p>command: $command <p>";
    // run insert_new_item.py
    system($escaped_command);
}
?>


