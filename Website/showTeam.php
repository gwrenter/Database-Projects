<style type="text/css">
    body{
        background-color: #E0FFFF;
        position:absolute;
        top: 25%;
        left: 45%;
        margin-top: -50px;
        margin-left: -100px;
        text-align: left;
        font-family: Arial,Helvetica,sans-serif;
        font-size: 25px;
    }

    h3{
        color: #191970;
    }

    .php{
        background-color: WhiteSmoke;
    }

</style>

<html>
<body>
<h3>List of all teams</h3>
<script>
function homepage(){
    window.open("http://www.csce.uark.edu/~gwrenter/project_python/mainMenu.php","_self");
}
</script>

<div class="php">
    <?php
        $command = 'python3 showTeam.py';

        // // remove dangerous characters from command to protect web server
        $escaped_command = escapeshellcmd($command);
        //echo "<p>command: $command <p>";
        // run showTeam.py
        system($escaped_command);
    ?>
</div>
<br></br><br></br>
<input type="button" value="<- Main Menu" onclick="homepage()">
</body>
</html>

