from django.contrib import admin

from core.models import Senhas,Chat,QuestaoUsuario,QuestaoResposta,Pontuacao,OWASP




admin.site.register(Senhas)
admin.site.register(Chat)

admin.site.register(OWASP)

admin.site.register(QuestaoResposta)
admin.site.register(QuestaoUsuario)
admin.site.register(Pontuacao)








# Register your modelpythos here.
