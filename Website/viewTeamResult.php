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

    .php{
        background-color: WhiteSmoke;
    }
</style>

<html>
<body>
<h3>Enter a university team name to view all the results this season:</h3>
<script>
function homepage(){
    window.open("http://www.csce.uark.edu/~gwrenter/project_python/mainMenu.php","_self");
}
</script>
<form action="viewTeamResult.php" method="post">
    University name: <input type="text" name="University_Name"><br><br><br>
    <input name="submit" type="submit" ><br><br><br><br>
    <input type="button" value="<- Main Menu" onclick="homepage()">
</form>
<br><br>
<div class="php">
    <?php
    if (isset($_POST['submit']))
    {
        // replace ' ' with '\ ' in the strings so they are treated as single command line args
        $University_Name = escapeshellarg($_POST[University_Name]);

        $command = 'python3 viewTeamResult.py' . ' ' .  $University_Name;

        // remove dangerous characters from command to protect web server
        $escaped_command = escapeshellcmd($command);
        //echo "<p>command: $command <p>";
        // run viewTeamResult.py
        system($escaped_command);
    }
    ?>
</div>
</body>
</html>


