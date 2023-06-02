from django.db import models

class Question(models.Model):
    gender_text = models.CharField(max_length=200) #modelo de pergunta em texto com um campo de caracteres e com máximo 200 char
    born_date = models.DateTimeField("Date born: ")#modelo numérico com data

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#alternativa da pergunta acima como aqui Masculino/Feminino
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)#contagem dos votos 