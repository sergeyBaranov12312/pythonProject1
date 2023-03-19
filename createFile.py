for i in range(1,9):
    myfile = open(f'/home/sergo/t{i}.html', 'w')
    myfile.write(
"""<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>t1</title>
    <style>
         p{
            text-align: center;
            text-align: justify;
        }
        h1{
            text-align: justify;
            text-align: center;
        }
        div{
            text-align: justify;
            text-align: center;
        }
    </style>
</head>
<body style="background-image: url('../fon.jpg')">
    <h1>Смартфон1</h1>
    <br>
    <a href="../index.html">На главную</a>
    <br>
    <p>Характеристики</p>
    <p>процессор mediatek</p>
    <p>камера 50мп</p>
    <p>оперативная память 4гб</p>
    <p>price 12000</p>
        <br>
        <br>
    <div>
        <img src="../goods/t1.jpg" width="50%" alt="picture"/>
    </div>

</body>
</html>""")