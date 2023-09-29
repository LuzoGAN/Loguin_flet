from flet import *

body = Container(
        Container(
        Stack([
            Container(
                border_radius=11,
                rotate=Rotate(0.98*3.14), #degrau
                width=360,
                height=560,
                bgcolor='#22ffffff',
            ),
            Container(
                Container(
                    Column([
                        Container(
                            Image(
                            src='logo.png',
                            width=60,
                            ),padding=padding.only(150,20),
                        ),
                        Text(
                            "Sign in",
                            width=360,
                            size=30,
                            weight='w900',
                            text_align='center',
                        ),
                        Text(
                            "Logue na plataforma",
                            width=360,
                            text_align='center',
                        ),
                        Container(
                            TextField(
                                width=280,
                                height=40,
                                hint_text='Login',
                                border='underline',
                                color='#303030',
                                prefix_icon= icons.EMAIL,
                            ),padding=padding.only(25,20),
                        ),
                        Container(
                            TextField(
                                width=280,
                                height=40,
                                hint_text='Senha',
                                border='underline',
                                color='#303030',
                                prefix_icon=icons.LOCK,
                            ),padding=padding.only(25,10),
                        ),
                        Container(
                            TextButton(
                                "Esqueci a senha!",
                            ),padding=padding.only(25),
                        ),
                        Container(
                            ElevatedButton(
                                content=Text(
                                    "Sing in",
                                    color="white",
                                    weight='w500',
                                ),width=280, bgcolor='black',
                            ),padding=padding.only(40,10)
                        ),
                        Container(
                            Row([
                                Text(
                                    "Não tenho conta",
                                ),
                                TextButton(
                                    "Criar uma conta"
                                )
                            ],spacing=0), padding=padding.only(40),
                        )
                    ]
                    )
                ),
                width=360,
                height=560,
                bgcolor='#22ffffff',
                border_radius=11
            )
        ]),
        padding=110,
        width=360,
        height=560,
    ),
    width=580,
    height=740,
    gradient=LinearGradient(['#002525','#66cdaa']),
)
def main(page: Page):
    page.window_max_width=580
    page.window_max_height=740
    page.padding=0
    page.add(body)

app(target=main)