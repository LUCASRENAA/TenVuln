from django.contrib import admin

from core.models import Senhas,Chat,QuestaoUsuario,QuestaoResposta,Pontuacao,OWASP,TextoHtml




admin.site.register(Senhas)
admin.site.register(Chat)

admin.site.register(OWASP)

admin.site.register(QuestaoResposta)
admin.site.register(QuestaoUsuario)
admin.site.register(Pontuacao)
admin.site.register(TextoHtml)








# Register your modelpythos here.
