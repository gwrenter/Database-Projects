<style type="text/css">
    body{
        background-color: #E0FFFF;
        position:absolute;
        top: 25%;
        left: 30%;
        margin-top: -50px;
        margin-left: -100px;
        text-align: center;
        font-family: Arial,Helvetica,sans-serif;
        font-size: 25px;
    }

    h3{
        color: #191970;
    }
    .php{
        background-color: WhiteSmoke;
        width: 270px;
        margin: auto;
    }
</style>

<html>
<h3>List of the teams with most victories/defeats</h3>
<script>
function homepage(){
    window.open("http://www.csce.uark.edu/~gwrenter/project_python/mainMenu.php","_self");
}
</script>
<body>
<div class="php">
    <?php
        // // replace ' ' with '\ ' in the strings so they are treated as single command line args
        // $University_Name = escapeshellarg($_POST[University_Name]);
        // $Nickname = escapeshellarg($_POST[Nickname]);
        // $Rank = escapeshellarg($_POST[Rank]);

        $command = 'python3 ShowVictories.py';

        // // remove dangerous characters from command to protect web server
        $escaped_command = escapeshellcmd($command);
        //echo "<p>command: $command <p>";
        // run insertTeam.py
        system($escaped_command);
    ?>
</div>
<br></br><br></br>
<input type="button" value="<- Main Menu" onclick="homepage()">
</body>
</html>
