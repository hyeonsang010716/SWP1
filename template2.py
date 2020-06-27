def get_template(x,y):
    try:
        sum = x + y
        mul = x * y
        return """
<html>
    <body>
        <form action="">
            x = <input type="number" name="x">
            y = <input type="number" name="y">
              <br><br>
            <input type="submit">
        </form>
        {}
        {}
    </body>
</html>
""".format("sum="+str(sum), "mul="+str(mul))

    except:
        return """
<html>
    <body>
        <form action="">
            x = <input type="number" name="x">
            y = <input type="number" name="y">
                <br><br>
            <input type="submit">
        </form>
    </body>
</html>
"""
