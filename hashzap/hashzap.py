import flet as ft
def main(page):
    def sendTunel(infos):
        chat.controls.append(ft.Text(infos))
        page.update()

    def iniChat(evento):
        page.dialog = popup
        popup.open = True
        page.update()

    def entrarChat(evento):
        popup.open = False
        page.remove(btnIni)
        page.add(chat)
        rowMsg = ft.Row([msgField,btnSend])
        page.add(rowMsg)
        text=f"{nameUser.value} entrou no chat"
        page.pubsub.send_all(text)
        page.update()

    def sendMsg(evento):
        txtMsg = f"{nameUser.value}: {msgField.value}"
        page.pubsub.send_all(txtMsg)
        msgField.value = ""
        page.update()

    page.pubsub.subscribe(sendTunel)

    text = ft.Text("Hashzap")
    nameUser = ft.TextField(label="Digite seu nome")
    msgField=ft.TextField(label="Digite sua mensagem aqui",on_submit=sendMsg)
    btnSend=ft.ElevatedButton("Enviar",on_click=sendMsg)
    chat=ft.Column()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nameUser,
        actions=[ft.ElevatedButton("Entrar",on_click=entrarChat)]
        )

    btnIni = ft.ElevatedButton("Iniciar Chat",on_click=iniChat)

    page.add(text)
    page.add(btnIni)

ft.app(main)
# ft.app(main, view=ft.WEB_BROWSER)