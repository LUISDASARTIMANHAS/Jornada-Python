# importando o flet 
import flet as ft

# função principal
def main(pagina):
    titulo = ft.Text("Hashzap")

    def enviar_mensagem_tunel(mensagem):
        # executar tudo que aconteca para todos os usuarios 
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(event):
        nome_usuario = caixa_nome.value
        text_campo_mensagem = campo_enviar_mensagem.value 
        mensagem = f"{nome_usuario}: {text_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)

        # limpar a caixa de texto
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem",on_submit=enviar_mensagem)
    botao_enviar=ft.ElevatedButton("Enviar",on_click=enviar_mensagem)

    chat = ft.Column()
    linha_enviar = ft.Row([campo_enviar_mensagem,botao_enviar])

    def entrar_chat(event):
        # fechar popup
        popup.open = False
        # remover titulo
        pagina.remove(titulo)
        # remover botão
        pagina.remove(botao)
        # carregar o chat
        pagina.add(chat)
        # carregar o campo enviar mensagem
        # carregar o botao de enviar
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat!"
        pagina.pubsub.send_all(mensagem)

        pagina.add(linha_enviar)
        pagina.update()

    botao_popup=ft.ElevatedButton("Entrar no chat",on_click=entrar_chat)
    caixa_nome = ft.TextField(label="Digite o seu nome")
    popup = ft.AlertDialog(
        title=ft.Text("Bem Vindo ao Hashzap"),
        content=caixa_nome,
        actions=[botao_popup]
        )

    # botão inicial
    def abrir_popup(event):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("clicou no botão")


    # titulo
    pagina.add(titulo)
    # botão
    botao = ft.ElevatedButton("Iniciar Chat",on_click=abrir_popup)
    pagina.add(botao)


# função pra quando um usuario entrar no site 
ft.app(main,view=ft.WEB_BROWSER)